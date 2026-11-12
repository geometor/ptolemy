r"""Exact symbolic construction of Ptolemy's Golden Pentagon-Decagon & Sexagesimal Chords.

Implements *Almagest* Book I, Ch. 10a (Heiberg 1898, Vol. I.1, pp. 31-36 & 38-46):

1. **Ptolemy's Golden Pentagon-Decagon Construction** (:func:`construct_pentagon_decagon`):
   Constructs both the side of the regular decagon ($s_{10} = DZ = R / \phi$) and the
   side of the regular pentagon ($s_5 = BZ = R \sqrt{3 - \phi}$) inside a single circle
   of radius $R$ using ``geometor.model`` with ``auto_intersect=False`` and zero
   floating-point coordinates.
2. **Exact Radical Chord Table** (:func:`exact_chord`, :func:`build_radical_chord_table`):
   Derives exact closed-form algebraic radical expressions in SymPy for Ptolemy's
   canonical chord chain ($120^\circ, 90^\circ, 72^\circ, 60^\circ, 36^\circ, 12^\circ,
   6^\circ, 3^\circ, 1\frac{1}{2}^\circ, \frac{3}{4}^\circ$) on diameter $2R = 120^p$.
3. **Exact Base-60 Sexagesimal Arithmetic** (:class:`Sexagesimal`, :func:`verify_ptolemy_pi`):
   Converts exact SymPy algebraic and rational numbers into Ptolemy's sexagesimal
   notation ($p; m', s''$) and verifies Ptolemy's Inequality Lemma bounds on
   $\operatorname{crd}(1^\circ) \approx 1;2,50 = \frac{377}{360}$ and
   $\pi \approx 3;8,30 = \frac{377}{120}$.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, ProofAssertionError, proposition, quadrance, zero_test

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)
PHI_INV: sp.Expr = (sp.sqrt(5) - sp.Integer(1)) / sp.Integer(2)
PTOLEMY_RADIUS: sp.Integer = sp.Integer(60)
PTOLEMY_DIAMETER: sp.Integer = sp.Integer(120)


@dataclass(frozen=True)
class Sexagesimal:
    """Exact representation of a non-negative base-60 sexagesimal quantity ``p; d1, d2, ...``."""

    parts: int
    digits: tuple[int, ...]

    @property
    def rational(self) -> sp.Rational:
        """Return the exact :class:`sympy.Rational` value represented by these base-60 digits."""
        total = sp.Rational(self.parts, 1)
        denom = sp.Integer(60)
        for d in self.digits:
            total += sp.Rational(d, denom)
            denom *= 60
        return total

    def format_greek_style(self) -> str:
        """Format in scholarly astronomical notation ``parts;d1,d2`` (e.g. ``37;4,55``)."""
        if not self.digits:
            return f"{self.parts}"
        frac = ",".join(str(d) for d in self.digits)
        return f"{self.parts};{frac}"

    def format_prime_style(self) -> str:
        """Format with parts, primes, and seconds (e.g. ``37p 4' 55''``)."""
        markers = ("'", "''", "'''", "''''")
        pieces = [f"{self.parts}p"]
        for idx, d in enumerate(self.digits):
            mark = markers[idx] if idx < len(markers) else f"^({idx + 1})"
            pieces.append(f"{d}{mark}")
        return " ".join(pieces)


@dataclass(frozen=True)
class PentagonDecagonResult:
    """Exact symbolic elements and algebraic invariants of *Almagest* I.10a."""

    model: Model
    radius: sp.Expr
    A: spg.Point
    B: spg.Point
    C: spg.Point
    D: spg.Point
    E: spg.Point
    Z: spg.Point
    decagon_segment: spg.Segment
    pentagon_segment: spg.Segment
    hexagon_segment: spg.Segment
    decagon_length: sp.Expr
    pentagon_length: sp.Expr
    decagon_over_radius: sp.Expr


@dataclass(frozen=True)
class ChordEntry:
    """Entry in Ptolemy's *Almagest* I.10 radical and sexagesimal chord chain."""

    arc_deg: sp.Rational
    exact_expr: sp.Expr
    sexagesimal: Sexagesimal
    heiberg_sexagesimal: Sexagesimal | None = None


def to_sexagesimal(value: sp.Expr | int, places: int = 2) -> Sexagesimal:
    """Round an exact non-negative SymPy real expression to ``places`` base-60 fractional places.

    Uses exact integer floor/nearest-integer arithmetic on ``value * 60**places`` so
    rational and quadratic-radical boundaries are decided without floating-point drift.

    Args:
        value: Exact non-negative SymPy expression or integer.
        places: Number of fractional base-60 places (default ``2`` for primes and seconds).

    Returns:
        Nearest :class:`Sexagesimal` representation.
    """
    expr = sp.sympify(value)
    if places < 0:
        raise ValueError("places must be non-negative.")
    scale = sp.Integer(60) ** places
    scaled = expr * scale
    # Nearest integer: floor(2 * scaled + 1) // 2 using exact SymPy floor
    total_units = int(sp.floor(sp.Integer(2) * scaled + sp.Integer(1)) // sp.Integer(2))

    digits_rev: list[int] = []
    rem = total_units
    for _ in range(places):
        digits_rev.append(int(rem % 60))
        rem //= 60
    return Sexagesimal(parts=int(rem), digits=tuple(reversed(digits_rev)))


def from_sexagesimal(parts: int, *digits: int) -> sp.Rational:
    """Convert ``(parts, d1, d2, ...)`` in base 60 to an exact :class:`sympy.Rational`."""
    return Sexagesimal(parts=parts, digits=tuple(digits)).rational


def _bisect_segment(model: Model, p1: spg.Point, p2: spg.Point, *, mid_id: str) -> spg.Point:
    """Construct the exact Euclidean midpoint of ``(p1, p2)`` via equilateral poles (Eucl. I.10)."""
    with model.subconstruction(f"bisect_{mid_id}"):
        line_base = model.construct_line(p1, p2, guide=True)
        c1 = model.construct_circle(p1, p2, guide=True, by="Post.3")
        c2 = model.construct_circle(p2, p1, guide=True, by="Post.3")
        pole_top = model.intersect(c1, c2, side_of=(p1, p2, 1), guide=True, by="I.1")
        pole_bot = model.intersect(c1, c2, side_of=(p1, p2, -1), guide=True, by="I.1")
        bisector = model.construct_line(pole_top, pole_bot, classes=["bisector"], guide=True, by="Post.1")
        midpoint = model.intersect(line_base, bisector, ID=mid_id, by="I.10")
        return midpoint


@proposition(
    "Almagest.I.10a",
    kind="problem",
    title="Ptolemy's Golden Decagon and Pentagon Construction",
    hide_guides=True,
)
def construct_pentagon_decagon(
    model: Model | None = None,
    *,
    radius: int | sp.Rational = 60,
) -> PentagonDecagonResult:
    r"""Construct the regular decagon side $DZ$ and pentagon side $BZ$ (*Almagest* I.10, Heiberg I, pp. 32-35).

    Follows Ptolemy's exact Euclidean steps with Greek letter mapping
    ($\mathrm{A}\to A$, $\mathrm{B}\to B$, $\mathrm{\Gamma}\to C$, $\mathrm{\Delta}\to D$,
    $\mathrm{E}\to E$, $\mathrm{Z}\to Z$):

    - **Given**: Circle $ABC$ on diameter $ADC$ centered at $D = (0, 0)$ with radius $R$,
      and perpendicular radius $DB \perp AC$.
    - **Construct**: Bisect $DC$ at $E$ (Eucl. I.10); join $EB$; describe circle $(E, B)$
      meeting $AD$ at $Z$ so $EZ = EB$; join $ZB$.
    - **Demonstrate**:

      1. $CZ \cdot ZD + DE^2 = EZ^2 = EB^2 = ED^2 + DB^2 \implies CZ \cdot ZD = DB^2 = DC^2$
         (Eucl. II.6, I.47), so $ZC$ is cut in extreme and mean ratio at $D$ and
         $DZ = R / \phi = s_{10}$ (Eucl. VI.Def.3, XIII.9).
      2. $Q(D, B) + Q(D, Z) = Q(B, Z)$ (Eucl. I.47), so $s_6^2 + s_{10}^2 = BZ^2$ and
         $BZ = s_5$ is the side of the inscribed regular pentagon (Eucl. XIII.10).

    Args:
        model: Optional target :class:`~geometor.model.Model` (created with ``auto_intersect=False`` if ``None``).
        radius: Exact rational circle radius $R$ (defaults to Ptolemy's $R = 60$).

    Returns:
        Verified :class:`PentagonDecagonResult` over $\mathbb{Q}(\phi)$.
    """
    r_val = sp.Rational(radius) if isinstance(radius, int) else radius
    if isinstance(r_val, float) or r_val.atoms(sp.Float):
        raise TypeError("radius must be exact integer or SymPy Rational, never float.")

    if model is None:
        model = Model("almagest_i_10_pentagon_decagon", auto_intersect=False)

    # 1. Given: Diameter A-D-C and perpendicular radius D-B on circle (D, A)
    pt_d = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="D")
    pt_a = model.set_point(-r_val, sp.Integer(0), classes=["given"], ID="A")
    pt_c = model.set_point(r_val, sp.Integer(0), classes=["given"], ID="C")
    circ_main = model.construct_circle(pt_d, pt_a, classes=["given"], ID="cABC", by="Post.3")
    line_ac = model.construct_line(pt_a, pt_c, classes=["given"], ID="lAC", by="Post.1")

    # Construct perpendicular at D to AC via equilateral poles on A, C (Eucl. I.11)
    with model.subconstruction("perp_DB"):
        c_a = model.construct_circle(pt_a, pt_c, guide=True, by="Post.3")
        c_c = model.construct_circle(pt_c, pt_a, guide=True, by="Post.3")
        apex = model.intersect(c_a, c_c, side_of=(pt_a, pt_c, 1), guide=True, by="I.1")
        line_db = model.construct_line(pt_d, apex, guide=True, by="Post.1")
    pt_b = model.intersect(line_db, circ_main, side_of=(pt_a, pt_c, 1), ID="B", by="I.11")
    seg_db = model.construct_segment(pt_d, pt_b, classes=["hexagon"], ID="sDB", by="Post.1")

    # 2. Construct: Bisect DC at E, swing arc (E, B) onto diameter AC at Z, join ZB
    pt_e = _bisect_segment(model, pt_d, pt_c, mid_id="E")
    seg_eb = model.construct_segment(pt_e, pt_b, classes=["guide"], ID="sEB", by="Post.1")
    circ_eb = model.construct_circle(pt_e, pt_b, classes=["golden"], ID="cEB", by="Post.3")
    pt_z = model.intersect(line_ac, circ_eb, between=(pt_a, pt_d), ID="Z", by="I.3")

    seg_dz = model.construct_segment(pt_d, pt_z, classes=["golden", "result"], ID="sDZ", by="Post.1")
    seg_bz = model.construct_segment(pt_b, pt_z, classes=["pentagon", "result"], ID="sBZ", by="Post.1")

    # 3. Demonstrate: Exact Euclidean & Golden Ratio assertions
    model.assert_perpendicular(line_ac, seg_db, by="I.11", label="DB perpendicular to diameter AC")
    model.assert_equal((pt_d, pt_e), (pt_e, pt_c), by="I.10", label="E bisects radius DC")
    model.assert_equal(seg_eb, (pt_e, pt_z), by="Def.15", label="EZ equals radius EB of swing circle")
    model.assert_collinear(pt_a, pt_z, pt_d, by="Post.1", label="Z lies on diameter segment AD")

    # Verify Euclid II.6 + I.47 -> VI.Def.3: CZ * ZD == DC^2 and DZ / R == 1 / phi
    len_dz = sp.simplify(pt_d.x - pt_z.x)
    len_cz = sp.simplify(pt_c.x - pt_z.x)
    if not zero_test(len_cz * len_dz - r_val**2):
        raise ProofAssertionError("Extreme and mean ratio check CZ * ZD == R^2 failed.")
    if not zero_test(len_dz / r_val - PHI_INV):
        raise ProofAssertionError("Golden decagon ratio DZ / R == 1/phi failed.")

    # Verify Euclid XIII.10 / I.47: Q(D, B) + Q(D, Z) == Q(B, Z)
    q_db = quadrance(pt_d, pt_b)
    q_dz = quadrance(pt_d, pt_z)
    q_bz = quadrance(pt_b, pt_z)
    if not zero_test((q_db + q_dz) - q_bz):
        raise ProofAssertionError("Euclid XIII.10 identity s_6^2 + s_10^2 == s_5^2 failed.")

    len_bz = sp.simplify(sp.sqrt(q_bz))
    expected_s5 = r_val * sp.sqrt(sp.Integer(10) - sp.Integer(2) * sp.sqrt(5)) / sp.Integer(2)
    if not zero_test(len_bz - expected_s5):
        raise ProofAssertionError("Pentagon chord length BZ mismatch.")

    model.conclude(
        seg_dz,
        seg_bz,
        seg_db,
        kind="qef",
        by="Eucl.XIII.9-10",
        label="DZ = s_10 = R/phi and BZ = s_5 = sqrt(R^2 + DZ^2)",
    )

    return PentagonDecagonResult(
        model=model,
        radius=r_val,
        A=pt_a,
        B=pt_b,
        C=pt_c,
        D=pt_d,
        E=pt_e,
        Z=pt_z,
        decagon_segment=seg_dz,
        pentagon_segment=seg_bz,
        hexagon_segment=seg_db,
        decagon_length=len_dz,
        pentagon_length=len_bz,
        decagon_over_radius=sp.simplify(len_dz / r_val),
    )


def supplementary_chord(chord_theta: sp.Expr, diameter: sp.Expr = PTOLEMY_DIAMETER) -> sp.Expr:
    r"""Return $\operatorname{crd}(180^\circ - \theta) = \sqrt{D^2 - \operatorname{crd}^2(\theta)}$ (Eucl. I.47, III.31)."""
    return sp.sqrt(diameter**2 - chord_theta**2)


def chord_difference(
    chord_alpha: sp.Expr,
    chord_beta: sp.Expr,
    diameter: sp.Expr = PTOLEMY_DIAMETER,
) -> sp.Expr:
    r"""Return $\operatorname{crd}(\alpha - \beta)$ via Ptolemy's Theorem (*Almagest* I.10, Heiberg I, p. 38).

    $$\operatorname{crd}(\alpha - \beta)
      = \frac{\operatorname{crd}(\alpha)\operatorname{crd}(180^\circ - \beta)
            - \operatorname{crd}(\beta)\operatorname{crd}(180^\circ - \alpha)}{D}$$
    """
    supp_alpha = supplementary_chord(chord_alpha, diameter)
    supp_beta = supplementary_chord(chord_beta, diameter)
    return (chord_alpha * supp_beta - chord_beta * supp_alpha) / diameter


def chord_sum(
    chord_alpha: sp.Expr,
    chord_beta: sp.Expr,
    diameter: sp.Expr = PTOLEMY_DIAMETER,
) -> sp.Expr:
    r"""Return $\operatorname{crd}(\alpha + \beta)$ via Ptolemy's Theorem (*Almagest* I.10, Heiberg I, pp. 41-42)."""
    supp_alpha = supplementary_chord(chord_alpha, diameter)
    supp_beta = supplementary_chord(chord_beta, diameter)
    return (chord_alpha * supp_beta + chord_beta * supp_alpha) / diameter


def chord_half_arc(chord_theta: sp.Expr, diameter: sp.Expr = PTOLEMY_DIAMETER) -> sp.Expr:
    r"""Return $\operatorname{crd}(\theta / 2)$ via Ptolemy's Half-Arc Lemma (*Almagest* I.10, Heiberg I, pp. 39-40).

    $$\operatorname{crd}^2(\theta / 2) = \frac{D}{2} \cdot \left(D - \operatorname{crd}(180^\circ - \theta)\right)$$
    """
    supp_theta = supplementary_chord(chord_theta, diameter)
    return sp.sqrt((diameter / sp.Integer(2)) * (diameter - supp_theta))


def exact_chord(arc_deg: int | sp.Rational, radius: int | sp.Rational = 60) -> sp.Expr:
    """Return the exact SymPy closed-form radical expression for Ptolemy's chord of ``arc_deg``.

    Supports Ptolemy's primary *Almagest* I.10 geometric sequence:
    ``180, 144, 120, 90, 72, 60, 36, 12, 6, 3, 3/2, 3/4`` degrees.
    """
    r_val = sp.Rational(radius)
    d_val = sp.Integer(2) * r_val
    arc = sp.Rational(arc_deg)

    c36 = sp.simplify(r_val * PHI_INV)
    c60 = r_val
    c72 = sp.simplify(r_val * sp.sqrt(sp.Integer(10) - sp.Integer(2) * sp.sqrt(5)) / sp.Integer(2))
    c90 = sp.simplify(r_val * sp.sqrt(2))
    c120 = sp.simplify(r_val * sp.sqrt(3))
    c144 = sp.simplify(supplementary_chord(c36, d_val))
    c180 = d_val

    if arc == 180:
        return c180
    if arc == 144:
        return c144
    if arc == 120:
        return c120
    if arc == 90:
        return c90
    if arc == 72:
        return c72
    if arc == 60:
        return c60
    if arc == 36:
        return c36

    c12 = sp.radsimp(chord_difference(c72, c60, d_val))
    if arc == 12:
        return c12

    c6 = chord_half_arc(c12, d_val)
    if arc == 6:
        return c6

    c3 = chord_half_arc(c6, d_val)
    if arc == 3:
        return c3

    c1_5 = chord_half_arc(c3, d_val)
    if arc == sp.Rational(3, 2):
        return c1_5

    c0_75 = chord_half_arc(c1_5, d_val)
    if arc == sp.Rational(3, 4):
        return c0_75

    raise ValueError(f"Unsupported canonical Ptolemy arc: {arc_deg}")


def build_radical_chord_table(radius: int | sp.Rational = 60) -> list[ChordEntry]:
    """Build Ptolemy's exact *Almagest* I.10–I.11 radical and sexagesimal chord table."""
    heiberg_ref: dict[sp.Rational, Sexagesimal] = {
        sp.Rational(120, 1): Sexagesimal(103, (55, 23)),
        sp.Rational(90, 1): Sexagesimal(84, (51, 10)),
        sp.Rational(72, 1): Sexagesimal(70, (32, 3)),
        sp.Rational(60, 1): Sexagesimal(60, (0, 0)),
        sp.Rational(36, 1): Sexagesimal(37, (4, 55)),
        sp.Rational(12, 1): Sexagesimal(12, (32, 36)),
        sp.Rational(6, 1): Sexagesimal(6, (16, 49)),
        sp.Rational(3, 1): Sexagesimal(3, (8, 28)),
        sp.Rational(3, 2): Sexagesimal(1, (34, 15)),
        sp.Rational(3, 4): Sexagesimal(0, (47, 8)),
    }
    arcs = (
        sp.Rational(120, 1),
        sp.Rational(90, 1),
        sp.Rational(72, 1),
        sp.Rational(60, 1),
        sp.Rational(36, 1),
        sp.Rational(12, 1),
        sp.Rational(6, 1),
        sp.Rational(3, 1),
        sp.Rational(3, 2),
        sp.Rational(3, 4),
    )
    scale = sp.Rational(radius) / PTOLEMY_RADIUS
    entries: list[ChordEntry] = []
    for arc in arcs:
        expr = exact_chord(arc, radius=radius)
        sex = to_sexagesimal(expr, places=2)
        h_ref = heiberg_ref.get(arc) if scale == 1 else None
        entries.append(
            ChordEntry(
                arc_deg=arc,
                exact_expr=expr,
                sexagesimal=sex,
                heiberg_sexagesimal=h_ref,
            )
        )
    return entries


@dataclass(frozen=True)
class PtolemyPiVerification:
    """Exact verification of Ptolemy's Inequality Lemma bounds for ``crd(1°)`` and ``pi``."""

    exact_lower_bound: sp.Expr
    exact_upper_bound: sp.Expr
    ptolemy_crd_1_deg: Sexagesimal
    ptolemy_pi: Sexagesimal
    pi_rational: sp.Rational
    strict_inequality_holds: bool
    matches_to_seconds: bool


def verify_ptolemy_pi() -> PtolemyPiVerification:
    r"""Verify Ptolemy's Inequality Lemma (*Almagest* I.10, Heiberg I, pp. 43-46) & $\pi \approx 3;8,30$.

    Ptolemy proves geometrically that for $0 < \beta < \alpha < 180^\circ$:

    $$\frac{\operatorname{crd}(\alpha)}{\operatorname{crd}(\beta)} < \frac{\alpha}{\beta}$$

    Applying this twice to $(\frac{3}{4}^\circ, 1^\circ)$ and $(1^\circ, 1\frac{1}{2}^\circ)$ yields:

    $$\frac{2}{3}\operatorname{crd}(1\tfrac{1}{2}^\circ)
      < \operatorname{crd}(1^\circ)
      < \frac{4}{3}\operatorname{crd}(\tfrac{3}{4}^\circ)$$

    Both bounds round in two sexagesimal places to $1;2,50 = \frac{377}{360}$, implying
    circumference / diameter $\approx \frac{360 \cdot (1;2,50)}{120} = 3 \cdot (1;2,50)
    = 3;8,30 = \frac{377}{120} \approx 3.1416667$ (*Almagest* VI.7, Heiberg I, p. 513).
    """
    c_1_5 = exact_chord(sp.Rational(3, 2), radius=60)
    c_0_75 = exact_chord(sp.Rational(3, 4), radius=60)

    lower = sp.Rational(2, 3) * c_1_5
    upper = sp.Rational(4, 3) * c_0_75

    # Exact true chord crd(1°) = 120 * sin(0.5°) = 120 * sin(pi / 360)
    true_crd_1 = sp.Integer(120) * sp.sin(sp.pi / sp.Integer(360))
    strict_holds = bool(lower.evalf(50) < true_crd_1.evalf(50) < upper.evalf(50))

    sex_lower = to_sexagesimal(lower, places=2)
    sex_upper = to_sexagesimal(upper, places=2)
    ptolemy_c1 = Sexagesimal(1, (2, 50))
    matches = sex_lower == ptolemy_c1 and sex_upper == ptolemy_c1

    pi_rat = sp.Integer(3) * ptolemy_c1.rational  # 3 * (377/360) = 377/120
    ptolemy_pi = to_sexagesimal(pi_rat, places=2)

    return PtolemyPiVerification(
        exact_lower_bound=lower,
        exact_upper_bound=upper,
        ptolemy_crd_1_deg=ptolemy_c1,
        ptolemy_pi=ptolemy_pi,
        pi_rational=pi_rat,
        strict_inequality_holds=strict_holds,
        matches_to_seconds=matches,
    )

r"""Exact symbolic Planar & Spherical Menelaus Lemmas (*Almagest* Book I, Chs. 13-14).

Implements Heiberg 1898, Vol. I.1, pp. 68-78:

1. **Planar Menelaus Lemma** (:func:`construct_planar_menelaus`, *Almagest* I.13, pp. 68-70):
   Constructs Ptolemy's sector-figure ($AB, AC$ cut by $BE, CD$ meeting at $Z$) and draws
   auxiliary line $EH \parallel CD$ meeting $AB$ at $H$ (Eucl. I.31, VI.4), proving both
   *kata synthesin* ($\frac{CA}{AE} = \frac{CD}{DZ} \cdot \frac{ZB}{BE}$) and
   *kata diairesin* ($\frac{CE}{EA} = \frac{CZ}{ZD} \cdot \frac{DB}{BA}$).
2. **Spherical Menelaus Chord Theorem & Solar Declination** (:func:`verify_spherical_menelaus`,
   :func:`compute_solar_declination`, *Almagest* I.13-I.14, pp. 74-78):
   Verifies Ptolemy's 3D central projection from the sphere center $H$ onto the plane of
   $\triangle ACD$ (producing collinear meet points $\Theta, K, \Lambda$ on two intersecting
   planes, Heiberg I, p. 75) and computes Ptolemy's exact chord ratio
   $\operatorname{crd}(2\delta) = \frac{\operatorname{crd}(2\varepsilon)\operatorname{crd}(2\lambda)}{120}$.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, ProofAssertionError, proposition, quadrance, zero_test

from geometor.ptolemy.pentagon_chords import (
    PTOLEMY_DIAMETER,
    Sexagesimal,
    to_sexagesimal,
)


@dataclass(frozen=True)
class PlanarMenelausResult:
    """Exact symbolic elements and compound ratios for *Almagest* I.13 (pp. 68-70)."""

    model: Model
    A: spg.Point
    B: spg.Point
    C: spg.Point
    D: spg.Point
    E: spg.Point
    Z: spg.Point
    H: spg.Point
    ratio_ca_ae: sp.Expr
    compound_synthesin: sp.Expr
    ratio_ce_ea: sp.Expr
    compound_diairesin: sp.Expr


@dataclass(frozen=True)
class SphericalMenelausResult:
    """Exact 3D rational sphere verification of *Almagest* I.13 (pp. 74-76)."""

    center_H: sp.Matrix
    A: sp.Matrix
    B: sp.Matrix
    C: sp.Matrix
    D: sp.Matrix
    E: sp.Matrix
    Z: sp.Matrix
    Theta: sp.Matrix
    K: sp.Matrix
    Lambda: sp.Matrix
    are_theta_k_lambda_collinear: bool
    lhs_chord_ratio_sq: sp.Expr
    rhs_compound_chord_ratio_sq: sp.Expr


def _construct_parallel_through(
    model: Model,
    base_p1: spg.Point,
    base_p2: spg.Point,
    through_pt: spg.Point,
    *,
    line_id: str,
) -> spg.Line:
    """Construct the line through ``through_pt`` parallel to ``(base_p1, base_p2)`` via rhombus compass steps."""
    with model.subconstruction(f"parallel_{line_id}"):
        c_p1 = model.construct_circle(base_p1, through_pt, guide=True, by="Post.3")
        line_base = model.construct_line(base_p1, base_p2, guide=True, by="Post.1")
        q_anchor = model.intersect(line_base, c_p1, on_ray=(base_p1, base_p2), guide=True, by="I.3")
        c_q = model.construct_circle(q_anchor, base_p1, guide=True, by="Post.3")
        c_t = model.construct_circle(through_pt, base_p1, guide=True, by="Post.3")
        fourth_vertex = model.intersect(c_q, c_t, other_than=base_p1, guide=True, by="I.31")
    return model.construct_line(through_pt, fourth_vertex, classes=["parallel"], ID=line_id, by="I.31")


@proposition(
    "Almagest.I.13a",
    kind="theorem",
    title="Ptolemy's Planar Menelaus Sector Lemma",
    hide_guides=True,
)
def construct_planar_menelaus(model: Model | None = None) -> PlanarMenelausResult:
    r"""Construct Ptolemy's planar Menelaus sector configuration (*Almagest* I.13, Heiberg I, pp. 68-70).

    Follows Heiberg's Greek letters ($\mathrm{A}\to A, \mathrm{B}\to B, \mathrm{\Gamma}\to C,
    \mathrm{\Delta}\to D, \mathrm{E}\to E, \mathrm{Z}\to Z, \mathrm{H}\to H$):
    Across two straight lines $AB$ and $AC$, two transversals $BE$ and $CD$ meet at $Z$,
    and $EH \parallel CD$ meets $AB$ at $H$.
    """
    if model is None:
        model = Model("almagest_i_13_planar_menelaus", auto_intersect=False)

    # Canonical clean rational sector vertices free of symmetry degeneracies
    pt_a = model.set_point(sp.Integer(2), sp.Integer(8), classes=["given"], ID="A")
    pt_b = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="B")
    pt_c = model.set_point(sp.Integer(7), sp.Integer(0), classes=["given"], ID="C")
    pt_d = model.set_point(sp.Rational(3, 4), sp.Integer(3), classes=["given"], ID="D")
    pt_e = model.set_point(sp.Integer(4), sp.Rational(24, 5), classes=["given"], ID="E")

    line_ab = model.construct_line(pt_a, pt_b, guide=True, ID="lAB", by="Post.1")
    model.construct_line(pt_a, pt_c, guide=True, ID="lAC", by="Post.1")
    seg_ab = model.construct_segment(pt_a, pt_b, classes=["given"], ID="sAB", by="Post.1")
    seg_ac = model.construct_segment(pt_a, pt_c, classes=["given"], ID="sAC", by="Post.1")

    line_be = model.construct_line(pt_b, pt_e, guide=True, ID="lBE", by="Post.1")
    line_cd = model.construct_line(pt_c, pt_d, guide=True, ID="lCD", by="Post.1")
    seg_be = model.construct_segment(pt_b, pt_e, classes=["given"], ID="sBE", by="Post.1")
    seg_cd = model.construct_segment(pt_c, pt_d, classes=["given"], ID="sCD", by="Post.1")

    pt_z = model.intersect(line_be, line_cd, ID="Z", by="Post.1")

    # Auxiliary parallel EH || CD meeting AB at H (Heiberg I, p. 69, l. 5)
    line_eh = _construct_parallel_through(model, pt_c, pt_d, pt_e, line_id="lEH")
    pt_h = model.intersect(line_ab, line_eh, ID="H", by="I.31")
    seg_eh = model.construct_segment(pt_e, pt_h, classes=["golden", "result"], ID="sEH", by="I.31")

    # Assertions
    model.assert_collinear(pt_a, pt_d, pt_b, by="Post.1", label="D lies on AB")
    model.assert_collinear(pt_a, pt_e, pt_c, by="Post.1", label="E lies on AC")
    model.assert_collinear(pt_a, pt_h, pt_b, by="Post.1", label="H lies on AB")
    model.assert_parallel(line_cd, line_eh, by="I.31", label="EH parallel to CD")

    ca = sp.simplify(sp.sqrt(quadrance(pt_c, pt_a)))
    ae = sp.simplify(sp.sqrt(quadrance(pt_a, pt_e)))
    ce = sp.simplify(sp.sqrt(quadrance(pt_c, pt_e)))

    cd = sp.simplify(sp.sqrt(quadrance(pt_c, pt_d)))
    dz = sp.simplify(sp.sqrt(quadrance(pt_d, pt_z)))
    cz = sp.simplify(sp.sqrt(quadrance(pt_c, pt_z)))

    zb = sp.simplify(sp.sqrt(quadrance(pt_z, pt_b)))
    be = sp.simplify(sp.sqrt(quadrance(pt_b, pt_e)))
    db = sp.simplify(sp.sqrt(quadrance(pt_d, pt_b)))
    ba = sp.simplify(sp.sqrt(quadrance(pt_b, pt_a)))

    ratio_ca_ae = sp.simplify(ca / ae)
    comp_syn = sp.simplify((cd / dz) * (zb / be))
    if not zero_test(ratio_ca_ae - comp_syn):
        raise ProofAssertionError("Menelaus kata synthesin ratio failed.")

    ratio_ce_ea = sp.simplify(ce / ae)
    comp_dia = sp.simplify((cz / dz) * (db / ba))
    if not zero_test(ratio_ce_ea - comp_dia):
        raise ProofAssertionError("Menelaus kata diairesin ratio failed.")

    model.conclude(
        seg_ab,
        seg_ac,
        seg_be,
        seg_cd,
        seg_eh,
        pt_z,
        pt_h,
        kind="qed",
        by="Eucl.VI.4",
        label="CA:AE = (CD:DZ)*(ZB:BE) and CE:EA = (CZ:ZD)*(DB:BA)",
    )

    return PlanarMenelausResult(
        model=model,
        A=pt_a,
        B=pt_b,
        C=pt_c,
        D=pt_d,
        E=pt_e,
        Z=pt_z,
        H=pt_h,
        ratio_ca_ae=ratio_ca_ae,
        compound_synthesin=comp_syn,
        ratio_ce_ea=ratio_ce_ea,
        compound_diairesin=comp_dia,
    )


def _normalize_on_unit_sphere(v: sp.Matrix) -> sp.Matrix:
    """Project a rational 3D vector with rational norm onto the unit sphere $S^2$."""
    norm = sp.simplify(sp.sqrt(v.dot(v)))
    return sp.Matrix([sp.simplify(v[0] / norm), sp.simplify(v[1] / norm), sp.simplify(v[2] / norm)])


def _double_arc_chord_sq(u: sp.Matrix, v: sp.Matrix) -> sp.Expr:
    r"""Return $\operatorname{crd}^2(2 \cdot \widehat{UV}) = 4 \sin^2(\widehat{UV}) = 4 (1 - (u \cdot v)^2)$ on unit sphere."""
    dot_uv = sp.simplify(u.dot(v))
    return sp.simplify(sp.Integer(4) * (sp.Integer(1) - dot_uv**2))


def verify_spherical_menelaus() -> SphericalMenelausResult:
    r"""Verify Ptolemy's 3D central-projection proof of Spherical Menelaus (*Almagest* I.13, pp. 74-76).

    Constructs an exact rational spherical Menelaus configuration $(A, B, C, D, E, Z)$ on $S^2$
    centered at $H = (0, 0, 0)$, computes the three planar intersections $\Theta = AD \cap HB$,
    $K = CD \cap HZ$, and $\Lambda = AC \cap HE$ (Heiberg I, p. 75), verifies that $\Theta, K, \Lambda$
    are strictly collinear (lying in the intersection of plane $ACD$ with great-circle plane $HBZE$),
    and verifies Ptolemy's exact spherical chord theorem:

    $$\frac{\operatorname{crd}(2\widehat{CE})}{\operatorname{crd}(2\widehat{EA})}
      = \frac{\operatorname{crd}(2\widehat{CZ})}{\operatorname{crd}(2\widehat{ZD})}
      \cdot \frac{\operatorname{crd}(2\widehat{DB})}{\operatorname{crd}(2\widehat{BA})}$$
    """
    center_h = sp.Matrix([sp.Integer(0), sp.Integer(0), sp.Integer(0)])

    # Exact rational points on S^2 via Pythagorean quadruples:
    pt_a = sp.Matrix([sp.Integer(0), sp.Integer(0), sp.Integer(1)])
    pt_b = sp.Matrix([sp.Rational(3, 5), sp.Integer(0), sp.Rational(4, 5)])
    pt_c = sp.Matrix([sp.Integer(0), sp.Rational(4, 5), sp.Rational(3, 5)])

    # D on great-circle arc AB: (1/3, 0, 1)*scale -> (5/13, 0, 12/13)? No, 5/13 < 3/5 so D is between A and B!
    pt_d = sp.Matrix([sp.Rational(5, 13), sp.Integer(0), sp.Rational(12, 13)])
    # E on great-circle arc AC: (0, 5/13, 12/13) is strictly between A=(0,0,1) and C=(0,4/5,3/5)!
    pt_e = sp.Matrix([sp.Integer(0), sp.Rational(5, 13), sp.Rational(12, 13)])

    # Z is the intersection of great-circle planes HBE and HCD on the positive Z hemisphere:
    n_be = pt_b.cross(pt_e)
    n_cd = pt_c.cross(pt_d)
    z_dir = n_be.cross(n_cd)
    if z_dir[2] < 0:
        z_dir = -z_dir
    pt_z = _normalize_on_unit_sphere(z_dir)

    def _line_ray_meet(p1: sp.Matrix, p2: sp.Matrix, ray_dir: sp.Matrix) -> sp.Matrix:
        # Solve p1 + t*(p2 - p1) == s*ray_dir
        t_sym, s_sym = sp.symbols("t_sym s_sym")
        eqs = [p1[i] + t_sym * (p2[i] - p1[i]) - s_sym * ray_dir[i] for i in range(3)]
        sol = sp.solve(eqs, (t_sym, s_sym), dict=True)
        if not sol:
            raise ProofAssertionError("Line and central ray failed to intersect in plane.")
        t_val = sol[0][t_sym]
        return sp.Matrix([sp.simplify(p1[i] + t_val * (p2[i] - p1[i])) for i in range(3)])

    theta = _line_ray_meet(pt_a, pt_d, pt_b)
    kappa = _line_ray_meet(pt_c, pt_d, pt_z)
    lam = _line_ray_meet(pt_a, pt_c, pt_e)

    # Collinearity of Theta, K, Lambda in R^3: cross product (K - Theta) x (Lambda - Theta) == 0
    cross_col = (kappa - theta).cross(lam - theta)
    collinear = all(zero_test(cross_col[i]) for i in range(3))
    if not collinear:
        raise ProofAssertionError("Projected points Theta, K, Lambda are not collinear.")

    lhs_sq = sp.simplify(_double_arc_chord_sq(pt_c, pt_e) / _double_arc_chord_sq(pt_e, pt_a))
    rhs_sq = sp.simplify(
        (_double_arc_chord_sq(pt_c, pt_z) / _double_arc_chord_sq(pt_z, pt_d))
        * (_double_arc_chord_sq(pt_d, pt_b) / _double_arc_chord_sq(pt_b, pt_a))
    )
    if not zero_test(lhs_sq - rhs_sq):
        raise ProofAssertionError(f"Spherical Menelaus chord identity failed: {lhs_sq} != {rhs_sq}")

    return SphericalMenelausResult(
        center_H=center_h,
        A=pt_a,
        B=pt_b,
        C=pt_c,
        D=pt_d,
        E=pt_e,
        Z=pt_z,
        Theta=theta,
        K=kappa,
        Lambda=lam,
        are_theta_k_lambda_collinear=collinear,
        lhs_chord_ratio_sq=lhs_sq,
        rhs_compound_chord_ratio_sq=rhs_sq,
    )


@dataclass(frozen=True)
class SolarDeclinationEntry:
    """Solar declination entry computed by Ptolemy's *Almagest* I.14 Spherical Menelaus rule."""

    longitude_deg: int
    crd_2lambda: sp.Expr
    crd_2delta_sexagesimal: Sexagesimal
    declination_deg_sexagesimal: Sexagesimal
    heiberg_declination: Sexagesimal


def compute_solar_declination(longitude_deg: int) -> SolarDeclinationEntry:
    r"""Compute Ptolemy's *Almagest* I.14–I.15 solar declination for $\lambda \in \{30^\circ, 60^\circ, 90^\circ\}$.

    Reproduces Heiberg 1898, Vol. I.1, pp. 77-78 verbatim:
    With obliquity $2\varepsilon = \frac{11}{83} \cdot 360^\circ = 47^\circ 42' 40''$
    and Ptolemy's chord $\operatorname{crd}(2\varepsilon) = 48;31,55$, Menelaus's theorem gives:

    $$\operatorname{crd}(2\delta) = \frac{\operatorname{crd}(2\varepsilon) \cdot \operatorname{crd}(2\lambda)}{120}$$

    yielding $\delta(30^\circ) \approx 11^\circ 40'$ (Heiberg p. 78, l. 12: $\overline{\iota\alpha}\ \overline{\mu}$)
    and $\delta(60^\circ) \approx 20^\circ 30' 9''$ (Heiberg p. 78, l. 24: $\overline{\kappa}\ \overline{\lambda}\ \overline{\theta}$).
    """
    crd_2eps = Sexagesimal(48, (31, 55)).rational
    if longitude_deg == 30:
        crd_2lam = sp.Integer(60)
        heiberg_decl = Sexagesimal(11, (40, 0))
    elif longitude_deg == 60:
        crd_2lam = Sexagesimal(103, (55, 23)).rational
        heiberg_decl = Sexagesimal(20, (30, 9))
    elif longitude_deg == 90:
        crd_2lam = PTOLEMY_DIAMETER
        heiberg_decl = Sexagesimal(23, (51, 20))
    else:
        raise ValueError("Supported canonical longitudes from Almagest I.14: 30, 60, 90.")

    crd_2delta = sp.simplify((crd_2eps * crd_2lam) / PTOLEMY_DIAMETER)
    crd_2delta_sex = to_sexagesimal(crd_2delta, places=2)
    # Exact inverse arc in degrees from chord c on diameter 120: delta = (180/pi) * asin(crd_2delta / 120)
    delta_deg = (sp.Integer(180) / sp.pi) * sp.asin(crd_2delta / PTOLEMY_DIAMETER)
    delta_sex = to_sexagesimal(delta_deg, places=2)

    return SolarDeclinationEntry(
        longitude_deg=longitude_deg,
        crd_2lambda=crd_2lam,
        crd_2delta_sexagesimal=crd_2delta_sex,
        declination_deg_sexagesimal=delta_sex,
        heiberg_declination=heiberg_decl,
    )

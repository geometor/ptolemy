r"""Exact symbolic 3D-to-2D Stereographic Projection & Astrolabe Geometry (*Planisphaerium*).

Implements Ptolemy's *Planisphaerium* (ed. J. L. Heiberg, *Opera Astronomica Minora*,
Vol. II, Leipzig: Teubner, 1907, §§1-4, pp. 227-234):

1. **Exact Rational Stereographic Bijection** (:func:`stereographic_forward`, :func:`stereographic_inverse`):
   Projects $P = (X, Y, Z) \in S^2 \setminus \{(0, 0, -1)\}$ from the South Pole
   $S = (0, 0, -1)$ onto the equatorial plane $Z = 0$:

   $$(x, y) = \left(\frac{X}{1 + Z},\, \frac{Y}{1 + Z}\right), \qquad
     (X, Y, Z) = \left(\frac{2x}{1 + x^2 + y^2},\, \frac{2y}{1 + x^2 + y^2},\, \frac{1 - x^2 - y^2}{1 + x^2 + y^2}\right)$$

2. **Universal Circle-Preservation & Conformal Metric Theorems**
   (:func:`project_sphere_circle_plane`, :func:`prove_circle_preservation_symbolically`,
   :func:`prove_conformal_metric_symbolically`, :func:`prove_parallel_inversion_symbolically`):
   Proves in exact SymPy algebra over $\mathbb{Q}[a, b, c, d, x, y]$ that every plane
   $aX + bY + cZ + d = 0$ cutting $S^2$ without passing through $S$ ($d \neq c$) projects
   to an exact Euclidean circle in the equatorial plane, that meridians ($d = c$) project
   to straight lines through the North Pole, that opposite parallels at :math:`\pm\delta` obey
   circular inversion :math:`r_+ \cdot r_- = R_{\mathrm{eq}}^2` (*Planisphaerium* §4, p. 233:
   ``ez : ed = ed : ek``), and that the pulled-back metric is conformally flat
   :math:`dX^2 + dY^2 + dZ^2 = \frac{4}{(1 + x^2 + y^2)^2}(dx^2 + dy^2)`.

3. **Exact ``geometor.model`` Astrolabe Tropics, Ecliptic & Almucantar Construction**
   (:func:`construct_astrolabe_planisphere`, :func:`construct_almucantar_circle`):
   Constructs Ptolemy's *Planisphaerium* §1 diagram (Heiberg 1907, p. 227: equator $ABGD$,
   North Pole $E$, Tropic of Cancer $TL$, Tropic of Capricorn $KM$, and oblique ecliptic
   circle $MBTD$ centered at $R$) in ``geometor.model`` with ``auto_intersect=False``
   and zero ``sp.Float`` coordinates.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, ProofAssertionError, proposition, quadrance, zero_test


@dataclass(frozen=True)
class ProjectedCircleData:
    """Exact algebraic parameters of a plane-sphere intersection under stereographic projection."""

    plane_coeffs: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
    is_line: bool
    center: tuple[sp.Expr, sp.Expr] | None
    radius_sq: sp.Expr | None
    cartesian_equation: sp.Expr


@dataclass(frozen=True)
class AstrolabePlanisphereResult:
    """Exact symbolic elements and invariants of Ptolemy's *Planisphaerium* §§1 & 4."""

    model: Model
    equator_radius: sp.Expr
    half_obliquity_tan: sp.Expr
    sin_obliquity: sp.Expr
    cos_obliquity: sp.Expr
    E: spg.Point
    A: spg.Point
    B: spg.Point
    G: spg.Point
    D: spg.Point
    T: spg.Point
    L: spg.Point
    K: spg.Point
    M: spg.Point
    R: spg.Point
    equator_circle: spg.Circle
    cancer_circle: spg.Circle
    capricorn_circle: spg.Circle
    ecliptic_circle: spg.Circle
    cancer_radius: sp.Expr
    capricorn_radius: sp.Expr
    ecliptic_radius: sp.Expr
    inversion_product: sp.Expr


def stereographic_forward(X: sp.Expr, Y: sp.Expr, Z: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    """Project 3D point ``(X, Y, Z)`` from South Pole ``(0, 0, -1)`` onto plane ``Z = 0``."""
    denom = sp.Integer(1) + sp.sympify(Z)
    if zero_test(denom):
        raise ValueError("South Pole (0, 0, -1) maps to the point at infinity.")
    return (sp.simplify(sp.sympify(X) / denom), sp.simplify(sp.sympify(Y) / denom))


def stereographic_inverse(x: sp.Expr, y: sp.Expr) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Lift planar point ``(x, y)`` back onto the unit sphere $X^2 + Y^2 + Z^2 = 1$."""
    xs = sp.sympify(x)
    ys = sp.sympify(y)
    r2 = xs**2 + ys**2
    denom = sp.Integer(1) + r2
    return (
        sp.simplify(sp.Integer(2) * xs / denom),
        sp.simplify(sp.Integer(2) * ys / denom),
        sp.simplify((sp.Integer(1) - r2) / denom),
    )


def project_sphere_circle_plane(
    a: sp.Expr,
    b: sp.Expr,
    c: sp.Expr,
    d: sp.Expr,
) -> ProjectedCircleData:
    r"""Project the spherical circle cut on $S^2$ by plane $aX + bY + cZ + d = 0$.

    Substituting $(X, Y, Z) = \left(\frac{2x}{1+r^2}, \frac{2y}{1+r^2}, \frac{1-r^2}{1+r^2}\right)$
    with $r^2 = x^2 + y^2$ yields:

    $$(d - c)(x^2 + y^2) + 2ax + 2by + (d + c) = 0$$

    - When $d = c$ (plane passes through South Pole $S = (0, 0, -1)$), the locus is the
      exact straight line $ax + by + c = 0$.
    - When $d \neq c$, completing the square yields an exact Euclidean circle with center
      $(-\frac{a}{d-c}, -\frac{b}{d-c})$ and squared radius $\frac{a^2 + b^2 + c^2 - d^2}{(d-c)^2}$.
    """
    a_s, b_s, c_s, d_s = (sp.sympify(v) for v in (a, b, c, d))
    x_sym, y_sym = sp.symbols("x y", real=True)
    X_lift, Y_lift, Z_lift = stereographic_inverse(x_sym, y_sym)
    numer = sp.expand(
        (a_s * X_lift + b_s * Y_lift + c_s * Z_lift + d_s)
        * (sp.Integer(1) + x_sym**2 + y_sym**2)
    )

    lead = sp.simplify(d_s - c_s)
    if zero_test(lead):
        line_eq = sp.simplify(numer / sp.Integer(2))
        return ProjectedCircleData(
            plane_coeffs=(a_s, b_s, c_s, d_s),
            is_line=True,
            center=None,
            radius_sq=None,
            cartesian_equation=line_eq,
        )

    cx = sp.simplify(-a_s / lead)
    cy = sp.simplify(-b_s / lead)
    r_sq = sp.simplify((a_s**2 + b_s**2 + c_s**2 - d_s**2) / (lead**2))
    std_circle_eq = (x_sym - cx) ** 2 + (y_sym - cy) ** 2 - r_sq
    # Verify exact algebraic identity numer / (d - c) == (x - cx)^2 + (y - cy)^2 - r^2
    diff = sp.simplify(sp.expand(numer / lead - std_circle_eq))
    if diff != 0:
        raise ProofAssertionError(f"Stereographic circle completion failed: residual {diff}")

    return ProjectedCircleData(
        plane_coeffs=(a_s, b_s, c_s, d_s),
        is_line=False,
        center=(cx, cy),
        radius_sq=r_sq,
        cartesian_equation=std_circle_eq,
    )


def prove_circle_preservation_symbolically() -> dict[str, sp.Expr]:
    r"""Prove stereographic circle preservation universally over $\mathbb{Q}(a, b, c, d, x, y)$."""
    a, b, c, d, x, y = sp.symbols("a b c d x y")
    X, Y, Z = stereographic_inverse(x, y)

    sphere_residual = sp.simplify(X**2 + Y**2 + Z**2 - sp.Integer(1))
    if sphere_residual != 0:
        raise ProofAssertionError("Inverse stereographic lift does not lie on S^2.")

    x_back, y_back = stereographic_forward(X, Y, Z)
    if sp.simplify(x_back - x) != 0 or sp.simplify(y_back - y) != 0:
        raise ProofAssertionError("Forward/inverse stereographic round-trip failed.")

    data = project_sphere_circle_plane(a, b, c, d)
    assert data.center is not None and data.radius_sq is not None
    return {
        "sphere_residual": sphere_residual,
        "center_x": data.center[0],
        "center_y": data.center[1],
        "radius_sq": data.radius_sq,
    }


def prove_conformal_metric_symbolically() -> sp.Expr:
    r"""Prove conformality of stereographic projection by computing the Jacobian metric tensor $J^T J$.

    Verifies that for $\Phi(x, y) = (X(x, y), Y(x, y), Z(x, y))$,

    $$J^T J = \frac{4}{(1 + x^2 + y^2)^2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

    so angles between intersecting curves on the sphere are preserved identically in the plane.
    """
    x, y = sp.symbols("x y")
    X, Y, Z = stereographic_inverse(x, y)
    vec = sp.Matrix([X, Y, Z])
    jac = vec.jacobian([x, y])
    metric = sp.simplify(jac.T * jac)
    conformal_factor = sp.Integer(4) / (sp.Integer(1) + x**2 + y**2) ** 2
    residual_matrix = sp.simplify(metric - conformal_factor * sp.eye(2))
    if residual_matrix != sp.zeros(2, 2):
        raise ProofAssertionError(f"Metric is not conformally flat: {residual_matrix}")
    return conformal_factor


def prove_parallel_inversion_symbolically() -> dict[str, sp.Expr]:
    r"""Prove *Planisphaerium* §4 (Heiberg 1907, p. 233): opposite parallels satisfy :math:`r_+ \cdot r_- = R^2`.

    Parameterizing :math:`\sin\delta = \frac{2t}{1+t^2}, \cos\delta = \frac{1-t^2}{1+t^2}` (:math:`0 < t < 1`),
    the parallel at :math:`+\delta` (:math:`Z = \sin\delta`) has projected radius :math:`r_+ = R \frac{1 - t}{1 + t}`
    and the southern parallel at :math:`-\delta` (:math:`Z = -\sin\delta`) has radius :math:`r_- = R \frac{1 + t}{1 - t}`,
    giving :math:`r_+ \cdot r_- = R^2` (``ez : ed = ed : ek``).
    """
    R, t = sp.symbols("R t", positive=True)
    sin_d = sp.Integer(2) * t / (sp.Integer(1) + t**2)
    cos_d = (sp.Integer(1) - t**2) / (sp.Integer(1) + t**2)
    r_north = sp.simplify(R * cos_d / (sp.Integer(1) + sin_d))
    r_south = sp.simplify(R * cos_d / (sp.Integer(1) - sin_d))
    product = sp.simplify(r_north * r_south)
    if sp.simplify(product - R**2) != 0:
        raise ProofAssertionError("Planisphaerium §4 inversion identity r_north * r_south == R^2 failed.")
    return {
        "r_north": r_north,
        "r_south": r_south,
        "product": product,
    }


@proposition(
    "Planisphaerium.1",
    kind="problem",
    title="Ptolemy's Astrolabe Tropics and Oblique Ecliptic Construction",
    hide_guides=True,
)
def construct_astrolabe_planisphere(
    model: Model | None = None,
    *,
    equator_radius: int | sp.Rational = 60,
    half_obliquity_tan: sp.Rational = sp.Rational(1, 5),
) -> AstrolabePlanisphereResult:
    r"""Construct Ptolemy's *Planisphaerium* §§1 & 4 astrolabe plate in ``geometor.model``.

    Follows Heiberg 1907, pp. 227-229 & 233 letter labels ($a\to A, b\to B, g\to G,
    d\to D, e\to E, t\to T, l\to L, k\to K, m\to M, r\to R$):

    - Equator $ABGD$ centered at North Pole $E = (0, 0)$ with orthogonal diameters $AG$ (vertical)
      and $BD$ (horizontal).
    - With rational half-obliquity parameter $u = \tan(\varepsilon / 2)$ (default $u = \frac{1}{5}$,
      so $\sin\varepsilon = \frac{5}{13} \implies \varepsilon \approx 22^\circ 37'$, 100% in $\mathbb{Q}$!),
      the Tropic of Cancer circle $TL$ has radius $r_{\mathrm{Can}} = R \frac{1 - u}{1 + u}$
      ($= 40$ when $R = 60, u = \frac{1}{5}$) and the Tropic of Capricorn circle $KM$ has radius
      $r_{\mathrm{Cap}} = R \frac{1 + u}{1 - u}$ ($= 90$ when $R = 60, u = \frac{1}{5}$),
      satisfying $40 \times 90 = 3600 = 60^2$ (*Planisphaerium* §4)!
    - Bisecting segment $TM$ ($T = (0, -r_{\mathrm{Can}})$, $M = (0, r_{\mathrm{Cap}})$) at
      $R = (0, \frac{r_{\mathrm{Cap}} - r_{\mathrm{Can}}}{2})$ ($= (0, 25)$), the circle on
      diameter $TM$ centered at $R$ has radius $\frac{r_{\mathrm{Cap}} + r_{\mathrm{Can}}}{2} = 65$
      and passes **exactly** through opposite equatorial points $B = (-60, 0)$ and $D = (60, 0)$
      since $25^2 + 60^2 = 65^2$ (*Planisphaerium* §1: $\angle MDT = 90^\circ$)!
    """
    r_eq = sp.Rational(equator_radius)
    u = sp.Rational(half_obliquity_tan)
    if u <= 0 or u >= 1:
        raise ValueError("half_obliquity_tan must satisfy 0 < u < 1.")

    if model is None:
        model = Model("planisphaerium_astrolabe", auto_intersect=False)

    sin_eps = sp.simplify(sp.Integer(2) * u / (sp.Integer(1) + u**2))
    cos_eps = sp.simplify((sp.Integer(1) - u**2) / (sp.Integer(1) + u**2))

    # 1. Given: Equator ABGD around North Pole E = (0, 0) with meridian AG (y-axis) and colure BD (x-axis)
    pt_e = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="E")
    pt_a = model.set_point(sp.Integer(0), r_eq, classes=["given"], ID="A")
    pt_g = model.set_point(sp.Integer(0), -r_eq, classes=["given"], ID="G")
    pt_b = model.set_point(-r_eq, sp.Integer(0), classes=["given"], ID="B")
    pt_d = model.set_point(r_eq, sp.Integer(0), classes=["given"], ID="D")

    circ_eq = model.construct_circle(pt_e, pt_d, classes=["given"], ID="cABGD", by="Post.3")
    line_ag = model.construct_line(pt_a, pt_g, classes=["given"], ID="lAG", by="Post.1")
    model.construct_line(pt_b, pt_d, classes=["given"], ID="lBD", by="Post.1")

    # 2. Construct: Folded meridian cross-section with stereographic pole at D = (+R, 0),
    # North Pole at B = (-R, 0), southern declination -eps at H = (+R*sin_eps, -R*cos_eps),
    # and northern declination +eps at N = (-R*sin_eps, +R*cos_eps):
    pt_h_south = model.set_point(r_eq * sin_eps, -r_eq * cos_eps, guide=True, ID="H")
    pt_n_north = model.set_point(-r_eq * sin_eps, r_eq * cos_eps, guide=True, ID="N")

    line_dh = model.construct_line(pt_d, pt_h_south, guide=True, ID="lDH", by="Post.1")
    line_dn = model.construct_line(pt_d, pt_n_north, guide=True, ID="lDN", by="Post.1")

    # Intersect stereographic rays with meridian AG:
    # K = (0, -r_cap) [Capricorn], T = (0, +r_can) or vice-versa matching Heiberg p. 227:
    # Let M = (0, +r_cap) [top Capricorn], K = (0, -r_cap), L = (0, +r_can), T = (0, -r_can)
    pt_k = model.intersect(line_ag, line_dh, ID="K", by="Post.1")
    pt_l = model.intersect(line_ag, line_dn, ID="L", by="Post.1")

    circ_cap = model.construct_circle(pt_e, pt_k, classes=["capricorn"], ID="cKM", by="Post.3")
    circ_can = model.construct_circle(pt_e, pt_l, classes=["cancer"], ID="cTL", by="Post.3")

    pt_m = model.intersect(line_ag, circ_cap, other_than=pt_k, ID="M", by="Post.3")
    pt_t = model.intersect(line_ag, circ_can, other_than=pt_l, ID="T", by="Post.3")

    # Bisect segment TM at R to construct the oblique Ecliptic circle MBTD (Heiberg 1907, p. 228, l. 15)
    with model.subconstruction("bisect_TM"):
        c_t = model.construct_circle(pt_t, pt_m, guide=True, by="Post.3")
        c_m = model.construct_circle(pt_m, pt_t, guide=True, by="Post.3")
        p_left = model.intersect(c_t, c_m, index=0, guide=True, by="I.1")
        p_right = model.intersect(c_t, c_m, index=1, guide=True, by="I.1")
        bis_tm = model.construct_line(p_left, p_right, guide=True, by="Post.1")
    pt_r = model.intersect(line_ag, bis_tm, ID="R", by="I.10")

    circ_ecliptic = model.construct_circle(pt_r, pt_m, classes=["golden", "result"], ID="cMBTD", by="Post.3")
    seg_md = model.construct_segment(pt_m, pt_d, classes=["guide"], ID="sMD", by="Post.1")
    seg_td = model.construct_segment(pt_t, pt_d, classes=["guide"], ID="sTD", by="Post.1")

    # 3. Demonstrate:
    # (a) Right angle <MDT = 90° (Planisphaerium §1, p. 228, l. 26: "angulum mdt rectum esse")
    model.assert_perpendicular(seg_md, seg_td, by="III.31", label="Angle MDT in semicircle is right")
    # (b) Oblique ecliptic circle on diameter TM passes strictly through opposite equator points B and D!
    model.assert_incident(pt_d, circ_ecliptic, by="III.31", label="Ecliptic circle passes through D")
    model.assert_incident(pt_b, circ_ecliptic, by="III.31", label="Ecliptic circle passes through B")
    # (c) Planisphaerium §4 circular inversion: r_cancer * r_capricorn == R_eq^2
    len_el = sp.simplify(sp.sqrt(quadrance(pt_e, pt_l)))
    len_ek = sp.simplify(sp.sqrt(quadrance(pt_e, pt_k)))
    len_rm = sp.simplify(sp.sqrt(quadrance(pt_r, pt_m)))
    inv_prod = sp.simplify(len_el * len_ek)
    if not zero_test(inv_prod - r_eq**2):
        raise ProofAssertionError("Planisphaerium §4 inversion EL * EK == ED^2 failed.")

    model.conclude(
        circ_eq,
        circ_can,
        circ_cap,
        circ_ecliptic,
        pt_r,
        pt_b,
        pt_d,
        pt_t,
        pt_m,
        kind="qef",
        by="Planisphaerium.1,4",
        label="Ecliptic circle cMBTD bisects equator at B, D and r_Can * r_Cap == R_eq^2",
    )

    return AstrolabePlanisphereResult(
        model=model,
        equator_radius=r_eq,
        half_obliquity_tan=u,
        sin_obliquity=sin_eps,
        cos_obliquity=cos_eps,
        E=pt_e,
        A=pt_a,
        B=pt_b,
        G=pt_g,
        D=pt_d,
        T=pt_t,
        L=pt_l,
        K=pt_k,
        M=pt_m,
        R=pt_r,
        equator_circle=circ_eq,
        cancer_circle=circ_can,
        capricorn_circle=circ_cap,
        ecliptic_circle=circ_ecliptic,
        cancer_radius=len_el,
        capricorn_radius=len_ek,
        ecliptic_radius=len_rm,
        inversion_product=inv_prod,
    )


def construct_almucantar_circle(
    sin_latitude: sp.Rational,
    cos_latitude: sp.Rational,
    sin_altitude: sp.Rational,
    *,
    equator_radius: int | sp.Rational = 60,
) -> ProjectedCircleData:
    r"""Compute the exact projected astrolabe almucantar (constant-altitude circle) over $\mathbb{Q}$.

    For observer latitude $\varphi$ (zenith $Z_0 = (0, \cos\varphi, \sin\varphi)$ on $S^2$)
    and altitude $h$ above the horizon ($h = 0$ gives Ptolemy's *Planisphaerium* §§2-3 horizon!),
    the almucantar plane on the unit sphere is:

    $$\cos\varphi \cdot Y + \sin\varphi \cdot Z - \sin h = 0$$

    When $h = 0$ (horizon), $d = 0$, and the projected horizon circle passes through the two
    diametrically opposite equatorial East/West points $(\pm R, 0)$.
    """
    if not zero_test(sin_latitude**2 + cos_latitude**2 - sp.Integer(1)):
        raise ValueError("sin_latitude^2 + cos_latitude^2 must equal 1.")
    r_eq = sp.Rational(equator_radius)
    unit_data = project_sphere_circle_plane(
        sp.Integer(0),
        cos_latitude,
        sin_latitude,
        -sin_altitude,
    )
    if unit_data.is_line or unit_data.center is None or unit_data.radius_sq is None:
        return unit_data
    cx = sp.simplify(r_eq * unit_data.center[0])
    cy = sp.simplify(r_eq * unit_data.center[1])
    r_sq = sp.simplify((r_eq**2) * unit_data.radius_sq)
    x_sym, y_sym = sp.symbols("x y", real=True)
    return ProjectedCircleData(
        plane_coeffs=unit_data.plane_coeffs,
        is_line=False,
        center=(cx, cy),
        radius_sq=r_sq,
        cartesian_equation=(x_sym - cx) ** 2 + (y_sym - cy) ** 2 - r_sq,
    )

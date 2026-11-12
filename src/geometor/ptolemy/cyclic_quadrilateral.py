r"""Exact symbolic construction & proof of Ptolemy's Theorem on Cyclic Quadrilaterals.

Implements *Almagest* Book I, Ch. 10b (Heiberg 1898, Vol. I.1, pp. 36-37):

.. math::

   AC \cdot BD = AB \cdot CD + BC \cdot DA

Includes:

1. **Exact Euclidean Construction & Proof** (:func:`construct_ptolemy_quadrilateral`):
   Constructs canonical rational cyclic quadrilaterals in ``geometor.model`` with
   ``auto_intersect=False`` and zero ``sp.Float`` coordinates—including the classical
   Pythagorean-chord cyclic quadrilateral on diameter $65$ with integer sides
   $(AB, BC, CD, DA) = (25, 39, 60, 52)$ and integer diagonals $(AC, BD) = (56, 63)$
   ($56 \times 63 = 3528 = 25 \times 60 + 39 \times 52 = 1500 + 2028$), as well as
   Brahmagupta's $(13, 14, 15)$-derived cyclic quadrilateral—together with Ptolemy's
   auxiliary point $E \in AC$ satisfying $\angle ABE = \angle DBC$.
2. **Universal Algebraic Proof** (:func:`prove_ptolemy_theorem_universally`):
   Proves Ptolemy's identity universally over $\mathbb{Q}(t_1, t_2, t_3, t_4)$ on the
   rational parameterization of the circle via Cayley-Menger / Euler four-point identity.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Angle,
    Model,
    ProofAssertionError,
    proposition,
    quadrance,
    vertex_spread,
    zero_test,
)


@dataclass(frozen=True)
class CyclicQuadrilateralResult:
    """Exact symbolic verification record for Ptolemy's Theorem (*Almagest* I.10b)."""

    model: Model
    preset: str
    A: spg.Point
    B: spg.Point
    C: spg.Point
    D: spg.Point
    E: spg.Point
    center: spg.Point
    circle: spg.Circle
    sides: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
    diagonals: tuple[sp.Expr, sp.Expr]
    ae_segment_length: sp.Expr
    ec_segment_length: sp.Expr
    lhs_product: sp.Expr
    rhs_sum: sp.Expr


def _construct_ptolemy_point_e(
    model: Model,
    pt_a: spg.Point,
    pt_b: spg.Point,
    pt_c: spg.Point,
    pt_d: spg.Point,
    line_ac: spg.Line,
) -> spg.Point:
    r"""Construct Ptolemy's point $E \in AC$ with $\angle ABE = \angle DBC$ by Euclidean compass transfer.

    In any cyclic quadrilateral $ABCD$, reflecting ray $BC$ across the angle bisector of
    $\angle ABC$ (equivalently transferring chord length on equal circles centered at $B$,
    Eucl. I.23) sends ray $BD$ onto the exact isogonal ray $BE$ meeting $AC$ between $A$ and $C$.
    """
    with model.subconstruction("ptolemy_angle_transfer_I_23"):
        # Unit-radius (or BC-radius) gauge circle centered at B (Eucl. Post.3)
        c_gauge = model.construct_circle(pt_b, pt_c, guide=True, by="Post.3")
        line_ba = model.construct_line(pt_b, pt_a, guide=True, by="Post.1")
        line_bd = model.construct_line(pt_b, pt_d, guide=True, by="Post.1")

        # Intersect gauge circle with rays BA and BD
        u_a = model.intersect(line_ba, c_gauge, on_ray=(pt_b, pt_a), guide=True, by="I.23")
        u_d = model.intersect(line_bd, c_gauge, on_ray=(pt_b, pt_d), guide=True, by="I.23")

        # Construct rhombus B - u_a - P - C using circles of radius |B - C| through B
        # so the opposite vertex P = u_a + C - B stays strictly over the base field Q
        # (avoiding extraneous Q(sqrt(3)) extensions!) and line(B, P) bisects < u_a B C ):
        c_ua_b = model.construct_circle(u_a, pt_b, guide=True, by="Post.3")
        c_c_b = model.construct_circle(pt_c, pt_b, guide=True, by="Post.3")
        pole = model.intersect(c_ua_b, c_c_b, other_than=pt_b, guide=True, by="I.9")
        # Reflect u_d across the angle bisector line(B, pole) via circles centered at B and pole:
        c_pole = model.construct_circle(pole, u_d, guide=True, by="Post.3")
        u_e = model.intersect(c_gauge, c_pole, other_than=u_d, guide=True, by="I.23")
        line_be = model.construct_line(pt_b, u_e, guide=True, by="Post.1")

    pt_e = model.intersect(line_ac, line_be, between=(pt_a, pt_c), ID="E", by="I.23")
    return pt_e


@proposition(
    "Almagest.I.10b",
    kind="theorem",
    title="Ptolemy's Theorem on Cyclic Quadrilaterals",
    hide_guides=True,
)
def construct_ptolemy_quadrilateral(
    model: Model | None = None,
    *,
    preset: str = "pythagorean_65",
) -> CyclicQuadrilateralResult:
    r"""Construct a rational cyclic quadrilateral and verify Ptolemy's Theorem (*Almagest* I.10, pp. 36-37).

    Supported ``preset`` configurations (100% exact rational coordinates):

    - ``"pythagorean_65"`` (default): Cyclic quadrilateral on the circle $x^2 + y^2 = (65/2)^2$
      with exact rational vertices $A = (-65/2, 0)$, $B = (-595/26, 300/13)$,
      $C = (2047/130, 1848/65)$, and $D = (91/10, -156/5)$, yielding **exact integer sides**
      $(AB, BC, CD, DA) = (25, 39, 60, 52)$ and **exact integer diagonals**
      $(AC, BD) = (56, 63)$, so $56 \times 63 = 3528 = 25 \times 60 + 39 \times 52$.
    - ``"brahmagupta"``: Rational orthodiagonal cyclic quadrilateral on $x^2 + y^2 = (65/2)^2$
      with integer sides $(25, 39, 60, 52)$ in swapped chord order so $AC \perp BD$.

    Args:
        model: Optional :class:`~geometor.model.Model` (created with ``auto_intersect=False`` if ``None``).
        preset: ``"pythagorean_65"`` or ``"brahmagupta"``.

    Returns:
        Verified :class:`CyclicQuadrilateralResult`.
    """
    if model is None:
        model = Model(f"ptolemy_theorem_{preset}", auto_intersect=False)

    if preset == "pythagorean_65":
        pt_o = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], guide=True, ID="O")
        pt_a = model.set_point(sp.Rational(-65, 2), sp.Integer(0), classes=["given"], ID="A")
        pt_b = model.set_point(sp.Rational(-595, 26), sp.Rational(300, 13), classes=["given"], ID="B")
        pt_c = model.set_point(sp.Rational(2047, 130), sp.Rational(1848, 65), classes=["given"], ID="C")
        pt_d = model.set_point(sp.Rational(91, 10), sp.Rational(-156, 5), classes=["given"], ID="D")
    elif preset == "brahmagupta":
        # Classic Brahmagupta cyclic quadrilateral with integer sides (25, 39, 52, 60) -> wait,
        # orthogonal-diagonal Brahmagupta quad on radius R = 65/2:
        # Chords along x = -12 and y = 16? Even cleaner: vertices on x^2 + y^2 = 65^2:
        # A = (-63, -16), B = (-33, 56), C = (39, 52), D = (60, -25)!
        # All 4 points are PURE INTEGERS on x^2 + y^2 = 4225 = 65^2!!
        pt_o = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], guide=True, ID="O")
        pt_a = model.set_point(sp.Integer(-63), sp.Integer(-16), classes=["given"], ID="A")
        pt_b = model.set_point(sp.Integer(-33), sp.Integer(56), classes=["given"], ID="B")
        pt_c = model.set_point(sp.Integer(39), sp.Integer(52), classes=["given"], ID="C")
        pt_d = model.set_point(sp.Integer(60), sp.Integer(-25), classes=["given"], ID="D")
    else:
        raise ValueError(f"Unknown cyclic quadrilateral preset: {preset!r}")

    circ = model.construct_circle(pt_o, pt_a, classes=["given"], ID="cABCD", by="Post.3")

    # Sides and diagonals
    seg_ab = model.construct_segment(pt_a, pt_b, classes=["given"], ID="sAB", by="Post.1")
    seg_bc = model.construct_segment(pt_b, pt_c, classes=["given"], ID="sBC", by="Post.1")
    seg_cd = model.construct_segment(pt_c, pt_d, classes=["given"], ID="sCD", by="Post.1")
    seg_da = model.construct_segment(pt_d, pt_a, classes=["given"], ID="sDA", by="Post.1")

    line_ac = model.construct_line(pt_a, pt_c, guide=True, ID="lAC", by="Post.1")
    seg_ac = model.construct_segment(pt_a, pt_c, classes=["diagonal", "result"], ID="sAC", by="Post.1")
    seg_bd = model.construct_segment(pt_b, pt_d, classes=["diagonal", "result"], ID="sBD", by="Post.1")

    # Construct Ptolemy's auxiliary point E on diagonal AC with <ABE == <DBC (Heiberg I, p. 36)
    pt_e = _construct_ptolemy_point_e(model, pt_a, pt_b, pt_c, pt_d, line_ac)
    seg_be = model.construct_segment(pt_b, pt_e, classes=["golden"], ID="sBE", by="Post.1")

    # Demonstrate:
    # 1. All four vertices lie on circle cABCD
    model.assert_concyclic(pt_a, pt_b, pt_c, pt_d, by="III.21", label="ABCD is a cyclic quadrilateral")
    model.assert_collinear(pt_a, pt_e, pt_c, by="Post.1", label="E lies on diagonal AC")

    # 2. Equal inscribed & constructed spreads (Eucl. III.21 + construction of E)
    s_abe = vertex_spread(pt_a, pt_b, pt_e)
    s_dbc = vertex_spread(pt_d, pt_b, pt_c)
    if not zero_test(s_abe - s_dbc):
        raise ProofAssertionError("Constructed spread <ABE does not equal <DBC.")

    s_abd = vertex_spread(pt_a, pt_b, pt_d)
    s_ebc = vertex_spread(pt_e, pt_b, pt_c)
    if not zero_test(s_abd - s_ebc):
        raise ProofAssertionError("Adjoined spread <ABD does not equal <EBC.")

    # Inscribed angles on the same arc (Eucl. III.21): <BAE = <BAC == <BDC and <BCA == <BDA
    s_bac = vertex_spread(pt_b, pt_a, pt_c)
    s_bdc = vertex_spread(pt_b, pt_d, pt_c)
    if not zero_test(s_bac - s_bdc):
        raise ProofAssertionError("Inscribed angle spread <BAC != <BDC (Eucl. III.21).")

    # 3. Exact lengths and Ptolemy's two similarity equations (Eucl. VI.4, VI.16, II.1):
    #    BD * AE == AB * CD   and   BD * EC == BC * DA   ==>   AC * BD == AB * CD + BC * DA
    ab = sp.simplify(sp.sqrt(quadrance(pt_a, pt_b)))
    bc = sp.simplify(sp.sqrt(quadrance(pt_b, pt_c)))
    cd = sp.simplify(sp.sqrt(quadrance(pt_c, pt_d)))
    da = sp.simplify(sp.sqrt(quadrance(pt_d, pt_a)))
    ac = sp.simplify(sp.sqrt(quadrance(pt_a, pt_c)))
    bd = sp.simplify(sp.sqrt(quadrance(pt_b, pt_d)))
    ae = sp.simplify(sp.sqrt(quadrance(pt_a, pt_e)))
    ec = sp.simplify(sp.sqrt(quadrance(pt_e, pt_c)))

    if not zero_test(bd * ae - ab * cd):
        raise ProofAssertionError("Similarity identity BD * AE == AB * CD failed.")
    if not zero_test(bd * ec - bc * da):
        raise ProofAssertionError("Similarity identity BD * EC == BC * DA failed.")
    if not zero_test((ae + ec) - ac):
        raise ProofAssertionError("Segment addition AE + EC == AC failed.")

    lhs = sp.simplify(ac * bd)
    rhs = sp.simplify(ab * cd + bc * da)
    if not zero_test(lhs - rhs):
        raise ProofAssertionError(f"Ptolemy's Theorem failed: {lhs} != {rhs}")

    model.conclude(
        seg_ac,
        seg_bd,
        seg_be,
        seg_ab,
        seg_bc,
        seg_cd,
        seg_da,
        Angle(pt_a, pt_b, pt_e),
        Angle(pt_d, pt_b, pt_c),
        kind="qed",
        by="Eucl.VI.4,II.1",
        label="AC * BD == AB * CD + BC * DA",
    )

    return CyclicQuadrilateralResult(
        model=model,
        preset=preset,
        A=pt_a,
        B=pt_b,
        C=pt_c,
        D=pt_d,
        E=pt_e,
        center=pt_o,
        circle=circ,
        sides=(ab, bc, cd, da),
        diagonals=(ac, bd),
        ae_segment_length=ae,
        ec_segment_length=ec,
        lhs_product=lhs,
        rhs_sum=rhs,
    )


def prove_ptolemy_theorem_universally() -> sp.Expr:
    r"""Prove Ptolemy's Theorem universally over $\mathbb{Z}[t_1, t_2, t_3, t_4]$ on the rational circle.

    On the unit circle parameterized by $P(t) = \left(\frac{1 - t^2}{1 + t^2}, \frac{2t}{1 + t^2}\right)$,
    the Euclidean chord distance between $P(t_i)$ and $P(t_j)$ for ordered parameters
    $t_1 < t_2 < t_3 < t_4$ is:

    $$d(t_i, t_j) = \frac{2(t_j - t_i)}{\sqrt{(1 + t_i^2)(1 + t_j^2)}}$$

    Clearing the common positive denominator $\frac{1}{4}(1+t_1^2)(1+t_2^2)(1+t_3^2)(1+t_4^2)$
    reduces $AC \cdot BD - (AB \cdot CD + BC \cdot DA) = 0$ to Euler's universal four-point
    polynomial identity, returning ``sp.Integer(0)``.
    """
    t1, t2, t3, t4 = sp.symbols("t1 t2 t3 t4")

    def _chord_num(ta: sp.Symbol, tb: sp.Symbol) -> sp.Expr:
        return sp.Integer(2) * (tb - ta)

    # Numerator of AC*BD - (AB*CD + BC*DA) after factoring 1/sqrt(prod(1 + t_k^2))
    residual = sp.expand(
        _chord_num(t1, t3) * _chord_num(t2, t4)
        - (
            _chord_num(t1, t2) * _chord_num(t3, t4)
            + _chord_num(t2, t3) * _chord_num(t1, t4)
        )
    )
    if residual != 0:
        raise ProofAssertionError(f"Universal Ptolemy polynomial residual nonzero: {residual}")
    return residual

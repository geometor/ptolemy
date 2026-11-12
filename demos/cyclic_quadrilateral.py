r"""Demonstration 2: Ptolemy's Theorem on Cyclic Quadrilaterals & Menelaus Sector Lemma.

Showcases *Almagest* Book I, Ch. 10b (Heiberg 1898, Vol. I.1, pp. 36-37) and Ch. 13-14
(pp. 68-78):

1. Constructs the Pythagorean cyclic quadrilateral on diameter $65$ with exact integer
   sides $(AB, BC, CD, DA) = (25, 39, 60, 52)$ and diagonals $(AC, BD) = (56, 63)$,
   verifying $56 \times 63 = 3528 = 25 \times 60 + 39 \times 52 = 1500 + 2028$ and
   locating Ptolemy's exact Euclidean similarity point $E \in AC$ ($AE = \frac{500}{21}$,
   $EC = \frac{676}{21}$).
2. Constructs the pure-integer Brahmagupta cyclic quadrilateral on $x^2 + y^2 = 65^2$.
3. Proves Ptolemy's Theorem universally over $\mathbb{Z}[t_1, t_2, t_3, t_4]$ and runs
   Ptolemy's Planar & 3D Spherical Menelaus verifications (*Almagest* I.13-I.14).
"""

from __future__ import annotations

import sys
from pathlib import Path

_SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.ptolemy import (  # noqa: E402
    compute_solar_declination,
    construct_planar_menelaus,
    construct_ptolemy_quadrilateral,
    prove_ptolemy_theorem_universally,
    verify_spherical_menelaus,
)


def run_demo() -> None:
    """Execute the Ptolemy's Theorem and Menelaus Trigonometry demonstration."""
    console = Console()

    for preset_name in ("pythagorean_65", "brahmagupta"):
        res = construct_ptolemy_quadrilateral(preset=preset_name)
        ab, bc, cd, da = res.sides
        ac, bd = res.diagonals
        q_table = Table(title=f"Almagest I.10b — Ptolemy's Theorem ({preset_name})")
        q_table.add_column("Element / Relation", style="cyan bold")
        q_table.add_column("Exact Symbolic Value", style="green")
        q_table.add_row("Sides (AB, BC, CD, DA)", f"({ab}, {bc}, {cd}, {da})")
        q_table.add_row("Diagonals (AC, BD)", f"({ac}, {bd})")
        q_table.add_row("Ptolemy Point E on AC", f"({res.E.x}, {res.E.y}) -> AE = {res.ae_segment_length}, EC = {res.ec_segment_length}")
        q_table.add_row("LHS = AC · BD", str(res.lhs_product))
        q_table.add_row("RHS = AB·CD + BC·DA", f"{ab * cd} + {bc * da} = {res.rhs_sum}")
        console.print(q_table)

    poly_res = prove_ptolemy_theorem_universally()
    men_p = construct_planar_menelaus()
    men_s = verify_spherical_menelaus()

    m_table = Table(title="Almagest I.13-14 — Universal Proof & Menelaus Spherical Trigonometry")
    m_table.add_column("Verification", style="bold yellow")
    m_table.add_column("Exact Result", style="cyan")
    m_table.add_row("Universal 4-Variable Circle Residual", str(poly_res))
    m_table.add_row(
        "Planar Menelaus (kata synthesin)",
        f"CA/AE = {men_p.ratio_ca_ae} == (CD/DZ)·(ZB/BE) = {men_p.compound_synthesin}",
    )
    m_table.add_row(
        "Planar Menelaus (kata diairesin)",
        f"CE/EA = {men_p.ratio_ce_ea} == (CZ/ZD)·(DB/BA) = {men_p.compound_diairesin}",
    )
    m_table.add_row(
        "3D Spherical Menelaus Plane Meet (Θ, K, Λ)",
        f"Collinear = {men_s.are_theta_k_lambda_collinear}; crd²(2CE)/crd²(2EA) = {men_s.lhs_chord_ratio_sq}",
    )
    for lon in (30, 60, 90):
        decl = compute_solar_declination(lon)
        m_table.add_row(
            f"I.14 Solar Declination δ(λ={lon}°)",
            f"Computed {decl.declination_deg_sexagesimal.format_greek_style()}° vs Heiberg {decl.heiberg_declination.format_greek_style()}°",
        )
    console.print(m_table)


if __name__ == "__main__":
    run_demo()

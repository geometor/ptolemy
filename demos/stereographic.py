r"""Demonstration 3: Stereographic Projection & Astrolabe Geometry (*Planisphaerium*).

Showcases Ptolemy's *Planisphaerium* (ed. J. L. Heiberg, *Opera Astronomica Minora*,
1907, §§1-4, pp. 227-234):

1. Verifies the universal algebraic Circle-Preservation Theorem over $\mathbb{Q}(a, b, c, d)$
   showing that every plane $aX + bY + cZ + d = 0$ ($d \neq c$) projects from the South
   Pole $S = (0, 0, -1)$ onto an exact Euclidean circle in the equatorial plane, while
   planes through $S$ ($d = c$, such as meridians) project to straight lines.
2. Verifies the conformal metric tensor $J^T J = \frac{4}{(1 + x^2 + y^2)^2} I_2$ and
   *Planisphaerium* §4 circular inversion $r_+ \cdot r_- = R^2$ (`ez : ed = ed : ek`).
3. Constructs Ptolemy's *Planisphaerium* §1 astrolabe plate (equator $ABGD$, Cancer $TL$,
   Capricorn $KM$, and oblique ecliptic $MBTD$) in ``geometor.model`` with zero ``sp.Float``
   coordinates, plus rational astrolabe horizon and almucantar circles.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

import sympy as sp  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.ptolemy import (  # noqa: E402
    construct_almucantar_circle,
    construct_astrolabe_planisphere,
    prove_circle_preservation_symbolically,
    prove_conformal_metric_symbolically,
    prove_parallel_inversion_symbolically,
)


def run_demo() -> None:
    """Execute the Stereographic Projection and Astrolabe demonstration."""
    console = Console()

    circ_proof = prove_circle_preservation_symbolically()
    conf_factor = prove_conformal_metric_symbolically()
    inv_proof = prove_parallel_inversion_symbolically()

    sym_table = Table(title="Planisphaerium — Universal Symbolic Stereographic Theorems")
    sym_table.add_column("Theorem", style="cyan bold")
    sym_table.add_column("Exact Algebraic Formula", style="green")
    sym_table.add_row(
        "Plane aX+bY+cZ+d=0 Projected Center",
        f"({circ_proof['center_x']}, {circ_proof['center_y']})",
    )
    sym_table.add_row("Projected Squared Radius r²", str(circ_proof["radius_sq"]))
    sym_table.add_row("Conformal Pullback Factor λ(x,y)", f"{conf_factor} · (dx² + dy²)")
    sym_table.add_row(
        "§4 Parallel Inversion r(+δ)·r(-δ)",
        f"({inv_proof['r_north']}) · ({inv_proof['r_south']}) = {inv_proof['product']}",
    )
    console.print(sym_table)

    astro = construct_astrolabe_planisphere(equator_radius=60, half_obliquity_tan=sp.Rational(1, 5))
    horizon = construct_almucantar_circle(
        sp.Rational(3, 5),
        sp.Rational(4, 5),
        sp.Integer(0),
        equator_radius=60,
    )
    alm_30 = construct_almucantar_circle(
        sp.Rational(3, 5),
        sp.Rational(4, 5),
        sp.Rational(1, 2),
        equator_radius=60,
    )

    ast_table = Table(title="Planisphaerium §§1-4 — Exact Astrolabe Construction (R_eq = 60)")
    ast_table.add_column("Astrolabe Locus", style="bold yellow")
    ast_table.add_column("Exact Rational Geometry", style="cyan")
    ast_table.add_row("Equator Circle cABGD", f"Center ({astro.E.x}, {astro.E.y}), Radius = {astro.equator_radius}")
    ast_table.add_row("Tropic of Cancer cTL", f"Center (0, 0), Radius EL = {astro.cancer_radius}")
    ast_table.add_row("Tropic of Capricorn cKM", f"Center (0, 0), Radius EK = {astro.capricorn_radius}")
    ast_table.add_row(
        "§4 Inversion Check EL · EK == ED²",
        f"{astro.cancer_radius} × {astro.capricorn_radius} = {astro.inversion_product} == {astro.equator_radius**2}",
    )
    ast_table.add_row(
        "Oblique Ecliptic Circle cMBTD",
        f"Center R = ({astro.R.x}, {astro.R.y}), Radius = {astro.ecliptic_radius} (passes through B={astro.B}, D={astro.D})",
    )
    ast_table.add_row(
        "Horizon Circle (sin φ = 3/5, h = 0°)",
        f"Center = {horizon.center}, Radius² = {horizon.radius_sq} (100² = 10000 -> Radius = 100)",
    )
    ast_table.add_row(
        "Almucantar Circle (sin φ = 3/5, sin h = 1/2)",
        f"Center = {alm_30.center}, Radius² = {alm_30.radius_sq}",
    )
    console.print(ast_table)


if __name__ == "__main__":
    run_demo()

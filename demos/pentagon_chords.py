r"""Demonstration 1: Ptolemy's Golden Pentagon-Decagon Construction & Radical Chord Table.

Showcases *Almagest* Book I, Chs. 10-11 (Heiberg 1898, Vol. I.1, pp. 32-46):

1. Constructs Ptolemy's single-circle regular decagon ($DZ = R / \phi$) and regular
   pentagon ($BZ = \sqrt{R^2 + DZ^2}$) in ``geometor.model`` with ``auto_intersect=False``
   and zero floating-point coordinates.
2. Computes the exact closed-form SymPy radical expressions and base-60 sexagesimal
   approximations for Ptolemy's chord cascade ($120^\circ \to 90^\circ \to 72^\circ \to
   60^\circ \to 36^\circ \to 12^\circ \to 6^\circ \to 3^\circ \to 1\frac{1}{2}^\circ
   \to \frac{3}{4}^\circ$), comparing each against Heiberg's Greek text.
3. Verifies Ptolemy's Inequality Lemma bounds for $\operatorname{crd}(1^\circ) \approx 1;2,50$
   and the resulting sexagesimal ratio $\pi \approx 3;8,30 = \frac{377}{120}$.
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
    PHI,
    PHI_INV,
    build_radical_chord_table,
    construct_pentagon_decagon,
    verify_ptolemy_pi,
)


def run_demo() -> None:
    """Execute the Golden Pentagon-Decagon and Sexagesimal Chord demonstration."""
    console = Console()

    res = construct_pentagon_decagon(radius=60)
    prop_table = Table(title="Almagest I.10a — Golden Pentagon-Decagon Construction (R = 60)")
    prop_table.add_column("Geometric Invariant", style="cyan bold")
    prop_table.add_column("Exact Symbolic Expression", style="green")
    prop_table.add_row("Golden Ratio φ", f"{PHI}")
    prop_table.add_row("Constructed Point E (bisect DC)", f"({res.E.x}, {res.E.y})")
    prop_table.add_row("Constructed Point Z (arc EB ∩ AD)", f"({res.Z.x}, {res.Z.y})")
    prop_table.add_row("Decagon Side s_10 = DZ", f"{res.decagon_length}")
    prop_table.add_row(
        "Ratio DZ / R == φ⁻¹",
        f"{res.decagon_over_radius} (exact match: {sp.simplify(res.decagon_over_radius - PHI_INV) == 0})",
    )
    prop_table.add_row("Pentagon Side s_5 = BZ", f"{res.pentagon_length}")
    prop_table.add_row(
        "Euclid XIII.10 (DZ² + DB² == BZ²)",
        f"{sp.simplify(res.decagon_length**2 + res.radius**2)} == {sp.simplify(res.pentagon_length**2)}",
    )
    prop_table.add_row("Proof Ledger Steps Recorded", str(len(res.model.steps)))
    console.print(prop_table)

    chord_table = Table(title="Almagest I.10-11 — Exact Radical & Sexagesimal Chord Cascade (2R = 120)")
    chord_table.add_column("Arc θ (°)", style="bold yellow")
    chord_table.add_column("Exact SymPy Radical", style="cyan")
    chord_table.add_column("Computed Base-60", style="green")
    chord_table.add_column("Heiberg (1898)", style="magenta")

    for entry in build_radical_chord_table(radius=60):
        h_str = entry.heiberg_sexagesimal.format_greek_style() if entry.heiberg_sexagesimal else "-"
        chord_table.add_row(
            str(entry.arc_deg),
            str(entry.exact_expr),
            entry.sexagesimal.format_greek_style(),
            h_str,
        )
    console.print(chord_table)

    pi_ver = verify_ptolemy_pi()
    pi_table = Table(title="Almagest I.10 & VI.7 — Ptolemy's Inequality Lemma & Sexagesimal π")
    pi_table.add_column("Quantity", style="cyan bold")
    pi_table.add_column("Value", style="green")
    pi_table.add_row("Lower Bound (2/3)·crd(1½°)", f"{float(pi_ver.exact_lower_bound.evalf()):.10f}")
    pi_table.add_row("Upper Bound (4/3)·crd(¾°)", f"{float(pi_ver.exact_upper_bound.evalf()):.10f}")
    pi_table.add_row("Strict Inequality Holds?", str(pi_ver.strict_inequality_holds))
    pi_table.add_row("Sexagesimal crd(1°)", f"{pi_ver.ptolemy_crd_1_deg.format_greek_style()} = {pi_ver.ptolemy_crd_1_deg.rational}")
    pi_table.add_row(
        "Implied Sexagesimal π = 3·crd(1°)",
        f"{pi_ver.ptolemy_pi.format_greek_style()} = {pi_ver.pi_rational} ≈ {float(pi_ver.pi_rational):.8f}",
    )
    console.print(pi_table)


if __name__ == "__main__":
    run_demo()

"""Command-line summary runner for ``geometor.ptolemy``."""

from __future__ import annotations

from rich.console import Console
from rich.table import Table

from geometor.ptolemy import (
    build_radical_chord_table,
    construct_astrolabe_planisphere,
    construct_pentagon_decagon,
    construct_planar_menelaus,
    construct_ptolemy_quadrilateral,
    verify_ptolemy_pi,
    verify_spherical_menelaus,
)


def main() -> None:
    """Run all exact symbolic Ptolemy verifications and display a Rich summary table."""
    console = Console()

    pent = construct_pentagon_decagon()
    quad = construct_ptolemy_quadrilateral(preset="pythagorean_65")
    men_p = construct_planar_menelaus()
    men_s = verify_spherical_menelaus()
    pi_v = verify_ptolemy_pi()
    astro = construct_astrolabe_planisphere()
    chords = build_radical_chord_table()

    table = Table(title="GEOMETOR • Claudius Ptolemy Symbolic Verification Summary")
    table.add_column("Locus", style="cyan bold")
    table.add_column("Theorem / Construction", style="yellow")
    table.add_column("Exact Symbolic Result", style="green")

    table.add_row(
        "Almagest I.10a",
        "Golden Decagon & Pentagon (R=60)",
        f"DZ/R = {pent.decagon_over_radius}, DZ = {pent.decagon_length}, BZ = {pent.pentagon_length}",
    )
    table.add_row(
        "Almagest I.10b",
        "Ptolemy's Cyclic Quad (D=65)",
        f"AC·BD = {quad.diagonals[0]}×{quad.diagonals[1]} = {quad.lhs_product} == {quad.rhs_sum}",
    )
    table.add_row(
        "Almagest I.10-11",
        "Radical Chord Chain & π",
        f"{len(chords)} exact chords; crd(1°) = {pi_v.ptolemy_crd_1_deg.format_greek_style()}, π = {pi_v.ptolemy_pi.format_greek_style()} ({pi_v.pi_rational})",
    )
    table.add_row(
        "Almagest I.13",
        "Planar & Spherical Menelaus",
        f"CA:AE = {men_p.ratio_ca_ae}; 3D Θ,K,Λ collinear={men_s.are_theta_k_lambda_collinear} (sq ratio={men_s.lhs_chord_ratio_sq})",
    )
    table.add_row(
        "Planisphaerium 1-4",
        "Stereographic Astrolabe (R=60)",
        f"r_Can={astro.cancer_radius}, r_Cap={astro.capricorn_radius}, r_Can·r_Cap={astro.inversion_product}=60², r_Ecl={astro.ecliptic_radius}",
    )
    console.print(table)


if __name__ == "__main__":
    main()

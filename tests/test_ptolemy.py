"""Test suite verifying exact symbolic constructions and apparatus for ``geometor.ptolemy``."""

from __future__ import annotations

import sympy as sp
import sympy.geometry as spg

from geometor.ptolemy import (
    PHI_INV,
    Sexagesimal,
    build_radical_chord_table,
    chord_difference,
    chord_half_arc,
    chord_sum,
    compute_solar_declination,
    construct_almucantar_circle,
    construct_astrolabe_planisphere,
    construct_pentagon_decagon,
    construct_planar_menelaus,
    construct_ptolemy_quadrilateral,
    exact_chord,
    from_sexagesimal,
    project_sphere_circle_plane,
    prove_circle_preservation_symbolically,
    prove_conformal_metric_symbolically,
    prove_parallel_inversion_symbolically,
    prove_ptolemy_theorem_universally,
    stereographic_forward,
    stereographic_inverse,
    to_sexagesimal,
    verify_ptolemy_pi,
    verify_spherical_menelaus,
)


def _assert_zero_floats_in_model(model: object) -> None:
    """Assert that every geometric primitive in ``model`` contains zero ``sp.Float`` atoms."""
    mapping = model if isinstance(model, dict) else {}
    for geom_key in mapping:
        if isinstance(geom_key, (spg.Point, spg.Line, spg.Circle, spg.Segment, spg.Polygon)):
            floats = geom_key.atoms(sp.Float)
            assert not floats, f"Found forbidden sp.Float {floats} in {geom_key}"


def test_pentagon_decagon_golden_proposition() -> None:
    """Verify Almagest I.10a Golden Decagon & Pentagon construction over Q(phi) with zero floats."""
    res = construct_pentagon_decagon(radius=60)
    _assert_zero_floats_in_model(res.model)

    assert sp.simplify(res.decagon_over_radius - PHI_INV) == 0
    assert sp.simplify(res.decagon_length - 30 * (sp.sqrt(5) - 1)) == 0
    assert sp.simplify(res.decagon_length**2 + sp.Integer(60) ** 2 - res.pentagon_length**2) == 0
    assert any(step.kind == "conclude" for step in res.model.steps)


def test_radical_chord_table_and_sexagesimal_pi() -> None:
    """Verify Ptolemy's radical chord chain, Heiberg sexagesimals, and pi = 3;8,30 = 377/120."""
    entries = build_radical_chord_table(radius=60)
    assert len(entries) == 10
    for entry in entries:
        assert not entry.exact_expr.atoms(sp.Float)
        if entry.heiberg_sexagesimal is not None:
            # Every computed chord matches Heiberg's printed base-60 value within 1'' (1/3600)
            diff = abs(entry.sexagesimal.rational - entry.heiberg_sexagesimal.rational)
            assert diff <= sp.Rational(1, 3600)

    # Exact difference, sum, and half-arc consistency
    c72 = exact_chord(72)
    c60 = exact_chord(60)
    c12 = exact_chord(12)
    assert sp.simplify(chord_difference(c72, c60) - c12) == 0
    assert sp.simplify(chord_sum(c60, c12) - c72) == 0
    assert sp.simplify(chord_half_arc(c72) - exact_chord(36)) == 0

    # Sexagesimal pi = 3;8,30 = 377/120
    pi_ver = verify_ptolemy_pi()
    assert pi_ver.strict_inequality_holds
    assert pi_ver.matches_to_seconds
    assert pi_ver.ptolemy_crd_1_deg == Sexagesimal(1, (2, 50))
    assert pi_ver.ptolemy_pi == Sexagesimal(3, (8, 30))
    assert pi_ver.pi_rational == sp.Rational(377, 120)
    assert from_sexagesimal(3, 8, 30) == sp.Rational(377, 120)
    assert to_sexagesimal(sp.Rational(377, 120), places=2).format_greek_style() == "3;8,30"


def test_ptolemy_cyclic_quadrilateral_theorem() -> None:
    """Verify Ptolemy's Theorem on both Pythagorean-65 and Brahmagupta rational cyclic quads."""
    res65 = construct_ptolemy_quadrilateral(preset="pythagorean_65")
    _assert_zero_floats_in_model(res65.model)
    assert res65.sides == (sp.Integer(25), sp.Integer(39), sp.Integer(60), sp.Integer(52))
    assert res65.diagonals == (sp.Integer(56), sp.Integer(63))
    assert res65.lhs_product == sp.Integer(3528)
    assert res65.rhs_sum == sp.Integer(3528)
    assert res65.ae_segment_length == sp.Rational(500, 21)
    assert res65.ec_segment_length == sp.Rational(676, 21)

    res_brahm = construct_ptolemy_quadrilateral(preset="brahmagupta")
    _assert_zero_floats_in_model(res_brahm.model)
    assert sp.simplify(res_brahm.lhs_product - res_brahm.rhs_sum) == 0

    assert prove_ptolemy_theorem_universally() == 0


def test_planar_and_spherical_menelaus() -> None:
    """Verify Almagest I.13 Planar & 3D Spherical Menelaus Lemmas and I.14 solar declination."""
    men_p = construct_planar_menelaus()
    _assert_zero_floats_in_model(men_p.model)
    assert sp.simplify(men_p.ratio_ca_ae - men_p.compound_synthesin) == 0
    assert sp.simplify(men_p.ratio_ce_ea - men_p.compound_diairesin) == 0

    men_s = verify_spherical_menelaus()
    assert men_s.are_theta_k_lambda_collinear
    assert sp.simplify(men_s.lhs_chord_ratio_sq - men_s.rhs_compound_chord_ratio_sq) == 0

    d30 = compute_solar_declination(30)
    d60 = compute_solar_declination(60)
    assert abs(d30.declination_deg_sexagesimal.rational - d30.heiberg_declination.rational) <= sp.Rational(1, 60)
    assert d60.declination_deg_sexagesimal == d60.heiberg_declination


def test_stereographic_projection_and_astrolabe() -> None:
    """Verify Planisphaerium stereographic circle preservation, conformality, and astrolabe."""
    circ_proof = prove_circle_preservation_symbolically()
    assert circ_proof["sphere_residual"] == 0

    conf_factor = prove_conformal_metric_symbolically()
    x, y = sp.symbols("x y")
    assert sp.simplify(conf_factor - sp.Integer(4) / (1 + x**2 + y**2) ** 2) == 0

    inv = prove_parallel_inversion_symbolically()
    R = sp.Symbol("R", positive=True)
    assert sp.simplify(inv["product"] - R**2) == 0

    # Plane through South Pole (d == c) maps to a straight line (meridians)
    meridian_proj = project_sphere_circle_plane(sp.Integer(3), sp.Integer(-4), sp.Integer(1), sp.Integer(1))
    assert meridian_proj.is_line

    # North Pole (0, 0, 1) -> (0, 0)
    assert stereographic_forward(0, 0, 1) == (0, 0)
    assert stereographic_inverse(0, 0) == (0, 0, 1)

    astro = construct_astrolabe_planisphere(equator_radius=60, half_obliquity_tan=sp.Rational(1, 5))
    _assert_zero_floats_in_model(astro.model)
    assert astro.cancer_radius == sp.Integer(40)
    assert astro.capricorn_radius == sp.Integer(90)
    assert astro.ecliptic_radius == sp.Integer(65)
    assert astro.inversion_product == sp.Integer(3600)

    horizon = construct_almucantar_circle(sp.Rational(3, 5), sp.Rational(4, 5), sp.Integer(0), equator_radius=60)
    assert not horizon.is_line
    assert horizon.center == (sp.Integer(0), sp.Integer(80))
    assert horizon.radius_sq == sp.Integer(10000)

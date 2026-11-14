r"""Exact symbolic geometry and Digital Scriptorium apparatus for Claudius Ptolemy.

Covers *Almagest* (*Μαθηματικὴ Σύνταξις*, Book I, Chs. 1–14, ed. J. L. Heiberg 1898)
and *Planisphaerium* (ed. J. L. Heiberg 1907):

- :mod:`geometor.ptolemy.pentagon_chords`: Ptolemy's Golden Pentagon–Decagon construction
  over $\mathbb{Q}(\phi)$, closed-form radical chord calculus, sexagesimal base-60 arithmetic,
  and Ptolemy's Inequality Lemma bounding $\operatorname{crd}(1^\circ) \approx 1;2,50$ and
  $\pi \approx 3;8,30 = \frac{377}{120}$.
- :mod:`geometor.ptolemy.cyclic_quadrilateral`: Exact ``geometor.model`` construction and
  universal rational proof of Ptolemy's Theorem ($AC \cdot BD = AB \cdot CD + BC \cdot DA$).
- :mod:`geometor.ptolemy.menelaus_sphaerica`: Planar and 3D Spherical Menelaus transversal
  lemmas (*Almagest* I.13) and solar declination chord ratios (*Almagest* I.14).
- :mod:`geometor.ptolemy.stereographic`: Exact 3D-to-2D stereographic projection, universal
  circle-preservation & conformal metric proofs, circular inversion of opposite parallels,
  and astrolabe tropics/ecliptic/almucantar constructions (*Planisphaerium* §§1–4).
"""

from __future__ import annotations

__version__ = "0.1.1"

from geometor.ptolemy.cyclic_quadrilateral import (
    CyclicQuadrilateralResult,
    construct_ptolemy_quadrilateral,
    prove_ptolemy_theorem_universally,
)
from geometor.ptolemy.menelaus_sphaerica import (
    PlanarMenelausResult,
    SolarDeclinationEntry,
    SphericalMenelausResult,
    compute_solar_declination,
    construct_planar_menelaus,
    verify_spherical_menelaus,
)
from geometor.ptolemy.pentagon_chords import (
    PHI,
    PHI_INV,
    PTOLEMY_DIAMETER,
    PTOLEMY_RADIUS,
    ChordEntry,
    PentagonDecagonResult,
    PtolemyPiVerification,
    Sexagesimal,
    build_radical_chord_table,
    chord_difference,
    chord_half_arc,
    chord_sum,
    construct_pentagon_decagon,
    exact_chord,
    from_sexagesimal,
    supplementary_chord,
    to_sexagesimal,
    verify_ptolemy_pi,
)
from geometor.ptolemy.stereographic import (
    AstrolabePlanisphereResult,
    ProjectedCircleData,
    construct_almucantar_circle,
    construct_astrolabe_planisphere,
    project_sphere_circle_plane,
    prove_circle_preservation_symbolically,
    prove_conformal_metric_symbolically,
    prove_parallel_inversion_symbolically,
    stereographic_forward,
    stereographic_inverse,
)

__all__ = [
    "AstrolabePlanisphereResult",
    "ChordEntry",
    "CyclicQuadrilateralResult",
    "PHI",
    "PHI_INV",
    "PTOLEMY_DIAMETER",
    "PTOLEMY_RADIUS",
    "PentagonDecagonResult",
    "PlanarMenelausResult",
    "ProjectedCircleData",
    "PtolemyPiVerification",
    "Sexagesimal",
    "SolarDeclinationEntry",
    "SphericalMenelausResult",
    "__version__",
    "build_radical_chord_table",
    "chord_difference",
    "chord_half_arc",
    "chord_sum",
    "compute_solar_declination",
    "construct_almucantar_circle",
    "construct_astrolabe_planisphere",
    "construct_pentagon_decagon",
    "construct_planar_menelaus",
    "construct_ptolemy_quadrilateral",
    "exact_chord",
    "from_sexagesimal",
    "project_sphere_circle_plane",
    "prove_circle_preservation_symbolically",
    "prove_conformal_metric_symbolically",
    "prove_parallel_inversion_symbolically",
    "prove_ptolemy_theorem_universally",
    "stereographic_forward",
    "stereographic_inverse",
    "supplementary_chord",
    "to_sexagesimal",
    "verify_ptolemy_pi",
    "verify_spherical_menelaus",
]

:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor • ptolemy`` reconstructs the foundational mathematical, trigonometric, and projective treatises of :person:`Claudius Ptolemy <ptolemy>` (c. 100–170 CE)—the supreme mathematical astronomer of Greco-Roman antiquity working in Alexandria. In Book I of the *Syntaxis Mathematica* (commonly known as the *Almagest*, c. 150 CE), Ptolemy lays down the computational and geometric bedrock of classical quantitative astronomy. Here he establishes the sphericity of the heavens and earth, the sexagesimal circle of chords ($R = 60^p$, $D = 120^p$), his ingenious single-circle construction of the regular decagon and pentagon over the golden ratio field $\mathbb{Q}(\phi)$, the fundamental theorem on cyclic quadrilaterals bearing his name ($AC \cdot BD = AB \cdot CD + BC \cdot DA$), the chord difference, sum, and half-arc lemmas, the inequality lemma bounding $\operatorname{crd} 1^\circ$ (yielding $\pi \approx 3;8,30 = \frac{377}{120}$), and the complete planar and spherical transversal trigonometry of Menelaus of Alexandria.

Alongside the *Almagest*, this edition reconstructs Ptolemy's *Planisphaerium*, the seminal work introducing the mathematical theory of **stereographic projection**. By projecting points on the celestial sphere from the South Celestial Pole onto the equatorial plane, Ptolemy proves that circles on the sphere project as circles on the plane—a conformal mapping grounded in :person:`Apollonius of Perga's <apollonius>` subcontrary sections of oblique cones (*Conics* I.5)—providing the foundational geometry for the planispheric astrolabe.

The implicit deductive structure of these masterpieces is extracted across four units (*Pentagon and Decagon Chords*, *Ptolemy's Theorem and Chord Calculus*, *Menelaus Sphaerica and Transversal Trigonometry*, and *Planisphaerium and Stereographic Projection*). Powered by ``photon-platform/publish``, every unit coordinates original English translations, verbatim polytonic Greek from J. L. Heiberg's 1898 Teubner edition, medieval scientific Latin from Hermann of Carinthia's 1143 translation (Heiberg 1907), deductive structural summaries, and critical notes featuring calibrated ``.euclid-graphic`` SVG diagrams and 100% exact symbolic demonstrations. Within the GEOMETOR canon, Ptolemy connects directly to :person:`Euclid's <euclid>` *Elements* Books III, IV, and XIII (``geometor/euclid`` & ``geometor/elements``), :person:`Proclus's <proclus>` *Commentary* (``geometor/proclus``), and :person:`Pappus of Alexandria's <pappus>` *Collection* (``geometor/pappus``), realizing ancient trigonometry in exact radical towers and Rational Trigonometry invariants.

The GEOMETOR Mission
--------------------

The GEOMETOR project, initiated and directed by **phi ARCHITECT**, is dedicated to the complete digital renaissance and computational re-grounding of classical geometry and axiomatic thought. The mission advances across three foundational pillars:

1. **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans, static PDFs, and raw OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. GEOMETOR elevates historical prose, marginal scholia, primary-source folios (via ``publish folio`` directives), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs. Each proposition, enunciation, step, hypothesis, and proof is rendered uniquely identifiable, computationally navigable, and interoperable across the entire historical canon.
2. **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions and spatial relations in 100% exact symbolic algebra via `SymPy` and Norman J. Wildberger's Rational Trigonometry invariants (quadrance, spread, cross-ratio). By operating strictly over exact algebraic number fields rather than floating-point approximations, GEOMETOR eliminates rounding degradation, preserves absolute mathematical truth, and guarantees that every geometric demonstration is provably exact.
3. **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and accessible EPUB 3 editions (powered by ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG exploratory laboratories (``geometor.explorer``), ultra-high-definition visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

All primary textual witnesses archived in ``resources/almagest_geometry/sources/`` are **100% Public Domain** worldwide and audited in ``resources/almagest_geometry/sources_manifest.json``:

* **Greek Textual Witness (*Almagest* Book I)**: :person:`Johan Ludvig Heiberg's <heiberg>` definitive critical Teubner edition, *Claudii Ptolemaei Opera quae exstant omnia*, Vol. I: *Syntaxis Mathematica*, Pars I (Leipzig: B. G. Teubner, 1898, pp. 4–11, 30–49, 66–81), collated from the ninth-century uncial witness *Codex Vaticanus Graecus 1594* (*A*) and Venice Marciana codices.
* **Latin Textual Witness (*Planisphaerium*)**: J. L. Heiberg's critical Teubner edition, *Claudii Ptolemaei Opera quae exstant omnia*, Vol. II: *Opera Astronomica Minora* (Leipzig: B. G. Teubner, 1907, pp. 225–259), presenting the 1143 Latin translation of :person:`Hermann of Carinthia <hermann>` (*Codex Dresdensis Db 87*) from Arabic transmission (*Thābit ibn Qurra / Maslama al-Majrīṭī*).
* **Historical Collation Editions**: Abbé Nicolas B. Halma's Greek-French edition (*Composition mathématique de Claude Ptolémée*, Paris: Henri Grand, 1813) and Karl Manitius's German translation (*Handbuch der Astronomie*, Leipzig: B. G. Teubner, 1912).
* **Original English Translation & Philology**: Fresh translations and scholarly commentary prepared specifically for GEOMETOR, avoiding modern copyrighted translations, verified against the Greek and Latin witnesses, and accompanied by 100% exact symbolic Python demonstrations in ``src/geometor/ptolemy/``.

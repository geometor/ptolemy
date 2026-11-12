=========
Changelog
=========

0.1.0 (Initial Codex & Symbolic Engine)
---------------------------------------

* **Digital Scriptorium Book Codex (`docsrc/almagest_geometry/`)**:
  * Four multi-track units (`:layout: book`) pairing original GEOMETOR English translations with scan-verified polytonic Greek (Heiberg 1898) and scientific Latin (Heiberg 1907), executive summaries, and historical/mathematical commentary.
  * Nine interactive `.euclid-graphic` SVG plates (`scripts/build_figures.py`) wired to `:g:`, `:eq:`, and `:just:` roles.
  * Complete apparatus (`concordance`, `bibliography`, `persons`, `glossary`) backed by JSON registries in `resources/almagest_geometry/`.
* **Exact Symbolic Geometry (`src/geometor/ptolemy/`)**:
  * `pentagon_chords`: Ptolemy's single-circle regular decagon & pentagon construction over $\mathbb{Q}(\phi)$, radical chord cascade ($120^\circ \to \frac{3}{4}^\circ$), sexagesimal arithmetic, and $\pi \approx 3;8,30 = \frac{377}{120}$.
  * `cyclic_quadrilateral`: Rational cyclic quadrilateral `@proposition` constructions (`pythagorean_65` & `brahmagupta`) and universal rational proof of Ptolemy's Theorem.
  * `menelaus_sphaerica`: Planar and 3D Spherical Menelaus lemmas and *Almagest* I.14 solar declination solver.
  * `stereographic`: 3D-to-2D stereographic projection, universal circle-preservation & conformal metric proofs, circular inversion ($r_+ \cdot r_- = R_{\text{eq}}^2$), and astrolabe construction.

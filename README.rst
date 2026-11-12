================
GEOMETOR Ptolemy
================

Digital Scriptorium Book Codex (``:layout: book``) and **100% exact symbolic SymPy / ``geometor.model`` constructions** for **Claudius Ptolemy (c. 100–170 CE)**:

1. ***Almagest* (*Μαθηματικὴ Σύνταξις*, Book I, Chapters 1–14)** — Grounded in J. L. Heiberg's Teubner critical Greek edition (*Syntaxis Mathematica*, Vol. I.1, Leipzig, 1898): cosmic sphericity, the sexagesimal chord circle ($R = 60^p, D = 120^p$), **Ptolemy's single-circle Golden Pentagon–Decagon construction**, **Ptolemy's Theorem on Cyclic Quadrilaterals** ($AC \cdot BD = AB \cdot CD + BC \cdot DA$), difference/sum/half-arc chord calculus, **Ptolemy's Inequality Lemma** ($\operatorname{crd} 1^\circ \approx 1;2,50 \implies \pi \approx 3;8,30 = \frac{377}{120}$), and **Planar & Spherical Menelaus Trigonometry**.
2. ***Planisphaerium* (Sections 1–4)** — Grounded in J. L. Heiberg's Teubner critical Latin edition (*Opera Astronomica Minora*, Vol. II, Leipzig, 1907; trans. Hermann of Carinthia, Toulouse, 1143): **stereographic projection** from the South Celestial Pole onto the equatorial plane, conformal circle-preservation via Apollonius *Conics* I.5, circular inversion of opposite parallels ($r_{\text{Cap}} \cdot r_{\text{Can}} = R_{\text{eq}}^2$), and planispheric astrolabe geometry.

Highlights
----------

* **Zero Floating-Point Coordinates**: Every ``geometor.model.Model`` construction runs with ``auto_intersect=False`` strictly over $\mathbb{Q}$, $\mathbb{Q}(\phi)$, and exact SymPy radical towers.
* **Multi-Track Scholarly Codex**: Synchronized **English**, **Greek (1898)** / **Latin**, **Summary**, and **Notes** tracks paired with 9 interactive ``.euclid-graphic`` SVG figures and cross-corpus GEOMETOR concordances.

Quick Start
-----------

.. code-block:: bash

   # Lint & test
   ruff check src scripts demos tests
   /home/phi/PROJECTS/geometor/.venv/bin/python -m pytest

   # Run symbolic Rich demonstrations
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/pentagon_chords.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/cyclic_quadrilateral.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/stereographic.py

   # Build Book Codex HTML into docs/
   publish build

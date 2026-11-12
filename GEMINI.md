# GEOMETOR Ptolemy (`geometor-ptolemy`)

Digital Scriptorium Book Codex (`:layout: book`) and 100% exact symbolic `SymPy` / `geometor.model` demonstrations for **Claudius Ptolemy (c. 100–170 CE)**:

1. ***Almagest* (*Μαθηματικὴ Σύνταξις*, Book I, Chapters 1–14)**: Edited from J. L. Heiberg's Teubner Greek edition (*Syntaxis Mathematica*, Vol. I.1, 1898), covering cosmic preliminaries, the sexagesimal chord circle ($R = 60^p, D = 120^p$), **Ptolemy's Golden Pentagon–Decagon Construction** over $\mathbb{Q}(\phi)$, **Ptolemy's Theorem on Cyclic Quadrilaterals** ($AC \cdot BD = AB \cdot CD + BC \cdot DA$), difference/sum/half-arc chord calculus, **Ptolemy's Inequality Lemma** ($\operatorname{crd} 1^\circ \approx 1;2,50 \implies \pi \approx 3;8,30 = \frac{377}{120}$), and **Planar & 3D Spherical Menelaus Trigonometry**.
2. ***Planisphaerium* (Sections 1–4)**: Edited from J. L. Heiberg's Teubner Latin edition (*Opera Astronomica Minora*, Vol. II, 1907; trans. Hermann of Carinthia, 1143), covering South-Pole **stereographic projection** onto the equatorial plane, conformal circle-preservation via Apollonius *Conics* I.5, circular inversion of opposite parallels ($r_{\text{Cap}} \cdot r_{\text{Can}} = R_{\text{eq}}^2$), and planispheric astrolabe geometry.

## Key Modules (`src/geometor/ptolemy/`)

- `pentagon_chords.py`: Single-circle regular decagon ($s_{10} = R/\phi$) & pentagon ($s_5 = \sqrt{R^2 + s_{10}^2}$) `@proposition` construction, closed-form radical chord tower, base-60 `Sexagesimal` arithmetic, and `verify_ptolemy_pi()`.
- `cyclic_quadrilateral.py`: Rational cyclic quadrilateral `@proposition` (`pythagorean_65` & `brahmagupta` presets) with pure-rational rhombus angle-bisector construction of Ptolemy's point $E \in AC$ and universal 4-variable SymPy proof.
- `menelaus_sphaerica.py`: Planar Menelaus sector `@proposition` (*kata synthesin* & *kata diairesin*), 3D rational sphere central-projection verification (`Theta, K, Lambda` collinearity), and I.14 solar declination chord solver.
- `stereographic.py`: Exact 3D-to-2D South-Pole stereographic forward/inverse maps, universal circle-preservation & conformal metric proofs, §4 parallel-inversion proof, and astrolabe `@proposition` construction.
- `sphinx_ext.py`: Registers `<stem>-el` ("Greek (1898)") alongside native `<stem>-la` ("Latin"), `en`, `summary`, and `notes` tracks in `photon-platform/publish` and binds offline local intersphinx inventories.

## Verification Commands

```bash
/home/phi/.local/bin/ruff check src scripts demos tests
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest
/home/phi/.local/bin/publish build
```

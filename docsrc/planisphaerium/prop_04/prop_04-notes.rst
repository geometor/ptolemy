:order: 4
:type: section
:book: Planisphaerium
:title: Section 4 · Notes
:folio: heiberg_1907_opera_minora_vol2:0442
:tracks: English: prop_04-en | Latin: prop_04-la | Summary: prop_04-summary | Notes: prop_04-notes

.. _planisphaerium-prop-04-notes:

Section 4 · Notes
=================

Connection to the *Almagest* & Practical Astrolabe Fabrication
--------------------------------------------------------------

1. **Explicit Cross-Reference to the *Almagest***:
   Ptolemy's explicit phrase on page 234, line 16—*quemadmodum in Almagesti constitutum est* ("as was established in the Almagest")—provides crucial internal evidence directly linking the *Planisphaerium* to the *Syntaxis Mathematica*. In the Arabic and medieval Latin traditions, this citation cemented the complementary status of the two works: the *Almagest* providing spherical astronomy and tabular parameters, and the *Planisphaerium* providing the practical planar geometry for instrument makers.

2. **Standard Astrolabe Dimensions**:
   In Islamic and Western European astrolabe workshops (from 10th-century Baghdad and al-Andalus through Renaissance Nuremberg and London), Ptolemy's exact radii from Section 4 governed the layout of every planispheric astrolabe:
   - Outer retaining rim of the *mater*: scaled to exceed $r_{\text{Cap}} \approx 92.14^p$.
   - Equator line on the plate: circle of radius $60^p$.
   - Inner horizon bounding circle: bounded by the Cancer circle ($r_{\text{Can}} \approx 39.07^p$).
   - Ecliptic ring of the Rete: eccentric circle of diameter $131;12,34^p$ shifted along the meridian by $26;31,58^p$.

3. **Symbolic Verification in ``geometor.ptolemy``**:
   In :func:`geometor.ptolemy.stereographic.construct_astrolabe_planisphere`, the geometric relationship $ez \cdot eh = ed^2$ is verified symbolically in pure algebra, establishing that the product of the radii is independent of the choice of obliquity $\varepsilon$, being a geometric property of stereographic projection itself.

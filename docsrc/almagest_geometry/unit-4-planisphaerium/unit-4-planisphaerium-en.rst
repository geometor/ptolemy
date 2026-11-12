.. _unit-4-planisphaerium-en:

Unit IV · Planisphaerium: Stereographic Projection & Astrolabe Geometry
=======================================================================

*Planisphaerium*, Sections 1–4 (:cite:`Heiberg 1907, Vol. II, pp. 227–234 <heiberg:1907>`)
------------------------------------------------------------------------------------------

Section 1 · Stereographic Projection of Equator, Tropics & Ecliptic (`Heiberg II, pp. 227–229`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. picture:: /_static/figures/fig09_planisphaerium_stereographic_astrolabe.svg

:line:`p. 227` Since it is possible, O :person:`Syrus <syrus>` (*Jesure*), and frequently necessary, that the circles occurring upon the solid sphere be represented in a flat plane just as if it actually were flat, in harmony with those things demonstrated upon the solid sphere, I judged it essential to investigate this method of construction as well.

Its principle rests upon placing **one single circle**, :g:`abgd <cABGD>`, in place of the **celestial equator** (*qui rectam speram determinat*), described around center :g:`e <E>`, which takes the place of the **visible [North] Pole** (*manifesti poli*). Through the center we draw two diameters cutting one another at right angles, :g:`ag <MK>` and :g:`bd <BD_ast>`, representing two great circles drawn through the poles perpendicular both to the equator and to one another (*the solstitial and equinoctial colures*).

Next, every circle parallel to the equator—because all points along its circumference maintain an equal distance from the poles—will likewise be described in the plane around the same center :g:`e <E>`, at distances cut off by visual rays drawn **from the hidden [South] Pole** (:g:`South Pole <S>`):

* Circles on the sphere lying toward the **visible [North] Pole** (such as the **Tropic of Cancer**) fall **inside** the equatorial circle :g:`abgd <cABGD>`, because straight lines drawn from the South Pole through northern parallels meet the equatorial plane closer to :g:`e <E>` (:g:`tl <cTL>`).
* Circles on the sphere lying toward the **hidden [South] Pole** (such as the **Tropic of Capricorn**) fall **outside** the equatorial circle :g:`abgd <cABGD>`, because rays from the South Pole through southern parallels diverge outward before piercing the extended equatorial plane (:g:`km <cKM>`).

:line:`p. 228` **Theorem (The Projected Oblique Zodiacal Circle Bisects the Equator).** Now let :g:`tl <cTL>` be the parallel nearest the visible pole (Cancer) and :g:`km <cKM>` the parallel nearest the hidden pole (Capricorn), cut by meridian :g:`km <MK>` at :g:`t <T>`, :g:`l <L>`, :g:`k <K>`, and :g:`m <M>`. Bisect segment :g:`tm <MK>` at center :g:`r <R>`, and with radius `rm = rt` describe the :term:`oblique zodiacal circle <circulus-declivis>` :g:`mbtd <cMBTD>`, tangent to the summer tropic at :g:`t <T>` and to the winter tropic at :g:`m <M>`. **I say that this circle passes directly through points** :g:`b <B>` **and** :g:`d <D>`, **thereby bisecting the equatorial circle** :g:`abgd <cABGD>` **in the plane just as the ecliptic bisects the equator on the solid sphere.**

*Demonstration.* Fold the meridian circle onto the plane so that :g:`d <D>` serves as the South Pole of projection while :g:`b <B>` serves as the North Pole, and draw straight rays from :g:`d <D>` to :g:`m <M>` (:g:`dm <MD>`) and to :g:`t <T>` (:g:`dt <TD>`):

1. On the meridian circle, the summer solstice and winter solstice are diametrically opposite on the sphere; hence the arc intercepted between the two solstitial points across the circumference is a **semicircle** ($180^\circ$).
2. Therefore, by :just:`Eucl. III.31 <III.31>`, the inscribed angle :g:`∠mdt <angMDT>` subtending that diameter at pole :g:`d <D>` is a **right angle** (`angulum mdt rectum esse`)!
3. Consequently, in the right-angled triangle :g:`mdt <triMDT>` with hypotenuse `tm` bisected at :g:`r <R>`, the circle described on diameter `tm` around center :g:`r <R>` **must pass through the right-angled vertex** :g:`d <D>`—and by symmetry across diameter `km`, through the opposite equinoctial point :g:`b <B>`!

Sections 2–3 · The Horizon & Inclined Great Circles (`Heiberg II, pp. 229–232`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 229–232` By the identical right-angle principle, Ptolemy demonstrates in Sections 2 and 3 that **every great circle inclined to the equator**—in particular the local **Horizon** (`circulus finitor`) for any terrestrial latitude $\varphi$—projects stereographically onto an eccentric circle whose center lies along the meridian line and which **bisects both the equatorial circle** (at `a` and `g`) **and the oblique zodiacal circle** :g:`mbtd <cMBTD>` at two diametrically opposite ecliptic degrees (`six signs always rising above the horizon and six below`).

Section 4 · Circular Inversion & Numerical Radii from the *Almagest* (`Heiberg II, pp. 233–234`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 233` **Theorem (Inversion of Opposite Parallels Across the Equator).** Take any two parallel circles equally distant on opposite sides of the celestial equator—specifically the winter tropic radius `ez` ($= r_{\text{Cap}}$) and the summer tropic radius `ek` ($= r_{\text{Can}}$) along meridian `eg`. Because the stereographic rays from the South Pole form right-angled similar triangles sharing the equatorial radius :g:`ed <BD_ast>` ($= R_{\text{eq}}$) as geometric mean:

$$\frac{ez}{ed} = \frac{ed}{ek}
\quad\Longleftrightarrow\quad
r_{\text{Cap}} \cdot r_{\text{Can}} = R_{\text{eq}}^2.$$

:line:`p. 234` **Explicit Sexagesimal Evaluation Citing the *Almagest*.** Ptolemy now inserts his own *Almagest* I.12 obliquity and I.11 chord values ("*quemadmodum in Almagesti constitutum est*") to compute the exact dimensions of an astrolabe plate of equatorial radius $R_{\text{eq}} = ed = 60^p$:

* Tropical distance from the equator: $\varepsilon = 23^\circ 51' 20''$ (`partibus XXIII punctis LI secundis XX`).
* Supplementary colure arcs: $90^\circ + \varepsilon = 113^\circ 51' 20''$, with supplement $90^\circ - \varepsilon = 66^\circ 8' 40''$.
* Corresponding *Almagest* chords ($D = 120^p$):

  $$\operatorname{crd}(113^\circ 51' 20'') = 100;33,28^p, \qquad \operatorname{crd}(66^\circ 8' 40'') = 65;29,0^p.$$

* Since $ez : ed = ed : ek = 100;33,28 : 65;29,0$ and $ed = 60^p$, Ptolemy obtains:

  1. **Winter Tropic (Capricorn) Radius**:

     $$r_{\text{Cap}} = ez = 92;8,15^p \qquad (\text{Latin: }\textit{partibus XCII puncta VIII secunde XV}).$$

  2. **Summer Tropic (Cancer) Radius**:

     $$r_{\text{Can}} = ek = 39;4,19^p \qquad (\text{Latin: }\textit{partes XXXIX puncta IIII secunde XVIIII}).$$

  3. **Total Diameter of the Projected Ecliptic (`tm = ez + ek`)**:

     $$D_{\text{ecl}} = 92;8,15^p + 39;4,19^p = 131;12,34^p, \qquad R_{\text{ecl}} = 65;36,17^p,$$

     with inversion check $92;8,15 \times 39;4,19 = 3599.991 \approx 3600 = 60^2$!

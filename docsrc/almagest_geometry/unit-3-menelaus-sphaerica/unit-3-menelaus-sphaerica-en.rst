.. _unit-3-menelaus-sphaerica-en:

Unit III · Table of Chords, Ecliptic Obliquity & Menelaus Sphaerica
===================================================================

*Almagest* Book I, Chapters 11–14 (:cite:`Heiberg 1898, Vol. I.1, pp. 47–78 <heiberg:1898>`)
--------------------------------------------------------------------------------------------

Chapter 11 · Layout & Error-Checking of the Table of Chords (`Heiberg I, pp. 47–63`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 47` So that on every practical occasion we may have the magnitudes of the chords set out ready at hand, we shall subjoin tables of $45$ rows each for symmetry:

1. **First Column**: Magnitudes of the arcs advancing by half a degree ($\frac{1}{2}^\circ, 1^\circ, 1\frac{1}{2}^\circ, \dots, 180^\circ$).
2. **Second Column**: Magnitudes of the :term:`subtending chords <eutheia-hypoteinousa>` in parts where the diameter is $120^p$, to two sexagesimal places (`parts; primes, seconds`).
3. **Third Column (`ἑξηκοστά`, Sixtieths)**: One-thirtieth of the chord increment across each half-degree step, giving the mean change per single arc-minute ($1'$)—imperceptibly different from exactness—for rapid linear interpolation of intermediate arcs.

Ptolemy adds an extraordinary methodological remark on **algorithmic self-verification** (`p. 47, ll. 13–20`): even if we fall into doubt regarding some **scribal error** (`γραφικῆς ἁμαρτίας`) in any chord entry in the table, the very theorems just proved enable immediate testing and correction—either from the chord of double the arc under inquiry, from its difference with other given arcs, or from the chord subtending the remainder of the semicircle!

Chapter 12 · On the Arc Between the Tropics (`Heiberg I, pp. 64–68`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 64–67` Before computing spherical tables, one single observational datum is required: the inclination (:term:`λόξωσις <loxosis>`) of the oblique zodiacal circle to the celestial equator. Ptolemy describes two meridian instruments—first a graduated bronze meridian double-ring, and second a still more convenient vertical stone or wooden quadrant plinth aligned along the meridian plane—measuring noon solar zenith distances at summer and winter solstices over multiple years.

:line:`p. 68` Across repeated solstice observations, Ptolemy finds that the full arc between the northernmost and southernmost tropics always exceeds $47\frac{2}{3}^\circ$ ($47^\circ 40'$) and falls short of $47\frac{3}{4}^\circ$ ($47^\circ 45'$). As he notes:

   *"From this rises very nearly the same ratio as that of :person:`Eratosthenes <eratosthenes>`, which :person:`Hipparchus <hipparchus>` also used: for the arc between the tropics comes to $11$ parts out of $83$ of the meridian circle."*

Since $\frac{11}{83} \times 360^\circ = 47^\circ 42' 39.03\dots'' \approx 47^\circ 42'40''$, bisecting gives Ptolemy's canonical **obliquity of the ecliptic**:

$$\varepsilon = 23^\circ 51' 20'', \qquad 2\varepsilon = 47^\circ 42' 40'', \qquad \operatorname{crd}(2\varepsilon) \approx 48;31,55^p.$$

Chapter 13 · Preliminaries for Spherical Demonstrations (`Heiberg I, pp. 68–76`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. picture:: /_static/figures/fig07_menelaus_planar_and_spherical.svg

1. Planar Menelaus Sector Lemma (`Heiberg I, pp. 68–70`)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

:line:`p. 68–69` Across two straight lines :g:`ΑΒ <AB>` and :g:`ΑΓ <AG>`, let two straight lines :g:`ΒΕ <BE>` and :g:`ΓΔ <GD>` be drawn intersecting one another at point :g:`Ζ <Z>`. **I say that the ratio of** :g:`ΓΑ <AG>` **to** :g:`ΑΕ` **is compounded of the ratio of** :g:`ΓΔ <GD>` **to** :g:`ΔΖ` **and the ratio of** :g:`ΖΒ` **to** :g:`ΒΕ <BE>`.

*Construction & Proof (:term:`κατὰ σύνθεσιν <kata-synthesin>`).* Through :g:`Ε <E>` draw :g:`ΕΗ <EH>` parallel to :g:`ΓΔ <GD>` (:just:`Eucl. I.31 <I.31>`), meeting :g:`ΑΒ <AB>` at :g:`Η <H>`.

* Since :g:`ΕΗ <EH>` $\parallel$ :g:`ΓΔ <GD>`, triangles `ΑΓΔ` and `ΑΕΗ` are equiangular (:just:`Eucl. VI.4 <VI.4>`), whence $\frac{\Gamma A}{AE} = \frac{\Gamma\Delta}{EH}$.
* Inserting the auxiliary magnitude `ΔΖ` as middle term in the ratio $\frac{\Gamma\Delta}{EH}$ gives $\frac{\Gamma A}{AE} = \frac{\Gamma\Delta}{\Delta Z} \cdot \frac{\Delta Z}{EH}$.
* Yet since :g:`ΕΗ <EH>` $\parallel$ `ΔΖ` inside triangle `ΒΕΗ`, we also have $\frac{\Delta Z}{EH} = \frac{ZB}{BE}$ (:just:`Eucl. VI.4 <VI.4>`). Therefore:

  $$\frac{\Gamma A}{AE} = \frac{\Gamma\Delta}{\Delta Z} \cdot \frac{ZB}{BE} \qquad\text{(by composition, }\text{:term:`κατὰ σύνθεσιν <kata-synthesin>`}\text{)}.$$

:line:`p. 69–70` *Second Form (:term:`κατὰ διαίρεσιν <kata-diairesin>`).* In the same way, by drawing through `Α` a parallel to :g:`ΒΕ <BE>` meeting :g:`ΓΔ <GD>` produced, Ptolemy proves the separated form:

$$\frac{\Gamma E}{EA} = \frac{\Gamma Z}{Z\Delta} \cdot \frac{\Delta B}{BA} \qquad\text{(by division, }\text{:term:`κατὰ διαίρεσιν <kata-diairesin>`}\text{)}.$$

2. Circle Chord-Division Lemmas (`Heiberg I, pp. 70–74`)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

:line:`p. 70–74` On any circle centered at $H$ with points $A, B, \Gamma$ on the circumference:

* **Internal Secant** (`pp. 70–71`): The radius $HB$ meets chord $A\Gamma$ at $E$ so that $\frac{AE}{E\Gamma} = \frac{\operatorname{crd}(2 AB)}{\operatorname{crd}(2 B\Gamma)}$, because dropping perpendiculars from $A$ and $\Gamma$ onto diameter $HB$ forms right triangles with altitudes $\frac{1}{2}\operatorname{crd}(2AB)$ and $\frac{1}{2}\operatorname{crd}(2B\Gamma)$.
* **External Secant** (`pp. 71–74`): Extending chord $\Gamma A$ to meet extended radius $HB$ outside the circle at $\Delta$ gives $\frac{\Gamma\Delta}{\Delta A} = \frac{\operatorname{crd}(2\Gamma B)}{\operatorname{crd}(2BA)}$.

3. Spherical Menelaus Theorem (`Heiberg I, pp. 74–76`)
""""""""""""""""""""""""""""""""""""""""""""""""""""""

:line:`p. 74–75` **Theorem (adapted from :person:`Menelaus <menelaus>`, :cite:`Sphaerica III.1 <menelaus:sphaerica>`).** Let great-circle arcs :g:`ΑΒ <arcAB>` and :g:`ΑΓ <arcAG>` on a sphere (each less than a semicircle) be cut by great-circle arcs :g:`ΒΕ <arcBE>` and :g:`ΓΔ <arcGD>` intersecting at :g:`Ζ <sZ>` (Panel II of Figure 7 above). **I say that the ratio** $\operatorname{crd}(2\Gamma E) : \operatorname{crd}(2EA)$ **is compounded of** $\operatorname{crd}(2\Gamma Z) : \operatorname{crd}(2Z\Delta)$ **and** $\operatorname{crd}(2\Delta B) : \operatorname{crd}(2BA)$.

*Demonstration via 3D Central Projection.* Take the center :g:`Η <sH>` of the sphere, draw radii :g:`ΗΒ`, :g:`ΗΖ <HZ>`, :g:`ΗΕ`, and join planar chords :g:`ΑΔ`, `ΓΖΔ`, and `ΓΕΑ`:

1. Chord :g:`ΑΔ` and radius `ΗΒ` lie in the plane of great circle :g:`ΑΒ <arcAB>`; let them meet at :g:`Λ <Lambda>`.
2. Chords `ΓΔ` and `ΓΑ` intersect radii :g:`ΗΖ <HZ>` and `ΗΕ` at interior points :g:`Κ <K>` and :g:`Θ <Theta>` (or chord `ΓΑ` produced meets `ΗΒ` produced; in Heiberg p. 75, `ΓΑ` extended meets `ΗΕ`—specifically, points :g:`Θ <Theta>`, :g:`Κ <K>`, :g:`Λ <Lambda>` lie simultaneously in **two distinct planes**: the plane of $\triangle A\Gamma\Delta$ and the plane of great circle :g:`ΒΖΕ <arcBE>`!).
3. By :just:`Eucl. XI.3 <XI.3>`, **the intersection of two planes is a straight line**; therefore points :g:`Θ <Theta>`, :g:`Κ <K>`, :g:`Λ <Lambda>` **lie on a single straight line** :g:`ΘΚΛ <lineThetaKLambda>` cutting the sides of planar triangle `ΑΓΔ`!
4. Applying the Planar Menelaus Lemma to $\triangle A\Gamma\Delta$ cut by transversal :g:`ΘΚΛ <lineThetaKLambda>` gives $\frac{\Gamma\Theta}{\Theta A} = \frac{\Gamma K}{K\Delta} \cdot \frac{\Delta\Lambda}{\Lambda A}$, and replacing each planar ratio by its double-arc chord ratio from the Circle Lemmas yields immediately:

$$\frac{\operatorname{crd}(2\Gamma E)}{\operatorname{crd}(2EA)}
  = \frac{\operatorname{crd}(2\Gamma Z)}{\operatorname{crd}(2Z\Delta)}
  \cdot \frac{\operatorname{crd}(2\Delta B)}{\operatorname{crd}(2BA)},
\qquad
\frac{\operatorname{crd}(2\Gamma A)}{\operatorname{crd}(2AE)}
  = \frac{\operatorname{crd}(2\Gamma\Delta)}{\operatorname{crd}(2\Delta Z)}
  \cdot \frac{\operatorname{crd}(2ZB)}{\operatorname{crd}(2BE)}.$$

Chapter 14 · Solar Declination Arcs (`Heiberg I, pp. 76–78`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. picture:: /_static/figures/fig08_solar_declination_quadrant.svg

:line:`p. 76–77` Let :g:`ΑΒΓΔ <cABGD>` be the solstitial colure through the poles :g:`Ζ <Z>` of the equator :g:`ΑΕΓ <arcAEG>` and through the solstices :g:`Β <B>`, :g:`Δ <D>` on the oblique ecliptic :g:`ΒΕΔ <arcBED>` intersecting at the vernal equinox :g:`Ε <E>`. Take any solar longitude arc `ΕΗ` $= \lambda$ along the ecliptic (for example $\lambda = 30^\circ$, one zodiacal sign from the equinox), and draw great circle :g:`ΖΗΘ <arcZHTheta>` from pole :g:`Ζ <Z>` through :g:`Η <H>` to meet the equator perpendicularly at :g:`Θ <Theta>`. We seek the solar declination arc :g:`ΗΘ <arcHTheta>` $= \delta$.

Applying the *kata synthesin* Spherical Menelaus Theorem to arcs `ΖΑ` and `ΑΕ` cut by `ΖΘ` and `ΕΒ` intersecting at :g:`Η <H>`:

$$\frac{\operatorname{crd}(2ZA)}{\operatorname{crd}(2AB)}
  = \frac{\operatorname{crd}(2Z\Theta)}{\operatorname{crd}(2\Theta H)}
  \cdot \frac{\operatorname{crd}(2HE)}{\operatorname{crd}(2EB)}.$$

Since $ZA = Z\Theta = EB = 90^\circ$, we have $\operatorname{crd}(2ZA) = \operatorname{crd}(2Z\Theta) = \operatorname{crd}(2EB) = \operatorname{crd}(180^\circ) = 120^p$, while $AB = \varepsilon = 23^\circ 51'20''$ ($\operatorname{crd} 2\varepsilon = 48;31,55^p$) and $HE = \lambda$:

$$\frac{120}{\operatorname{crd}(2\varepsilon)}
  = \frac{120}{\operatorname{crd}(2\delta)} \cdot \frac{\operatorname{crd}(2\lambda)}{120}
\quad\Longrightarrow\quad
\operatorname{crd}(2\delta) = \frac{\operatorname{crd}(2\varepsilon)\cdot\operatorname{crd}(2\lambda)}{120}.$$

:line:`p. 78` **Sample Numerical Evaluations in Heiberg I, p. 78:**

* For $\lambda = 30^\circ$: $\operatorname{crd}(60^\circ) = 60^p$, so $\operatorname{crd}(2\delta) = \frac{48;31,55 \times 60}{120} = 24;15,57^p$, whence $2\delta = 23^\circ 19'59''$ and **$\delta(30^\circ) = 11^\circ 40'$** (`μοίρας ιαʹ καὶ μʹ ἑξηκοστά`).
* For $\lambda = 60^\circ$: $\operatorname{crd}(120^\circ) = 103;55,23^p$, so $\operatorname{crd}(2\delta) = 42;1,48^p$, whence $2\delta = 41^\circ 0'18''$ and **$\delta(60^\circ) = 20^\circ 30'9''$** (`μοιρῶν κʹ λʹ θʹʹ`).

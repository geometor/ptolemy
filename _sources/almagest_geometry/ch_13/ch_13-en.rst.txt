:order: 5
:type: chapter
:book: Syntaxis Mathematica (Almagest)
:title: Chapter 13 · Preliminaries for Spherical Demonstrations & Menelaus Sphaerica
:folio: heiberg_1898_syntaxis_vol1_pt1:0078
:tracks: English: ch_13-en | Greek: ch_13-el | Summary: ch_13-summary | Notes: ch_13-notes

.. _unit-3-menelaus-sphaerica-en:
.. _almagest-ch-13-en:

Chapter 13 · Preliminaries for Spherical Demonstrations & Menelaus Sphaerica
============================================================================

*Almagest* Book I, Chapters 13–14 (:cite:`Heiberg 1898, Vol. I.1, pp. 68–78 <heiberg:1898>`)
----------------------------------------------------------------------------------------------

.. picture:: /_static/figures/fig07_menelaus_planar_and_spherical.svg

1. Planar Menelaus Sector Lemma (`Heiberg I, pp. 68–70`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 68–69` Across two straight lines :g:`ΑΒ <AB>` and :g:`ΑΓ <AG>`, let two straight lines :g:`ΒΕ <BE>` and :g:`ΓΔ <GD>` be drawn intersecting one another at point :g:`Ζ <Z>`. **I say that the ratio of** :g:`ΓΑ <AG>` **to** :g:`ΑΕ` **is compounded of the ratio of** :g:`ΓΔ <GD>` **to** :g:`ΔΖ` **and the ratio of** :g:`ΖΒ` **to** :g:`ΒΕ <BE>`.

*Construction & Proof (:term:`κατὰ σύνθεσιν <kata-synthesin>`).* Through :g:`Ε <E>` draw :g:`ΕΗ <EH>` parallel to :g:`ΓΔ <GD>` (:just:`Eucl. I.31 <I.31>`), meeting :g:`ΑΒ <AB>` at :g:`Η <H>`.

* Since :g:`ΕΗ <EH>` $\parallel$ :g:`ΓΔ <GD>`, triangles `ΑΓΔ` and `ΑΕΗ` are equiangular (:just:`Eucl. VI.4 <VI.4>`), whence $\frac{\Gamma A}{AE} = \frac{\Gamma\Delta}{EH}$.
* Inserting the auxiliary magnitude `ΔΖ` as middle term in the ratio $\frac{\Gamma\Delta}{EH}$ gives $\frac{\Gamma A}{AE} = \frac{\Gamma\Delta}{\Delta Z} \cdot \frac{\Delta Z}{EH}$.
* Yet since :g:`ΕΗ <EH>` $\parallel$ `ΔΖ` inside triangle `ΒΕΗ`, we also have $\frac{\Delta Z}{EH} = \frac{ZB}{BE}$ (:just:`Eucl. VI.4 <VI.4>`). Therefore:

  $$\frac{\Gamma A}{AE} = \frac{\Gamma\Delta}{\Delta Z} \cdot \frac{ZB}{BE} \qquad\text{(by composition, }\text{:term:`κατὰ σύνθεσιν <kata-synthesin>`}\text{)}.$$

:line:`p. 69–70` *Second Form (:term:`κατὰ διαίρεσιν <kata-diairesin>`).* In the same way, by drawing through `Α` a parallel to :g:`ΒΕ <BE>` meeting :g:`ΓΔ <GD>` produced, Ptolemy proves the separated form:

$$\frac{\Gamma E}{EA} = \frac{\Gamma Z}{Z\Delta} \cdot \frac{\Delta B}{BA} \qquad\text{(by division, }\text{:term:`κατὰ διαίρεσιν <kata-diairesin>`}\text{)}.$$

2. Circle Chord-Division Lemmas (`Heiberg I, pp. 70–74`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 70–74` On any circle centered at $H$ with points $A, B, \Gamma$ on the circumference:

* **Internal Secant** (`pp. 70–71`): The radius $HB$ meets chord $A\Gamma$ at $E$ so that $\frac{AE}{E\Gamma} = \frac{\operatorname{crd}(2 AB)}{\operatorname{crd}(2 B\Gamma)}$, because dropping perpendiculars from $A$ and $\Gamma$ onto diameter $HB$ forms right triangles with altitudes $\frac{1}{2}\operatorname{crd}(2AB)$ and $\frac{1}{2}\operatorname{crd}(2B\Gamma)$.
* **External Secant** (`pp. 71–73`): The secant through $A\Gamma$ produced meets the radius perpendicular at $K$, establishing the equivalent exterior ratio.

3. The 3D Spherical Menelaus Theorem (`Heiberg I, pp. 74–76`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 74` **Theorem (Menelaus on the Sphere).** On the surface of a sphere, let two great circle arcs :g:`ΑΒ <arcAB>` and :g:`ΑΓ <arcAG>` be intersected by two other great circle arcs :g:`ΒΕ <arcBE>` and :g:`ΓΔ <arcGD>` intersecting each other at :g:`Ζ <sZ>`, with every arc being less than a semicircle. **I say that:**

$$\frac{\operatorname{crd}(2 \Gamma E)}{\operatorname{crd}(2 EA)}
  = \frac{\operatorname{crd}(2 \Gamma Z)}{\operatorname{crd}(2 Z\Delta)}
    \cdot \frac{\operatorname{crd}(2 \Delta B)}{\operatorname{crd}(2 BA)}.$$

:line:`p. 75` *Demonstration.* Let the center of the sphere be :g:`Η <sH>`. Draw straight lines from $H$ through the vertices and intersection points of the arcs, meeting the planes of the intersecting great circles. By :just:`Eucl. XI.3 <XI.3>`, the intersection of two planes is a straight line; hence the points :g:`Θ <Theta>`, :g:`Κ <K>`, :g:`Λ <Lambda>` formed by extending the planar chords lie on a single straight line in space!

Applying the Planar Menelaus Lemma to the planar triangle formed by these chords in three dimensions, and substituting the ratio of the spherical chords via the Circle Chord-Division Lemma, yields the exact spherical theorem:

$$\frac{\operatorname{crd}(2\Gamma A)}{\operatorname{crd}(2AE)}
  = \frac{\operatorname{crd}(2\Gamma\Delta)}{\operatorname{crd}(2\Delta Z)}
    \cdot \frac{\operatorname{crd}(2 Z B)}{\operatorname{crd}(2 BE)}.$$

4. Chapter 14 · The Solar Declination Law (`Heiberg I, pp. 76–78`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 76` In Chapter 14, Ptolemy applies the Spherical Menelaus Theorem to the celestial sphere, where arc $AE$ is the celestial equator, arc $BE$ is the oblique ecliptic, and arc $ZH$ is the meridian arc of declination $\delta$ for any solar longitude $\lambda$:

:line:`p. 77–78` Since $ZA = 90^\circ$ and $EB = 90^\circ$, we have $\operatorname{crd}(2ZA) = \operatorname{crd}(180^\circ) = 120^p$ and $\operatorname{crd}(2EB) = 120^p$. The compound ratio reduces directly to:

$$\operatorname{crd}(2\delta) = \frac{\operatorname{crd}(2\varepsilon) \cdot \operatorname{crd}(2\lambda)}{120}.$$

For example:

* At $\lambda = 30^\circ$ (Taurus / end of Aries): $\operatorname{crd}(2\lambda) = \operatorname{crd}(60^\circ) = 60^p$.
* Since $\operatorname{crd}(2\varepsilon) \approx 48;31,55^p$, we obtain $\operatorname{crd}(2\delta) = \frac{48;31,55 \times 60}{120} = 24;15,57^p$, which corresponds to solar declination:

$$\delta(30^\circ) \approx 11^\circ 40'.$$

* At $\lambda = 60^\circ$: $\operatorname{crd}(2\lambda) = \operatorname{crd}(120^\circ) = 103;55,23^p$, yielding $\delta(60^\circ) \approx 20^\circ 30' 9''$.

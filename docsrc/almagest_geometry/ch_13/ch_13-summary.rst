:order: 5
:type: chapter
:book: Syntaxis Mathematica (Almagest)
:title: Chapter 13 · Summary
:folio: heiberg_1898_syntaxis_vol1_pt1:0078
:tracks: English: ch_13-en | Greek: ch_13-el | Summary: ch_13-summary | Notes: ch_13-notes

.. _almagest-ch-13-summary:

Chapter 13 · Summary
====================

The Menelaus Spherical Calculus & Solar Declination
---------------------------------------------------

1. **Planar Menelaus Sector Lemma**:
   Drawing auxiliary parallel $EH \parallel \Gamma\Delta$ demonstrates the compound ratios:

   $$\frac{\Gamma A}{AE} = \frac{\Gamma\Delta}{\Delta Z}\cdot\frac{ZB}{BE} \qquad\text{(:term:`κατὰ σύνθεσιν <kata-synthesin>`)}.$$

   $$\frac{\Gamma E}{EA} = \frac{\Gamma Z}{Z\Delta}\cdot\frac{\Delta B}{BA} \qquad\text{(:term:`κατὰ διαίρεσιν <kata-diairesin>`)}.$$

2. **3D Central Projection onto the Sphere**:
   Projecting great-circle intersections from the sphere center $H$ onto the plane of $\triangle A\Gamma\Delta$ maps great circle $BZE$ to the straight line $\Theta K\Lambda$ in space (:just:`Eucl. XI.3 <XI.3>`), establishing the spherical Menelaus theorem for double-arc chords.

3. **The Solar Declination Law (*Almagest* I.14)**:
   Specializing Spherical Menelaus to the celestial quadrant between celestial equator and ecliptic reduces the compound ratio to the exact chord equivalent of the modern spherical sine law $\sin\delta = \sin\varepsilon \sin\lambda$:

   $$\operatorname{crd}(2\delta) = \frac{\operatorname{crd}(2\varepsilon)\cdot\operatorname{crd}(2\lambda)}{120}.$$

Exact Symbolic vs. Heiberg (1898) Declination Check
---------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20 20

   * - Solar Longitude $\lambda$
     - $\operatorname{crd}(2\lambda)$
     - $\operatorname{crd}(2\delta)$
     - Computed $\delta(\lambda)$
     - Heiberg (1898, p. 78)
   * - $30^\circ$ (Taurus / 1 sign)
     - ``60;0,0``
     - ``24;15,57``
     - ``11;40,0°``
     - ``11° 40'``
   * - $60^\circ$ (Gemini / 2 signs)
     - ``103;55,23``
     - ``42;1,48``
     - ``20;30,9°``
     - ``20° 30' 9''``
   * - $90^\circ$ (Solstice)
     - ``120;0,0``
     - ``48;31,55``
     - ``23;51,20°``
     - ``23° 51' 20''``

.. _unit-3-menelaus-sphaerica-summary:

Unit III · Executive Summary
============================

From Planar Chords to Spherical Astronomy (*Almagest* I.11–I.14)
----------------------------------------------------------------

1. **Table of Chords (I.11)**: Tabulates $\operatorname{crd}(\theta)$ for $\theta = \frac{1}{2}^\circ, 1^\circ, \dots, 180^\circ$ ($360$ entries) in base-60 parts ($2R = 120^p$) together with sexagesimal *sixtieths* ($\Delta\operatorname{crd}/30$) per arc-minute and built-in algebraic checksums against scribal corruption.
2. **Obliquity of the Ecliptic (I.12)**: Confirms Eratosthenes' & Hipparchus's solstice-to-solstice ratio $2\varepsilon = \frac{11}{83} \times 360^\circ \approx 47^\circ 42'40''$, fixing $\varepsilon = 23^\circ 51'20''$ ($\operatorname{crd} 2\varepsilon = 48;31,55^p$).
3. **Planar & Spherical Menelaus Calculus (I.13)**:
   * **Planar Sector Lemma**: Drawing $EH \parallel \Gamma\Delta$ proves both $\frac{\Gamma A}{AE} = \frac{\Gamma\Delta}{\Delta Z}\cdot\frac{ZB}{BE}$ (*kata synthesin*) and $\frac{\Gamma E}{EA} = \frac{\Gamma Z}{Z\Delta}\cdot\frac{\Delta B}{BA}$ (*kata diairesin*).
   * **3D Central Projection**: Projecting great-circle intersections from sphere center $H$ onto the plane of $\triangle A\Gamma\Delta$ maps great circle $BZE$ to a straight line $\Theta K\Lambda$ (:just:`Eucl. XI.3 <XI.3>`), lifting the planar compound ratios directly onto double-arc chords on the sphere.
4. **Solar Declination Law (I.14)**: Specializing Spherical Menelaus to the right spherical quadrant $Z\text{–}E\text{–}B$ gives the exact Greek equivalent of $\sin\delta = \sin\varepsilon\sin\lambda$:

   $$\operatorname{crd}(2\delta) = \frac{\operatorname{crd}(2\varepsilon)\cdot\operatorname{crd}(2\lambda)}{120}.$$

Exact Symbolic vs. Heiberg (1898) Declination Check
---------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 22 25 18 17

   * - Solar Longitude $\lambda$
     - $\operatorname{crd}(2\lambda)$
     - $\operatorname{crd}(2\delta)$
     - Computed $\delta(\lambda)$
     - Heiberg (1898, p. 78)
   * - $30^\circ$ (1 sign)
     - ``60;0,0``
     - ``24;15,57``
     - ``11;40,0°``
     - ``11° 40'``
   * - $60^\circ$ (2 signs)
     - ``103;55,23``
     - ``42;1,48``
     - ``20;30,9°``
     - ``20° 30' 9''``
   * - $90^\circ$ (Solstice)
     - ``120;0,0``
     - ``48;31,55``
     - ``23;51,20°``
     - ``23° 51' 20''``

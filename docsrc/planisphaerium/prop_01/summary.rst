:order: 1
:type: section
:book: Planisphaerium
:title: Section 1 · Summary
:folio: heiberg_1907_opera_minora_vol2:0437

.. _planisphaerium-prop-01-summary:

Section 1 · Summary
===================

Geometric Principles of Section 1
---------------------------------

1. **The South-Pole Stereographic Projection**:
   - Center of projection: The South Celestial Pole :math:`S = (0, 0, -R)` on the sphere :math:`S^2`.
   - Projection plane: The equatorial plane :math:`Z = 0`, centered at the North Celestial Pole :math:`e = (0, 0, 0)`.
   - Ray mapping: A point :math:`P = (X, Y, Z)` on the celestial sphere is mapped along line :math:`SP` to equatorial intersection :math:`(x, y)`:

     .. math::

        (x, y) = \left(\frac{R\,X}{R + Z},\; \frac{R\,Y}{R + Z}\right).

2. **Concentric Parallels**:
   - Celestial equator: Projects to fixed circle :math:`abgd` with radius :math:`R_{\text{eq}} = 60^p`.
   - Northern parallels (:math:`Z > 0`, e.g. Tropic of Cancer): Project inside the equator with radius :math:`r_{\text{Can}} < R_{\text{eq}}`.
   - Southern parallels (:math:`Z < 0`, e.g. Tropic of Capricorn): Project outside the equator with radius :math:`r_{\text{Cap}} > R_{\text{eq}}`.

3. **Theorem on Ecliptic Bisection**:
   - The oblique ecliptic circle meets the solstitial colure at summer solstice :math:`t` and winter solstice :math:`m`.
   - The diameter :math:`tm` has center :math:`r = \frac{1}{2}(t + m)`.
   - When viewed from South Pole :math:`d`, the intercepted arc between the solstices on the sphere is a semicircle (:math:`180^\circ`).
   - By :just:`Eucl. III.31 <III.31>`, the inscribed angle :math:`\angle mdt` is a right angle (:math:`90^\circ`).
   - Therefore, the circle described on diameter :math:`tm` must pass through vertex :math:`d`—and by symmetry through :math:`b`—bisecting the equatorial circle in the plane!

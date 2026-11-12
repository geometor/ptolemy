.. _unit-4-planisphaerium-summary:

Unit IV · Executive Summary
===========================

Mathematical Architecture of Ptolemy's *Planisphaerium*
-------------------------------------------------------

1. **South-Pole Stereographic Map**: Projects every point $(X, Y, Z) \in S^2 \setminus \{(0,0,-R)\}$ from the South Celestial Pole $(0, 0, -R)$ onto the equatorial plane $Z = 0$:

   $$(x, y) = \left(\frac{R\,X}{R + Z},\; \frac{R\,Y}{R + Z}\right),
   \qquad
   (X, Y, Z) = R\left(\frac{2Rx}{R^2 + r^2},\; \frac{2Ry}{R^2 + r^2},\; \frac{R^2 - r^2}{R^2 + r^2}\right).$$

2. **Circle Preservation**: Every plane section $aX + bY + cZ + d = 0$ of $S^2$ maps to an exact circle $(c - d)(x^2 + y^2) + 2Rax + 2Rby + R^2(c + d) = 0$ (or a straight line through $e$ when $c = d$, i.e. meridians through the South Pole).
3. **Conformal Pullback**: $dX^2 + dY^2 + dZ^2 = \frac{4R^4}{(R^2 + x^2 + y^2)^2}(dx^2 + dy^2)$, preserving all angles of intersection between celestial circles!
4. **Circular Inversion of Opposite Parallels (§4)**: Parallel circles at declinations $+\delta$ and $-\delta$ project to concentric circles of radii $r(\delta) = R\tan\left(\frac{90^\circ - \delta}{2}\right)$ satisfying:

   $$r(+\delta)\cdot r(-\delta) = R^2.$$

Comparison of Exact Rational (`u = 1/5`) & Historical (`ε = 23°51'20''`) Astrolabe Radii
----------------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 36 36

   * - Astrolabe Element
     - Rational Model ($\tan\frac{\varepsilon}{2} = \frac{1}{5}, \varepsilon \approx 22^\circ 37'$)
     - Ptolemy's *Planisphaerium* §4 ($\varepsilon = 23^\circ 51'20''$)
   * - Equatorial Radius $R_{\text{eq}} = ed$
     - $60$
     - ``60;0,0``
   * - Tropic of Cancer Radius $r_{\text{Can}}$
     - $40$
     - ``39;4,19``
   * - Tropic of Capricorn Radius $r_{\text{Cap}}$
     - $90$
     - ``92;8,15``
   * - Inversion Product $r_{\text{Can}} \cdot r_{\text{Cap}}$
     - $40 \times 90 = 3600 = 60^2$
     - $39;4,19 \times 92;8,15 \approx 3600 = 60^2$
   * - Oblique Ecliptic Center & Radius
     - Center $(0, 25)$, Radius $65$
     - Center $(0,\; 26;31,58)$, Radius ``65;36,17``

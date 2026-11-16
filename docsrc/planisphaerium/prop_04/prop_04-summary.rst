:order: 4
:type: section
:book: Planisphaerium
:title: Section 4 · Summary
:folio: heiberg_1907_opera_minora_vol2:0442
:tracks: English: prop_04-en | Latin: prop_04-la | Summary: prop_04-summary | Notes: prop_04-notes

.. _planisphaerium-prop-04-summary:

Section 4 · Summary
===================

Geometric Inversion & Astrolabe Radii Calculation
-------------------------------------------------

1. **The Inversion Law for Parallels**:
   For any parallel at declination $\pm \delta$, the stereographic radii from the South Pole satisfy:

   $$r(+\delta) = R\tan\left(\frac{90^\circ - \delta}{2}\right), \qquad r(-\delta) = R\tan\left(\frac{90^\circ + \delta}{2}\right) = \frac{R}{\tan(\frac{90^\circ - \delta}{2})}.$$

   Consequently, their product is identically constant:

   $$r(+\delta) \cdot r(-\delta) = R^2 = 60^2 = 3600.$$

2. **Deductive Derivation from *Almagest* I.11–I.12 Chords**:
   With $\varepsilon = 23^\circ 51' 20''$ and $R_{\text{eq}} = 60^p$:

   - Supplement colure arc: $90^\circ + \varepsilon = 113^\circ 51' 20''$.
   - Complement colure arc: $90^\circ - \varepsilon = 66^\circ 8' 40''$.
   - Chords from *Almagest* Table ($D = 120^p$): $\operatorname{crd}(113^\circ 51' 20'') = 100;33,28^p$ and $\operatorname{crd}(66^\circ 8' 40'') = 65;29,0^p$.

   - Radius ratio:

     $$\frac{r_{\text{Cap}}}{60} = \frac{60}{r_{\text{Can}}} = \frac{100;33,28}{65;29,0} \approx 1.535626.$$

Numerical Radii Summary
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Astrolabe Circle
     - Base-60 (Heiberg II, p. 234)
     - Decimal Value ($R = 60$)
   * - Equator ($R_{\text{eq}}$)
     - ``60;0,0``
     - $60.0$
   * - Winter Tropic / Capricorn ($r_{\text{Cap}}$)
     - ``92;8,15``
     - $92.1375$
   * - Summer Tropic / Cancer ($r_{\text{Can}}$)
     - ``39;4,19``
     - $39.07194$
   * - Inversion Product ($r_{\text{Cap}} \cdot r_{\text{Can}}$)
     - ``3600;0,0``
     - $3600.0$
   * - Zodiac Total Diameter
     - ``131;12,34``
     - $131.20944$
   * - Zodiac Semidiameter
     - ``65;36,17``
     - $65.60472$
   * - Zodiac Center Offset ($d_{\text{ecl}}$)
     - ``26;31,58``
     - $26.53278$

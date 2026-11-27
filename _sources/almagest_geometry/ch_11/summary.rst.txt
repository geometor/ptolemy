:order: 11
:type: chapter
:book: Almagest (Book I)
:title: Chapter 11 · Summary
:folio: heiberg_1898_syntaxis_vol1_pt1:0058

.. _almagest-ch-11-summary:

Chapter 11 · Summary
====================

Structure & Computational Logic of the Table of Chords
------------------------------------------------------

1. **Table Organization**:
   - **Full extent**: :math:`0^\circ 30'` through :math:`180^\circ 00'` in uniform half-degree increments (360 rows across 16 printed pages, folios ``0058``–``0073``, grouped into 8 classical 45-line panels).
   - **Base parameters**: Circle circumference :math:`= 360^\circ`, diameter :math:`D = 120^p`, radius :math:`R = 60^p`.

2. **Column Structure**:
   - **Arcs** (*περιφερειῶν*): Central arc :math:`\theta` in degrees and half-degrees (:math:`\angle' = 30'`).
   - **Chords** (*εὐθειῶν*): Subtending chord :math:`\operatorname{crd}(\theta) = 120 \sin(\theta/2)` expressed in sexagesimal parts, primes, and seconds (:math:`p;\,m,s`).
   - **Sixtieths** (*ἑξηκοστῶν*): One-thirtieth of the half-degree difference :math:`\delta = \frac{1}{30}[\operatorname{crd}(\theta + 30') - \operatorname{crd}(\theta)]`, giving the linear increment per arc-minute (:math:`1'`) to sexagesimal thirds (:math:`0;\,p_1,p_2,p_3`).

3. **Interpolation Algorithm**:
   For any intermediate arc :math:`\theta + \Delta` with :math:`0 < \Delta < 30'`:

   .. math::

      \operatorname{crd}(\theta + \Delta) \approx \operatorname{crd}(\theta) + \Delta \cdot \delta.

   Because the second derivative :math:`\operatorname{crd}''(\theta) = -30\sin(\theta/2)` remains small across a :math:`30'` interval, linear interpolation has maximum error bounded by:

   .. math::

      \text{Error} \le \frac{1}{8}(\Delta\theta)^2 \cdot \max|\operatorname{crd}''| \approx \frac{1}{8}\left(\frac{\pi}{360}\right)^2 \times 30 \approx 2.8 \times 10^{-4}\text{ parts},

   comparable to a single sexagesimal second (:math:`1'' = \frac{1}{3600} \approx 2.78 \times 10^{-4}`), preserving two-place sexagesimal accuracy across the entire semicircle.

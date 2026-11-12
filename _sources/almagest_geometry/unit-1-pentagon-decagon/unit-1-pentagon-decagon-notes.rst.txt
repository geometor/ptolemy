.. _unit-1-pentagon-decagon-notes:

Unit I · Historical & Mathematical Notes
========================================

1. Ptolemy's Single-Circle Pentagon vs. Euclid IV.11
----------------------------------------------------

In :person:`Euclid's <euclid>` *Elements* IV.11, inscribing a regular pentagon in a given circle proceeds indirectly: one first constructs an auxiliary golden isosceles triangle ($72^\circ\text{–}72^\circ\text{–}36^\circ$) outside the circle via *Elements* II.11 and IV.10, inscribes a similar triangle via IV.2, and bisects its base angles.

In *Almagest* I.10 (:cite:`Heiberg 1898, pp. 32–33 <heiberg:1898>`), :person:`Ptolemy <ptolemy>` replaces that multi-stage sequence with an extraordinarily economical **direct construction inside the target circle itself**, combining :just:`Eucl. II.6 <II.6>`, :just:`Eucl. XIII.9 <XIII.9>`, and :just:`Eucl. XIII.10 <XIII.10>`:

* Because $E$ bisects radius $\Delta\Gamma = R$, the right triangle $\triangle B\Delta E$ has legs $R$ and $\frac{R}{2}$, hence hypotenuse $EB = \frac{\sqrt{5}}{2}R$.
* Swinging $EB$ onto the opposite radius $\Delta A$ produces $\Delta Z = EB - E\Delta = \frac{\sqrt{5} - 1}{2}R = \frac{R}{\phi}$, the exact regular decagon chord $s_{10} = 2R\sin 18^\circ$.
* Simultaneously, the hypotenuse $BZ$ of right triangle $\triangle B\Delta Z$ combines $B\Delta = R = s_6$ and $\Delta Z = s_{10}$ at right angles, realizing *Elements* XIII.10 ($s_5^2 = s_6^2 + s_{10}^2$) in a **single line segment** $BZ$!

Nearly seventeen centuries later, Renaissance and modern geometers (and Herbert W. Richmond in 1893) popularized variants of this exact Ptolemaic compass swing as the canonical studio construction of the regular pentagon.

2. Why $D = 120^p$ and Base-60 Fractions?
-----------------------------------------

Whereas :person:`Hipparchus <hipparchus>` had used a chord circle of radius $R = 3438'$ (chosen so that $2\pi R \approx 21600' = 360 \times 60'$, making $1'$ of arc nearly equal to $1$ unit of radius), Ptolemy adopts $D = 120^p$ ($R = 60^p$) so that the radius itself equals **one sexagesimal sixty** ($1,0^p = 60^p$). Every division by the diameter $D = 120 = 2 \times 60$ in Ptolemy's chord formulas reduces to halving and shifting one sexagesimal place!

3. Exact Verification in ``geometor.ptolemy``
---------------------------------------------

The module :mod:`geometor.ptolemy.pentagon_chords` (:func:`~geometor.ptolemy.pentagon_chords.construct_pentagon_decagon`) executes Ptolemy's exact compass-and-straightedge steps in ``geometor.model`` with ``auto_intersect=False``, verifying symbolically over $\mathbb{Q}(\sqrt{5})$ that $\frac{\Delta Z}{\Delta\Gamma} = \phi^{-1}$ and $\Delta Z^2 + \Delta B^2 = BZ^2$ with zero floating-point approximations.

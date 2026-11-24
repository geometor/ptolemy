:order: 10
:type: chapter
:book: Almagest (Book I)
:title: Chapter 10 · Summary
:folio: heiberg_1898_syntaxis_vol1_pt1:0041
:tracks: English: ch_10-en | Greek: ch_10-el | Summary: ch_10-summary | Notes: ch_10-notes

.. _almagest-ch-10-summary:

Chapter 10 · Summary
====================

The Deductive Architecture of Ptolemy's Chord Calculus (*Almagest* I.10)
-------------------------------------------------------------------------

1. **Single-Circle Compass Construction of the Golden Decagon & Pentagon** (*pp. 31–35*):
   In semicircle :math:`AB\Gamma` on diameter :math:`A\Delta\Gamma` with :math:`\Delta B \perp A\Gamma` and :math:`E` bisecting :math:`\Delta\Gamma`, swinging :math:`EB = 30\sqrt{5}` onto :math:`\Delta A` at :math:`Z` yields in a single right triangle :math:`\triangle B\Delta Z`:

   .. math::

      \Delta Z = s_{10} = \frac{R}{\phi} = 30(\sqrt{5} - 1) \approx 37;4,55^p, \qquad BZ = s_5 = \sqrt{R^2 + s_{10}^2} = 30\sqrt{10 - 2\sqrt{5}} \approx 70;32,3^p

2. **Ptolemy's Theorem on Cyclic Quadrilaterals** (*pp. 36–37*):
   In any cyclic quadrilateral :math:`AB\Gamma\Delta`, setting :math:`\angle ABE = \angle\Delta B\Gamma` creates two pairs of similar triangles (:math:`\triangle ABE \sim \triangle\Delta B\Gamma` and :math:`\triangle EB\Gamma \sim \triangle AB\Delta`), yielding:

   .. math::

      A\Gamma \cdot B\Delta = AB \cdot \Delta\Gamma + A\Delta \cdot B\Gamma

3. **Difference & Sum Laws** (*pp. 38, 41–42*):
   When one diagonal is the diameter :math:`D = 120^p`, Ptolemy's Theorem transforms directly into the difference and sum formulas:

   .. math::

      \operatorname{crd}(\alpha \mp \beta) = \frac{\operatorname{crd}(\alpha)\operatorname{crd}(180^\circ - \beta) \mp \operatorname{crd}(\beta)\operatorname{crd}(180^\circ - \alpha)}{120}

   Applied to :math:`72^\circ` (pentagon) and :math:`60^\circ` (hexagon), this yields :math:`\operatorname{crd}(12^\circ) \approx 12;32,36^p`.

4. **Half-Arc Chord Law** (*pp. 39–40*):
   Bisecting arc :math:`B\Gamma` at :math:`\Delta` on semicircle :math:`AB\Gamma` gives:

   .. math::

      \operatorname{crd}^2(\theta / 2) = 60\bigl(120 - \operatorname{crd}(180^\circ - \theta)\bigr)

   Repeated bisection extracts :math:`6^\circ, 3^\circ, 1\frac{1}{2}^\circ, \frac{3}{4}^\circ`.

5. **Irreducibility of Angle Trisection** (*p. 42*):
   Ptolemy explicitly states that :math:`\operatorname{crd}(\frac{1}{2}^\circ)` cannot be constructed ``διὰ τῶν γραμμῶν`` ("by means of lines") from :math:`\operatorname{crd}(1\frac{1}{2}^\circ)`—anticipating the algebraic cubic irreducibility of angle trisection.

6. **Ptolemy's Inequality Lemma & the Squeeze of** :math:`\operatorname{crd}(1^\circ)` (*pp. 43–46*):
   Proving :math:`\frac{\operatorname{crd}\alpha}{\operatorname{crd}\beta} < \frac{\alpha}{\beta}` for :math:`\alpha > \beta` traps :math:`\operatorname{crd}(1^\circ)` between:

   .. math::

      \frac{2}{3}\operatorname{crd}\left(1\frac{1}{2}^\circ\right) = 1;2,50,0^p < \operatorname{crd}(1^\circ) < \frac{4}{3}\operatorname{crd}\left(\frac{3}{4}^\circ\right) = 1;2,50,40^p

   This establishes :math:`\operatorname{crd}(1^\circ) \approx 1;2,50^p`, halving to :math:`\operatorname{crd}(\frac{1}{2}^\circ) \approx 0;31,25^p`.

7. **Architecture of the 45-Line Chord Table** (*p. 47*):
   The canon arranges arcs at :math:`\frac{1}{2}^\circ` steps in 45-row columns alongside chords (:math:`D = 120^p`) and :math:`\frac{1}{30}` interpolation differences per arc-minute, permitting cross-checks via doubling, differences, or supplements.

Primary Polygon Chords (:math:`R = 60^p, D = 120^p`)
----------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 12 36 16 16

   * - Inscribed Polygon
     - Arc :math:`\theta`
     - Exact Radical (:math:`\mathbb{Q}(\sqrt{2}, \sqrt{3}, \phi)`)
     - Computed Base-60
     - Heiberg (1898)
   * - Regular Decagon (:math:`s_{10}`)
     - :math:`36^\circ`
     - :math:`30(\sqrt{5} - 1) = 60\phi^{-1}`
     - ``37;4,55``
     - ``37;4,55``
   * - Regular Hexagon (:math:`s_6`)
     - :math:`60^\circ`
     - :math:`60`
     - ``60;0,0``
     - ``60;0,0``
   * - Regular Pentagon (:math:`s_5`)
     - :math:`72^\circ`
     - :math:`30\sqrt{10 - 2\sqrt{5}}`
     - ``70;32,3``
     - ``70;32,3``
   * - Inscribed Square (:math:`s_4`)
     - :math:`90^\circ`
     - :math:`60\sqrt{2}`
     - ``84;51,10``
     - ``84;51,10``
   * - Equilateral Triangle (:math:`s_3`)
     - :math:`120^\circ`
     - :math:`60\sqrt{3}`
     - ``103;55,23``
     - ``103;55,23``
   * - Decagon Supplement
     - :math:`144^\circ`
     - :math:`30\sqrt{10 + 2\sqrt{5}}`
     - ``114;7,37``
     - ``114;7,37``
   * - Difference Arc
     - :math:`12^\circ`
     - :math:`\operatorname{crd}(72^\circ - 60^\circ)`
     - ``12;32,36``
     - ``12;32,36``
   * - Half-Arc Steps
     - :math:`6^\circ, 3^\circ, 1\frac{1}{2}^\circ, \frac{3}{4}^\circ`
     - Half-Arc Formula
     - ``6;16,49``, ``3;8,28``, ``1;34,15``, ``0;47,8``
     - ``6;16,49``, ``3;8,28``, ``1;34,15``, ``0;47,8``
   * - Fundamental Step
     - :math:`1^\circ, \frac{1}{2}^\circ`
     - Inequality Squeeze & Bisection
     - ``1;2,50``, ``0;31,25``
     - ``1;2,50``, ``0;31,25``

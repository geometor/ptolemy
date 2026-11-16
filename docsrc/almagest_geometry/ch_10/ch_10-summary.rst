:order: 2
:type: chapter
:book: Syntaxis Mathematica (Almagest)
:title: Chapter 10 · Summary
:folio: heiberg_1898_syntaxis_vol1_pt1:0041
:tracks: English: ch_10-en | Greek: ch_10-el | Summary: ch_10-summary | Notes: ch_10-notes

.. _almagest-ch-10-summary:

Chapter 10 · Summary
====================

The Deductive Architecture of Ptolemy's Chord Calculus (*Almagest* I.10)
-------------------------------------------------------------------------

1. **Single-Circle Compass Construction of the Golden Decagon & Pentagon** (*pp. 31–35*):
   In semicircle $AB\Gamma$ on diameter $A\Delta\Gamma$ with $\Delta B \perp A\Gamma$ and $E$ bisecting $\Delta\Gamma$, swinging $EB = 30\sqrt{5}$ onto $\Delta A$ at $Z$ yields in a single right triangle $\triangle B\Delta Z$:

   $$\Delta Z = s_{10} = \frac{R}{\phi} = 30(\sqrt{5} - 1) \approx 37;4,55^p, \qquad BZ = s_5 = \sqrt{R^2 + s_{10}^2} = 30\sqrt{10 - 2\sqrt{5}} \approx 70;32,3^p.$$

2. **Ptolemy's Theorem on Cyclic Quadrilaterals** (*pp. 36–37*):
   In any cyclic quadrilateral $AB\Gamma\Delta$, setting $\angle ABE = \angle \Delta B\Gamma$ creates two pairs of similar triangles ($\triangle ABE \sim \triangle \Delta B\Gamma$ and $\triangle E B\Gamma \sim \triangle AB\Delta$), yielding:

   $$A\Gamma \cdot B\Delta = AB \cdot \Delta\Gamma + A\Delta \cdot B\Gamma.$$

3. **Difference & Sum Laws** (*pp. 38, 41–42*):
   When one diagonal is the diameter $D = 120^p$, Ptolemy's Theorem transforms directly into the difference formula:

   $$\operatorname{crd}(\alpha - \beta) = \frac{\operatorname{crd}(\alpha)\operatorname{crd}(180^\circ - \beta) - \operatorname{crd}(\beta)\operatorname{crd}(180^\circ - \alpha)}{120}.$$

   Applied to $72^\circ$ (pentagon) and $60^\circ$ (hexagon), this yields $\operatorname{crd}(12^\circ) \approx 12;32,36^p$.

4. **Half-Arc Chord Law** (*pp. 39–40*):
   Bisecting arc $B\Gamma$ at $\Delta$ on semicircle $AB\Gamma$ gives:

   $$\operatorname{crd}^2(\theta / 2) = 60\bigl(120 - \operatorname{crd}(180^\circ - \theta)\bigr).$$

   Repeated bisection extracts $6^\circ, 3^\circ, 1\frac{1}{2}^\circ, \frac{3}{4}^\circ$.

5. **Irreducibility of Angle Trisection** (*p. 42*):
   Ptolemy explicitly states that $\operatorname{crd}(\frac{1}{2}^\circ)$ cannot be constructed `διὰ τῶν γραμμῶν` ("by means of lines") from $\operatorname{crd}(1\frac{1}{2}^\circ)$—anticipating the algebraic cubic irreducibility of angle trisection.

6. **Ptolemy's Inequality Lemma & the Squeeze of $\operatorname{crd}(1^\circ)$** (*pp. 43–46*):
   Proving $\frac{\operatorname{crd}\alpha}{\operatorname{crd}\beta} < \frac{\alpha}{\beta}$ for $\alpha > \beta$ traps $\operatorname{crd}(1^\circ)$ between:

   $$\frac{2}{3}\operatorname{crd}\left(1\frac{1}{2}^\circ\right) = 1;2,50,0^p < \operatorname{crd}(1^\circ) < \frac{4}{3}\operatorname{crd}\left(\frac{3}{4}^\circ\right) = 1;2,50,40^p.$$

   This establishes $\operatorname{crd}(1^\circ) \approx 1;2,50^p$, halving to $\operatorname{crd}(\frac{1}{2}^\circ) \approx 0;31,25^p$.

Primary Polygon Chords ($R = 60^p, D = 120^p$)
----------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 12 36 16 16

   * - Inscribed Polygon
     - Arc $\theta$
     - Exact Radical ($\mathbb{Q}(\sqrt{2}, \sqrt{3}, \phi)$)
     - Computed Base-60
     - Heiberg (1898)
   * - Regular Decagon ($s_{10}$)
     - $36^\circ$
     - $30(\sqrt{5} - 1) = 60\phi^{-1}$
     - ``37;4,55``
     - ``37;4,55``
   * - Regular Hexagon ($s_6$)
     - $60^\circ$
     - $60$
     - ``60;0,0``
     - ``60;0,0``
   * - Regular Pentagon ($s_5$)
     - $72^\circ$
     - $30\sqrt{10 - 2\sqrt{5}}$
     - ``70;32,3``
     - ``70;32,3``
   * - Inscribed Square ($s_4$)
     - $90^\circ$
     - $60\sqrt{2}$
     - ``84;51,10``
     - ``84;51,10``
   * - Equilateral Triangle ($s_3$)
     - $120^\circ$
     - $60\sqrt{3}$
     - ``103;55,23``
     - ``103;55,23``
   * - Decagon Supplement
     - $144^\circ$
     - $30\sqrt{10 + 2\sqrt{5}}$
     - ``114;7,37``
     - ``114;7,37``
   * - Difference Arc
     - $12^\circ$
     - $\operatorname{crd}(72^\circ - 60^\circ)$
     - ``12;32,36``
     - ``12;32,36``
   * - Half-Arc Steps
     - $6^\circ, 3^\circ, 1\frac{1}{2}^\circ, \frac{3}{4}^\circ$
     - Half-Arc Formula
     - ``6;16,49``, ``3;8,28``, ``1;34,15``, ``0;47,8``
     - ``6;16,49``, ``3;8,28``, ``1;34,15``, ``0;47,8``
   * - Fundamental Step
     - $1^\circ, \frac{1}{2}^\circ$
     - Inequality Squeeze & Bisection
     - ``1;2,50``, ``0;31,25``
     - ``1;2,50``, ``0;31,25``

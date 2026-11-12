.. _unit-2-ptolemy-chords-summary:

Unit II · Executive Summary
===========================

The Five Pillars of Ptolemy's Chord Calculus (*Almagest* I.10b)
---------------------------------------------------------------

1. **Ptolemy's Theorem** (*pp. 36–37*): In any cyclic quadrilateral $AB\Gamma\Delta$, drawing $BE$ with $\angle ABE = \angle \Delta B\Gamma$ splits diagonal $A\Gamma$ at $E$ into two pairs of similar triangles ($\triangle ABE \sim \triangle \Delta B\Gamma$ and $\triangle E B\Gamma \sim \triangle AB\Delta$), proving:

   $$A\Gamma \cdot B\Delta = AB \cdot \Delta\Gamma + A\Delta \cdot B\Gamma.$$

2. **Difference & Sum Laws** (*pp. 38, 41–42*): Setting one diagonal equal to the diameter $D = 120^p$ turns Ptolemy's Theorem directly into the trigonometric addition/subtraction theorems:

   $$\operatorname{crd}(\alpha \pm \beta)
     = \frac{\operatorname{crd}(\alpha)\operatorname{crd}(180^\circ - \beta)
           \pm \operatorname{crd}(\beta)\operatorname{crd}(180^\circ - \alpha)}{120}.$$

3. **Half-Arc Chord Law** (*pp. 39–40*): Bisecting arc $B\Gamma$ at $\Delta$ on semicircle $AB\Gamma$ yields:

   $$\operatorname{crd}^2(\theta / 2) = \frac{D}{2}\bigl(D - \operatorname{crd}(180^\circ - \theta)\bigr) = 60\bigl(120 - \operatorname{crd}(180^\circ - \theta)\bigr).$$

4. **Irreducibility of Angle Trisection** (*p. 42*): Ptolemy explicitly recognizes that $\operatorname{crd}(\frac{1}{2}^\circ)$ cannot be constructed `διὰ τῶν γραμμῶν` ("by means of lines") from $\operatorname{crd}(1\frac{1}{2}^\circ)$—anticipating the cubic irreducibility of $4x^3 - 3x = \cos(3\psi)$ over $\mathbb{Q}(\cos 3\psi)$.
5. **Ptolemy's Inequality Lemma & $\pi \approx 3;8,30$** (*pp. 43–46*): Proving $\frac{\operatorname{crd}\alpha}{\operatorname{crd}\beta} < \frac{\alpha}{\beta}$ for $\alpha > \beta$ traps $\operatorname{crd}(1^\circ)$ strictly between $\frac{2}{3}\operatorname{crd}(1\frac{1}{2}^\circ) = 1;2,50,0^p$ and $\frac{4}{3}\operatorname{crd}(\frac{3}{4}^\circ) \approx 1;2,50,40^p$, fixing $\operatorname{crd}(1^\circ) = 1;2,50^p = \frac{377}{360}$ and implying $\pi \approx 3 \cdot (1;2,50) = 3;8,30 = \frac{377}{120} \approx 3.1416667$.

Complete Radical & Sexagesimal Verification Cascade
---------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 15 35 25 25

   * - Arc $\theta$
     - Constructive Derivation
     - Exact Radical Computed Base-60
     - Heiberg (1898) Printed Text
   * - $12^\circ$
     - $\operatorname{crd}(72^\circ - 60^\circ)$ (Diff. Law)
     - ``12;32,36``
     - ``12;32,36`` (*p. 38*)
   * - $6^\circ$
     - Half-arc of $12^\circ$
     - ``6;16,49``
     - ``6;16,49`` (*p. 40*)
   * - $3^\circ$
     - Half-arc of $6^\circ$
     - ``3;8,28``
     - ``3;8,28`` (*p. 40*)
   * - $1\frac{1}{2}^\circ$
     - Half-arc of $3^\circ$
     - ``1;34,15``
     - ``1;34,15`` (*p. 40*)
   * - $\frac{3}{4}^\circ$
     - Half-arc of $1\frac{1}{2}^\circ$
     - ``0;47,7`` ($0;47,7,25\dots$)
     - ``0;47,8`` (*p. 40*)
   * - $1^\circ$
     - Inequality sandwich ($1\frac{1}{2}^\circ$ & $\frac{3}{4}^\circ$)
     - ``1;2,50`` ($= 377/360$)
     - ``1;2,50`` (*p. 46*)
   * - $\frac{1}{2}^\circ$
     - Half-arc of $1^\circ$
     - ``0;31,25``
     - ``0;31,25`` (*p. 46*)

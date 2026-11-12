.. _unit-2-ptolemy-chords-en:

Unit II · Ptolemy's Theorem on Cyclic Quadrilaterals & Chord Calculus
=====================================================================

*Almagest* Book I, Chapter 10b (:cite:`Heiberg 1898, Vol. I.1, pp. 36–46 <heiberg:1898>`)
-----------------------------------------------------------------------------------------

1. Ptolemy's Theorem on Cyclic Quadrilaterals (`Heiberg I, pp. 36–37`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 36` Having obtained these primary chords, the next step is to set forth the corollary that follows directly through the theorem we are about to write down, being most useful on every occasion:

.. picture:: /_static/figures/fig03_ptolemy_cyclic_quadrilateral.svg

**Proposition (Ptolemy's Theorem).** Let there be any :term:`quadrilateral inscribed in a circle <tetragonon-eggegrammenon>`, :g:`ΑΒΓΔ <cABCD>`, and let its diagonals :g:`ΑΓ <AE>`–:g:`Γ <EC>` and :g:`ΒΔ <BD>` be joined. **We must prove that the rectangle contained by** :g:`ΑΓ` **and** :g:`ΒΔ` **is equal to the sum of the rectangles contained by the opposite sides,** :g:`ΑΒ · ΔΓ` **and** :g:`ΑΔ · ΒΓ`.

*Construction.* Let angle :g:`∠ΑΒΕ <angABE>` be set out :eq:`equal to angle ∠ΔΒΓ <angABE = angDBC>` by drawing :g:`ΒΕ <BE>` to meet diagonal :g:`ΑΓ` at :g:`Ε <E>` (:just:`Eucl. I.23 <I.23>`).

:line:`p. 37` *Demonstration.* If to each of the equal angles :g:`∠ΑΒΕ <angABE>` and :g:`∠ΔΒΓ <angDBC>` we add the common angle `∠ΕΒΔ`, then the whole angle `∠ΑΒΔ` is equal to the whole angle `∠ΕΒΓ`. Yet angle `∠ΒΔΑ` is also equal to angle `∠ΒΓΕ`, for they stand upon the same circumference :g:`ΑΒ <AB>` (:just:`Eucl. III.21 <III.21>`). Therefore triangle `ΑΒΔ` is equiangular with triangle `ΕΒΓ`! Consequently, by :just:`Eucl. VI.4 <VI.4>`, their sides about the equal angles are proportional—as :g:`ΒΓ <BC>` is to :g:`ΓΕ <EC>`, so is :g:`ΒΔ <BD>` to :g:`ΔΑ <DA>`:

$$\frac{B\Gamma}{\Gamma E} = \frac{B\Delta}{\Delta A}
\quad\Longrightarrow\quad
B\Gamma \cdot \Delta A = B\Delta \cdot \Gamma E \qquad\text{(}:just:`Eucl. VI.16 <VI.16>`\text{)}.$$

Again, since angle :g:`∠ΑΒΕ <angABE>` is equal to angle :g:`∠ΔΒΓ <angDBC>`, and angle `∠ΒΑΕ` is equal to angle `∠ΒΔΓ` (subtending the same arc :g:`ΒΓ <BC>`, :just:`Eucl. III.21 <III.21>`), triangle :g:`ΑΒΕ <triABE>` is equiangular with triangle :g:`ΔΒΓ <triDBC>`. Therefore proportionally, as :g:`ΒΑ <AB>` is to :g:`ΑΕ <AE>`, so is :g:`ΒΔ <BD>` to :g:`ΔΓ <CD>`:

$$\frac{BA}{AE} = \frac{B\Delta}{\Delta\Gamma}
\quad\Longrightarrow\quad
BA \cdot \Delta\Gamma = B\Delta \cdot AE \qquad\text{(}:just:`Eucl. VI.16 <VI.16>`\text{)}.$$

Now it was proved above that $B\Gamma \cdot \Delta A = B\Delta \cdot \Gamma E$. Adding the two equalities together and invoking :just:`Eucl. II.1 <II.1>` ($B\Delta \cdot AE + B\Delta \cdot \Gamma E = B\Delta \cdot A\Gamma$), **the whole rectangle contained by** $A\Gamma$ **and** $B\Delta$ **is equal to the sum of the rectangle** $AB \cdot \Delta\Gamma$ **and the rectangle** $A\Delta \cdot B\Gamma$. *Which was to be proved.*

2. Chord of the Difference (`Heiberg I, p. 38`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. picture:: /_static/figures/fig04_chord_difference_and_sum.svg

:line:`p. 38` **Corollary (Difference of Two Arcs).** Given a semicircle :g:`ΑΒΓΔ <semiDiff>` on diameter :g:`ΑΔ <AD>`, suppose the chords :g:`ΑΒ <AB>` and :g:`ΑΓ <AG>` from :g:`Α <A>` are given in magnitude. Joining :g:`ΒΓ <BG>`, :g:`ΒΔ <BD>`, and :g:`ΓΔ <GD>`, the supplementary chords :g:`ΒΔ <BD>` and :g:`ΓΔ <GD>` are immediately given via :just:`Eucl. III.31 <III.31>` and :just:`Eucl. I.47 <I.47>` ($\operatorname{crd}^2(180^\circ - \theta) = D^2 - \operatorname{crd}^2\theta$). Since :g:`ΑΒΓΔ <quadDiff>` is a cyclic quadrilateral in the circle, Ptolemy's Theorem gives:

$$AB \cdot \Gamma\Delta + A\Delta \cdot B\Gamma = A\Gamma \cdot B\Delta
\quad\Longrightarrow\quad
B\Gamma = \frac{A\Gamma \cdot B\Delta - AB \cdot \Gamma\Delta}{A\Delta}.$$

Applying this immediately to the pentagon arc ($72^\circ$) and hexagon arc ($60^\circ$), Ptolemy obtains the chord of their difference ($12^\circ$):

$$\operatorname{crd}(12^\circ)
  = \frac{\operatorname{crd}(72^\circ)\operatorname{crd}(120^\circ) - \operatorname{crd}(60^\circ)\operatorname{crd}(108^\circ)}{120}
  \approx 12;32,36^p.$$

3. Half-Arc Chord Lemma (`Heiberg I, pp. 39–40`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 39` Next, if any chord in the circle be given, how do we find the chord subtending **half the same arc**?

.. picture:: /_static/figures/fig05_half_arc_chord_lemma.svg

Let :g:`ΑΒΓ <semiABG>` be a semicircle on diameter :g:`ΑΓ <AG>`, let chord :g:`ΓΒ <BG>` be given, and let its arc be bisected at :g:`Δ <D>`, joining :g:`ΑΒ <AB>`, :g:`ΑΔ <AD>`, :g:`ΒΔ <BD>`, and :g:`ΔΓ <GD>`. Cut off :g:`ΑΕ <AE>` along :g:`ΑΓ <AG>` :eq:`equal to ΑΒ <AB = AE>`, and drop perpendicular :g:`ΔΖ <DZ>` onto :g:`ΑΓ <AG>` (:g:`∠ΔΖΓ <angDZG>`).

*Demonstration.* Since :eq:`ΑΒ = ΑΕ <AB = AE>`, :g:`ΑΔ <AD>` is common, and `∠ΒΑΔ = ∠ΕΑΔ` (standing on equal half-arcs :g:`ΒΔ <BD>` and :g:`ΔΓ <GD>`), triangles :g:`ΒΑΔ <triABD>` and :g:`ΕΑΔ <triAED>` are congruent (:just:`Eucl. I.4 <I.4>`), so :eq:`ΒΔ = ΔΕ <BD = DE>`. Yet :eq:`ΒΔ = ΔΓ <BD = GD>` since the arcs are equal; therefore triangle `ΔΕΓ` is isosceles with :eq:`ΔΕ = ΔΓ <DE = GD>`, and the altitude :g:`ΔΖ <DZ>` bisects the base so `ΕΖ = ΖΓ = ½ ΕΓ`. Now in the right triangle `ΑΔΓ` inscribed in the semicircle (:just:`Eucl. III.31 <III.31>`), triangle `ΑΔΓ` is similar to triangle `ΔΖΓ` (:just:`Eucl. VI.8 <VI.8>`), whence:

$$\frac{A\Gamma}{\Gamma\Delta} = \frac{\Gamma\Delta}{\Gamma Z}
\quad\Longrightarrow\quad
\Gamma\Delta^2 = A\Gamma \cdot \Gamma Z = \frac{1}{2}\,A\Gamma \cdot (A\Gamma - AB)
= 60 \cdot \bigl(120 - \operatorname{crd}(180^\circ - \theta)\bigr).$$

:line:`p. 40` Iterating this half-arc formula four times from $\operatorname{crd}(12^\circ) = 12;32,36^p$, Ptolemy derives:

* $\operatorname{crd}(6^\circ) \approx 6;16,49^p$
* $\operatorname{crd}(3^\circ) \approx 3;8,28^p$
* $\operatorname{crd}(1\tfrac{1}{2}^\circ) \approx 1;34,15^p$
* $\operatorname{crd}(\tfrac{3}{4}^\circ) \approx 0;47,8^p$

4. Chord of the Sum & Impossibility of Trisection by Lines (`Heiberg I, pp. 41–42`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 41` Again, let arcs :g:`ΑΒ <AB_sum>` and :g:`ΒΓ <BG_sum>` be given in a circle around center :g:`Ε <E_sum>` (Panel II of Figure 4 above), and draw diameter :g:`ΒΕΔ <BD_sum>`. Because :g:`ΑΒΓΔ <quadSum>` is cyclic with diagonal :g:`ΒΔ <BD_sum>` equal to the diameter $D = 120^p$, Ptolemy's Theorem yields the chord of the combined arc :g:`ΑΓ <AG_sum>`:

$$\operatorname{crd}(\alpha + \beta)
  = \frac{\operatorname{crd}(\alpha)\operatorname{crd}(180^\circ - \beta)
        + \operatorname{crd}(\beta)\operatorname{crd}(180^\circ - \alpha)}{120}.$$

:line:`p. 42` By combining $1\frac{1}{2}^\circ$ with all preceding chords, one immediately fills in every multiple of $1\frac{1}{2}^\circ$—yet two intermediates remain inside each $1\frac{1}{2}^\circ$ interval if the table is to advance by half-degrees! For if we possessed $\operatorname{crd}(\frac{1}{2}^\circ)$, both missing entries would follow immediately by sum and difference with $1\frac{1}{2}^\circ$. **However, when a chord such as that of** $1\frac{1}{2}^\circ$ **is given, the chord subtending one-third of the same arc can in no way be found geometrically** :term:`by means of lines <dia-ton-grammon>` (`οὐδαμῶς γίνεται διὰ τῶν γραμμῶν`)—though if that were possible, we would immediately have $\operatorname{crd}(\frac{1}{2}^\circ)$ itself!

5. Ptolemy's Inequality Lemma & $\operatorname{crd}(1^\circ) \approx 1;2,50^p$ (`Heiberg I, pp. 43–46`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 43` Instead, Ptolemy establishes a rigorous geometric sandwich for $\operatorname{crd}(1^\circ)$ from the known chords of $1\frac{1}{2}^\circ$ and $\frac{3}{4}^\circ$:

.. picture:: /_static/figures/fig06_ptolemy_inequality_lemma.svg

**Lemma (Ptolemy's Chord–Arc Inequality).** In circle :g:`ΑΒΓΔ <cABGD>`, let two unequal consecutive chords :g:`ΑΒ <AB>` $<$ :g:`ΒΓ <BG>` be drawn. Bisect angle `∠ΑΒΓ` by :g:`ΒΔ <BD>` meeting chord :g:`ΑΓ <AG>` at :g:`Ε <E>` and the circumference at :g:`Δ <D>`, join :g:`ΑΔ <DH>` and :g:`ΓΔ <DG>`, and drop perpendicular :g:`ΔΖ <DZ>` onto :g:`ΑΓ <AG>` (:g:`∠ΔΖΑ <angDZA>`).

*Demonstration.* Since `∠ΑΒΔ = ∠ΓΒΔ`, chords `ΑΔ` and :g:`ΓΔ <DG>` are equal, and since :g:`ΓΒ <BG>` $>$ :g:`ΒΑ <AB>`, by :just:`Eucl. VI.3 <VI.3>` we have `ΓΕ > ΕΑ`, so the foot :g:`Ζ <Z>` of the altitude in isosceles triangle `ΑΔΓ` falls between :g:`Ε <E>` and :g:`Γ <G>`. Consequently `ΔΑ > ΔΕ > ΔΖ`. Describing the circular arc :g:`ΗΕΘ <arcHETheta>` centered at :g:`Δ <D>` with radius `ΔΕ` (meeting `ΔΑ` produced at :g:`Η <H>` and :g:`ΔΖ <DZ>` at :g:`Θ <Theta>`), triangle :g:`ΔΕΖ <triDEZ>` is strictly larger than sector `ΔΕΘ`, whereas triangle :g:`ΔΕΑ <triDAE>` is strictly smaller than sector `ΔΕΗ`:

$$\frac{EZ}{EA}
  = \frac{\operatorname{area}(\triangle \Delta EZ)}{\operatorname{area}(\triangle \Delta EA)}
  > \frac{\operatorname{area}(\text{sector }\Delta E\Theta)}{\operatorname{area}(\text{sector }\Delta EH)}
  = \frac{\angle E\Delta Z}{\angle E\Delta A}.$$

:line:`p. 44–45` By *componendo* and doubling (`ΓΑ = 2 ΓΖ`), it follows that $\frac{\Gamma E}{EA} < \frac{\angle\Gamma\Delta B}{\angle B\Delta A}$, and since $\frac{\Gamma B}{BA} = \frac{\Gamma E}{EA}$ (:just:`Eucl. VI.3 <VI.3>`) while central/inscribed angles stand as their arcs (:just:`Eucl. VI.33 <VI.33>`):

$$\frac{\operatorname{crd}(B\Gamma)}{\operatorname{crd}(BA)} < \frac{\operatorname{arc}(B\Gamma)}{\operatorname{arc}(BA)}.$$

:line:`p. 45–46` **Pinching $\operatorname{crd}(1^\circ)$ to Sexagesimal Seconds:**

1. Setting $\operatorname{arc}(BA) = \frac{3}{4}^\circ$ and $\operatorname{arc}(B\Gamma) = 1^\circ$ gives $\operatorname{crd}(1^\circ) < \frac{4}{3}\operatorname{crd}(\frac{3}{4}^\circ) = \frac{4}{3}(0;47,8^p) = 1;2,50,40^p \approx 1;2,50^p$.
2. Setting $\operatorname{arc}(BA) = 1^\circ$ and $\operatorname{arc}(B\Gamma) = 1\frac{1}{2}^\circ$ gives $\operatorname{crd}(1^\circ) > \frac{2}{3}\operatorname{crd}(1\frac{1}{2}^\circ) = \frac{2}{3}(1;34,15^p) = 1;2,50,0^p = 1;2,50^p$.

Since $\operatorname{crd}(1^\circ)$ has been proved strictly **both smaller and larger than quantities that agree to** $1;2,50^p$, Ptolemy concludes with complete rigor:

$$\operatorname{crd}(1^\circ) = 1;2,50^p = \frac{377}{360}, \qquad \operatorname{crd}(\tfrac{1}{2}^\circ) \approx 0;31,25^p,$$

from which every remaining entry in the $360$-row Table of Chords follows!

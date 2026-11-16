:order: 2
:type: chapter
:book: Syntaxis Mathematica (Almagest)
:title: Chapter 10 · Magnitude of Chords in a Circle
:folio: heiberg_1898_syntaxis_vol1_pt1:0041
:tracks: English: ch_10-en | Greek: ch_10-el | Summary: ch_10-summary | Notes: ch_10-notes

.. _unit-2-ptolemy-chords-en:
.. _almagest-ch-10-en:

Chapter 10 · On the Magnitude of Straight Lines in a Circle
===========================================================

*Almagest* Book I, Chapter 10 (:cite:`Heiberg 1898, Vol. I.1, pp. 31–46 <heiberg:1898>`)
-----------------------------------------------------------------------------------------

:line:`p. 31` For ease of practical use, then, we shall subsequently construct a tabular exposition of the magnitudes of these :term:`chords <eutheia-hypoteinousa>`, dividing the circumference into $360$ :term:`segments <moira>`, setting out the arcs side by side at increments of half a degree, and giving alongside each arc the straight line subtending it when the diameter is divided into $120$ :term:`parts <tmema>`—because of the arithmetical symmetry of this number, as will become evident from the calculations themselves.

:line:`p. 32` First, however, we shall show how, through the fewest and exactest theorems—and the very same ones throughout—we carry out a rapid and systematic demonstration of their magnitudes, so that we do not merely have the tabular magnitudes of the chords set out nakedly without inspection, but may also manage their verification and proof cleanly through a geometric construction. In general we shall employ the **sexagesimal system** (:term:`ἑξηκοστά <hexekoston>`) because of the awkwardness of unit fractions, always carrying multiplications and divisions out to yield approximations whose discrepancy does not differ even sensibly from rigorous precision.

1. Golden Decagon & Pentagon Construction (`Heiberg I, pp. 32–35`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. picture:: /_static/figures/fig02_pentagon_decagon_construction.svg

**Proposition (Ptolemy's Golden Decagon & Pentagon Construction).** Let there be a semicircle :g:`ΑΒΓ <cABG>` upon diameter :g:`ΑΔΓ <AG>` around center :g:`Δ <D>`, and from :g:`Δ <D>` let :g:`ΔΒ <DB>` be drawn at right angles (:g:`∠ΑΔΒ <angADB>`) to :g:`ΑΓ <AG>`. Let :g:`ΔΓ <EG>` be bisected at :g:`Ε <E>` (:eq:`ΔΕ = ΕΓ <DE = EG>`), let :g:`ΕΒ <EB>` be joined, and let :g:`ΕΖ <DZ>` be placed :eq:`equal to ΕΒ <EB>` along :g:`ΔΑ <AG>` (via the circular arc :g:`ΒΖ <arcBZ>` centered at :g:`Ε <E>`), and let :g:`ΖΒ <BZ>` be joined.

**I say that** :g:`ΖΔ <DZ>` **is the side of the regular decagon, and** :g:`ΒΖ <BZ>` **that of the regular pentagon.**

:line:`p. 33` *Demonstration.* Since the straight line :g:`ΔΓ <EG>` is bisected at :g:`Ε <E>` and another straight line :g:`ΔΖ <DZ>` is added to it in a straight line, by :just:`Eucl. II.6 <II.6>` the rectangle contained by :g:`ΓΖ <AG>` and :g:`ΖΔ <DZ>`, together with the square on :g:`ΕΔ <DE>`, is equal to the square on :g:`ΕΖ <DZ>`—that is, to the square on :g:`ΒΕ <EB>`, since :g:`ΒΕ = ΕΖ <EB>`:

$$\Gamma Z \cdot Z\Delta + E\Delta^2 = EZ^2 = BE^2.$$

Yet because angle :g:`∠ΕΔΒ <angADB>` is right, by :just:`Eucl. I.47 <I.47>` the squares on :g:`ΕΔ <DE>` and :g:`ΔΒ <DB>` are equal to the square on :g:`ΒΕ <EB>`:

$$E\Delta^2 + \Delta B^2 = BE^2.$$

Subtracting the common square on :g:`ΕΔ <DE>`, the remaining rectangle :g:`ΓΖ · ΖΔ` is equal to the square on :g:`ΔΒ <DB>`, that is, to the square on :g:`ΔΓ <EG>`:

$$\Gamma Z \cdot Z\Delta = \Delta B^2 = \Delta\Gamma^2.$$

Therefore, as :g:`ΓΖ <AG>` is to :g:`ΓΔ <EG>`, so is :g:`ΓΔ <EG>` to :g:`ΔΖ <DZ>`. Consequently :g:`ΓΖ <AG>` has been cut in :term:`extreme and mean ratio <akron-kai-meson-logon>` at :g:`Δ <D>` (:just:`Eucl. VI.Def.3 <VI.def.3>`).

Now since the side of the hexagon and the side of the decagon inscribed in the same circle, when placed in a single straight line, cut the whole line in extreme and mean ratio (:just:`Eucl. XIII.9 <XIII.9>`), and since :g:`ΓΔ <EG>` being a radius is equal to the side of the hexagon (:just:`Eucl. IV.15 Coroll. <IV.15>`), therefore :g:`ΔΖ <DZ>` is equal to the **side of the regular decagon**.

And in the same manner, since the side of the regular pentagon has its square equal to the sum of the squares on the side of the hexagon and the side of the decagon inscribed in the same circle (:just:`Eucl. XIII.10 <XIII.10>`), and in the right-angled triangle :g:`ΒΔΖ <triBDZ>` the square on :g:`ΒΖ <BZ>` is equal to the squares on :g:`ΒΔ <DB>` (the hexagon side) and :g:`ΔΖ <DZ>` (the decagon side), therefore :g:`ΒΖ <BZ>` is equal to the **side of the regular pentagon**.

:line:`p. 34` **Sexagesimal Evaluation of the Primary Chords.** Since then, as I stated, we set the diameter of the circle to $120$ parts ($120^p$), it is immediate from what has been established that:

1. **Regular Hexagon** ($\theta = 60^\circ$): $\Delta E = \frac{1}{2}\Delta\Gamma = 30^p$ and $\Delta B = 60^p$, while the hexagon chord itself equals the radius:

   $$\operatorname{crd}(60^\circ) = 60;0,0^p.$$

2. **Regular Decagon** ($\theta = 36^\circ$): Since $E\Delta^2 = 900$ and $\Delta B^2 = 3600$, we have $EB^2 = EZ^2 = 4500$, whence $EZ \approx 67;4,55^p$ in sexagesimals. Subtracting $E\Delta = 30^p$, the decagon side :g:`ΔΖ <DZ>` is:

   $$\operatorname{crd}(36^\circ) = 30(\sqrt{5} - 1) \approx 37;4,55^p, \qquad \Delta Z^2 \approx 1375;4,15.$$

3. **Regular Pentagon** ($\theta = 72^\circ$): Adding $\Delta B^2 = 3600$ to $\Delta Z^2 = 1375;4,15$ gives :g:`ΒΖ² <BZ>` $= 4975;4,15$, whose square root yields the pentagon side :g:`ΒΖ <BZ>`:

   $$\operatorname{crd}(72^\circ) = 30\sqrt{10 - 2\sqrt{5}} \approx 70;32,3^p.$$

:line:`p. 35` 4. **Inscribed Square & Equilateral Triangle** ($\theta = 90^\circ, 120^\circ$): Instantly from the center ($R^2 = 3600$), the square on the $90^\circ$ chord is $2R^2 = 7200$ and the square on the $120^\circ$ chord is $3R^2 = 10800$:

   $$\operatorname{crd}(90^\circ) = 60\sqrt{2} \approx 84;51,10^p, \qquad \operatorname{crd}(120^\circ) = 60\sqrt{3} \approx 103;55,23^p.$$

5. **Supplementary Chords** ($180^\circ - \theta$): Since the sum of the squares on any chord and on the chord subtending the remainder of the semicircle equals the square on the diameter ($D^2 = 14400$, by :just:`Eucl. III.31 <III.31>` and :just:`Eucl. I.47 <I.47>`), subtracting $\operatorname{crd}^2(36^\circ) = 1375;4,15$ from $14400$ leaves $13024;55,45$, whence $\operatorname{crd}(144^\circ) \approx 114;7,37^p$; and similarly $\operatorname{crd}(108^\circ) \approx 97;4,56^p$.

2. Ptolemy's Theorem on Cyclic Quadrilaterals (`Heiberg I, pp. 36–37`)
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

3. Chord of the Difference (`Heiberg I, p. 38`)
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

4. Half-Arc Chord Lemma (`Heiberg I, pp. 39–42`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. picture:: /_static/figures/fig05_half_arc_chord_lemma.svg

:line:`p. 39` **Proposition (Half-Arc Chord).** Let there be a semicircle :g:`ΑΒΓ <semiHalf>` on diameter :g:`ΑΓ <AG>`, let chord :g:`ΓΒ <GB>` be given, and let arc :g:`ΓΒ <GB>` be bisected at :g:`Δ <D>` (:eq:`arc ΓΔ = arc ΔΒ <arcGD = arcDB>`). Let :g:`ΑΒ <AB>`, :g:`ΒΔ <BD>`, :g:`ΓΔ <GD>`, and :g:`ΑΔ <AD>` be joined, and from :g:`Δ <D>` let perpendicular :g:`ΔΖ <DZ_perp>` be dropped onto :g:`ΑΓ <AG>`.

**I say that** :g:`ΓΖ <GZ>` **is equal to half the excess of the diameter** :g:`ΑΓ <AG>` **over chord** :g:`ΑΒ <AB>`, **and that** :g:`\Gamma\Delta^2 = A\Gamma \cdot \Gamma Z`.

:line:`p. 40` *Demonstration.* Cut off :g:`ΑΕ = ΑΒ <AE = AB>` along :g:`ΑΓ <AG>` and join :g:`ΔΕ <DE>`. Since $AB = AE$, $A\Delta$ is common, and angle $B A\Delta = E A\Delta$ (subtending equal arcs $B\Delta$ and $\Delta\Gamma$), triangle :g:`ΑΒΔ <triABD>` is congruent to triangle :g:`ΑΕΔ <triAED>` (:just:`Eucl. I.4 <I.4>`). Therefore base :g:`ΒΔ = ΕΔ <BD = ED>`, and since $B\Delta = \Gamma\Delta$, we have :g:`ΔΕ = ΔΓ <DE = DG>`.

In the isosceles triangle :g:`ΔΕΓ <triDEG>`, the perpendicular :g:`ΔΖ <DZ_perp>` bisects the base :g:`ΕΓ <EG>` (:just:`Eucl. I.26 <I.26>`); hence :g:`ΓΖ = \frac{1}{2}ΕΓ = \frac{1}{2}(ΑΓ - ΑΒ)`.

In right triangle :g:`ΑΔΓ <triADG>` (right-angled at $\Delta$ by :just:`Eucl. III.31 <III.31>`), altitude :g:`ΔΖ <DZ_perp>` to hypotenuse :g:`ΑΓ <AG>` yields by :just:`Eucl. VI.8 <VI.8>`:

$$\frac{A\Gamma}{\Gamma\Delta} = \frac{\Gamma\Delta}{\Gamma Z}
\quad\Longrightarrow\quad
\Gamma\Delta^2 = A\Gamma \cdot \Gamma Z = 60 \cdot (120 - \operatorname{crd}(180^\circ - \theta)).$$

:line:`p. 41` Through successive bisections of the $12^\circ$ chord, Ptolemy extracts:

* $\operatorname{crd}(6^\circ) \approx 6;16,49^p$
* $\operatorname{crd}(3^\circ) \approx 3;8,28^p$
* $\operatorname{crd}(1\frac{1}{2}^\circ) \approx 1;34,15^p$
* $\operatorname{crd}(\frac{3}{4}^\circ) \approx 0;47,8^p$

:line:`p. 42` Ptolemy notes an essential limitation of classical planar geometry: finding the chord subtending one-third of a given arc (trisection of $1\frac{1}{2}^\circ$ into $\frac{1}{2}^\circ$) **can by no means be achieved by means of lines** (:term:`οὐδαμῶς γίνεται διὰ τῶν γραμμῶν <dia-ton-grammon>`).

5. Ptolemy's Inequality Lemma & Squeeze of $\operatorname{crd}(1^\circ)$ (`Heiberg I, pp. 43–46`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. picture:: /_static/figures/fig06_ptolemy_inequality_lemma.svg

:line:`p. 43` To overcome the impossibility of angle trisection, Ptolemy establishes his famous inequality lemma:

**Lemma (Ratio of Unequal Chords).** *In any circle, the ratio of a greater chord to a lesser chord is strictly less than the ratio of the corresponding arcs:*

$$\frac{\operatorname{crd}\alpha}{\operatorname{crd}\beta} < \frac{\alpha}{\beta} \qquad (\text{for } \alpha > \beta).$$

*Demonstration.* In circle :g:`ΑΒΓΔ <cABGD>`, let chords :g:`ΒΓ > ΑΒ <BC > AB>`. Bisect angle :g:`∠ΑΒΓ <angABC>` by :g:`ΒΔ <BD>`, cutting chord :g:`ΑΓ <AG>` at :g:`Ε <E>`. Since :g:`ΒΔ <BD>` bisects the angle, by :just:`Eucl. VI.3 <VI.3>`:

$$\frac{\Gamma E}{EA} = \frac{\Gamma B}{BA}.$$

:line:`p. 44` Because $BC > AB$, point $E$ lies closer to $A$ than to $\Gamma$. Dropping perpendicular :g:`ΔΖ <DZ_lem>` onto :g:`ΑΓ <AG>` and drawing arcs around $\Delta$, Ptolemy demonstrates through sector inequalities that:

$$\frac{\Gamma E}{EA} < \frac{\operatorname{arc}\Gamma B}{\operatorname{arc} BA}
\quad\Longrightarrow\quad
\frac{\operatorname{crd}\alpha}{\operatorname{crd}\beta} < \frac{\alpha}{\beta}.$$

:line:`p. 45–46` **The Squeeze on $1^\circ$:**

1. Since $1^\circ < 1\frac{1}{2}^\circ$, the lemma yields $\frac{\operatorname{crd}(1\frac{1}{2}^\circ)}{\operatorname{crd}(1^\circ)} < \frac{1\frac{1}{2}}{1} = \frac{3}{2}$, whence:

   $$\operatorname{crd}(1^\circ) > \frac{2}{3}\operatorname{crd}(1\frac{1}{2}^\circ) = \frac{2}{3}(1;34,15^p) = 1;2,50^p.$$

2. Since $\frac{3}{4}^\circ < 1^\circ$, the lemma yields $\frac{\operatorname{crd}(1^\circ)}{\operatorname{crd}(\frac{3}{4}^\circ)} < \frac{1}{\frac{3}{4}} = \frac{4}{3}$, whence:

   $$\operatorname{crd}(1^\circ) < \frac{4}{3}\operatorname{crd}(\frac{3}{4}^\circ) = \frac{4}{3}(0;47,8^p) = 1;2,50\frac{2}{3}^p.$$

Because both upper and lower bounds agree to seconds at $1;2,50^p$, Ptolemy definitively establishes:

$$\operatorname{crd}(1^\circ) \approx 1;2,50^p.$$

Applying the half-arc lemma to $1^\circ$, he obtains the fundamental table step:

$$\operatorname{crd}\left(\frac{1}{2}^\circ\right) \approx 0;31,25^p.$$

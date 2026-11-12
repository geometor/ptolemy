.. _unit-2-ptolemy-chords-notes:

Unit II · Historical & Mathematical Notes
=========================================

1. Equivalent Modern Trigonometric Identities
---------------------------------------------

Translating Ptolemy's chord function via $\operatorname{crd}(\theta) = 2R\sin(\theta/2) = 120\sin(\theta/2)$ and $\operatorname{crd}(180^\circ - \theta) = 120\cos(\theta/2)$ reveals that **every foundational identity of plane trigonometry** enters Western mathematics through *Almagest* I.10b:

* **Supplementary Chord** (*p. 35*): $\sin^2\frac{\theta}{2} + \cos^2\frac{\theta}{2} = 1$.
* **Chord Difference & Sum** (*pp. 38, 41*): $\sin(\frac{\alpha}{2} \pm \frac{\beta}{2}) = \sin\frac{\alpha}{2}\cos\frac{\beta}{2} \pm \cos\frac{\alpha}{2}\sin\frac{\beta}{2}$.
* **Half-Arc Chord Lemma** (*p. 39*): $\sin^2\frac{\theta}{4} = \frac{1 - \cos(\theta/2)}{2}$.
* **Ptolemy's Inequality Lemma** (*p. 43*): Strict concavity of $\sin x$ on $(0, \frac{\pi}{2})$, i.e. $\frac{\sin x}{x}$ strictly decreases so $\frac{\sin(\alpha/2)}{\sin(\beta/2)} < \frac{\alpha}{\beta}$ for $0 < \beta < \alpha < \pi$.

2. Note on $\operatorname{crd}(\frac{3}{4}^\circ) = 0;47,8^p$ vs. Exact $0;47,7,25^p$
-------------------------------------------------------------------------------------

Evaluating the exact SymPy radical expression for $\operatorname{crd}(\frac{3}{4}^\circ)$ in :func:`geometor.ptolemy.pentagon_chords.build_radical_chord_table` gives $0.78539398\dots = 0;47,7,25^p$ (which rounds to ``0;47,7``), whereas Heiberg's Greek text (*p. 40, l. 19*) prints ``0;47,8`` (`οʹ μζʹ ηʹʹ`) because Ptolemy took the square root of the already-rounded sexagesimal difference $120 - \operatorname{crd}(178\frac{1}{2}^\circ)$ at two sexagesimal places! Crucially, whether one uses the exact radical $\frac{4}{3}\operatorname{crd}(\frac{3}{4}^\circ) = 1.04719007\dots = 1;2,50,23^p$ or Ptolemy's rounded $\frac{4}{3}(0;47,8) = 1;2,50,40^p$, **both round identically to** ``1;2,50``!

3. Ptolemy's $\pi \approx 3;8,30 = \frac{377}{120}$ and Archimedes' Bounds
--------------------------------------------------------------------------

In *Almagest* VI.7 (:cite:`Heiberg 1898, p. 513 <heiberg:1898>`), Ptolemy explicitly states that the ratio of circumference to diameter is $3;8,30$, "for such a ratio lies very nearly halfway between $3\frac{1}{7}$ and $3\frac{10}{71}$, which :person:`Archimedes <archimedes>` used." Indeed, multiplying the $360$-gon perimeter $360 \cdot \operatorname{crd}(1^\circ) = 360 \cdot (1;2,50^p)$ and dividing by $D = 120^p$ gives:

$$\pi_{\text{Ptolemy}} = 3 \times \left(1 + \frac{2}{60} + \frac{50}{3600}\right) = 3;8,30 = \frac{377}{120} = 3.1416666\dots,$$

lying within $7.4 \times 10^{-5}$ of true $\pi = 3.14159265\dots$ and strictly inside :person:`Archimedes' <archimedes>` interval $\left(\frac{223}{71}, \frac{22}{7}\right) \approx (3.140845, 3.142857)$ (:cite:`Dimensio Circuli Prop. 3 <archimedes:dimensio>`).

4. Pure-Rational Verification in ``geometor.ptolemy.cyclic_quadrilateral``
--------------------------------------------------------------------------

In :func:`geometor.ptolemy.cyclic_quadrilateral.construct_ptolemy_quadrilateral`, Ptolemy's auxiliary similarity point $E \in AC$ ($\angle ABE = \angle DBC$) is constructed by compass-and-straightedge rhombus reflection strictly over $\mathbb{Q}$ (avoiding extraneous $\mathbb{Q}(\sqrt{3})$ extensions!). On the circle of diameter $65$ (`preset="pythagorean_65"`), the four rational vertices yield integer sides $(25, 39, 60, 52)$, integer diagonals $(56, 63)$, and exact rational similarity division $AE = \frac{500}{21}, EC = \frac{676}{21}$, verifying $56 \times 63 = 3528 = 25 \times 60 + 39 \times 52$ in pure rational arithmetic.

.. _unit-4-planisphaerium-notes:

Unit IV · Historical & Mathematical Notes
=========================================

1. Textual Survival: Alexandria $\to$ Baghdad $\to$ Córdoba $\to$ Toulouse (1143)
---------------------------------------------------------------------------------

Unlike the *Almagest*, no Greek manuscript of :person:`Ptolemy's <ptolemy>` *Planisphaerium* (*Ἅπλωσις ἐπιφανείας σφαίρας*) has survived. Translated into Arabic in ninth-century Baghdad and revised with astrolabe chapters around 1000 CE in Córdoba by :person:`Maslama al-Majrītī <maslama>`, the work entered Latin Europe when :person:`Hermann of Carinthia <hermann>` (*Hermannus Secundus*) completed his Latin version at Toulouse on **1 June 1143** (dedicated to Thierry of Chartres). Notice the charming philological fossil in the very first sentence: the vocative `ὦ Σύρε` ("O Syrus", matching *Almagest* I.1!) passed through Arabic transcription (`Yā Sūrus` $\to$ `Iyāsūrus`) into Hermann's Latin as **`Jesure`**!

2. Apollonius *Conics* I.5 & Stereographic Circle Preservation
--------------------------------------------------------------

Why does an oblique circle on the sphere—whose visual rays from the South Pole form an **oblique circular cone**—cut the equatorial plane in a **true circle** rather than an ellipse? As :person:`Federico Commandino <commandino>` demonstrated synthetically in his 1558 commentary (:cite:`Commandino 1558 <commandino:1558>`), the axial triangle of that oblique visual cone intersects the sphere in a meridian circle; by the inscribed-angle theorem (:just:`Eucl. III.21 <III.21>`), the equatorial plane cuts the two extreme generators of the cone at **anti-parallel (subcontrary) angles** equal to those of the circular base on the sphere! By :person:`Apollonius's <apollonius>` **Subcontrary Section Theorem** (:cite:`Conics I.5 <apollonius:conics>`), every :term:`subcontrary section <subcontraria-sectio>` of an oblique circular cone is an exact circle.

3. Exact Symbolic Proofs in ``geometor.ptolemy.stereographic``
--------------------------------------------------------------

In :mod:`geometor.ptolemy.stereographic`:

* :func:`~geometor.ptolemy.stereographic.prove_circle_preservation_symbolically` proves algebraically over $\mathbb{Q}(a, b, c, d, x, y)$ that $aX + bY + cZ + d = 0$ on $S^2$ maps to $(x + \frac{a}{c-d})^2 + (y + \frac{b}{c-d})^2 = \frac{a^2 + b^2 + c^2 - d^2}{(c - d)^2}$.
* :func:`~geometor.ptolemy.stereographic.prove_conformal_metric_symbolically` computes the exact Jacobian Gram matrix $J^T J = \frac{4}{(1 + x^2 + y^2)^2} I_2$ ($g_{xx} - g_{yy} = 0$, $g_{xy} = 0$).
* :func:`~geometor.ptolemy.stereographic.construct_astrolabe_planisphere` executes Ptolemy's folded-meridian compass-and-straightedge construction in ``geometor.model``, proving $\angle MDT = 90^\circ$, incidence of $B$ and $D$ on `cMBTD`, and $EL \cdot EK = ED^2$ with zero `Float` atoms.

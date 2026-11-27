:order: 1
:type: section
:book: Planisphaerium
:title: Section 1 · Notes
:folio: heiberg_1907_opera_minora_vol2:0437

.. _planisphaerium-prop-01-notes:

Section 1 · Notes
=================

Textual Survival & Philological Apparatus
-----------------------------------------

1. Textual Survival: Alexandria :math:`\to` Baghdad :math:`\to` Córdoba :math:`\to` Toulouse (1143)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlike the *Almagest*, no Greek manuscript of :person:`Ptolemy's <ptolemy>` *Planisphaerium* (*Ἅπλωσις ἐπιφανείας σφαίρας*) has survived. Translated into Arabic in ninth-century Baghdad and revised with astrolabe chapters around 1000 CE in Córdoba by :person:`Maslama al-Majrīṭī <maslama>`, the work entered Latin Europe when :person:`Hermann of Carinthia <hermann>` (*Hermannus Secundus*) completed his Latin version at Toulouse on **1 June 1143** (dedicated to Thierry of Chartres).

A fascinating philological fossil occurs in the very first sentence: the Greek vocative `ὦ Σύρε` ("O Syrus", matching *Almagest* I.1!) passed through Arabic transcription (`Yā Sūrus` :math:`\to` `Iyāsūrus`) into Hermann's Latin as **`Jesure`**!

2. Apollonius *Conics* I.5 & Stereographic Circle Preservation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Why does an oblique circle on the sphere—whose visual rays from the South Pole form an **oblique circular cone**—cut the equatorial plane in a **true circle** rather than an ellipse? As :person:`Federico Commandino <commandino>` demonstrated synthetically in his 1558 commentary (:cite:`Commandino 1558 <commandino:1558>`), the axial triangle of that oblique visual cone intersects the sphere in a meridian circle; by the inscribed-angle theorem (:just:`Eucl. III.21 <III.21>`), the equatorial plane cuts the two extreme generators of the cone at **anti-parallel (subcontrary) angles** equal to those of the circular base on the sphere! By :person:`Apollonius's <apollonius>` **Subcontrary Section Theorem** (:cite:`Conics I.5 <apollonius:conics>`), every :term:`subcontrary section <subcontraria-sectio>` of an oblique circular cone is an exact circle.

3. Exact Symbolic Proofs in ``geometor.ptolemy.stereographic``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In :mod:`geometor.ptolemy.stereographic`:

* :func:`~geometor.ptolemy.stereographic.prove_circle_preservation_symbolically` proves algebraically over :math:`\mathbb{Q}(a, b, c, d, x, y)` that :math:`aX + bY + cZ + d = 0` on :math:`S^2` maps to :math:`(x + \frac{a}{c-d})^2 + (y + \frac{b}{c-d})^2 = \frac{a^2 + b^2 + c^2 - d^2}{(c - d)^2}`.
* :func:`~geometor.ptolemy.stereographic.prove_conformal_metric_symbolically` computes the exact Jacobian Gram matrix :math:`J^T J = \frac{4}{(1 + x^2 + y^2)^2} I_2` (:math:`g_{xx} - g_{yy} = 0`, :math:`g_{xy} = 0`).
* :func:`~geometor.ptolemy.stereographic.construct_astrolabe_planisphere` executes Ptolemy's folded-meridian compass-and-straightedge construction in ``geometor.model``, proving :math:`\angle MDT = 90^\circ`, incidence of :math:`B` and :math:`D` on `cMBTD`, and :math:`EL \cdot EK = ED^2` with zero `Float` atoms.

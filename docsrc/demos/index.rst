:order: 25
:nav_title: Demos

Symbolic Demonstrations
=======================

Executable pure-symbolic Python demonstrations (`Model(..., auto_intersect=False)`) verifying every geometric construction and algebraic identity in *Almagest* Book I and *Planisphaerium* with **zero floating-point coordinates**.

.. contents:: On this page
   :local:
   :depth: 2

1. Golden Pentagon–Decagon & Radical Chord Table
------------------------------------------------

Constructs Ptolemy's single-circle regular decagon (:math:`s_{10} = R/\phi`) and regular pentagon (:math:`s_5 = \sqrt{R^2 + s_{10}^2}`) over :math:`\mathbb{Q}(\phi)` (*Almagest* I.10a, Heiberg I, pp. 32–35), evaluates the closed-form SymPy radical tower for Ptolemy's chord cascade (:math:`120^\circ \to \dots \to \frac{3}{4}^\circ`), and verifies Ptolemy's Inequality Lemma bounding :math:`\operatorname{crd}(1^\circ) \approx 1;2,50` and :math:`\pi \approx 3;8,30 = \frac{377}{120}`.

.. literalinclude:: ../../demos/pentagon_chords.py
   :language: python
   :linenos:

Run locally:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/pentagon_chords.py

2. Ptolemy's Theorem on Cyclic Quadrilaterals & Menelaus Calculus
-----------------------------------------------------------------

Constructs rational cyclic quadrilaterals (`pythagorean_65` with integer sides :math:`25, 39, 60, 52` and integer diagonals :math:`56, 63` where :math:`56 \times 63 = 3528 = 25 \times 60 + 39 \times 52`, plus `brahmagupta` with perpendicular diagonals) alongside Ptolemy's Planar & 3D Spherical Menelaus lemmas and I.14 solar declinations.

.. literalinclude:: ../../demos/cyclic_quadrilateral.py
   :language: python
   :linenos:

Run locally:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/cyclic_quadrilateral.py

3. Planisphaerium Stereographic Projection & Astrolabe Plate
------------------------------------------------------------

Proves universal stereographic circle-preservation, the conformal metric pullback :math:`ds^2 = \frac{4(dx^2 + dy^2)}{(1 + x^2 + y^2)^2}`, and §4 circular inversion (:math:`r_+ \cdot r_- = R_{\text{eq}}^2`), and constructs the exact rational astrolabe plate (:math:`R_{\text{eq}} = 60`, :math:`r_{\text{Can}} = 40`, :math:`r_{\text{Cap}} = 90`, oblique ecliptic center :math:`(0, 25)` and radius :math:`65`).

.. literalinclude:: ../../demos/stereographic.py
   :language: python
   :linenos:

Run locally:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/stereographic.py

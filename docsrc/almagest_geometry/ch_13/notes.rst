:order: 13
:type: chapter
:book: Almagest (Book I)
:title: Chapter 13 · Notes
:folio: heiberg_1898_syntaxis_vol1_pt1:0078

.. _almagest-ch-13-notes:

Chapter 13 · Notes
==================

Historical & Projective Analysis
--------------------------------

1. Why One Theorem Sufficed for All Spherical Trigonometry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Modern spherical trigonometry relies on multiple triangle laws (spherical law of cosines, law of sines, Napier's rules for right spherical triangles). Throughout Books I, II, and VIII of the *Almagest*, :person:`Ptolemy <ptolemy>` uses **only a single spherical theorem**: the six-quantity Menelaus transversal configuration of Chapter 13 (:person:`Menelaus <menelaus>`, :cite:`Sphaerica III.1 <menelaus:sphaerica>`).

By choosing three quadrant arcs (:math:`90^\circ`, whose double-arc chord is the diameter :math:`120^p`) in the six-arc Menelaus figure, three of the six chords collapse to :math:`120^p`, instantly yielding right-spherical-triangle identities:

* :math:`\sin\delta = \sin\varepsilon\sin\lambda` (Declination, I.14)
* :math:`\tan\alpha = \cos\varepsilon\tan\lambda` (Right Ascension, I.16)
* :math:`\sin\Delta\alpha = \tan\varphi\tan\delta` (Ascensional Difference, II.7)

2. Projective Essence of Ptolemy's 3D Proof (``Eucl. XI.3``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Ptolemy's proof on page 75 of Heiberg, rather than working intrinsically on the curved sphere, Ptolemy projects the spherical figure from the center :math:`H` of the sphere onto the flat plane containing :math:`\triangle A\Gamma\Delta`.
Under central (gnomonic) projection from :math:`H`, **every great circle on the sphere is the intersection of a central plane with the sphere**, and therefore projects onto the plane :math:`\Pi(A,\Gamma,\Delta)` as a **straight line** (:just:`Eucl. XI.3 <XI.3>`). Thus the great-circle transversal :math:`B\text{–}Z\text{–}E` becomes the straight planar Menelaus line :math:`\Lambda\text{–}K\text{–}\Theta`.

In :func:`geometor.ptolemy.menelaus_sphaerica.verify_spherical_menelaus`, we instantiate six exact rational points on the 3D sphere :math:`X^2 + Y^2 + Z^2 = 9`, compute the exact 3D line-plane intersections :math:`\Theta, K, \Lambda \in \mathbb{Q}^3`, verify :math:`\Theta - \Lambda \parallel K - \Lambda`, and confirm exact equality of squared double-arc chord ratios (:math:`1089/625 = 1089/625`).

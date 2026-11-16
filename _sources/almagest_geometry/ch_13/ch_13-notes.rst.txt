:order: 5
:type: chapter
:book: Syntaxis Mathematica (Almagest)
:title: Chapter 13 · Notes
:folio: heiberg_1898_syntaxis_vol1_pt1:0078
:tracks: English: ch_13-en | Greek: ch_13-el | Summary: ch_13-summary | Notes: ch_13-notes

.. _almagest-ch-13-notes:

Chapter 13 · Notes
==================

Historical & Projective Analysis
--------------------------------

1. Why One Theorem Sufficed for All Spherical Trigonometry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Modern spherical trigonometry relies on multiple triangle laws (spherical law of cosines, law of sines, Napier's rules for right spherical triangles). Throughout Books I, II, and VIII of the *Almagest*—computing solar declinations (I.14), right ascensions (I.16), ascensional differences, oblique ascensions, length of daylight, meridian shadows, and rising/setting stars (Book II)—:person:`Ptolemy <ptolemy>` uses **only a single spherical theorem**: the six-quantity Menelaus transversal configuration of Chapter 13 (:person:`Menelaus <menelaus>`, :cite:`Sphaerica III.1 <menelaus:sphaerica>`).

By choosing three quadrant arcs ($90^\circ$, whose double-arc chord is the diameter $120^p$) in the six-arc Menelaus figure, three of the six chords collapse to $120^p$, instantly producing every right-spherical-triangle identity:

* $\sin\delta = \sin\varepsilon\sin\lambda$ (*Almagest* I.14, Declination)
* $\tan\alpha = \cos\varepsilon\tan\lambda$ (*Almagest* I.16, Right Ascension)
* $\sin\Delta\alpha = \tan\varphi\tan\delta$ (*Almagest* II.7, Ascensional Difference / Rising Time)

2. Projective Essence of Ptolemy's 3D Proof (`Eucl. XI.3`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Ptolemy's proof on page 75 of Heiberg: rather than working intrinsically on the curved sphere, Ptolemy projects the spherical figure from the center $H$ of the sphere onto the flat plane containing $\triangle A\Gamma\Delta$. Under central (gnomonic) projection from $H$, **every great circle on the sphere is the intersection of a central plane with the sphere**, and therefore projects onto the plane $\Pi(A,\Gamma,\Delta)$ as a **straight line** (:just:`Eucl. XI.3 <XI.3>`). Thus the great-circle transversal $B\text{–}Z\text{–}E$ becomes the straight planar Menelaus line $\Lambda\text{–}K\text{–}\Theta$!

In :func:`geometor.ptolemy.menelaus_sphaerica.verify_spherical_menelaus`, we instantiate six exact rational points on the 3D sphere $X^2 + Y^2 + Z^2 = 9$ (`A = (0,0,3)`, `B = (2,-1,2)`, `C = (1,2,2)`, etc.), compute the exact 3D line-plane intersections $\Theta, K, \Lambda \in \mathbb{Q}^3$, verify $\Theta - \Lambda \parallel K - \Lambda$ ($\vec{u} \times \vec{v} = \vec{0}$), and confirm exact equality of squared double-arc chord ratios ($\frac{1089}{625} = \frac{1089}{625}$).

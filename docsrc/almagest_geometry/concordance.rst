.. _ptolemy-concordance:

Cross-Corpus Geometric Concordance
==================================

Bidirectional mapping linking :person:`Claudius Ptolemy's <ptolemy>` propositions in *Almagest* Book I and *Planisphaerium* to sister repositories across the **GEOMETOR** canon and to executable symbolic modules in ``geometor.ptolemy``.

.. list-table::
   :header-rows: 1
   :widths: 20 28 26 26

   * - Ptolemy Locus
     - Geometric Proposition / Construction
     - Companion GEOMETOR Canon
     - Symbolic Module (``geometor.ptolemy``)
   * - *Almagest* I.1 (*Heiberg I, pp. 4–7*)
     - Tripartite division of theoretical philosophy (*physics, mathematics, theology*)
     - ``aristotle`` (*Metaphysics* E.1, 1026a18–19); ``proclus`` (*Prologue I*)
     - —
   * - *Almagest* I.10a (*Heiberg I, pp. 32–35*)
     - Single-circle construction of regular decagon ($s_{10} = R/\phi$) & pentagon ($s_5 = \sqrt{R^2 + s_{10}^2}$)
     - ``euclid`` / ``elements`` (II.6, VI.Def.3, XIII.9, XIII.10); ``divine`` ($\mathbb{Q}(\phi)$)
     - :func:`~geometor.ptolemy.pentagon_chords.construct_pentagon_decagon`
   * - *Almagest* I.10b (*Heiberg I, pp. 36–37*)
     - **Ptolemy's Theorem** on cyclic quadrilaterals ($AC \cdot BD = AB \cdot CD + BC \cdot DA$)
     - ``euclid`` (III.21, VI.4, VI.16, II.1); ``casey`` (*Sequel* VI.6); ``altshiller-court``
     - :func:`~geometor.ptolemy.cyclic_quadrilateral.construct_ptolemy_quadrilateral`
   * - *Almagest* I.10b (*Heiberg I, pp. 38–42*)
     - Chord Difference, Half-Arc Lemma, Chord Sum, & Irreducibility of Angle Trisection
     - ``euclid`` / ``elements`` (I.47, III.31, VI.8)
     - :func:`~geometor.ptolemy.pentagon_chords.chord_difference`, :func:`~geometor.ptolemy.pentagon_chords.chord_half_arc`
   * - *Almagest* I.10b & VI.7 (*Heiberg I, pp. 43–46, 513*)
     - **Ptolemy's Inequality Lemma** ($\frac{\operatorname{crd}\alpha}{\operatorname{crd}\beta} < \frac{\alpha}{\beta}$), $\operatorname{crd}(1^\circ) \approx 1;2,50$, $\pi \approx 3;8,30 = \frac{377}{120}$
     - ``archimedes`` (*Dimensio Circuli* Prop. 3); ``euclid`` (VI.3, VI.33)
     - :func:`~geometor.ptolemy.pentagon_chords.verify_ptolemy_pi`
   * - *Almagest* I.13a (*Heiberg I, pp. 68–70*)
     - **Planar Menelaus Sector Lemma** (*kata synthesin* & *kata diairesin* via $EH \parallel \Gamma\Delta$)
     - ``menelaus``; ``pappus`` (*Synagoge* VII); ``euclid`` (I.31, VI.4)
     - :func:`~geometor.ptolemy.menelaus_sphaerica.construct_planar_menelaus`
   * - *Almagest* I.13b–I.14 (*Heiberg I, pp. 70–78*)
     - **3D Spherical Menelaus Theorem** ($\Theta, K, \Lambda$ collinear) & Solar Declination Law
     - ``menelaus`` (*Sphaerica* III.1); ``euclid`` (VI.1, XI.3)
     - :func:`~geometor.ptolemy.menelaus_sphaerica.verify_spherical_menelaus`, :func:`~geometor.ptolemy.menelaus_sphaerica.compute_solar_declination`
   * - *Planisphaerium* §§1–3 (*Heiberg II, pp. 227–232*)
     - Stereographic projection of equator, tropics, oblique ecliptic ($\angle mdt = 90^\circ$), & horizon
     - ``apollonius`` (*Conics* I.5 subcontrary section); ``euclid`` (III.31)
     - :func:`~geometor.ptolemy.stereographic.construct_astrolabe_planisphere`
   * - *Planisphaerium* §4 (*Heiberg II, pp. 233–234*)
     - Circular inversion of opposite parallels ($r_{\text{Cap}} \cdot r_{\text{Can}} = R_{\text{eq}}^2$; $92;8,15 \times 39;4,19 \approx 60^2$)
     - ``casey``; ``altshiller-court`` (Ch. IX Inversion)
     - :func:`~geometor.ptolemy.stereographic.prove_parallel_inversion_symbolically`

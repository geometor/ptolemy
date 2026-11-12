Claudius Ptolemy
================

*Chord Trigonometry, Cyclic Quadrilaterals, Spherical Menelaus Calculus, and Stereographic Projection*

.. epigraph::

   Οἶδ' ὅτι θνητὸς ἔφυν καὶ ἐφήμερος· ἀλλ' ὅταν ἄστρων
   μαστίζω πυκινὰς ἀμφιδρόμους ἕλικας,
   οὐκέτ' ἐπιψαύω γαίης ποσίν, ἀλλὰ παρ' αὐτῷ
   Ζηνὶ διοτρεφέος πίμπλαμαι ἀμβροσίης.

   *I know that I am mortal and a creature of a day; yet when I trace the close-set wheeling spirals of the stars, my feet no longer touch the earth, but beside Zeus himself I take my fill of god-nurturing ambrosia.*

   — Epigram prefixed to :person:`Claudius Ptolemy's <ptolemy>` *Syntaxis Mathematica* (:cite:`Heiberg 1898, p. 4 <heiberg:1898>`)

Overview
--------

**GEOMETOR Ptolemy** (`geometor-ptolemy`) unites a scholarly **Digital Scriptorium Book Codex** with **100% exact symbolic SymPy / ``geometor.model`` constructions and proofs** for the two foundational geometric treatises of :person:`Claudius Ptolemy <ptolemy>` (c. 100–170 CE):

1. ***Almagest* (*Μαθηματικὴ Σύνταξις*, Book I, Chapters 1–14)**: Edited from :person:`J. L. Heiberg's <heiberg>` Teubner Greek edition (*Syntaxis Mathematica*, Vol. I.1, 1898), establishing cosmic sphericity, the sexagesimal chord circle ($R = 60^p$, $D = 120^p$), **Ptolemy's single-circle construction of the regular decagon and pentagon** over $\mathbb{Q}(\phi)$, **Ptolemy's Theorem on Cyclic Quadrilaterals** ($AC \cdot BD = AB \cdot CD + BC \cdot DA$), the difference/sum/half-arc chord calculus, **Ptolemy's Inequality Lemma** ($\operatorname{crd} 1^\circ \approx 1;2,50 \implies \pi \approx 3;8,30 = \frac{377}{120}$), and **Planar & Spherical Menelaus Transversal Trigonometry**.
2. ***Planisphaerium* (Sections 1–4)**: Edited from :person:`J. L. Heiberg's <heiberg>` Teubner Latin edition (*Opera Astronomica Minora*, Vol. II, 1907) of :person:`Hermann of Carinthia's <hermann>` 1143 translation, establishing **stereographic projection** of the celestial sphere from the South Pole onto the equatorial plane, conformal circle-preservation via :person:`Apollonius's <apollonius>` subcontrary cone section (*Conics* I.5), circular inversion of opposite parallels ($r_{\text{Cap}} \cdot r_{\text{Can}} = R_{\text{eq}}^2$), and the geometry of the planispheric astrolabe.

Architecture of the Repository
------------------------------

* **Digital Scriptorium Codex** (:doc:`almagest_geometry/index`): Four multi-track units (`:layout: book`) pairing original English translations with verbatim polytonic Greek (1898) and scientific Latin (1907) primary texts, executive geometric summaries, historical commentary, interactive `.euclid-graphic` SVGs, and linked apparatus registries (:doc:`Concordance <almagest_geometry/concordance>`, :doc:`Bibliography <almagest_geometry/bibliography>`, :doc:`Persons <almagest_geometry/persons>`, :doc:`Glossary <almagest_geometry/glossary>`).
* **Exact Symbolic Demonstrations** (:doc:`demos/index`): Pure-symbolic Python constructions (`Model(..., auto_intersect=False)`) free of floating-point coordinates, verifying every chord, cyclic quadrilateral, Menelaus transversal ratio, and stereographic circle over $\mathbb{Q}$, $\mathbb{Q}(\phi)$, and exact radical towers.
* **Python API Reference** (:doc:`modules/index`): Documented modules in ``geometor.ptolemy`` (`pentagon_chords`, `cyclic_quadrilateral`, `menelaus_sphaerica`, `stereographic`).

.. toctree::
   :maxdepth: 2
   :hidden:

   almagest_geometry/index
   demos/index
   modules/index

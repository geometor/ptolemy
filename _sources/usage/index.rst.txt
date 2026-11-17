:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Reader's Guide to the Multi-Track Digital Scriptorium of Claudius Ptolemy

A guide to navigating the **GEOMETOR Ptolemy** digital edition, designed for scholars, mathematicians, and students exploring classical chord trigonometry, cyclic quadrilaterals, spherical Menelaus transversals, and stereographic projection.

.. contents:: On this page
   :local:
   :depth: 2

Synchronized Reading Tracks
---------------------------

Every treatise unit in **Almagest Book I** and **Planisphaerium** features synchronized parallel reading tracks accessible via the top track switcher:

* **English (EN)**: Modern mathematical translation faithfully expressing Ptolemy's geometric proofs, sexagesimal calculations, and systematic theorems.
* **Greek / Latin Primary Text (EL / LA)**: Verbatim polytonic Greek text from :person:`J. L. Heiberg's <heiberg>` critical edition (:cite:`1898 <heiberg:1898>`) for the *Almagest*, and medieval scientific Latin from Hermann of Carinthia's 1143 translation (:cite:`Heiberg 1907 <heiberg:1907>`) for *Planisphaerium*.
* **Summary**: Executive mathematical summaries highlighting the essential propositions, algebraic identities, trigonometric values, and axiomatic dependency chains.
* **Notes & Commentary**: In-depth historical, philological, and mathematical commentary analyzing Euclidean foundations, alternative proofs, and modern connections.

Primary-Source Folio Milestones
-------------------------------

Marginal milestone references coordinate each chapter and theorem directly with classical and modern scholarly editions:

* **Heiberg Pagination**: Page and line markers throughout the text link directly to the authoritative volumes of *Claudii Ptolemaei Opera quae exstant omnia* (Vol. I.1, 1898; Vol. II, 1907).
* **Comparative Editions**: Parallel cross-references coordinate loci across :person:`N. B. Halma <halma>` (:cite:`1813 <halma:1813>`) and :person:`Karl Manitius <manitius>` (:cite:`1912 <manitius:1912>`).

Interactive Diagrams & Deductive Links
--------------------------------------

Figures throughout the codex are rendered using responsive, pure-vector SVGs generated directly from symbolic models:

* **Geometric Hover Labels**: Hovering over or clicking element labels (such as points, circles, chords, and transversal arcs) visually highlights corresponding geometric features in the figures.
* **Cross-Proposition Anchors**: Citations to Euclid's *Elements* (e.g. I.47, III.21, VI.4, XIII.9–10) and Apollonius's *Conics* (I.5) connect Ptolemy's deductive chain to the broader GEOMETOR canon.
* **Symbolic Precision**: All diagrams reflect exact algebraic coordinates over $\mathbb{Q}(\phi)$ and quadratic radical extensions, avoiding floating-point rounding errors.

Full-Text Search with In-Page Highlighting
------------------------------------------

The built-in documentation search engine offers deep indexing across all tracks:

* **Instant Search**: Querying terms like *chord of difference*, *cyclic quadrilateral*, *Menelaus*, or *stereographic* indexes all translations, summaries, and commentaries.
* **In-Page Term Highlighting**: Clicking search results opens the target document with matching terms highlighted via `?highlight=`, allowing rapid traversal of dense mathematical texts.

Categories, Tags, Document Types & Collection Views
---------------------------------------------------

The edition is organized using multi-dimensional metadata facets:

* **Sidebar Facets**: Browse content grouped by historical era, mathematical discipline, or document type.
* **Collection Views**: Index pages support multiple display modes (**Cards**, **Banners**, or **List**) for flexible navigation of treatise units and demonstrations.

People, Bibliography & Glossary Tooltips
----------------------------------------

Rich contextual references are woven into every page:

* **People Hover Cards**: Interactive `:person:` cross-references (such as :person:`Claudius Ptolemy <ptolemy>`, :person:`Hipparchus <hipparchus>`, and :person:`Menelaus <menelaus>`) link directly to biographical profiles in the :doc:`People </almagest_geometry/people/index>` register.
* **Citation Popups**: Inline bibliographic citations (:cite:`Heiberg 1898 <heiberg:1898>`) provide provenance and direct links to the :doc:`Bibliography </almagest_geometry/bibliography>`.
* **Technical Glossary**: Specialized Greek and Latin terms (e.g., :term:`Syntaxis Mathematica <syntaxis-mathematike>`, :term:`extreme and mean ratio <akron-kai-meson-logon>`) connect directly to the :doc:`Glossary </almagest_geometry/glossary>`.
* **Theme Switching**: Toggle between Light and Dark reading modes via the header controls.

Command-Line & Python API
-------------------------

The underlying ``geometor.ptolemy`` package provides executable Python modules for verification and computation:

Run the CLI summary:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python -m geometor.ptolemy

Import symbolic constructions in Python:

.. code-block:: python

   from geometor.ptolemy.pentagon_chords import construct_pentagon_decagon, verify_ptolemy_pi
   from geometor.ptolemy.cyclic_quadrilateral import construct_ptolemy_quadrilateral
   from geometor.ptolemy.stereographic import construct_astrolabe_planisphere

   # Verify Ptolemy's approximation of pi via chord inequality
   pi_bounds = verify_ptolemy_pi()

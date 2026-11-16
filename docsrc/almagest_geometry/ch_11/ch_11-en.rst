:order: 3
:type: chapter
:book: Syntaxis Mathematica (Almagest)
:title: Chapter 11 · Table of Chords in a Circle
:folio: heiberg_1898_syntaxis_vol1_pt1:0057
:tracks: English: ch_11-en | Greek: ch_11-el | Summary: ch_11-summary | Notes: ch_11-notes

.. _almagest-ch-11-en:

Chapter 11 · Table of Chords in a Circle
========================================

*Almagest* Book I, Chapter 11 (:cite:`Heiberg 1898, Vol. I.1, pp. 47–63 <heiberg:1898>`)
----------------------------------------------------------------------------------------

Layout & Method of the Table (`Heiberg I, pp. 47–48`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:line:`p. 47` So that on every practical occasion we may have the magnitudes of the :term:`chords <eutheia-hypoteinousa>` set out ready at hand, we shall subjoin tables arranged in sections of $45$ lines each for symmetry:

1. **First Column**: The magnitudes of the arcs advancing by increments of half a degree ($\frac{1}{2}^\circ, 1^\circ, 1\frac{1}{2}^\circ, \dots, 180^\circ$).
2. **Second Column**: The magnitudes of the straight lines subtending them in parts where the diameter is divided into $120^p$, expressed in parts, sexagesimal minutes (*primes*), and sexagesimal seconds.
3. **Third Column (`ἑξηκοστά`, Sixtieths)**: One-thirtieth of the excess of the chord across each half-degree interval, giving the mean change per single arc-minute ($1'$)—imperceptibly differing from exactness—for rapid linear interpolation of intermediate arcs.

Algorithmic Error-Checking & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ptolemy adds an extraordinary methodological principle on **computational self-verification** (`p. 47, ll. 13–20`):

   *Even if we fall into doubt regarding some scribal error (`γραφικῆς ἁμαρτίας`) in any chord value in the table, the very theorems demonstrated above enable immediate verification and correction—either from the chord subtending double the arc under inquiry, from its difference with other given arcs, or from the chord subtending the remainder of the semicircle.*

Representative Table of Chords ($D = 120^p$)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Arcs ($\theta$)
     - Subtending Chords ($\operatorname{crd}\theta$)
     - Sixtieths (Interpolation per $1'$)
   * - $0^\circ 30'$
     - ``0;31,25``
     - ``0;1,2,50``
   * - $1^\circ 00'$
     - ``1;2,50``
     - ``0;1,2,50``
   * - $1^\circ 30'$
     - ``1;34,15``
     - ``0;1,2,48``
   * - $30^\circ 00'$
     - ``31;3,30``
     - ``0;0,57,59``
   * - $36^\circ 00'$ (Decagon)
     - ``37;4,55``
     - ``0;0,56,43``
   * - $60^\circ 00'$ (Hexagon)
     - ``60;0,0``
     - ``0;0,51,58``
   * - $72^\circ 00'$ (Pentagon)
     - ``70;32,3``
     - ``0;0,48,34``
   * - $90^\circ 00'$ (Square)
     - ``84;51,10``
     - ``0;0,42,25``
   * - $120^\circ 00'$ (Triangle)
     - ``103;55,23``
     - ``0;0,30,0``
   * - $180^\circ 00'$ (Diameter)
     - ``120;0,0``
     - ``0;0,0,0``

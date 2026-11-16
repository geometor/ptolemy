:order: 3
:type: chapter
:book: Syntaxis Mathematica (Almagest)
:title: Chapter 11 · Summary
:folio: heiberg_1898_syntaxis_vol1_pt1:0057
:tracks: English: ch_11-en | Greek: ch_11-el | Summary: ch_11-summary | Notes: ch_11-notes

.. _almagest-ch-11-summary:

Chapter 11 · Summary
====================

Structure & Computational Logic of the Table of Chords
------------------------------------------------------

1. **Table Organization**:
   - Total extent: $0^\circ 30'$ to $180^\circ 00'$ in uniform increments of $0^\circ 30'$ (360 rows, organized into 8 pages of 45 rows each).
   - Base parameters: Circle circumference $= 360^\circ$, Diameter $D = 120^p$, Radius $R = 60^p$.

2. **Column Structure**:
   - Column 1: Arc length $\theta$ in degrees and minutes ($\text{deg}, \text{min}$).
   - Column 2: Subtending chord $\operatorname{crd}\theta$ in sexagesimal parts ($p; m, s$).
   - Column 3: Differences / Sixtieths ($\delta$), representing $\frac{1}{30}[\operatorname{crd}(\theta + 30') - \operatorname{crd}\theta]$ in parts per arc-minute ($1'$).

3. **Interpolation Algorithm**:
   For any intermediate arc $\theta + \Delta$ where $0 < \Delta < 30'$:

   $$\operatorname{crd}(\theta + \Delta) \approx \operatorname{crd}\theta + \Delta \cdot \delta.$$

   Because the second derivative of the chord function $\operatorname{crd}''(\theta) = -30\sin(\theta/2)$ is small over a $30'$ interval, linear interpolation yields an error bounded by:

   $$\text{Error} \le \frac{1}{8} (\Delta\theta)^2 \cdot \max |\operatorname{crd}''| \approx \frac{1}{8} \left(\frac{\pi}{360}\right)^2 \times 30 \approx 2.8 \times 10^{-4} \text{ parts},$$

   which is well below one sexagesimal second ($1'' = \frac{1}{3600} \approx 2.78 \times 10^{-4}$). Thus linear interpolation preserves full two-place sexagesimal precision throughout the entire table.

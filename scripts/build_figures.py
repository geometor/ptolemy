#!/usr/bin/env python3
"""Generate the 9 interactive .euclid-graphic SVG plates for GEOMETOR Ptolemy.

Each SVG strictly obeys the ``photon-platform/publish`` ``.euclid-graphic`` contract:
- ``<defs>`` tick markers (``#geom-tick-1..3``)
- Ordered layer groups: ``#elements``, ``#graphics``, ``#highlights``, ``#points``, ``#labels``
- 3-vertex midpoint ``<path d="M x1 y1 L mx my L x2 y2">`` segments
- Canonical ``data-ref`` attributes wired to ``:g:`` roles in the Book Codex
- Theme-adaptive CSS variables for seamless dark/light mode rendering
"""

from __future__ import annotations

import math
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[1] / "docsrc" / "_static" / "figures"

DEFS_BLOCK = """  <defs>
    <marker id="geom-tick-1" viewBox="-2 -6 4 12" refX="0" refY="0" markerWidth="4" markerHeight="12" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
    </marker>
    <marker id="geom-tick-2" viewBox="-4 -6 8 12" refX="0" refY="0" markerWidth="8" markerHeight="12" orient="auto">
      <line x1="-1.8" y1="-4.5" x2="-1.8" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      <line x1="1.8" y1="-4.5" x2="1.8" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" orient="auto">
      <line x1="-3.4" y1="-4.5" x2="-3.4" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      <line x1="3.4" y1="-4.5" x2="3.4" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
    </marker>
  </defs>"""


class EuclidSVGBuilder:
    """Helper assembling a clean, theme-adaptive ``.euclid-graphic`` SVG."""

    def __init__(self, width: int, height: int, aria_label: str) -> None:
        """Initialize layer buffers."""
        self.width = width
        self.height = height
        self.aria_label = aria_label
        self.elements: list[str] = []
        self.graphics: list[str] = []
        self.highlights: list[str] = []
        self.points: list[str] = []
        self.labels: list[str] = []

    def seg(
        self,
        p1: tuple[float, float],
        p2: tuple[float, float],
        ref: str,
        *,
        cls: str = "geom-line",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
        ticks: int = 0,
    ) -> None:
        """Add a 3-vertex midpoint path segment to ``#elements``."""
        x1, y1 = p1
        x2, y2 = p2
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        attrs = [
            f'class="{cls}"',
            f'd="M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}"',
            'fill="none"',
            f'data-ref="{ref}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        if ticks in (1, 2, 3):
            attrs.append(f'marker-mid="url(#geom-tick-{ticks})"')
        self.elements.append(f"    <path {' '.join(attrs)}/>")

    def circle(
        self,
        center: tuple[float, float],
        radius: float,
        ref: str,
        *,
        cls: str = "geom-circle",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
    ) -> None:
        """Add a circle to ``#elements``."""
        cx, cy = center
        attrs = [
            f'class="{cls}"',
            f'cx="{cx:.2f}"',
            f'cy="{cy:.2f}"',
            f'r="{radius:.2f}"',
            'fill="none"',
            f'data-ref="{ref}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        self.elements.append(f"    <circle {' '.join(attrs)}/>")

    def ellipse(
        self,
        center: tuple[float, float],
        rx: float,
        ry: float,
        ref: str,
        *,
        rot_deg: float = 0.0,
        cls: str = "geom-circle",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
    ) -> None:
        """Add a projected 3D great-circle / small-circle ellipse to ``#elements``."""
        cx, cy = center
        attrs = [
            f'class="{cls}"',
            f'cx="{cx:.2f}"',
            f'cy="{cy:.2f}"',
            f'rx="{rx:.2f}"',
            f'ry="{ry:.2f}"',
            'fill="none"',
            f'data-ref="{ref}"',
        ]
        if abs(rot_deg) > 1e-6:
            attrs.append(f'transform="rotate({rot_deg:.2f} {cx:.2f} {cy:.2f})"')
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        self.elements.append(f"    <ellipse {' '.join(attrs)}/>")

    def arc(
        self,
        center: tuple[float, float],
        radius: float,
        deg_start: float,
        deg_end: float,
        ref: str,
        *,
        cls: str = "geom-arc",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
        layer: str = "elements",
    ) -> None:
        """Add an SVG circular arc (standard math CCW degrees converted to SVG screen coords)."""
        cx, cy = center
        a1 = math.radians(deg_start)
        a2 = math.radians(deg_end)
        x1, y1 = cx + radius * math.cos(a1), cy - radius * math.sin(a1)
        x2, y2 = cx + radius * math.cos(a2), cy - radius * math.sin(a2)
        span = (deg_end - deg_start) % 360.0
        large = 1 if span > 180.0 else 0
        # Counter-clockwise in math (y-up) is sweep-flag=0 in SVG (y-down)
        d_str = f"M {x1:.2f} {y1:.2f} A {radius:.2f} {radius:.2f} 0 {large} 0 {x2:.2f} {y2:.2f}"
        attrs = [f'class="{cls}"', f'd="{d_str}"', 'fill="none"', f'data-ref="{ref}"']
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        target = self.graphics if layer == "graphics" else self.elements
        target.append(f"    <path {' '.join(attrs)}/>")

    def right_angle(
        self,
        vertex: tuple[float, float],
        u1: tuple[float, float],
        u2: tuple[float, float],
        ref: str,
        *,
        size: float = 13.0,
    ) -> None:
        """Draw a crisp right-angle square marker in ``#graphics``."""
        vx, vy = vertex
        p1 = (vx + u1[0] * size, vy + u1[1] * size)
        p12 = (vx + (u1[0] + u2[0]) * size, vy + (u1[1] + u2[1]) * size)
        p2 = (vx + u2[0] * size, vy + u2[1] * size)
        self.graphics.append(
            f'    <path class="geom-ang-arc" d="M {p1[0]:.2f} {p1[1]:.2f} '
            f'L {p12[0]:.2f} {p12[1]:.2f} L {p2[0]:.2f} {p2[1]:.2f}" '
            f'fill="none" stroke="var(--geom-muted, #64748b)" stroke-width="1.25" data-ref="{ref}"/>'
        )

    def polygon(
        self,
        pts: list[tuple[float, float]],
        ref: str,
        *,
        fill: str = "var(--geom-accent, #d97706)",
        fill_opacity: float = 0.11,
    ) -> None:
        """Add a translucent highlight polygon to ``#highlights``."""
        coords = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        self.highlights.append(
            f'    <polygon class="geom-polygon" points="{coords}" '
            f'fill="{fill}" fill-opacity="{fill_opacity:.2f}" stroke="none" data-ref="{ref}"/>'
        )

    def point(
        self,
        pt: tuple[float, float],
        ref: str,
        *,
        r: float = 3.6,
        fill: str | None = None,
    ) -> None:
        """Add a point dot to ``#points``."""
        px, py = pt
        fill_attr = f' fill="{fill}"' if fill else ""
        self.points.append(
            f'    <circle class="geom-point" cx="{px:.2f}" cy="{py:.2f}" r="{r:.2f}"{fill_attr} data-ref="{ref}"/>'
        )

    def label(
        self,
        pt: tuple[float, float],
        text: str,
        ref: str,
        *,
        dx: float = 0.0,
        dy: float = 0.0,
        size: int = 15,
        italic: bool = True,
        anchor: str = "middle",
    ) -> None:
        """Add a label to ``#labels``."""
        lx, ly = pt[0] + dx, pt[1] + dy
        style_italic = "font-style: italic; " if italic else ""
        self.labels.append(
            f'    <text class="geom-label" x="{lx:.2f}" y="{ly:.2f}" '
            f'text-anchor="{anchor}" dominant-baseline="central" '
            f'style="{style_italic}font-size: {size}px;" data-ref="{ref}">{text}</text>'
        )

    def caption(self, x: float, y: float, text: str, *, size: int = 13) -> None:
        """Add a subtle structural caption inside multi-panel plates."""
        self.labels.append(
            f'    <text class="geom-label" x="{x:.2f}" y="{y:.2f}" '
            f'text-anchor="middle" style="font-size: {size}px; opacity: 0.82;">{text}</text>'
        )

    def render(self) -> str:
        """Return complete formatted SVG string."""
        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
            f'viewBox="0 0 {self.width} {self.height}" role="img" aria-label="{self.aria_label}">',
            DEFS_BLOCK,
            '  <g id="elements">',
            *self.elements,
            "  </g>",
            '  <g id="graphics">',
            *self.graphics,
            "  </g>",
            '  <g id="highlights">',
            *self.highlights,
            "  </g>",
            '  <g id="points">',
            *self.points,
            "  </g>",
            '  <g id="labels">',
            *self.labels,
            "  </g>",
            "</svg>",
            "",
        ]
        return "\n".join(parts)


def build_fig01_celestial_sphere() -> str:
    """Almagest I.1-I.8: Spherical heavens, central Earth O, equator, ecliptic (23°51'), & horizon."""
    b = EuclidSVGBuilder(560, 440, "Almagest Book I Chs. 1-8 Celestial Sphere and Oblique Ecliptic")
    cx, cy, r = 280.0, 220.0, 165.0

    # Meridian outer circle
    b.circle((cx, cy), r, "cABGD", cls="geom-circle", width=1.8)
    # Horizon (horizontal ellipse)
    b.ellipse((cx, cy), r, 44.0, "cHOR", cls="geom-dashed", dash="6 4")
    # Celestial Equator (tilted by co-latitude 36°)
    eq_tilt = -26.0
    b.ellipse((cx, cy), r, 52.0, "cEQ", stroke="var(--geom-assert, #2563eb)", width=1.8, rot_deg=eq_tilt)
    # Oblique Ecliptic (tilted by +23.85° relative to Equator -> -2.15°)
    ecl_tilt = eq_tilt + 23.85
    b.ellipse((cx, cy), r, 52.0, "cECL", cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=2.2, rot_deg=ecl_tilt)

    # Celestial Axis P - P' perpendicular to Equator
    ax_rad = math.radians(eq_tilt + 90.0)
    pt_p = (cx - r * math.cos(ax_rad), cy - r * math.sin(ax_rad))
    pt_ps = (cx + r * math.cos(ax_rad), cy + r * math.sin(ax_rad))
    b.seg(pt_p, pt_ps, "PPprime", cls="geom-dashed", dash="5 4")

    # Equator diameter A - G and Ecliptic diameter B - D
    eq_rad = math.radians(eq_tilt)
    pt_a = (cx - r * math.cos(eq_rad), cy - r * math.sin(eq_rad))
    pt_g = (cx + r * math.cos(eq_rad), cy + r * math.sin(eq_rad))
    b.seg(pt_a, pt_g, "AG", stroke="var(--geom-assert, #2563eb)", width=1.3)

    ecl_rad = math.radians(ecl_tilt)
    pt_b = (cx - r * math.cos(ecl_rad), cy - r * math.sin(ecl_rad))
    pt_d = (cx + r * math.cos(ecl_rad), cy + r * math.sin(ecl_rad))
    b.seg(pt_b, pt_d, "BD", stroke="var(--geom-accent, #d97706)", width=1.5)

    # Zenith Z and Nadir N
    pt_z = (cx, cy - r)
    pt_n = (cx, cy + r)
    b.seg(pt_z, pt_n, "ZN", cls="geom-dashed", dash="3 4")

    # Obliquity angle arc between Equator and Ecliptic near G/D
    b.arc((cx, cy), 68.0, 2.15, 26.0, "angEps", cls="geom-ang-arc", stroke="var(--geom-accent, #d97706)", width=1.5, layer="graphics")

    for p, ref in [
        ((cx, cy), "O"),
        (pt_p, "P"),
        (pt_ps, "Pprime"),
        (pt_a, "A"),
        (pt_g, "G"),
        (pt_b, "B"),
        (pt_d, "D"),
        (pt_z, "Z"),
    ]:
        b.point(p, ref)

    b.label((cx, cy), "O", "O", dx=-12, dy=15)
    b.label(pt_p, "P (North Pole)", "P", dx=-38, dy=-12, size=13)
    b.label(pt_ps, "P' (South Pole)", "Pprime", dx=42, dy=12, size=13)
    b.label(pt_a, "A", "A", dx=-16, dy=-6)
    b.label(pt_g, "Γ (Equator)", "G", dx=44, dy=-8, size=13)
    b.label(pt_b, "B", "B", dx=-16, dy=6)
    b.label(pt_d, "Δ (Ecliptic)", "D", dx=44, dy=8, size=13)
    b.label(pt_z, "Z (Zenith)", "Z", dx=0, dy=-14, size=13)
    b.label((cx + 80, cy - 16), "ε", "angEps", size=14)
    return b.render()


def build_fig02_pentagon_decagon() -> str:
    """Almagest I.10a (Heiberg I, p. 32): Golden Pentagon & Decagon construction."""
    b = EuclidSVGBuilder(560, 430, "Almagest I.10a Golden Pentagon and Decagon Construction")
    cx, cy, r = 280.0, 235.0, 155.0

    pt_d = (cx, cy)
    pt_a = (cx - r, cy)
    pt_g = (cx + r, cy)
    pt_b = (cx, cy - r)
    pt_e = (cx + r / 2.0, cy)
    eb_len = math.hypot(pt_b[0] - pt_e[0], pt_b[1] - pt_e[1])
    pt_z = (pt_e[0] - eb_len, cy)  # DZ = R / phi

    # Highlight right triangle B D Z (Euclid XIII.10: BZ^2 = BD^2 + DZ^2)
    b.polygon([pt_b, pt_d, pt_z], "triBDZ", fill="var(--geom-accent, #d97706)", fill_opacity=0.13)

    # Semicircle ABG (and full faint reference circle)
    b.circle(pt_d, r, "cABG_full", cls="geom-dashed", dash="4 4")
    b.arc(pt_d, r, 0.0, 180.0, "cABG", cls="geom-circle", width=1.9)

    # Diameter AG and perpendicular radius DB
    b.seg(pt_a, pt_g, "AG", width=1.5)
    b.seg(pt_d, pt_b, "DB", stroke="var(--geom-assert, #2563eb)", width=1.9)
    b.right_angle(pt_d, (-1.0, 0.0), (0.0, -1.0), "angADB")

    # Bisected segments DE == EG with single tick marks
    b.seg(pt_d, pt_e, "DE", ticks=1)
    b.seg(pt_e, pt_g, "EG", ticks=1)

    # Golden compass swing EB -> EZ
    b.seg(pt_e, pt_b, "EB", cls="geom-dashed", stroke="var(--geom-accent, #d97706)", dash="6 4", width=1.5)
    theta_eb = math.degrees(math.atan2(pt_e[1] - pt_b[1], pt_b[0] - pt_e[0]))  # ~116.565 deg
    b.arc(pt_e, eb_len, theta_eb, 180.0, "arcBZ", cls="geom-arc", stroke="var(--geom-accent, #d97706)", dash="5 4", width=1.6)

    # Resulting Decagon side DZ (golden) and Pentagon side BZ (bold assert)
    b.seg(pt_d, pt_z, "DZ", cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=2.8)
    b.seg(pt_b, pt_z, "BZ", cls="geom-bold", stroke="var(--geom-assert, #2563eb)", width=2.6)

    # Inscribed decagon & pentagon reference chords on semicircle
    ang_36 = math.radians(144.0)
    ang_72 = math.radians(108.0)
    pt_p10 = (cx + r * math.cos(ang_36), cy - r * math.sin(ang_36))
    pt_p5 = (cx + r * math.cos(ang_72), cy - r * math.sin(ang_72))
    b.seg(pt_a, pt_p10, "s10_arc", cls="geom-dashed", stroke="var(--geom-accent, #d97706)", dash="3 3")
    b.seg(pt_a, pt_p5, "s5_arc", cls="geom-dashed", stroke="var(--geom-assert, #2563eb)", dash="3 3")

    for p, ref in [(pt_a, "A"), (pt_b, "B"), (pt_g, "G"), (pt_d, "D"), (pt_e, "E"), (pt_z, "Z")]:
        b.point(p, ref)

    b.label(pt_a, "A", "A", dx=-16, dy=2)
    b.label(pt_b, "B", "B", dx=0, dy=-16)
    b.label(pt_g, "Γ", "G", dx=16, dy=2)
    b.label(pt_d, "Δ", "D", dx=6, dy=18)
    b.label(pt_e, "E", "E", dx=4, dy=18)
    b.label(pt_z, "Z", "Z", dx=-6, dy=18)
    b.label(((pt_d[0] + pt_z[0]) / 2, cy + 34), "ΔZ = R/φ = s₁₀ (37;4,55ᵖ)", "DZ", size=12, italic=False)
    b.label(((pt_b[0] + pt_z[0]) / 2 - 48, (pt_b[1] + pt_z[1]) / 2 - 8), "BZ = s₅ (70;32,3ᵖ)", "BZ", size=12, italic=False)
    return b.render()


def build_fig03_ptolemy_cyclic_quadrilateral() -> str:
    """Almagest I.10b (Heiberg I, p. 37): Ptolemy's Theorem on Cyclic Quadrilaterals."""
    b = EuclidSVGBuilder(540, 440, "Almagest I.10b Ptolemy Theorem on Cyclic Quadrilaterals")
    cx, cy, scale = 270.0, 225.0, 4.9  # Diameter 65 * 4.9 = 318.5 px (R = 159.25)
    r_math = 32.5

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx + mx * scale, cy - my * scale)

    # Exact rational Pythagorean-65 cyclic quadrilateral coordinates!
    m_a = (-32.5, 0.0)
    m_b = (-595.0 / 26.0, 300.0 / 13.0)
    m_c = (2047.0 / 130.0, 1848.0 / 65.0)
    m_d = (91.0 / 10.0, -156.0 / 5.0)
    # Point E divides AC in ratio AE : EC = 500/21 : 676/21 = 125 : 169
    t_e = 125.0 / 294.0
    m_e = (m_a[0] + t_e * (m_c[0] - m_a[0]), m_a[1] + t_e * (m_c[1] - m_a[1]))

    pt_a, pt_b, pt_c, pt_d, pt_e = (
        to_svg(*m_a),
        to_svg(*m_b),
        to_svg(*m_c),
        to_svg(*m_d),
        to_svg(*m_e),
    )

    # Highlight similar triangles ABE and DBC
    b.polygon([pt_a, pt_b, pt_e], "triABE", fill="var(--geom-accent, #d97706)", fill_opacity=0.14)
    b.polygon([pt_d, pt_b, pt_c], "triDBC", fill="var(--geom-assert, #2563eb)", fill_opacity=0.10)

    b.circle((cx, cy), r_math * scale, "cABCD", cls="geom-circle", width=1.8)

    # Four sides
    b.seg(pt_a, pt_b, "AB", width=1.8)
    b.seg(pt_b, pt_c, "BC", width=1.8)
    b.seg(pt_c, pt_d, "CD", width=1.8)
    b.seg(pt_d, pt_a, "DA", width=1.8)

    # Diagonals AC (split at E) and BD, plus Ptolemy's auxiliary line BE
    b.seg(pt_a, pt_e, "AE", cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=2.4)
    b.seg(pt_e, pt_c, "EC", cls="geom-bold", stroke="var(--geom-assert, #2563eb)", width=2.4)
    b.seg(pt_b, pt_d, "BD", stroke="var(--geom-assert, #2563eb)", width=1.9)
    b.seg(pt_b, pt_e, "BE", cls="geom-dashed", stroke="var(--geom-accent, #d97706)", dash="6 4", width=1.9)

    # Equal angle arcs <ABE == <DBC at vertex B
    def math_deg(src: tuple[float, float], dst: tuple[float, float]) -> float:
        return math.degrees(math.atan2(src[1] - dst[1], dst[0] - src[0])) % 360.0

    ang_ba = math_deg(pt_b, pt_a)
    ang_be = math_deg(pt_b, pt_e)
    ang_bd = math_deg(pt_b, pt_d)
    ang_bc = math_deg(pt_b, pt_c)
    b.arc(pt_b, 28.0, ang_ba, ang_be, "angABE", cls="geom-ang-arc", stroke="var(--geom-accent, #d97706)", width=1.7, layer="graphics")
    b.arc(pt_b, 34.0, ang_bd, ang_bc, "angDBC", cls="geom-ang-arc", stroke="var(--geom-accent, #d97706)", width=1.7, layer="graphics")

    for p, ref in [(pt_a, "A"), (pt_b, "B"), (pt_c, "C"), (pt_d, "D"), (pt_e, "E")]:
        b.point(p, ref)

    b.label(pt_a, "A", "A", dx=-16, dy=2)
    b.label(pt_b, "B", "B", dx=-14, dy=-12)
    b.label(pt_c, "Γ (C)", "C", dx=22, dy=-12, size=14)
    b.label(pt_d, "Δ (D)", "D", dx=22, dy=12, size=14)
    b.label(pt_e, "E", "E", dx=-4, dy=17)
    return b.render()


def build_fig04_chord_difference_and_sum() -> str:
    """Almagest I.10b (Heiberg I, pp. 38 & 41): Semicircle Chord Difference & Sum."""
    b = EuclidSVGBuilder(680, 340, "Almagest I.10b Chord of Difference and Chord of Sum")

    # Left panel: Chord Difference (Heiberg p. 38: semicircle ABGD on diameter AD)
    cx1, cy1, r = 175.0, 235.0, 130.0
    a1 = (cx1 - r, cy1)
    d1 = (cx1 + r, cy1)
    b1 = (cx1 + r * math.cos(math.radians(142.0)), cy1 - r * math.sin(math.radians(142.0)))
    g1 = (cx1 + r * math.cos(math.radians(96.0)), cy1 - r * math.sin(math.radians(96.0)))

    b.polygon([a1, b1, g1, d1], "quadDiff", fill="var(--geom-accent, #d97706)", fill_opacity=0.09)
    b.arc((cx1, cy1), r, 0.0, 180.0, "semiDiff", cls="geom-circle", width=1.8)
    b.seg(a1, d1, "AD", width=1.8)
    b.seg(a1, b1, "AB", stroke="var(--geom-assert, #2563eb)", width=1.8)
    b.seg(a1, g1, "AG", stroke="var(--geom-assert, #2563eb)", width=1.8)
    b.seg(b1, d1, "BD", cls="geom-dashed", dash="5 4")
    b.seg(g1, d1, "GD", cls="geom-dashed", dash="5 4")
    b.seg(b1, g1, "BG", cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=2.7)

    for p, ref, lbl, dx, dy in [
        (a1, "A", "A", -14, 4),
        (b1, "B", "B", -13, -11),
        (g1, "G", "Γ", 2, -15),
        (d1, "D", "Δ", 14, 4),
    ]:
        b.point(p, ref)
        b.label(p, lbl, ref, dx=dx, dy=dy)
    b.caption(cx1, 285, "I. Chord of Difference: BΓ = crd(α − β)")

    # Right panel: Chord Sum (Heiberg p. 41: circle on diameter AD, B above, G below, or B,G flanking diameter BD)
    cx2, cy2 = 505.0, 175.0
    r2 = 115.0
    # Diameter B E D horizontal, A above, G below so arc AB + arc BG = arc AG!
    pb2 = (cx2 - r2, cy2)
    pd2 = (cx2 + r2, cy2)
    pa2 = (cx2 + r2 * math.cos(math.radians(132.0)), cy2 - r2 * math.sin(math.radians(132.0)))
    pg2 = (cx2 + r2 * math.cos(math.radians(235.0)), cy2 - r2 * math.sin(math.radians(235.0)))

    b.polygon([pa2, pb2, pg2, pd2], "quadSum", fill="var(--geom-assert, #2563eb)", fill_opacity=0.09)
    b.circle((cx2, cy2), r2, "circSum", cls="geom-circle", width=1.8)
    b.seg(pb2, pd2, "BD_sum", width=1.8)
    b.seg(pb2, pa2, "AB_sum", stroke="var(--geom-assert, #2563eb)", width=1.8)
    b.seg(pb2, pg2, "BG_sum", stroke="var(--geom-assert, #2563eb)", width=1.8)
    b.seg(pa2, pd2, "AD_sum", cls="geom-dashed", dash="5 4")
    b.seg(pg2, pd2, "GD_sum", cls="geom-dashed", dash="5 4")
    b.seg(pa2, pg2, "AG_sum", cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=2.7)

    for p, ref, lbl, dx, dy in [
        (pa2, "A_sum", "A", -10, -14),
        (pb2, "B_sum", "B", -15, 0),
        (pg2, "G_sum", "Γ", -12, 14),
        (pd2, "D_sum", "Δ", 15, 0),
        ((cx2, cy2), "E_sum", "E", 4, -13),
    ]:
        b.point(p, ref)
        b.label(p, lbl, ref, dx=dx, dy=dy)
    b.caption(cx2, 315, "II. Chord of Sum: AΓ = crd(α + β)")
    return b.render()


def build_fig05_half_arc_chord_lemma() -> str:
    """Almagest I.10b (Heiberg I, p. 39): Half-Arc Chord Lemma GD^2 = (1/2) AG * EG."""
    b = EuclidSVGBuilder(540, 380, "Almagest I.10b Half-Arc Chord Lemma")
    cx, cy, r = 270.0, 235.0, 155.0

    pt_a = (cx - r, cy)
    pt_g = (cx + r, cy)
    # Arc BG = 84 deg from G -> B at 84 deg from G (0 deg), D bisects BG at 42 deg!
    ang_b = math.radians(84.0)
    ang_d = math.radians(42.0)
    pt_b = (cx + r * math.cos(ang_b), cy - r * math.sin(ang_b))
    pt_d = (cx + r * math.cos(ang_d), cy - r * math.sin(ang_d))

    ab_len = math.hypot(pt_b[0] - pt_a[0], pt_b[1] - pt_a[1])
    pt_e = (pt_a[0] + ab_len, cy)  # AE = AB along diameter AG
    pt_z = (pt_d[0], cy)  # Perpendicular DZ onto AG -> EZ = ZG!

    b.polygon([pt_a, pt_b, pt_d], "triABD", fill="var(--geom-assert, #2563eb)", fill_opacity=0.09)
    b.polygon([pt_a, pt_e, pt_d], "triAED", fill="var(--geom-accent, #d97706)", fill_opacity=0.11)

    b.arc((cx, cy), r, 0.0, 180.0, "semiABG", cls="geom-circle", width=1.9)
    b.seg(pt_a, pt_g, "AG", width=1.8)
    b.seg(pt_a, pt_b, "AB", ticks=1, width=1.7)
    b.seg(pt_a, pt_e, "AE", ticks=1, stroke="var(--geom-accent, #d97706)", width=2.0)
    b.seg(pt_a, pt_d, "AD", width=1.5)
    b.seg(pt_b, pt_d, "BD", ticks=2, stroke="var(--geom-assert, #2563eb)", width=1.8)
    b.seg(pt_d, pt_e, "DE", ticks=2, cls="geom-dashed", dash="5 4", width=1.6)
    b.seg(pt_d, pt_g, "GD", ticks=2, cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=2.7)
    b.seg(pt_b, pt_g, "BG", cls="geom-dashed", dash="5 4", width=1.4)
    b.seg(pt_d, pt_z, "DZ", stroke="var(--geom-assert, #2563eb)", width=1.8)
    b.right_angle(pt_z, (-1.0, 0.0), (0.0, -1.0), "angDZG", size=11.0)

    for p, ref, lbl, dx, dy in [
        (pt_a, "A", "A", -15, 2),
        (pt_b, "B", "B", 0, -15),
        (pt_g, "G", "Γ", 15, 2),
        (pt_d, "D", "Δ", 14, -10),
        (pt_e, "E", "E", -4, 18),
        (pt_z, "Z", "Z", 4, 18),
    ]:
        b.point(p, ref)
        b.label(p, lbl, ref, dx=dx, dy=dy)

    b.caption(270, 315, "AE = AB, ΔZ ⊥ AΓ  ⇒  EZ = ZΓ = ½ EΓ  ⇒  ΓΔ² = AΓ · ΓZ = ½ AΓ · EΓ")
    return b.render()


def build_fig06_ptolemy_inequality_lemma() -> str:
    """Almagest I.10b (Heiberg I, p. 43): Ptolemy's Inequality Lemma crd(a)/crd(b) < a/b."""
    b = EuclidSVGBuilder(540, 440, "Almagest I.10b Ptolemy Inequality Lemma")
    cx, cy, r = 265.0, 215.0, 150.0

    # Place chords AB (smaller) and BG (larger) along top-left/top, angle bisector BD vertical-down!
    # Wait: make BD vertical so A, E, G, Z are horizontal just like Heiberg p. 43!
    # Choose B at top (90 deg), D at bottom (270 deg) so BD is vertical angle bisector of <ABG!
    # Wait: if BD bisects <ABG, then arc AD == arc DG, so A and G are at symmetric angles?
    # NO! If AB < BG, then <ADB < <BDG, so BD bisects <ABG ONLY IF B is NOT opposite D!
    # Let's compute exact circle points:
    # Put A at 172 deg, B at 118 deg (arc AB = 54 deg), G at 34 deg (arc BG = 84 deg > 54 deg)!
    # Bisector of <ABG meets circle at D = midpoint of arc AG (from 172 deg to 394 deg? No: opposite B is arc A-D-G:
    # From G=34 deg going clockwise through 0 to A=172? Wait: 172 -> 118 -> 34 goes clockwise:
    # Remaining arc from 34 deg down through 270 deg to 172 deg has midpoint (172 + 394)/2 = 283 deg!
    ang_a, ang_b, ang_g = 172.0, 118.0, 34.0
    ang_d = 283.0  # Exact midpoint of lower arc G(394) - A(172): arc AD = 111 deg, arc DG = 111 deg -> DA == DG!

    def c_pt(deg: float) -> tuple[float, float]:
        rad = math.radians(deg)
        return (cx + r * math.cos(rad), cy - r * math.sin(rad))

    pt_a, pt_b, pt_g, pt_d = c_pt(ang_a), c_pt(ang_b), c_pt(ang_g), c_pt(ang_d)

    # Line intersection helper
    def line_inter(
        p1: tuple[float, float],
        p2: tuple[float, float],
        p3: tuple[float, float],
        p4: tuple[float, float],
    ) -> tuple[float, float]:
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
        return (px, py)

    # E = AC intersect BD
    pt_e = line_inter(pt_a, pt_g, pt_b, pt_d)
    # Z = foot of perpendicular from D onto AG
    ag_dx, ag_dy = pt_g[0] - pt_a[0], pt_g[1] - pt_a[1]
    ag_len2 = ag_dx**2 + ag_dy**2
    t_z = ((pt_d[0] - pt_a[0]) * ag_dx + (pt_d[1] - pt_a[1]) * ag_dy) / ag_len2
    pt_z = (pt_a[0] + t_z * ag_dx, pt_a[1] + t_z * ag_dy)

    # Auxiliary arc centered at D with radius DE cutting DA (extended) at H and DZ at Theta!
    r_de = math.hypot(pt_e[0] - pt_d[0], pt_e[1] - pt_d[1])
    da_ux = (pt_a[0] - pt_d[0]) / math.hypot(pt_a[0] - pt_d[0], pt_a[1] - pt_d[1])
    da_uy = (pt_a[1] - pt_d[1]) / math.hypot(pt_a[0] - pt_d[0], pt_a[1] - pt_d[1])
    dz_ux = (pt_z[0] - pt_d[0]) / math.hypot(pt_z[0] - pt_d[0], pt_z[1] - pt_d[1])
    dz_uy = (pt_z[1] - pt_d[1]) / math.hypot(pt_z[0] - pt_d[0], pt_z[1] - pt_d[1])
    pt_h = (pt_d[0] + r_de * da_ux, pt_d[1] + r_de * da_uy)
    pt_theta = (pt_d[0] + r_de * dz_ux, pt_d[1] + r_de * dz_uy)

    b.polygon([pt_d, pt_a, pt_e], "triDAE", fill="var(--geom-assert, #2563eb)", fill_opacity=0.08)
    b.polygon([pt_d, pt_e, pt_z], "triDEZ", fill="var(--geom-accent, #d97706)", fill_opacity=0.14)

    b.circle((cx, cy), r, "cABGD", cls="geom-circle", width=1.8)
    b.seg(pt_a, pt_b, "AB", width=1.8)
    b.seg(pt_b, pt_g, "BG", width=1.8)
    b.seg(pt_a, pt_g, "AG", width=1.7)
    b.seg(pt_b, pt_d, "BD", stroke="var(--geom-assert, #2563eb)", width=1.7)
    b.seg(pt_d, pt_h, "DH", cls="geom-dashed", dash="5 4", width=1.5)
    b.seg(pt_d, pt_g, "DG", width=1.5)
    b.seg(pt_d, pt_z, "DZ", stroke="var(--geom-accent, #d97706)", width=1.8)

    # Right angle at Z
    u_ag = (-ag_dx / math.sqrt(ag_len2), -ag_dy / math.sqrt(ag_len2))
    u_zd = (-dz_ux, -dz_uy)
    b.right_angle(pt_z, u_ag, u_zd, "angDZA", size=10.5)

    # Sector arc H - E - Theta centered at D
    deg_dh = math.degrees(math.atan2(pt_d[1] - pt_h[1], pt_h[0] - pt_d[0])) % 360.0
    deg_dt = math.degrees(math.atan2(pt_d[1] - pt_theta[1], pt_theta[0] - pt_d[0])) % 360.0
    b.arc(pt_d, r_de, deg_dt, deg_dh, "arcHETheta", cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=2.2)

    for p, ref, lbl, dx, dy in [
        (pt_a, "A", "A", -15, -4),
        (pt_b, "B", "B", -8, -15),
        (pt_g, "G", "Γ", 15, -8),
        (pt_d, "D", "Δ", 6, 16),
        (pt_e, "E", "E", -10, -14),
        (pt_z, "Z", "Z", 10, -13),
        (pt_h, "H", "H", -15, -8),
        (pt_theta, "Theta", "Θ", 14, 4),
    ]:
        b.point(p, ref)
        b.label(p, lbl, ref, dx=dx, dy=dy)

    b.caption(270, 418, "ΔA = ΔΓ > ΔE > ΔZ  ⇒  EZ / EA < ∠EΔZ / ∠EΔA  ⇒  BΓ / BA < arc BΓ / arc BA")
    return b.render()


def build_fig07_menelaus_planar_and_spherical() -> str:
    """Almagest I.13 (Heiberg I, pp. 69 & 75): Planar & Spherical Menelaus Theorem."""
    b = EuclidSVGBuilder(720, 400, "Almagest I.13 Planar and Spherical Menelaus Theorem")

    # Left panel: Planar Menelaus sector with EH || GD (Heiberg I, p. 69)
    def p_svg(mx: float, my: float) -> tuple[float, float]:
        return (42.0 + mx * 38.0, 325.0 - my * 33.0)

    pa = p_svg(2.0, 8.0)
    pb = p_svg(0.0, 0.0)
    pg = p_svg(7.0, 0.0)
    pd = p_svg(0.75, 3.0)
    pe = p_svg(4.0, 4.8)
    pz = p_svg(2.0, 2.4)
    ph = p_svg(1.5, 6.0)

    b.polygon([pa, pb, pe], "triABE_m", fill="var(--geom-assert, #2563eb)", fill_opacity=0.07)
    b.polygon([pa, pd, pg], "triADG_m", fill="var(--geom-accent, #d97706)", fill_opacity=0.08)

    b.seg(pa, pb, "AB", width=1.9)
    b.seg(pa, pg, "AG", width=1.9)
    b.seg(pb, pe, "BE", stroke="var(--geom-assert, #2563eb)", width=1.9)
    b.seg(pg, pd, "GD", stroke="var(--geom-accent, #d97706)", width=1.9)
    b.seg(pe, ph, "EH", cls="geom-bold", stroke="var(--geom-accent, #d97706)", dash="6 4", width=2.3)

    for p, ref, lbl, dx, dy in [
        (pa, "A", "A", 0, -15),
        (pb, "B", "B", -14, 8),
        (pg, "G", "Γ", 14, 8),
        (pd, "D", "Δ", -15, -4),
        (pe, "E", "E", 15, -4),
        (pz, "Z", "Z", 0, 18),
        (ph, "H", "H", -15, -4),
    ]:
        b.point(p, ref)
        b.label(p, lbl, ref, dx=dx, dy=dy)
    b.caption(175, 368, "I. Planar Sector Lemma (EH ∥ ΓΔ)")

    # Right panel: Spherical Menelaus projected from sphere center H onto plane AGD -> collinear Theta-K-Lambda
    # Schematic faithful to Heiberg I, p. 75!
    sa = (505.0, 62.0)
    sb = (388.0, 295.0)
    sg = (628.0, 285.0)
    sd = (432.0, 178.0)
    se = (576.0, 168.0)
    sz = (496.0, 218.0)
    sh = (475.0, 325.0)  # Sphere center H

    # Projected collinear line Theta - K - Lambda on intersection of plane(H, B, E) with plane(A, G, D)
    s_theta = (684.0, 232.0)
    s_k = (545.0, 198.0)
    s_lam = (456.0, 176.0)

    # Curved spherical arcs AB, AG, BE, GD
    b.elements.append(
        f'    <path class="geom-arc" d="M {sa[0]:.1f} {sa[1]:.1f} Q 420 165 {sb[0]:.1f} {sb[1]:.1f}" fill="none" stroke-width="1.9" data-ref="arcAB"/>'
    )
    b.elements.append(
        f'    <path class="geom-arc" d="M {sa[0]:.1f} {sa[1]:.1f} Q 585 160 {sg[0]:.1f} {sg[1]:.1f}" fill="none" stroke-width="1.9" data-ref="arcAG"/>'
    )
    b.elements.append(
        f'    <path class="geom-arc" d="M {sb[0]:.1f} {sb[1]:.1f} Q 485 215 {se[0]:.1f} {se[1]:.1f}" fill="none" stroke="var(--geom-assert, #2563eb)" stroke-width="1.9" data-ref="arcBE"/>'
    )
    b.elements.append(
        f'    <path class="geom-arc" d="M {sg[0]:.1f} {sg[1]:.1f} Q 525 220 {sd[0]:.1f} {sd[1]:.1f}" fill="none" stroke="var(--geom-accent, #d97706)" stroke-width="1.9" data-ref="arcGD"/>'
    )

    # Central rays from sphere center H and planar chords
    b.seg(sh, sa, "HA", cls="geom-dashed", dash="4 4")
    b.seg(sh, sd, "HD", cls="geom-dashed", dash="4 4")
    b.seg(sh, sz, "HZ", cls="geom-dashed", dash="4 4")
    b.seg(sa, se, "chordAG_ext", cls="geom-dashed", dash="3 3")
    b.seg(se, s_theta, "HE_ext", cls="geom-dashed", dash="3 3")
    b.seg(sg, s_theta, "HG_ext", cls="geom-dashed", dash="3 3")
    # Collinear plane-intersection line Lambda - K - Theta!
    b.seg(s_lam, s_theta, "lineThetaKLambda", cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=2.4)

    for p, ref, lbl, dx, dy in [
        (sa, "sA", "A", 0, -14),
        (sb, "sB", "B", -14, 6),
        (sg, "sG", "Γ", 12, 12),
        (sd, "sD", "Δ", -15, -4),
        (se, "sE", "E", 14, -6),
        (sz, "sZ", "Z", -10, 14),
        (sh, "sH", "H (center)", 0, 17),
        (s_theta, "Theta", "Θ", 14, 2),
        (s_k, "K", "K", 4, -14),
        (s_lam, "Lambda", "Λ", -2, -14),
    ]:
        b.point(p, ref)
        b.label(p, lbl, ref, dx=dx, dy=dy, size=13)
    b.caption(535, 368, "II. 3D Projection from Center H ⇒ Θ, K, Λ Collinear")
    return b.render()


def build_fig08_solar_declination_quadrant() -> str:
    """Almagest I.14 (Heiberg I, p. 76): Solar Declination Menelaus Quadrant."""
    b = EuclidSVGBuilder(520, 420, "Almagest I.14 Solar Declination Spherical Menelaus Figure")
    cx, cy, r = 260.0, 210.0, 155.0

    # Solstitial colure outer circle ABGD: Z = North Pole at top, A-E-G = Equator, B-E-D = Ecliptic
    pt_z = (cx, cy - r)
    pt_n = (cx, cy + r)
    pt_a = (cx - r, cy)
    pt_g = (cx + r, cy)
    pt_e = (cx, cy + 16.0)  # Exact t=0.5 intersection of Equator and Ecliptic Bézier arcs

    eps_rad = math.radians(23.86)
    pt_b = (cx - r * math.cos(eps_rad), cy - r * math.sin(eps_rad))
    pt_d = (cx + r * math.cos(eps_rad), cy + r * math.sin(eps_rad))

    b.circle((cx, cy), r, "cABGD", cls="geom-circle", width=1.9)
    # Equator AEG horizontal curve
    b.elements.append(
        f'    <path class="geom-line" d="M {pt_a[0]:.1f} {pt_a[1]:.1f} Q {cx:.1f} {cy + 32:.1f} {pt_g[0]:.1f} {pt_g[1]:.1f}" '
        f'fill="none" stroke="var(--geom-assert, #2563eb)" stroke-width="1.9" data-ref="arcAEG"/>'
    )
    # Ecliptic BED tilted curve
    b.elements.append(
        f'    <path class="geom-bold" d="M {pt_b[0]:.1f} {pt_b[1]:.1f} Q {cx:.1f} {cy + 32:.1f} {pt_d[0]:.1f} {pt_d[1]:.1f}" '
        f'fill="none" stroke="var(--geom-accent, #d97706)" stroke-width="2.3" data-ref="arcBED"/>'
    )

    # Meridian arc Z - H - Theta from pole Z through Sun H (on ecliptic EB) to Equator at Theta!
    pt_h = (cx - 66.0, cy - 9.0)
    pt_theta = (cx - 72.0, cy + 12.0)
    b.elements.append(
        f'    <path class="geom-line" d="M {pt_z[0]:.1f} {pt_z[1]:.1f} Q {cx - 78:.1f} {cy - 30:.1f} {pt_theta[0]:.1f} {pt_theta[1]:.1f}" '
        f'fill="none" stroke-width="1.8" data-ref="arcZHTheta"/>'
    )
    # Highlight declination arc H-Theta
    b.seg(pt_h, pt_theta, "arcHTheta", cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=3.0)
    b.seg(pt_z, pt_n, "axisZN", cls="geom-dashed", dash="4 4")

    for p, ref, lbl, dx, dy in [
        (pt_a, "A", "A (Equator)", -42, 4),
        (pt_b, "B", "B (Solstice)", -42, -10),
        (pt_g, "G", "Γ", 16, 4),
        (pt_d, "D", "Δ", 16, 10),
        (pt_e, "E", "E (Equinox)", 34, 15),
        (pt_z, "Z", "Z (Pole)", 0, -15),
        (pt_h, "H", "H (Sun, λ)", -36, -12),
        (pt_theta, "Theta", "Θ", -14, 15),
    ]:
        b.point(p, ref)
        b.label(p, lbl, ref, dx=dx, dy=dy, size=13)

    b.caption(260, 396, "crd(2 HΘ) / crd(180°) = [crd(2 AB) / crd(2 ZB)] · [crd(2 EH) / crd(2 EB)]  ⇒  sin δ = sin ε · sin λ")
    return b.render()


def build_fig09_planisphaerium_astrolabe() -> str:
    """Planisphaerium §§1-4 (Heiberg II, pp. 227-234): Stereographic Cone & Astrolabe Plate."""
    b = EuclidSVGBuilder(740, 420, "Planisphaerium Stereographic Projection and Astrolabe Plate")

    # Left panel: Meridian cross-section of celestial sphere showing South-Pole projection & inversion
    cx1, cy1, r1 = 180.0, 210.0, 110.0
    ps = (cx1, cy1 + r1)  # South Pole S = (0, -R)
    pn = (cx1, cy1 - r1)  # North Pole N -> projects to E=(0,0)
    peq_l = (cx1 - r1, cy1)
    peq_r = (cx1 + r1, cy1)

    # Declination +-eps (~23.86 deg)
    eps = math.radians(23.86)
    p_can = (cx1 - r1 * math.cos(eps), cy1 - r1 * math.sin(eps))
    p_cap = (cx1 + r1 * math.cos(eps), cy1 + r1 * math.sin(eps))

    # Projected points on equatorial plane y = cy1 from South Pole ps = (cx1, cy1 + r1):
    def proj_x(pt: tuple[float, float]) -> tuple[float, float]:
        t = (cy1 - ps[1]) / (pt[1] - ps[1])
        return (ps[0] + t * (pt[0] - ps[0]), cy1)

    proj_can = proj_x(p_can)
    proj_cap = proj_x(p_cap)

    b.circle((cx1, cy1), r1, "sphereCross", cls="geom-circle", width=1.8)
    b.seg((28.0, cy1), (355.0, cy1), "planeEq", stroke="var(--geom-assert, #2563eb)", width=1.9)
    b.seg(pn, ps, "axisNS", cls="geom-dashed", dash="4 4")
    b.seg(p_can, p_cap, "eclConeDiam", stroke="var(--geom-accent, #d97706)", width=2.0)

    # Stereographic rays from South Pole S
    b.seg(ps, proj_can, "rayCan", cls="geom-dashed", stroke="var(--geom-assert, #2563eb)", dash="5 4", width=1.5)
    b.seg(ps, proj_cap, "rayCap", cls="geom-dashed", stroke="var(--geom-accent, #d97706)", dash="5 4", width=1.5)

    for p, ref, lbl, dx, dy in [
        (ps, "S", "South Pole", 0, 16),
        (pn, "N_pole", "North Pole", 0, -15),
        ((cx1, cy1), "E_cross", "e", -10, 14),
        (peq_l, "B_cross", "b", -12, -12),
        (peq_r, "D_cross", "d", 10, -12),
        (proj_can, "T_cross", "t (r_Can)", 0, 16),
        (proj_cap, "M_cross", "m (r_Cap)", 6, -15),
    ]:
        b.point(p, ref)
        b.label(p, lbl, ref, dx=dx, dy=dy, size=12)
    b.caption(190, 388, "I. Stereographic Section from South Pole (et · em = ed²)")

    # Right panel: Exact Planisphaerium Astrolabe Plate (R_eq = 60, r_Can = 40, r_Cap = 90, Ecliptic R = 65 at (0, 25))
    cx2, cy2, sc = 545.0, 215.0, 1.55  # 90 * 1.55 = 139.5 px

    def a_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx2 + mx * sc, cy2 - my * sc)

    pe = a_svg(0, 0)
    pa = a_svg(0, 60)
    pg = a_svg(0, -60)
    pb = a_svg(-60, 0)
    pd = a_svg(60, 0)
    pl = a_svg(0, 40)
    pt = a_svg(0, -40)
    pm = a_svg(0, 90)
    pk = a_svg(0, -90)
    pr = a_svg(0, 25)

    # Triangle MDT showing right angle <MDT = 90 deg (Planisphaerium §1, p. 228)
    b.polygon([pm, pd, pt], "triMDT", fill="var(--geom-accent, #d97706)", fill_opacity=0.09)

    # Tropic of Capricorn (r = 90), Equator (r = 60), Tropic of Cancer (r = 40)
    b.circle(pe, 90.0 * sc, "cKM", cls="geom-dashed", dash="5 4", width=1.5)
    b.circle(pe, 60.0 * sc, "cABGD", stroke="var(--geom-assert, #2563eb)", width=1.9)
    b.circle(pe, 40.0 * sc, "cTL", cls="geom-dashed", stroke="var(--geom-assert, #2563eb)", dash="4 3", width=1.5)

    # Oblique Ecliptic Circle MBTD centered at R=(0, 25) of radius 65 passing through B and D!
    b.circle(pr, 65.0 * sc, "cMBTD", cls="geom-bold", stroke="var(--geom-accent, #d97706)", width=2.5)

    # Meridian KM and Colure BD + chords MD, TD perpendicular at D
    b.seg(pm, pk, "MK", width=1.4)
    b.seg(pb, pd, "BD_ast", width=1.4)
    b.seg(pm, pd, "MD", cls="geom-dashed", stroke="var(--geom-accent, #d97706)", dash="4 3", width=1.5)
    b.seg(pt, pd, "TD", cls="geom-dashed", stroke="var(--geom-accent, #d97706)", dash="4 3", width=1.5)

    # Right-angle marker at D between DM and DT
    u_dm = ((pm[0] - pd[0]) / math.hypot(pm[0] - pd[0], pm[1] - pd[1]), (pm[1] - pd[1]) / math.hypot(pm[0] - pd[0], pm[1] - pd[1]))
    u_dt = ((pt[0] - pd[0]) / math.hypot(pt[0] - pd[0], pt[1] - pd[1]), (pt[1] - pd[1]) / math.hypot(pt[0] - pd[0], pt[1] - pd[1]))
    b.right_angle(pd, u_dm, u_dt, "angMDT", size=10.0)

    for p, ref, lbl, dx, dy in [
        (pe, "E", "e", -10, 12),
        (pa, "A", "a", -11, -9),
        (pg, "G", "g", -11, 11),
        (pb, "B", "b", -14, -9),
        (pd, "D", "d", 14, -9),
        (pl, "L", "l", 11, -7),
        (pt, "T", "t", 11, 9),
        (pm, "M", "m", 13, -8),
        (pk, "K", "k", 13, 8),
        (pr, "R", "r", 11, 0),
    ]:
        b.point(p, ref)
        b.label(p, lbl, ref, dx=dx, dy=dy, size=13)
    b.caption(545, 388, "II. Astrolabe Plate: Equator abgd, Tropics tl & km, Ecliptic mbtd")
    return b.render()


def main() -> None:
    """Build all 9 `.euclid-graphic` SVG plates into `docsrc/_static/figures/`."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plates = {
        "fig01_celestial_sphere_preliminaries.svg": build_fig01_celestial_sphere,
        "fig02_pentagon_decagon_construction.svg": build_fig02_pentagon_decagon,
        "fig03_ptolemy_cyclic_quadrilateral.svg": build_fig03_ptolemy_cyclic_quadrilateral,
        "fig04_chord_difference_and_sum.svg": build_fig04_chord_difference_and_sum,
        "fig05_half_arc_chord_lemma.svg": build_fig05_half_arc_chord_lemma,
        "fig06_ptolemy_inequality_lemma.svg": build_fig06_ptolemy_inequality_lemma,
        "fig07_menelaus_planar_and_spherical.svg": build_fig07_menelaus_planar_and_spherical,
        "fig08_solar_declination_quadrant.svg": build_fig08_solar_declination_quadrant,
        "fig09_planisphaerium_stereographic_astrolabe.svg": build_fig09_planisphaerium_astrolabe,
    }
    for filename, builder in plates.items():
        svg_text = builder()
        out_path = OUT_DIR / filename
        out_path.write_text(svg_text, encoding="utf-8")
        print(f"Wrote {out_path.relative_to(OUT_DIR.parents[2])} ({len(svg_text)} bytes)")


if __name__ == "__main__":
    main()

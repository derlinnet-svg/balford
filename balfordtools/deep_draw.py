"""First-pass deep drawing design checks.

Formulas (engineering estimates, not simulation):
  - Blank diameter (cylindrical cup, no flange, thin wall):
        D = sqrt(d^2 + 4 * d * h)
  - Draw ratio:            beta = D / d
  - Single-hit limit:      beta <= ~1.9 for mild steel (material dependent)
  - Draw force (approx.):  F = pi * d * t * UTS * (beta - 0.7)
"""

from dataclasses import dataclass
import math


MAX_SINGLE_HIT_RATIO = 1.9


@dataclass
class DeepDrawResult:
    blank_diameter_mm: float
    draw_ratio: float
    verdict: str
    note: str
    draw_force_estimate_kn: float


def blank_diameter_mm(inside_or_outside_diameter_mm: float, height_mm: float) -> float:
    """Approx. blank diameter for a plain cylindrical cup."""
    d = inside_or_outside_diameter_mm
    return math.sqrt(d * d + 4.0 * d * height_mm)


def deep_draw_check(
    diameter_mm: float,
    height_mm: float,
    thickness_mm: float,
    uts_mpa: float = 400.0,
    max_ratio: float = MAX_SINGLE_HIT_RATIO,
) -> DeepDrawResult:
    d = diameter_mm
    blank = blank_diameter_mm(d, height_mm)
    ratio = blank / d if d > 0 else float("inf")
    force_n = math.pi * d * thickness_mm * uts_mpa * max(ratio - 0.7, 0.1)
    if ratio <= max_ratio:
        verdict = "single-hit"
        note = "Feasible in one draw for typical mild steel; confirm with DFM review."
    else:
        verdict = "multi-stage"
        note = "Requires multi-stage deep drawing tooling (redraws and possible annealing)."
    return DeepDrawResult(
        blank_diameter_mm=round(blank, 1),
        draw_ratio=round(ratio, 2),
        verdict=verdict,
        note=note,
        draw_force_estimate_kn=round(force_n / 1000.0, 1),
    )

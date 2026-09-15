"""Bend allowance with K-factor.

  BA = angle_rad * (R + K * t)

Typical K values: 0.33 for R > 2t, ~0.5 for sharp bends. Material and
tooling condition change K, so treat results as first-pass estimates.
"""

from __future__ import annotations

import math


def bend_allowance_mm(radius_mm: float, thickness_mm: float, angle_deg: float, k: float | None = None) -> float:
    if k is None:
        k = 0.33 if radius_mm > 2.0 * thickness_mm else 0.5
    angle_rad = math.radians(angle_deg)
    return angle_rad * (radius_mm + k * thickness_mm)

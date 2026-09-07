"""Blanking and cutting force estimates.

  - Cutting force:  F = L * t * tau,  tau ~= 0.7 * UTS
  - Stripping force: ~10-15% of cutting force for typical steels
"""

from dataclasses import dataclass


@dataclass
class ForceResult:
    cutting_force_kn: float
    stripping_force_estimate_kn: float


def blanking_force(
    perimeter_mm: float,
    thickness_mm: float,
    uts_mpa: float,
    shear_factor: float = 0.7,
    stripping_ratio: float = 0.12,
) -> ForceResult:
    shear_strength = uts_mpa * shear_factor
    cutting_n = perimeter_mm * thickness_mm * shear_strength
    stripping_n = cutting_n * stripping_ratio
    return ForceResult(
        cutting_force_kn=round(cutting_n / 1000.0, 1),
        stripping_force_estimate_kn=round(stripping_n / 1000.0, 1),
    )

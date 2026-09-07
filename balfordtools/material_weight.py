"""Blank/part weight from developed area, thickness and material density."""

DENSITY_G_PER_CM3 = {
    "steel": 7.85,
    "carbon-steel": 7.85,
    "stainless": 7.93,
    "stainless-steel": 7.93,
    "aluminum": 2.70,
    "aluminium": 2.70,
    "copper": 8.94,
    "brass": 8.50,
}


def part_weight_grams(area_mm2: float, thickness_mm: float, material: str = "steel") -> float:
    density = DENSITY_G_PER_CM3.get(material.lower(), 7.85)
    volume_mm3 = area_mm2 * thickness_mm
    return round(volume_mm3 / 1000.0 * density, 2)

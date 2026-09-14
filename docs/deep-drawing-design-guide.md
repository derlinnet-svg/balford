# Deep drawing design guide

Reference values for feasibility checks and quotation sanity checks on deep drawn
cylindrical parts — cups, housings, sleeves, cans and covers. The numbers come
from the deep drawing guide maintained by [Balford](https://balford.net/deep-drawing/),
a metal forming plant that runs these parts in production.

> These are planning values, not simulation results. The limiting draw ratio of a
> specific material lot has to be confirmed in tooling tryout.

## 1. The four numbers that decide everything

Before a deep drawing job can be quoted, four values are established. Together
they decide whether the part needs one die or five, and whether it needs an
anneal.

| # | Value | Formula / rule | What it decides |
|---|---|---|---|
| 1 | Blank diameter | `D ≈ √(d² + 4·d·h)` | Material cost, trim allowance |
| 2 | Draw ratio | `β = D / d` (blank ÷ punch diameter) | Single hit vs. multi-stage |
| 3 | Draw force | `F ≈ π · d · t · σ_uts · factor` | Press tonnage (plus blank holder force) |
| 4 | Die clearance | see table below | Wall thickness, ironing effect, wrinkling risk |

`d` = cup diameter (mm), `h` = wall height (mm), `t` = sheet thickness (mm),
`σ_uts` = ultimate tensile strength (MPa).

The blank formula is a constant-area starting estimate for a flat-bottomed cup
without a flange. Real blanks need a trim allowance, because a drawn edge is
never perfectly even.

## 2. Limiting draw ratio (LDR) by material

The LDR is the largest blank-to-punch ratio a material survives in one draw
without tearing. Plan the first draw at or below the low end of the range, then
redraw.

| Material | Typical designation | First draw ratio | Typical redraw ratio |
|---|---|---|---|
| Low carbon steel | DC01, DC04, SPHE | **1.8 – 2.0** | 1.2 – 1.4 |
| Pure iron | DT4, DT4C | **1.8 – 2.0** | 1.2 – 1.4 |
| Brass / copper | CuZn37, Cu-ETP | **1.8 – 2.2** | 1.2 – 1.4 |
| Stainless steel | 1.4301 (304), 1.4404 (316L) | **1.6 – 1.8** | 1.15 – 1.3 |
| Aluminium | EN AW-1050, 3003, 5754 | **~1.4 – 1.6** (alloy dependent) | 1.15 – 1.3 |

Notes that matter in practice:

- Deep drawing grades with a high r-value behave best; DC04 outperforms DC01 on
  the same geometry.
- Stainless work hardens fast, so it usually needs an earlier anneal and an extra
  redraw for the same total reduction.
- Aluminium varies widely by alloy. Soft grades draw well, high-strength alloys
  do not.
- Machine-readable copy: [`data/limit-draw-ratios.csv`](../data/limit-draw-ratios.csv).

## 3. Estimating the number of draws

```
total ratio        β_total = D / d
first draw         β₁ ≤ LDR (table above)
each redraw        β_n ≈ 1.2 – 1.4

approximate stage count:
    n ≈ 1 + ln(β_total / β₁) / ln(1.3)
```

Round up. A part with `β_total = 3.0` and `β₁ = 1.9` lands at `n ≈ 3`, which is
the classic housing progression: draw → redraw → redraw, with an anneal between
the later stages if the material work hardens (stainless, high-strength
aluminium).

## 4. Die clearance per side

| Material | Clearance per side |
|---|---|
| Steel | 1.1 – 1.3 × thickness |
| Aluminium | 1.0 – 1.2 × thickness |
| Stainless steel | 1.2 – 1.4 × thickness |

Clearance controls how much ironing effect the draw has. Tighter clearance
deliberately thins the wall; looser clearance keeps the wall closer to nominal
but raises the wrinkling risk.

Machine-readable copy: [`data/die-clearance.csv`](../data/die-clearance.csv).

## 5. Blank holder force — the balance that decides success

When the punch pulls the flange inward, the flange circumference has to shrink.
In thin sheet the excess material buckles out of plane: that is a wrinkle.

| Blank holder force | Result |
|---|---|
| Too low | Wrinkles in the flange, and the wrinkles travel into the wall |
| Too high | Material cannot flow, the wall stretches instead, and the part tears at the die radius |

Blank holder pressure is adjustable on a real draw tool, because the correct
setting depends on the material lot, thickness tolerance and lubricant. This is
also why deep drawing tooling needs tryout time that press forming does not.

## 6. Ironing: when the wall should get thinner on purpose

Ironing pushes the part through a die whose clearance is *less* than the wall
thickness, so the wall is squeezed thinner as it passes. It solves three problems
at once:

- Outside diameter is set by the die bore
- Inside diameter is set by the punch
- Surface finish is formed against polished tooling instead of cut by an insert

The commercial consequence: a deep drawn and ironed housing can hold **both**
diameters in tolerance without a turning operation. For a part that would
otherwise be machined from bar, that removes most of the machining cost — and a
formed bore can be smoother than a machined one, which matters for armature
guidance in solenoid valves.

## 7. Defects and remedies

| Defect | Appearance | Usual cause | Usual remedy |
|---|---|---|---|
| Wrinkling | Folds in the wall or flange | Blank holder force too low; flange unsupported | Increase blank holder pressure; adjust draw radius; add draw beads |
| Tearing / fracture | Split at the die radius or in the wall | Ratio exceeds the material limit; die radius too tight; clearance too small; friction too high | Add a redraw, open the die radius, correct clearance, improve lubrication |
| Earing | Wavy, scalloped top edge | Planar anisotropy in the sheet | Accept and trim; change material or rolling direction; adjust blank shape |
| Excessive thinning | Wall too thin at the radius | Die radius too tight; excessive tension | Increase die radius; add a redraw; anneal |
| Springback | Diameter or shape relaxes after forming | Elastic recovery, worse in high-strength material | Compensate tool dimensions; restrike; change material |
| Orange peel | Grainy stretched surface | Coarse grain structure; excessive stretch | Finer-grain material; reduce local strain |
| Draw marks / scoring | Longitudinal scratches on the wall | Tool wear, galling, inadequate lubricant | Polish the die radius; re-coat or re-polish tooling; review lubricant |
| Bottom fracture | Split across the base | Punch radius too small; too little material available | Increase punch radius; enlarge the blank |

Almost every remedy above is a **tooling** change rather than a material change.
That is why deep drawing tooling is a design problem first and a production
problem second.

Machine-readable copy: [`data/deep-drawing-defects.csv`](../data/deep-drawing-defects.csv).

## 8. What holds tolerance, and what does not

| Feature | Behaviour |
|---|---|
| Diameters | Repeat well, because they are set by tooling — a drawn diameter holds tolerance more consistently than a formed one |
| Wall thickness | A gradient, not a constant; tolerance must be tied to a measurement position |
| Wall height | The least precise dimension, because the top edge is trimmed |
| Inside finish | Can be excellent: formed against the punch rather than cut, which suits armature guidance and sealing surfaces |
| Outside finish | Will carry draw marks unless a finishing operation is added |

If both the inside and outside diameter of your part are functional, ironing is
usually cheaper than forming the part and then machining one of the diameters.

## 9. DFM checklist

The full checklist lives in [`dfm-checklist.md`](dfm-checklist.md). The five items
that change cost the most:

1. State the limiting draw ratio you designed to, and for which material.
2. Say whether the wall thickness has a tolerance tied to a position.
3. Flag any diameter that must be machined after drawing — ironing may remove it.
4. Give the wall height with the trim allowance, not as a theoretical value.
5. Say whether the part will be annealed between draws (stainless, DT4, hard
   aluminium).

## 10. Reference data files

| File | Contents |
|---|---|
| [`data/limit-draw-ratios.csv`](../data/limit-draw-ratios.csv) | First-draw and redraw ratios by material |
| [`data/die-clearance.csv`](../data/die-clearance.csv) | Clearance per side by material |
| [`data/deep-drawing-defects.csv`](../data/deep-drawing-defects.csv) | Defect → cause → remedy |
| [`data/deep-drawing-materials.csv`](../data/deep-drawing-materials.csv) | Material designations and where they are used |

## 11. Running the checks in code

```bash
pip install -e .

# blank diameter, draw ratio, stage verdict, draw force estimate
balford deep-draw --diameter 22 --height 45 --thickness 1.2

# blanking / cutting force
balford blanking-force --perimeter 220 --thickness 1.5 --uts 400
```

## 12. Related references

- Full deep drawing guide (process, calculations, defects): https://balford.net/deep-drawing/
- Terminology (drawing vs deep drawing, redrawing, ironing, hydroforming): https://balford.net/deep-drawing-terminology/
- Deep draw force calculator: https://balford.net/resources/calculator/deep-draw/
- Metal weight calculator (blank weight): https://balford.net/resources/calculator/material-weight/
- Capability boundaries, stated honestly: https://balford.net/deep-drawn-metal-stamping-our-capability-boundaries/

Language editions of the same guide: [Deutsch](https://balford.net/de/tiefziehen/) ·
[中文](https://balford.net/zh/deep-drawing/) · [日本語](https://balford.net/ja/deep-drawing/) ·
[Français](https://balford.net/fr/deep-drawing/) · [Italiano](https://balford.net/it/deep-drawing/)

# DFM checklist for deep drawn and stamped parts

Send this list with your drawing and the first quotation round usually collapses
into one iteration instead of three. Adapted from the DFM reviews Balford runs on
incoming drawings ([in-house tooling design & build](https://balford.net/capabilities/in-house-tooling-design-build/)).

## A. Part definition

- [ ] All functional dimensions toleranced, not just the easy ones
- [ ] Diameters given as inside / outside, and which one is functional
- [ ] Wall thickness tolerance tied to a measurement position (it is a gradient)
- [ ] Wall height given with the trim allowance
- [ ] Radius at the die side and at the punch side specified separately
- [ ] Datum scheme stated (what the part is measured from)
- [ ] GD&T only where it is inspected, with the inspection method implied

## B. Material

- [ ] Material grade and standard (e.g. DC04, 1.4301, EN AW-5754, DT4C)
- [ ] Sheet thickness and thickness tolerance
- [ ] Grain / rolling direction is allowed to matter, or must not matter
- [ ] Magnetic requirement? (DT4 / DT4C + magnetic annealing is a different route)
- [ ] Surface finish requirement on the drawn surface (draw marks acceptable?)
- [ ] Coating or plating: which surface, and is it specified on the drawing?

## C. Process feasibility

- [ ] Draw ratio stated (blank ÷ punch), and the limiting draw ratio for that material
- [ ] Number of draws assumed, and whether annealing between draws is allowed
- [ ] Ironing allowed? (usually removes a turning operation on housings)
- [ ] Blank holder arrangement considered (wrinkling vs tearing balance)
- [ ] Die clearance chosen per material, not as a default
- [ ] Lubricant restrictions (cleanliness, medical or food-contact requirements)

## D. Quantity and commercial

- [ ] Annual volume and batch size
- [ ] Expected programme life
- [ ] Tooling budget expectation (single station vs. progressive die vs. transfer)
- [ ] Sample / PPAP requirements and timing
- [ ] Packaging requirement, including any "perfect part" cosmetic selection

## E. Post-processing

- [ ] Machining after drawing: which feature, and could ironing replace it?
- [ ] Heat treatment: hardening, tempering, annealing, magnetic annealing
- [ ] Surface treatment: barrel plating vs. rack plating, and the handling cost
  difference between them
- [ ] Welding / assembly / sub-assembly
- [ ] Inspection: CMM, projector, roughness, hardness, salt spray, functional test

## F. Files

- [ ] 2D drawing with dimensions (PDF is fine)
- [ ] 3D model (STEP / IGES / Parasolid) if available
- [ ] CAD source (DXF/DWG) where the 2D drawing is not fully dimensioned
- [ ] Existing part for reference, if this is a transfer or a second source

## What we send back

For a drawing sent to [rfq.balford.net](https://rfq.balford.net/), the DFM answer
normally covers: draw ratio and stage count, blank size and material utilisation,
press tonnage, tooling concept (single station / progressive / transfer),
post-processing operations, and the risk register — the features most likely to
drive scrap or price.

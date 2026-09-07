import argparse

from .bend_allowance import bend_allowance_mm
from .deep_draw import deep_draw_check
from .material_weight import part_weight_grams
from .stamping_force import blanking_force


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="balford",
        description="Balford stamping & deep drawing design calculators",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    dd = sub.add_parser("deep-draw", help="blank diameter, ratio and stage verdict")
    dd.add_argument("--diameter", type=float, required=True, help="part diameter in mm")
    dd.add_argument("--height", type=float, required=True, help="draw height in mm")
    dd.add_argument("--thickness", type=float, default=1.0, help="wall thickness in mm")
    dd.add_argument("--uts", type=float, default=400.0, help="material UTS in MPa")

    bf = sub.add_parser("blanking-force", help="cutting/stripping force estimate")
    bf.add_argument("--perimeter", type=float, required=True, help="cut perimeter in mm")
    bf.add_argument("--thickness", type=float, required=True, help="sheet thickness in mm")
    bf.add_argument("--uts", type=float, default=400.0, help="material UTS in MPa")

    ba = sub.add_parser("bend-allowance", help="bend allowance with K-factor")
    ba.add_argument("--radius", type=float, required=True, help="inside radius in mm")
    ba.add_argument("--thickness", type=float, required=True, help="sheet thickness in mm")
    ba.add_argument("--angle", type=float, required=True, help="bend angle in degrees")
    ba.add_argument("--k", type=float, help="optional K-factor override")

    w = sub.add_parser("weight", help="blank/part weight")
    w.add_argument("--area", type=float, required=True, help="developed area in mm²")
    w.add_argument("--thickness", type=float, required=True, help="thickness in mm")
    w.add_argument("--material", default="steel", help="steel/stainless/aluminum/copper/brass")

    args = parser.parse_args()

    if args.command == "deep-draw":
        r = deep_draw_check(args.diameter, args.height, args.thickness, args.uts)
        print("Blank diameter (approx.) : %s mm" % r.blank_diameter_mm)
        print("Draw ratio                : %s" % r.draw_ratio)
        print("Verdict                   : %s" % r.verdict)
        print("Draw force (estimate)     : %s kN" % r.draw_force_estimate_kn)
        print("Hint                      : %s" % r.note)
    elif args.command == "blanking-force":
        r = blanking_force(args.perimeter, args.thickness, args.uts)
        print("Cutting force             : %s kN" % r.cutting_force_kn)
        print("Stripping force (approx.) : %s kN" % r.stripping_force_estimate_kn)
    elif args.command == "bend-allowance":
        ba = bend_allowance_mm(args.radius, args.thickness, args.angle, args.k)
        print("Bend allowance            : %s mm" % round(ba, 2))
    elif args.command == "weight":
        g = part_weight_grams(args.area, args.thickness, args.material)
        print("Part weight (approx.)     : %s g" % g)


if __name__ == "__main__":
    main()

import argparse
import numpy as np
from pdb_id_imports import get_structure


parser = argparse.ArgumentParser(
    description="Calculate distances between all atoms of two residues."
)

parser.add_argument(
    "pdb",
    help="PDB file or PDB ID"
)

parser.add_argument(
    "chain1",
    help="Chain ID of first residue"
)

parser.add_argument(
    "residue1",
    type=int,
    help="Residue number of first residue"
)

parser.add_argument(
    "chain2",
    help="Chain ID of second residue"
)

parser.add_argument(
    "residue2",
    type=int,
    help="Residue number of second residue"
)

args = parser.parse_args()

st = get_structure(args.pdb)


# Selection of first residue
res1 = st[0][args.chain1][args.residue1]

# Selection of second residue
res2 = st[0][args.chain2][args.residue2]


print(
    f"Residue {args.residue1} is",
    res1.get_resname()
)

print(
    f"Residue {args.residue2} is",
    res2.get_resname()
)


print("\nAtom1 Atom2 dist1 dist2")
print("-------------------------")


# Compare every atom of residue 1
# with every atom of residue 2

for at1 in res1.get_atoms():

    for at2 in res2.get_atoms():

        # Distance using Bio.PDB
        dist = at2 - at1

        # Distance using coordinates
        vector = at2.coord - at1.coord

        distance = np.sqrt(
            np.sum(vector ** 2)
        )

        print(
            f"{at1.id:<6} "
            f"{at2.id:<6} "
            f"{dist:8.3f} "
            f"{distance:8.3f}"
        )


# Distance of residue 1 atoms
# from [10, 10, 10]

center = np.array([10, 10, 10])

print(
    f"\nDistance of residue "
    f"{args.residue1} to {center}\n"
)

for at1 in res1.get_atoms():

    vector = at1.coord - center

    distance = np.sqrt(
        np.sum(vector ** 2)
    )

    print(
        f"{at1.id:<6} "
        f"{distance:8.3f}"
    )
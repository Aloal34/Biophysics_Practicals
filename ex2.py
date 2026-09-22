import argparse
from pdb_id_imports import get_structure


parser = argparse.ArgumentParser(
    description="List all atoms of a given residue."
)

parser.add_argument(
    "pdb",
    help="PDB file or PDB ID"
)

parser.add_argument(
    "chain",
    help="Chain ID"
)

parser.add_argument(
    "residue",
    type=int,
    help="Residue number"
)

args = parser.parse_args()

st = get_structure(args.pdb)

res = st[0][args.chain][args.residue]

atoms = list(res.get_atoms())

# Sort by atom name
atoms.sort(key=lambda atom: atom.id)

print (f"Residue: {res.get_resname()}, {res.id[1]}")
print("Atoms:")
for atom in res.get_atoms():
    print(f"{res.get_resname()} {res.id} {atom.get_name()} {atom.get_coord()}")
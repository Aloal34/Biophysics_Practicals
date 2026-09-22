import argparse
from Bio.PDB import NeighborSearch
from pdb_id_imports import get_structure


parser = argparse.ArgumentParser(
    description="Find possible hydrogen bonds "
                "between polar atoms."
)

parser.add_argument(
    "pdb",
    help="PDB file or PDB ID"
)

parser.add_argument(
    "-d",
    "--distance",
    type=float,
    default=3.5,
    help="Maximum polar-atom distance "
         "(default: 3.5 Å)"
)

args = parser.parse_args()

st = get_structure(args.pdb)
selecti = []

polar_atoms = ['N', 'O', 'S']


for atom in st.get_atoms():
    if atom.id in polar_atoms:
        selecti.append(atom)

nbsearch = NeighborSearch(selecti)

for atom1, atom2 in nbsearch.search_all(args.distance):
    print(atom1, atom2)
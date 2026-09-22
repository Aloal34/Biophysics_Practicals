import argparse
from Bio.PDB import NeighborSearch
from pdb_id_imports import get_structure


parser = argparse.ArgumentParser(
    description="Find possible disulfide bonds."
)

parser.add_argument(
    "pdb",
    help="PDB file or PDB ID"
)

parser.add_argument(
    "-d",
    "--distance",
    type=float,
    default=2.5,
    help="Maximum S-S distance "
         "(default: 2.5 Å)"
)

args = parser.parse_args()

st = get_structure(args.pdb)

select = []

for atom in st.get_atoms():
    if atom.id == 'SG':
        select.append(atom)

print("Number of SG atoms:", len(select))

nbsearch = NeighborSearch(select)

for atom1, atom2 in nbsearch.search_all(3.5):

    res1 = atom1.get_parent()
    res2 = atom2.get_parent()

    if res1 != res2: #residue display
        print(
            res1.get_resname(), res1.id[1],
            '-',
            res2.get_resname(), res2.id[1]
        )

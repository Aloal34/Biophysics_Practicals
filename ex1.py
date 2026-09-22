import argparse
from Bio.PDB import NeighborSearch
from pdb_id_imports import get_structure


parser = argparse.ArgumentParser(
    description="Find pairs of residues whose CA atoms "
                "are closer than a given distance."
)

parser.add_argument(
    "pdb",
    help="PDB file or PDB ID"
)

parser.add_argument(
    "distance",
    type=float,
    help="Maximum CA-CA distance in Angstroms"
)

args = parser.parse_args()

st = get_structure(args.pdb)

select = []
for at in st.get_atoms():
    if at.id == 'CA':
        select.append(at)
        print(f"ATOM: {at.get_parent().get_resname()}, {at.get_parent().id[1]}, {at.id}")

MAXDIST = 20 #define distance for a contact

nbsearch = NeighborSearch(select)

print("NBSEARCH:")

#search for contacts under HBLNK

ncontact = 1

for at1, at2 in nbsearch.search_all(MAXDIST):
    print(f"Contact: {ncontact}")
    print(f"at1: {at1}, {at1.get_serial_number()}, {at1.get_parent().get_resname()}")
    print(f"at2: {at2}, {at2.get_serial_number()}, {at2.get_parent().get_resname()}")
    print()
    ncontact += 1
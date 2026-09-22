import argparse
from Bio.PDB import NeighborSearch
from pdb_id_imports import get_structure


parser = argparse.ArgumentParser(
    description="Find peptide-bond C-N connections."
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
    help="Maximum C-N distance "
         "(default: 2.5 Å)"
)

args = parser.parse_args()

st = get_structure(args.pdb)

select = []

for atom in st.get_atoms():

    if atom.id == "C" or atom.id == "N":
        select.append(atom)

nbsearch = NeighborSearch(select)

bonds = []

for atom1, atom2 in nbsearch.search_all(args.distance):

    # Peptide bond must be C -> N
    if atom1.id == "C" and atom2.id == "N":

        res1 = atom1.get_parent()
        res2 = atom2.get_parent()

        # Must belong to different residues
        if res1 != res2:

            bonds.append(
                (
                    res1.id[1],
                    res2.id[1],
                    res1.get_resname(),
                    res2.get_resname(),
                    atom1 - atom2
                )
            )

# Sort by first residue, then second residue
bonds.sort(key=lambda x: (x[0], x[1]))

print("\nEx 5. Peptide-bond connectivity")
print("-" * 65)

for number, bond in enumerate(bonds, start=1):

    r1_num, r2_num, r1_name, r2_name, distance = bond

    print(
        f"{number:4d}. "
        f"{r1_name:>3} {r1_num:4d} C -- "
        f"{r2_name:>3} {r2_num:4d} N "
        f"{distance:6.2f} Å"
    )
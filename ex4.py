import argparse
from pdb_id_imports import get_structure


parser = argparse.ArgumentParser(
    description="List CA atoms of a given residue type "
                "with coordinates."
)

parser.add_argument(
    "pdb",
    help="PDB file or PDB ID"
)

parser.add_argument(
    "res_type",
    help="Residue type, e.g. W or TRP"
)

args = parser.parse_args()

st = get_structure(args.pdb)

aa_codes = {
    "A": "ALA",
    "R": "ARG",
    "N": "ASN",
    "D": "ASP",
    "C": "CYS",
    "E": "GLU",
    "Q": "GLN",
    "G": "GLY",
    "H": "HIS",
    "I": "ILE",
    "L": "LEU",
    "K": "LYS",
    "M": "MET",
    "F": "PHE",
    "P": "PRO",
    "S": "SER",
    "T": "THR",
    "W": "TRP",
    "Y": "TYR",
    "V": "VAL"
}

res_type = args.res_type.upper()

if len(res_type) == 1:

    if res_type not in aa_codes:
        raise ValueError(
            f"Unknown amino acid code: {res_type}"
        )

    res_type = aa_codes[res_type]

elif len(res_type) == 3:

    if res_type not in aa_codes.values():
        raise ValueError(
            f"Unknown amino acid code: {res_type}"
        )

else:

    raise ValueError(
        "Residue type must be a one- or three-letter code."
    )


selected = []

for residue in st.get_residues():

    if residue.get_resname() == res_type:

        if residue.has_id("CA"):

            selected.append(residue["CA"])


# Sort by residue number
selected.sort(
    key=lambda atom: atom.get_parent().id[1]
)

print("\nEx 4. CA atoms of residue type")
print("-" * 70)

print(f"Residue type: {res_type}")
print()

print(
    f"{'Residue':<8} "
    f"{'Number':>6} "
    f"{'Atom':>6} "
    f"{'X':>10} "
    f"{'Y':>10} "
    f"{'Z':>10}"
)

print("-" * 55)

for atom in selected:

    residue = atom.get_parent()

    x, y, z = atom.get_coord()

    print(
        f"{residue.get_resname():<8} "
        f"{residue.id[1]:6d} "
        f"{atom.id:>6} "
        f"{x:10.3f} "
        f"{y:10.3f} "
        f"{z:10.3f}"
    )
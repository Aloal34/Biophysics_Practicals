import os
import urllib.request
from Bio.PDB import PDBParser


def get_structure(pdb_input):

    if os.path.isfile(pdb_input):
        pdb_file = pdb_input

    else:
        pdb_id = os.path.splitext(os.path.basename(pdb_input))[0].upper()
        pdb_file = f"{pdb_id}.pdb"
        url = f"https://files.rcsb.org/download/{pdb_file}"

        urllib.request.urlretrieve(url, pdb_file)

    parser = PDBParser(QUIET=True)

    structure_id = os.path.splitext(os.path.basename(pdb_file))[0]

    return parser.get_structure(structure_id,pdb_file)
Exercises 1–8: Explanation of the Results

The examples show how the command-line arguments control each exercise and how the resulting lists should be interpreted. The PDB structure used for most examples is 1UBQ.

Ex1 — CA contacts

Ex1 selects CA atoms, uses NeighborSearch to find pairs within the requested distance, and reports the two residues and their CA-CA distance. The results are sorted by residue number. A 4 armstrong cutoff produces many contacts because neighboring residues in a protein backbone are only a few Å apart.

Ex2 — Atoms of a residue

Ex2 selects one residue using its chain ID and residue number. The output lists each atom belonging to that residue and its three Cartesian coordinates. The atom list is sorted by atom name to make the output easier to inspect.

Ex3 — Possible hydrogen-bond contacts

Ex3 uses the simplified definition from the exercise: N, O and S atoms are considered possible polar partners when they are closer than the selected cutoff. This is a geometric contact search rather than a full chemical hydrogen-bond assignment, so the output can include contacts that would need further chemical interpretation. It is merely theoretical speculation because actual hydrogen bonds are "implicit" in the pdb structure.

Ex4 — Residue type

Ex4 converts a one-letter amino-acid code such as G into its three-letter residue name, GLY, and then selects the CA atom of every matching residue. The results are ordered by residue number. There are some amino acids where no results appear as calcium is not present there.

Ex5 — Peptide-bond connectivity

Ex5 searches for short C-N pairs belonging to different residues. The short distances, around 1.3 Å in the example, identify the ordinary peptide-bond connections. We can see the bonds follow the structure of the protein chains as all amino acids are united by a peptide bond.

Ex6 — Disulfide bonds

Ex6 specifically selects SG atoms from CYS residues. If two SG atoms from different cysteines are close enough, the pair is reported as a possible disulffide bond. For 1UBQ, no CYS SG atoms are present, so the correct result is an empty disulfide-bond list. However, to demonstrate the correct use of the algorithm, we can download another structure and find these bonds.

Ex7 — Pairwise residue distances

Ex7 compares every atom of one selected residue with every atom of the second selected residue. The two distance calculations demonstrate that Bio.PDB atom subtraction and the Euclidean formula using NumPy coordinates give the same result.

Ex8 — Import/download module

Ex8 provides get_structure(), which the other scripts import. It can load an existing local PDB file or download a structure from the RCSB PDB when a PDB ID is supplied. This keeps the download/loading code out of the individual exercise scripts.
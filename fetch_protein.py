from Bio.PDB import PDBList, PDBParser
import nglview as nv

# Function to download a PDB structure
def fetch_pdb_structure(pdb_id):
    pdbl = PDBList()
    filename = pdbl.retrieve_pdb_file(pdb_id, file_format="pdb", pdir=".")
    return filename

# Fetch a sample protein (e.g., Hemoglobin: 1HHO)
pdb_id = "1HHO"  # Change this to any PDB ID
pdb_file = fetch_pdb_structure(pdb_id)

# Parse the structure
parser = PDBParser(QUIET=True)
structure = parser.get_structure(pdb_id, pdb_file)

# Visualize with nglview
view = nv.show_biopython(structure)
view

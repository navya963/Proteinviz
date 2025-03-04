from biopandas.pdb import PandasPdb
import py3Dmol

def visualize_protein(pdb_id):
    """Fetch and visualize a protein structure from the RCSB PDB database."""
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    
    try:
        ppdb = PandasPdb().fetch_pdb(pdb_id)
        ppdb.to_pdb(f"{pdb_id}.pdb", gz=False)
        
        # Display in 3D
        view = py3Dmol.view(width=800, height=600)
        view.addModel(open(f"{pdb_id}.pdb", "r").read(), "pdb")
        view.setStyle({"cartoon": {"color": "spectrum"}})
        view.zoomTo()
        return view.show()
    
    except Exception as e:
        print(f"Error fetching {pdb_id}: {e}")

# Ask user for PDB ID
pdb_id = input("Enter a PDB ID (e.g., 1BNA, 1A8M): ").strip()
visualize_protein(pdb_id)

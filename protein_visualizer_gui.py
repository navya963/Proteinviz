import tkinter as tk
from tkinter import messagebox
import py3Dmol
from Bio.PDB import PDBList

# Function to fetch and visualize protein structure
def visualize_protein():
    pdb_id = entry.get().strip().upper()
    if not pdb_id:
        messagebox.showerror("Error", "Please enter a valid PDB ID")
        return
    
    pdbl = PDBList()
    pdb_filename = pdbl.retrieve_pdb_file(pdb_id, file_format='pdb')
    
    with open(pdb_filename, "r") as f:
        pdb_data = f.read()
    
    # Create a Py3Dmol viewer
    viewer = py3Dmol.view(width=500, height=400)
    viewer.addModel(pdb_data, "pdb")
    viewer.setStyle({"cartoon": {"color": "spectrum"}})
    viewer.zoomTo()
    viewer.show()
    
    # Option to save the image
    def save_image():
        with open("protein_structure.png", "wb") as f:
    f.write(viewer.png())
        messagebox.showinfo("Saved", "Protein structure saved as protein_structure.png")
    
    save_button = tk.Button(root, text="Save Image", command=save_image)
    save_button.pack()

# GUI Setup
root = tk.Tk()
root.title("3D Protein Visualizer")

label = tk.Label(root, text="Enter PDB ID:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Visualize", command=visualize_protein)
button.pack()

root.mainloop()

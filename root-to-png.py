import ROOT
import sys

# Ensure a ROOT file argument is provided
if len(sys.argv) < 2:
    raise ValueError("No ROOT file provided. Please pass the file path as an argument.")

# Get the ROOT file path from the command-line arguments
root_file_path = sys.argv[1]

# Open the merged ROOT file
file = ROOT.TFile.Open(root_file_path)
if not file or file.IsZombie():
    raise RuntimeError(f"Failed to open ROOT file: {root_file_path}")

# Retrieve the histogram
hist = file.Get("h_M_Hyy")
if not hist:
    raise RuntimeError("Histogram h_M_Hyy not found in the merged ROOT file.")

# Set up the canvas and draw the histogram
canvas = ROOT.TCanvas("canvas", "", 800, 600)
hist.Draw()
canvas.SetLogy()

# Define output filename based on input file
output_filename = root_file_path.replace(".root", ".png")
canvas.SaveAs(output_filename)

# Close the ROOT file
file.Close()

print(f"Histogram saved as {output_filename}")

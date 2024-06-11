import ROOT

nmax = 100_000
def process_file(file_path, Muons_Signed_Distance):
    file = ROOT.TFile.Open(file_path)
    tree = ROOT.TChain("Truth_Info")
    tree.Add(file_path)
    hist = ROOT.TH1D(Muons_Signed_Distance, "Number of Muons vs Signed Distance;Signed Distance (mm);Number of Muons", 100, -2000, 2000)

    # Replace with your actual tree na
    nevents = tree.GetEntries()
    if nmax >= 0 and nevents > nmax: nevents = nmax
    # Figure out how often to print progress information.
    # Setting carriage = True will use a carriage return which keeps the progress on a single line
    # But if you add print statements, it will be ugly so it's not default
    carriage = False
    if carriage:
        if nevents <= 100: print_every = 1 
        elif nevents <= 1000: print_every = 10
        elif nevents <= 10000: print_every = 100
        else: print_every = 1000
    else:
        if nevents < 100: print_every = 1 # Print every event if < 100 events
        elif 100 <= nevents < 1000: print_every = 20
        elif 1000 <= nevents < 10000: print_every = 100
        elif 10000 <= nevents < 100000: print_every = 1000
        else: print_every = 10000
    # Now loop over all events
    for i, event in enumerate(tree):
        if i > nevents: break
        if tree != None: tree.GetEntry(i)
        # Print current progress, with carriage return \r to prevent long list of progress and have everything on a singe line.
        if i % print_every == 0 and carriage: print(f"\rOn {i} / {nevents}  {i/nevents*100}%", end='')
        if i % print_every == 0 and not carriage: print(f"On {i} / {nevents}   {i/nevents*100:.1f}%")
        # Create histogram with same binning for all files
        # hist = ROOT.TH1D(Muons_Signed_Distance, "Number of Muons vs Signed Distance;Signed Distance (mm);Number of Muons", 100, -2000, 2000)
        tree.GetEntry(i)

        x_start_tms = tree.PositionTMSStart[0]
        y_start_tms = tree.PositionTMSStart[1]
        z_start_tms = tree.PositionTMSStart[2]
        x_end = tree.DeathPosition[0]
        y_end = tree.DeathPosition[1]
        z_end = tree.DeathPosition[2]
        p_x = tree.MomentumTMSStart[0]
        p_z = tree.MomentumTMSStart[2]
        
        if p_z == 0:
            continue

        m = p_x / p_z
        b = x_start_tms - m * z_start_tms
        x_extrapolate = m * z_end + b
        signed_dist = x_end - x_extrapolate
        hist.Fill(signed_dist)
        # count+=1
        
        # file.Close()
    
    return hist

file_paths = [
    "/exp/dune/app/users/sushils/new_files/dune-tms/scripts/Reco/2024-04-19_bfield_0p0T.tmsreco.root",
    "/exp/dune/app/users/sushils/new_files/dune-tms/scripts/Reco/2024-04-19_bfield_1p0T.tmsreco.root",
    ]

labels = ["0T", "1T"]
colors = [ROOT.kRed, ROOT.kBlue]

# Create a TCanvas
canvas = ROOT.TCanvas("canvas", "Overlay Plot", 800, 600)

# Process each file and draw histograms with the "SAME" option
for i, file_path in enumerate(file_paths):
    hist = process_file(file_path, f"hist_{i}")
    # hist.SetLineColor(colors[i])
    draw_option = "colz"
    hist.Draw(draw_option)

# # Add a legend
# legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
# for hist, label in zip(histograms, labels):
#     legend.AddEntry(hist, label, "l")
# legend.Draw()

canvas.Print("overlay_plot.png")
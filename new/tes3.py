import glob
import argparse
import os
import math
import ROOT
import array

# Set ROOT to batch mode and configure styles
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.TH1.AddDirectory(False)
ROOT.TH2.AddDirectory(False)

# Define muon mass and fiducial cuts
MUON_MASS = 105.7  # MeV/c^2
FUDICIAL_CUT = 50
LAR_START = (-3478.48, -2166.71, 4179.24)
LAR_END = (3478.48, 829.282, 9135.88)

class Momentum:
    def __init__(self, kinetic_energy, classification="muon"):
        self.ke = kinetic_energy
        self.classification = classification
        self.ranges = [(0, 1000), (1000, 2000), (2000, 3000), (3000, 4000), (4000, 5000)]

    def momentum_from_kinetic_energy(self, ke):
        return math.sqrt((ke + MUON_MASS) ** 2 - MUON_MASS ** 2)

    def get_range_index(self):
        for i, r in enumerate(self.ranges):
            if r[0] <= self.ke <= r[1]:
                return i
        return None

def inside_tms(x, y, z):
    return -3500 < x < 3500 and -3700 < y < 1000 and 11000 < z < 18200

def inside_lar(x, y, z):
    return -4500 < x < 3700 and -3200 < y < 1000 and 4100 < z < 9200

def region1(x):
    return -4000 < x < -2500

def region2(x):
    return -1500 < x < 1500

def region3(x):
    return 2500 < x < 4000

def run(c, truth, outfilename, nmax=-1):
    bin_edges = array.array('d', [0, 1000, 2000, 3000, 4000, 5000])
    hist_signed_distance_muon = [ROOT.TH1D(f"muon_{i}", f"Muon and Anti Muon Momentum corresponding to K.E ({bin_edges[i]}-{bin_edges[i+1]} MeV)", 100, -2000, 2000) for i in range(len(bin_edges)-1)]
    hist_signed_distance_amuon = [ROOT.TH1D(f"amuon_{i}", f"Muon and Anti Muon Momentum corresponding to K.E ({bin_edges[i]}-{bin_edges[i+1]} MeV)", 100, -2000, 2000) for i in range(len(bin_edges)-1)]

    # Set axis labels for each histogram
    for hist in hist_signed_distance_muon + hist_signed_distance_amuon:
        hist.SetXTitle("Signed Distance (mm)")
        hist.SetYTitle("Number of Muons")

    nevents = min(c.GetEntries(), nmax if nmax >= 0 else float('inf'))
    print_every = max(1, nevents // 10)

    for i in range(nevents):
        if i % print_every == 0: print(f"On {i} / {nevents} ({i/nevents*100:.1f}%)")
        c.GetEntry(i)
        truth.GetEntry(i)

        for index, pdg in enumerate(truth.PDG):
            signed_dist = None
            if pdg in [13, -13]:
                x_start = truth.BirthPosition[4*index]
                y_start = truth.BirthPosition[4*index+1]
                z_start = truth.BirthPosition[4*index+2]
                x_end = truth.DeathPosition[4*index]
                y_end = truth.DeathPosition[4*index+1]
                z_end = truth.DeathPosition[4*index+2]
                x_start_tms = truth.PositionTMSStart[4*index]
                z_start_tms = truth.PositionTMSStart[4*index+2]

                if isinstance(truth.Muon_TrueKE, (list, tuple, ROOT.vector('float'))):
                    KE_muon = truth.Muon_TrueKE[index]
                else:
                    KE_muon = truth.Muon_TrueKE

                if inside_lar(x_start, y_start, z_start) and inside_tms(x_end, y_end, z_end):
                    if region1(x_start_tms) and region1(x_end):
                        p_z = truth.MomentumTMSStart[4*index+2]
                        p_x = truth.MomentumTMSStart[4*index]
                        if p_z != 0: signed_dist = x_end - (p_x/p_z * z_end + (x_start_tms - p_x/p_z * z_start_tms))
                    elif region2(x_start_tms) and region2(x_end):
                        p_z, p_x = truth.MomentumTMSStart[4*index+2], truth.MomentumTMSStart[4*index]
                        if p_z != 0: signed_dist = -(x_end - (p_x/p_z * z_end + (x_start_tms - p_x/p_z * z_start_tms)))
                    elif region3(x_start_tms) and region3(x_end):
                        p_z, p_x = truth.MomentumTMSStart[4*index+2], truth.MomentumTMSStart[4*index]
                        if p_z != 0: signed_dist = x_end - (p_x/p_z * z_end + (x_start_tms - p_x/p_z * z_start_tms))

                    p = Momentum(KE_muon, classification="muon" if pdg == 13 else "amuon")
                    range_index = p.get_range_index()
                    if range_index is not None and signed_dist is not None:
                        if pdg == 13:
                            hist_signed_distance_muon[range_index].Fill(signed_dist)
                        else:
                            hist_signed_distance_amuon[range_index].Fill(signed_dist)

    tf = ROOT.TFile(outfilename, "recreate")
    canvas = ROOT.TCanvas("canvas", "canvas", 800, 600)

    for i in range(len(bin_edges) - 1):
        hist_signed_distance_muon[i].SetLineColor(ROOT.kRed)
        hist_signed_distance_amuon[i].SetLineColor(ROOT.kBlue)

        hist_signed_distance_muon[i].Draw("hist")
        hist_signed_distance_amuon[i].Draw("hist same")

        legend = ROOT.TLegend(0.65, 0.75, 0.85, 0.85)
        legend.SetTextSize(0.03)
        legend.SetFillColor(ROOT.kWhite)
        legend.SetBorderSize(1)
        legend.AddEntry(hist_signed_distance_muon[i], "Muon", "l")
        legend.AddEntry(hist_signed_distance_amuon[i], "Antimuon", "l")
        legend.Draw()

        canvas.Write()
        canvas.Print(f"{outfilename.replace('.root', '')}_ke_{bin_edges[i]}_{bin_edges[i+1]}.png")

    for hist in hist_signed_distance_muon + hist_signed_distance_amuon:
        hist.Write()
    tf.Close()
    print("Done saving.")

def validate_then_run(args):
    infile = args.filename
    if infile != "":
        # In this case, the user specified exactly one file. Usually they'd hadd many files together.
        files_to_use = infile

    outdir = args.outdir
    if outdir == "":
        # No output directory was specified so use the default
        # First we need the username
        username = os.environ["USER"]
        outdir = f"/exp/dune/app/users/{username}/dune-tms_hists"
    else:
        # Check if it follows the correct conventions
        good_locations = ["/dune/data/users", "/dune/data2/users", "/pnfs/dune/persistent", "/pnfs/dune/scratch"]
        if not any(location in outdir for location in good_locations):
            print(f"Warning: outdir is not in list of good locations. Don't want to write root files to app area. {outdir}")
    
    # Make sure the output directory exists
    
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    outname = args.name
    if ".root" not in outname:
        raise ValueError(f"The output file should be a root file. {outname}")
    outfilename = os.path.join(outdir, outname)
    if os.path.exists(outfilename):
        if args.allow_overwrite:
            print(f"Warning: A file already exists at {outfilename}, but you specified allow_overwrite. It will be overwritten")
        else:
            raise ValueError(f"The output file already exists at {outfilename}. Please specify another location, allow_overwrite or delete the file yourself.")
    print(f"Output will be in {outfilename}")
    
        
    has_truth = True

    for f in files_to_use:
    # Make the TChain objects. One for truth information and one for reconstructed information.
        c = ROOT.TChain("Line_Candidates")
        truth = None
        if has_truth: truth = ROOT.TChain("Truth_Info")
    # for f in files_to_use:
        c.Add(f)
        if has_truth: truth.Add(f)
        assert c.GetEntries() > 0, "Didn't get any entries in Line_Candidates TChain."
        if has_truth: assert truth.GetEntries() > 0, "Didn't get any entries in Truth_Info TChain."

        nevents = args.nevents
        assert nevents >= -1, f"nevents <= -1, why? {nevents}"
        run(c, truth, outfilename, args.nevents)



if __name__ == "__main__":
    def list_of_strings(arg):
        return arg.split(',')

    parser = argparse.ArgumentParser(description='Draws spills.')
    parser.add_argument('--outdir', type=str, help="The output dir. Will be made if it doesn't exist.", default="")
    parser.add_argument('--name', type=str, help="The name of the output files.", default="dune-tms_hists.root")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--indir', type=str, help="The location of the input tmsreco files", default="")
    group.add_argument('--inlist', type=str, help="The input filelist", default="")
    group.add_argument('--filename', '-f', type=list_of_strings, help="The input file, if you have a single file", default="")
    parser.add_argument('--nevents', '-n', type=int, help="The maximum number of events to loop over", default=-1)
    parser.add_argument('--allow_overwrite', help="Allow the output file to overwrite", action=argparse.BooleanOptionalAction)
    parser.add_argument('--preview', help="Save preview images of the histograms", action=argparse.BooleanOptionalAction)

    args = parser.parse_args()

    validate_then_run(args)
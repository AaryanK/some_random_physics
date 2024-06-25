import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph



with open("python_object_new.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)
red_colors = matplotlib.cm.Reds(np.linspace(0.5, 1, 5))
indexes = ['0p0T','0p9T','1p0T','1p1T','2p0T']
muon_graph = Hists_Graph("hist_signed_distance", "Muons signed distance: (x_extropolate - x_truth) (using truth_info);True signed distance(mm) ;Number of muons")
muon_names = []
print(loaded_data.keys())

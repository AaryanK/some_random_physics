
import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph



with open("python_object.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)

amuon_graph = Hists_Graph("hist_signed_distance_muon_antimuon", "Particles signed distance: (x_extropolate - x_truth) (using truth_info) ;True signed distance(mm); Number of Particles")
red_colors = matplotlib.cm.Reds(np.linspace(0.2, 1, 5))
blue_colors = matplotlib.cm.Blues(np.linspace(0.2, 1, 5))

indexes = ['0p0T','0p9T','1p0T','1p1T','2p0T']
amuon_names=[]
for count,i in enumerate(loaded_data['AMUONS']):
    filtered_name = i.split("_")[-1].split(".")[0]
    ind = indexes.index(filtered_name)
    # print(ind)
    amuon_graph.add(np.array(loaded_data['AMUONS'][i]),color=blue_colors[ind])
    amuon_graph.add(np.array(loaded_data['MUONS'][i]),color=red_colors[ind])
    amuon_names.append("AMuon " + filtered_name)
    amuon_names.append("Muon " + filtered_name)
amuon_graph.finish(amuon_names)
amuon_graph.save("Amuons and Muons.jpg")
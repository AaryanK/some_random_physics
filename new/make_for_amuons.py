
import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph



with open("python_object.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)

amuon_graph = Hists_Graph("hist_signed_distance_antimuon", "Antimuons signed distance: (x_extropolate - x_truth) (using truth_info) ;True signed distance(mm); Number of antimuons")
indexes = ['0p0T','0p9T','1p0T','1p1T','2p0T']
blue_colors = matplotlib.cm.Blues(np.linspace(0.5, 1, 5))

amuon_names=[]
for i in loaded_data['AMUONS']:
    filtered_name = i.split("_")[-1].split(".")[0]
    ind = indexes.index(filtered_name)

    amuon_graph.add(np.array(loaded_data['AMUONS'][i]),color=blue_colors[ind])
    amuon_names.append(filtered_name)
amuon_graph.finish(amuon_names)
amuon_graph.save("Amuons.jpg")
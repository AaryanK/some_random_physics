import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph



with open("python_object.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)

muon_graph = Hists_Graph("hist_signed_distance", "Muons signed distance: (x_extropolate - x_truth) (using truth_info);True signed distance(mm) ;Number of muons")
muon_names = []
for i in loaded_data['MUONS']:
    filtered_name = i.split("_")[-1].split(".")[0]
    muon_graph.add(np.array(loaded_data['MUONS'][i]))
    muon_names.append(filtered_name)

muon_graph.finish(muon_names)
muon_graph.save("Muons.jpg")


import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph



with open("python_object.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)

amuon_graph = Hists_Graph("hist_signed_distance_antimuon", "Antimuons signed distance: (x_extropolate - x_truth) (using truth_info) ;True signed distance(mm); Number of antimuons")

amuon_names=[]
for i in loaded_data['AMUONS']:
    filtered_name = i.split("_")[-1].split(".")[0]
    amuon_graph.add(np.array(loaded_data['AMUONS'][i]))
    amuon_names.append(filtered_name)
amuon_graph.finish(amuon_names)
amuon_graph.save("Amuons.jpg")
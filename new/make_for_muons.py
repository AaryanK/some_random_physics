import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph



with open("python_object.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)
# red_colors = matplotlib.cm.Reds(np.linspace(0.5, 1, 5))
# indexes = ['0p0T','0p9T','1p0T','1p1T','2p0T']
indexes = ['0p0T','0p5T', '0p7T', '0p9T', '1p0T', '1p1T', '1p3T','1p5T','2p0T']

# red_colors = ['#FFCCCC', '#FF9999', '#FF6666', '#FF3333', '#FF0000']
red_colors = matplotlib.cm.Blues(np.linspace(0.5, 1, 9))

muon_graph = Hists_Graph("hist_signed_distance", "Muons signed distance: (x_extropolate - x_truth) (using truth_info);True signed distance(mm) ;Number of muons")
muon_names = []
for i in loaded_data['MUONS']:
    filtered_name = i.split("_")[-1].split(".")[0]
    # print(filtered_name)
    ind = indexes.index(filtered_name)
    muon_graph.add(np.array(loaded_data['MUONS'][i]),color=red_colors[ind])
    muon_names.append(filtered_name)

muon_graph.finish(muon_names)
muon_graph.save("Muons.jpg")

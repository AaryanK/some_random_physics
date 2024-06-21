
import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph



with open("python_object_latest.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)

muon_graph = Hists_Graph("Muons Correct Charge Percent", "True Muon KE (Mev) ;True signed distance(mm); Fraction")

muon_names=[]
for i in loaded_data['AMUONS']:
    filtered_name = i.split("_")[-1].split(".")[0]

    for k in range(1, len(loaded_data['MUONS_CORRECT'][i][0])):
        key = loaded_data['MUONS_CORRECT'][i][0][k]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = k - 1
        while j >= 0 and key < loaded_data['MUONS_CORRECT'][i][0][j]:
            loaded_data['MUONS_CORRECT'][i][0][j + 1] = loaded_data['MUONS_CORRECT'][i][0][j]
            loaded_data['MUONS_CORRECT'][i][1][j+1] = loaded_data['MUONS_CORRECT'][i][1][j]
            j -= 1
        loaded_data['MUONS_CORRECT'][i][0][j + 1] = key

    muon_graph.add_plot(loaded_data['MUONS_CORRECT'][i][0],loaded_data['MUONS_CORRECT'][i][1])
    # muon_graph.add(loaded_data['MUONS_CORRECT'][i][0])
    muon_names.append(filtered_name)
    print("passed")
muon_graph.finish(muon_names)
muon_graph.save("muons_Correct.jpg")
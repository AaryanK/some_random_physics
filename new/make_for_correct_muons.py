
import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph



with open("python_object.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)

muon_graph = Hists_Graph("Muons Correct Charge Percent", "True Muon KE (Mev) ;True signed distance(mm); Fraction")

muon_names=[]
for i in loaded_data['AMUONS']:
    filtered_name = i.split("_")[-1].split(".")[0]
    muon_graph.add(loaded_data['MUONS_CORRECT'][i])
    muon_names.append(filtered_name)
muon_graph.finish(muon_names)
muon_graph.save("muons_Correct.jpg")
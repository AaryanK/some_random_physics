
import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph



with open("python_object_lat_ultra.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)

amuon_graph = Hists_Graph("Anti-Muons Correct Charge Percent", "True Anti-Muon KE (Mev) ;True signed distance(mm); Fraction")

amuon_names=[]
for i in loaded_data['AMUONS']:
    filtered_name = i.split("_")[-1].split(".")[0]
    # num,den = np.array(loaded_data['AMUONS_CORRECT'][i][0]),np.array(loaded_data['AMUONS_CORRECT'][i][1])
    # # print(num/den)
    # bins = np.linspace(0, 10000, 100)  # 100 bins from -5 to 5
    
    # hist1, bin_edges1 = np.histogram(num, bins=bins)
    # hist2, bin_edges2 = np.histogram(den, bins=bins)
    # bin_centers = (bin_edges1[:-1] + bin_edges1[1:]) / 2
    # hist_ratio = np.divide(hist1, hist2, out=np.zeros_like(hist1, dtype=float), where=hist2 != 0)
    # amuon_graph.make_bar(bin_centers, hist_ratio, width=bin_edges1[1] - bin_edges1[0],)


    # print(max(loaded_data['AMUONS_CORRECT'][i][1]))
    # break
    # print(len(loaded_data['AMUONS_CORRECT'][i][0]),len(loaded_data['AMUONS_CORRECT'][i][1]))
    # print(loaded_data['AMUONS_CORRECT'][i][0][29],loaded_data['AMUONS_CORRECT'][i][1][29])
#     for k in range(1, len(loaded_data['AMUONS_CORRECT'][i][0])):
#         key = loaded_data['AMUONS_CORRECT'][i][0][k]
#         # Move elements of arr[0..i-1], that are greater than key,
#         # to one position ahead of their current position
#         j = k - 1
#         while j >= 0 and key < loaded_data['AMUONS_CORRECT'][i][0][j]:
#             loaded_data['AMUONS_CORRECT'][i][0][j + 1] = loaded_data['AMUONS_CORRECT'][i][0][j]
#             loaded_data['AMUONS_CORRECT'][i][1][j+1] = loaded_data['AMUONS_CORRECT'][i][1][j]
#             j -= 1
#         loaded_data['AMUONS_CORRECT'][i][0][j + 1] = key


    
#     # amuon_graph.add(loaded_data['AMUONS_CORRECT'][i][0],loaded_data['AMUONS_CORRECT'][i][1])
#     amuon_graph.add_plot(loaded_data['AMUONS_CORRECT'][i][0],loaded_data['AMUONS_CORRECT'][i][1])
    amuon_names.append(filtered_name)
# amuon_graph.finish(amuon_names)
# amuon_graph.save("Amuons_Correct.jpg")
print(amuon_names)
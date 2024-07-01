
import pickle
import matplotlib
import numpy as np
from mat_helper import Hists_Graph
import matplotlib.colors as mcolors



with open("python_object_lat_ultra.sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)

muon_graph = Hists_Graph("Muons Correct Charge Percent", "True Muon KE (Mev) ;True signed distance(mm); Fraction")

# red_colors = ['#FFCCCC', '#FF9999', '#FF6666', '#FF3333', '#FF0000']
# red_colors = matplotlib.cm.Reds(np.linspace(0.5, 1, 9))

num_colors = 9
# red_colors = [mcolors.to_hex((1, i/num_colors, i/num_colors)) for i in range(num_colors)]
# red_colors = [mcolors.to_hex((i/num_colors, 0, 0)) for i in range(num_colors)]
# red_colors = [mcolors.to_hex((1, i/(num_), i/(num_colors-1))) for i in range(num_colors,0,-1)]
# red_colors = [mcolors.to_hex((i/num_colors,0,0)) for i in range(num_colors,0,-1)]
alpha_colors = np.linspace(0.5,1,num_colors)

# indexes = ['0p5T', '0p7T', '0p9T', '1p0T', '1p1T', '1p3T', '1p5T']
indexes = ['0p0T','0p5T', '0p7T', '0p9T', '1p0T', '1p1T', '1p3T','1p5T','2p0T']

muon_names=[]
for i in loaded_data['AMUONS']:
    filtered_name = i.split("_")[-1].split(".")[0]

    # for k in range(1, len(loaded_data['MUONS_CORRECT'][i][0])):
    #     key = loaded_data['MUONS_CORRECT'][i][0][k]
    #     # Move elements of arr[0..i-1], that are greater than key,
    #     # to one position ahead of their current position
    #     j = k - 1
    #     while j >= 0 and key < loaded_data['MUONS_CORRECT'][i][0][j]:
    #         loaded_data['MUONS_CORRECT'][i][0][j + 1] = loaded_data['MUONS_CORRECT'][i][0][j]
    #         loaded_data['MUONS_CORRECT'][i][1][j+1] = loaded_data['MUONS_CORRECT'][i][1][j]
    #         j -= 1
    #     loaded_data['MUONS_CORRECT'][i][0][j + 1] = key

    num,den = np.array(loaded_data['MUONS_CORRECT'][i][0]),np.array(loaded_data['MUONS_CORRECT'][i][1])
    bins = np.linspace(500, 5000, 100)  # 100 bins from -5 to 5
    
    hist1, bin_edges1 = np.histogram(num, bins=bins)
    hist2, bin_edges2 = np.histogram(den, bins=bins)
    bin_centers = (bin_edges1[:-1] + bin_edges1[1:]) / 2
    hist_ratio = np.divide(hist1, hist2, out=np.zeros_like(hist1, dtype=float), where=hist2 != 0)
    ind = indexes.index(filtered_name)
    muon_graph.make_bar(bin_centers, hist_ratio, width=bin_edges1[1] - bin_edges1[0],color="red",alpha=alpha_colors[ind])

    # muon_graph.add(loaded_data['MUONS_CORRECT'][i][0])
    muon_names.append(filtered_name)
    print("passed")
muon_graph.finish(muon_names)
muon_graph.save("muons_Correct.jpg")
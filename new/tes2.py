import pickle
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mat_helper import Hists_Graph
import matplotlib.colors as mcolors
import math

# Define muon mass and fiducial cuts
MUON_MASS = 105.7  # MeV/c^2
FUDICIAL_CUT = 50
LAR_START = (-3478.48, -2166.71, 4179.24)
LAR_END = (3478.48, 829.282, 9135.88)



class Momentum:
    def __init__(self, kinetic_energy, classification="muon"):
        self.ke = kinetic_energy
        self.classification = classification
        self.ranges = [(0, 1000), (1000, 2000), (2000, 3000), (3000, 4000), (4000, 5000)]

    def momentum_from_kinetic_energy(self, ke):
        return math.sqrt((ke + MUON_MASS) ** 2 - MUON_MASS ** 2)

    def get_range_index(self):
        for i, r in enumerate(self.ranges):
            if r[0] <= self.ke <= r[1]:
                return i
        return None

def inside_tms(x, y, z):
    return -3500 < x < 3500 and -3700 < y < 1000 and 11000 < z < 18200

def inside_lar(x, y, z):
    return -4500 < x < 3700 and -3200 < y < 1000 and 4100 < z < 9200

def region1(x):
    return -4000 < x < -2500

def region2(x):
    return -1500 < x < 1500

def region3(x):
    return 2500 < x < 4000

with open("python_object (20).sushil_dai", 'rb') as file:
    loaded_data = pickle.load(file)

# muon_graph = Hists_Graph("Muons Correct TMS", "TMSMomentumStart ;True signed distance(mm); Fraction")
# num_colors = 10
indexes = ['0p0T','0p5T', '0p7T', '0p9T', '1p0T', '1p1T', '1p3T','1p5T','2p0T']
graphs = [["Muon and Anti Muon Momentum corresponding to K.E 0-1000", "Signed Distance ;True signed distance(mm); Number of muons"],
               ["Muon and Anti Muon Momentum corresponding to K.E 1000-2000","Signed Distance ;True signed distance(mm); Number of muons"],
               ["Muon and Anti Muon Momentum corresponding to K.E 2000-3000", "Signed Distance ;True signed distance(mm); Number of muons"],
               ["Muon and Anti Muon Momentum corresponding to K.E 3000-4000", "Signed Distance ;True signed distance(mm); Number of muons"],
               ["Muon and Anti Muon Momentum corresponding to K.E 4000-5000", "Signed Distance ;True signed distance(mm); Number of muons"]]

red_colors = matplotlib.cm.Reds(np.linspace(0.3, 1, len(indexes)))
blue_colors = matplotlib.cm.Blues(np.linspace(0.3, 1, len(indexes)))
muon_data=[{},{},{},{},{}]
amuon_data = [{},{},{},{},{}]
for i in loaded_data['AMUONS']:
    # print(loaded_data['MUONS'][i])
    count = 0
    for signed_distance,muon_ke in zip(loaded_data['MUONS'][i],loaded_data['MUONS_CORRECT'][i][1]):
        p = Momentum(muon_ke)
        count+=1
        if p.get_range_index() is not None:
            if i not in muon_data[p.get_range_index()].keys(): muon_data[p.get_range_index()][i] = []
            muon_data[p.get_range_index()][i].append(signed_distance)
    for signed_distance,amuon_ke in zip(loaded_data['AMUONS'][i],loaded_data['AMUONS_CORRECT'][i][1]):
        p = Momentum(amuon_ke)
        if p.get_range_index() is not None:
            if i not in amuon_data[p.get_range_index()].keys(): amuon_data[p.get_range_index()][i] = []
            amuon_data[p.get_range_index()][i].append(signed_distance)
    print(i.split("_")[-1].split(".")[0],count)

for i,(range_muon,range_amuon) in enumerate(zip(muon_data,amuon_data)):
    g = Hists_Graph(graphs[i][0],graphs[i][1])
    anames = []
    mnames = []
    for fname in range_muon:
        # print(fname)
        filtered_name = fname.split("_")[-1].split(".")[0]
        print(filtered_name)
        ind = indexes.index(filtered_name)
        # print(filtered_name)

        g.add(np.array(range_muon[fname]),name="Muon "+filtered_name,color=red_colors[ind],alpha=0.9)
        mnames.append("Muon " + filtered_name)
        if fname in range_amuon.keys():
            g.add(np.array(range_amuon[fname]),name="Amuon "+filtered_name,color=blue_colors[ind],alpha=0.9)
            anames.append("AMuon " + filtered_name)
        # mnames.append("Muon " + filtered_name)

    # if 
    g.finish(anames,handle="Amuon "+filtered_name,loc="upper right")
    g.finish(mnames,handle="Muon "+filtered_name,loc="upper left")

    g.save(f"Momentum_Ranges/{g.title}.jpg")


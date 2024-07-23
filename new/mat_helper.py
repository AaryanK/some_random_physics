import matplotlib.pyplot as plt
import numpy as np

class Hists_Graph():
    def __init__(self,Title,xy):
        self.title = Title
        x,y = xy.split(";")[0],xy.split(";")[2]
        plt.title(Title,fontweight='bold')
        plt.xlabel(x)
        plt.ylabel(y)

    def add(self,x,color=None,ylim=None,bins=None):
        # Create a histogram with 200 bins
        plt.hist(x,histtype="step",color=color,bins=bins)   
        # plt.hist(x,bins=100,color=color)   
        plt.xlim(-2000, 2000)
        

    def make_bar(self,bin_centers,hist_ratio,width,color,alpha):
        plt.step(bin_centers, hist_ratio, where='mid',linestyle="-",color=color,alpha=alpha)
        # plt.ylim(0,1)

    def show(self):
        plt.show()

    def scatter(self,x,y,color=None):
        plt.scatter(x,y)
        
    def finish(self,f):
        plt.legend(f,loc="upper right")
    
    def add_plot(self,x,y):
        plt.plot(x,y)
    
    def add_gradient(self,data,color,bins,label,alpha=0.7):
        counts,bin_edges = np.histogram(data,bins=bins)
        counts = counts / counts.max()  # Normalize counts
        
        for i in range(len(bin_edges) - 1):
            plt.fill_between([bin_edges[i], bin_edges[i+1]], 0, counts[i], color=color, alpha=alpha, label=label if i == 0 else "")
        
    def save(self,f):
        plt.savefig(f)
        # plt.title(self.title)
        plt.close()

    def step(self,x,y):
        plt.step(x, y, where='mid', label='Efficiency',bins=100)

import matplotlib.pyplot as plt
import numpy as np

class Hists_Graph():
    def __init__(self,Title,xy):
        x,y = xy.split(";")[0],xy.split(";")[2]
        plt.title(Title, fontsize=15, fontweight='bold', color='purple')
        plt.xlabel(x)
        plt.ylabel(y)

    def add(self,x,color=None):
        # Create a histogram with 200 bins
        plt.hist(x,histtype="step",bins=100,color=color)   

    def finish(self,f):
        
        plt.legend(f,loc="upper right")
    
    def add_plot(self,x,y):
        plt.plot(x,y)
    
    
    def save(self,f):
        plt.savefig(f)



        
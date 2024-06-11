import math
# Define muon mass
MUON_MASS = 105.658  # MeV/c^2

#These bars are set from observational evidence, in all the entries the minimum and the maximum of the momentums were calculated and compared leading to these insights.
MINIMUM_MOMENTUM_M,MINIMUM_MOMENTUM_AM,MAXIMUM_MOMENTUM_M,MAXIMUM_MOMENTUM_AM=1.5156060996446286e-05, 0.013872138024538572, 89068.26396962765, 69257.1880976166

class Momentum:#Creating a custom class so that methods could be applied to the momentum
    def __init__(self,kinetic_energy,classification="muon"):
        global MINIMUM_MOMENTUM_M,MINIMUM_MOMENTUM_AM,MAXIMUM_MOMENTUM_M,MAXIMUM_MOMENTUM_AM
        self.ke = kinetic_energy
        self.classification =classification

        self.ZERO_THOUSAND =(0,1000)
        self.THOUSAND_2THOUSAND =(1000,2000)
        self.THOUSAND2_3THOUSAND =(2000,300)
        self.THOUSAND3_4THOUSAND=(3000,4000)
        self.THOUSAND4_5THOUSAND=(4000,5000)

    #Define a function to return the momentum given muon's kinetic energy
    def momentum_from_kinetic_energy(self,ke):
        global MUON_MASS
        return math.sqrt(ke**2 + MUON_MASS**2) - MUON_MASS
    
    def is_ZERO_THOUSAND(self):
        if self.ZERO_THOUSAND[0]<=self.ke<=self.ZERO_THOUSAND[1]: return True
        else: return False
    
    def is_THOUSAND_2THOUSAND(self):
        if self.THOUSAND_2THOUSAND[0]<=self.ke<=self.THOUSAND_2THOUSAND[1]: return True
        else: return False

    def is_THOUSAND2_3THOUSAND(self):
        if self.THOUSAND2_3THOUSAND[0]<=self.ke<=self.THOUSAND2_3THOUSAND[1]: return True
        else: return False

    def is_THOUSAND3_4THOUSAND(self):
        if self.THOUSAND3_4THOUSAND[0]<=self.ke<=self.THOUSAND3_4THOUSAND[1]: return True
        else: return False

    def is_THOUSAND4_5THOUSAND(self):
        if self.THOUSAND4_5THOUSAND[0]<=self.ke<=self.THOUSAND4_5THOUSAND[1]: return True
        else: return False
        
p = Momentum(20,'muon')

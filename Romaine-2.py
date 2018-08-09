##########################################

## Developed - R.D 2018
## Please leave comments in case of any changes to the code.
## User must change the path from where the file (dam model) is loaded.
## In case of changes to the mesh, coordinates in the resultsINV(g_o)
## and resultsINH(g_o) may have to be modified. Presently it is
## based on very fine mesh state.
## Avoid commenting the g_o = CallSolver() as subsequent methods
## require the return value.
## Modify the password for the server connection.

##########################################
import sys
sys.path.append(r"C:\Program Files\Plaxis\PLAXIS 2D\python\Lib\site-packages")

plaxis_path = 'C:\Program Files\Plaxis\PLAXIS 2D\python\Lib\site-packages'

import imp
import math
import csv
import numpy as np
import matplotlib.pyplot as plt
from array import *
from matplotlib import interactive


found_module = imp.find_module('plxscripting', [plaxis_path])
plxscripting = imp.load_module('plxscripting', *found_module)

from itertools import zip_longest
from plxscripting.easy import *

#Connect the server
s_i, g_i = new_server('localhost',10000,password='6N4@X%Xngtg51/G$')


# Load the project. Always check the path of the project
s_i.open(r"C:\Users\rdas\Documents\Romaine-2 dam-MC.p2dx")




# Used to store coordinate and displacement values
totaldisplacementY_INV01 = []
coordinatesY_INV01 = []
totaldisplacementY_INV02 = []
coordinatesY_INV02 = []
totaldisplacementY_INH01 = []
coordinatesY_INH01 =[]
totaldisplacementY_INH02 = []
coordinatesY_INH02 =[]



# Soil material counter
counterMaterial = len(g_i.Materials)

#Phase counter
counterPhases = len(g_i.Phases)

#Check the phase and material counts
print('*********Number of Phases=' + str(counterPhases) + '**********')
print('*** Number of Soil Materials=' + str(counterMaterial) + '**********')

def get_phasedetails():

 #Loop through the phases to extract details (comprises initial phase)
 for y in range(counterPhases):
 
 
  ##***** Print phase details on the console********************* 
  print('********Phase Details************')
  print('***********' + str(g_i.Phases[y].Identification) + '**********')
  print('**********************************')
  print('*** Phase number='+ str(g_i.Phases[y].Number) + '****')    
  print('*****First step=' + str(g_i.Phases[y].FirstStep) + '************')
  print('******Last step=' + str(g_i.Phases[y].LastStep) + '***************')
  print('****** Phase design approach='+ str(g_i.Phases[y].DesignApproach) + '********')

 
 
 """
  ## For more phase details uncomment the following lines 
  #print(g_i.Phases[y].DeformCalcType)
  #print(g_i.Phases[y].PorePresCalcType)
  #print(g_i.Phases[y].LogInfo)
  #print(g_i.Phases[y].ShouldCalculate)
  #print(g_i.Phases[y].CalculationResult)
  ## For more phase details uncomment the above lines 
 
 """


def get_soilmaterials():

 #Loop through soil materials for details
 for x in range(counterMaterial):

 
##*** Print soil properties on the console*********************

  print("") 
  print("")
  print('********Material Details************')
  print('***********' + str(g_i.Materials[x].MaterialName) + '*************')
  print('**********************************') 
  print('***** Solid model=' + str(g_i.Materials[x].SoilModel) + '**********')
  print(g_i.Materials[x].DrainageType)
  print('***** Gref='+ str(g_i.Materials[x].Gref) + '***********') 
  print('***** Cohesion=' + str(g_i.Materials[x].cref) + '*************')
  print('****Friction angle='+ str(g_i.Materials[x].phi) + '******************')
  print( '****Dilatancy angle='+ str(g_i.Materials[x].psi) + '****************')
  print(g_i.Materials[x].verticalref)
  print(g_i.Materials[x].K0)
  print(g_i.Materials[x].cinc)
  print('****gamma='+ str(g_i.Materials[x].gammaUnsat) + '*************')
  print('****gammaf='+ str(g_i.Materials[x].gammaSat) + '**************')
  print('***Per Horizontal axis =' + str(g_i.Materials[x].perm_primary_horizontal_axis) + '*********')
  print('*******Per Vertical axis=' + str(g_i.Materials[x].perm_vertical_axis) + '******************')
  print('***** Rayleigh Alpha=' + str(g_i.Materials[x].RayleighAlpha) + '*************')
  print('***** Rayleigh Beta=' + str(g_i.Materials[x].RayleighBeta) + '***************')
  print('****Poisson ratio='+ str(g_i.Materials[x].nu) + '**********')
  print('***Eref =' + str(g_i.Materials[x].Eref)+ '***********' )
  print('****Eoed ='+ str(g_i.Materials[x].Eoed) + '**********')
  print('*****Vs=' + str(g_i.Materials[x].Vs) + '**********')
  print('*****Vp=' + str(g_i.Materials[x].Vp) + '*********' )
  print('***Einc=' + str(g_i.Materials[x].Einc) + '************')
  print('***K0Primary=' + str(g_i.Materials[x].K0Primary) + '********')
  print('******Specific heat capacity=' + str(g_i.Materials[x].SpecificHeatCapacity) + '*********')
  print('***** Thermal conductivity='+ str(g_i.Materials[x].ThermalConductivity) + '*************')

  ## Uncomment the following lines to obtain additional soil material details  
  #print(g_i.Materials[x].Rinter)
  #print(g_i.Materials[x].TensileStrength)
  #print(g_i.Materials[x].UDPower)
  #print(g_i.Materials[x].verticalinc)
  #print(g_i.Materials[x].Ginc)
  #print(g_i.Materials[x].ninit)
  #print(g_i.Materials[x].nmin)
  #print(g_i.Materials[x].nmax)
  #print(g_i.Materials[x].gammaPore) 
  #print(g_i.Materials[x].ck)
  #print(g_i.Materials[x].nuu)
  #print(g_i.Materials[x].UDPRef)
  #print(g_i.Materials[x].einit)
  #print(g_i.Materials[x].emin)
  #print(g_i.Materials[x].emax)
  #print(g_i.Materials[x].Dinter)
  #print(g_i.Materials[x].SkemptonB)
  #print(g_i.Materials[x].KwRefN)
  #print(g_i.Materials[x].VolumetricSpecificStorage)
  
  #print(g_i.Materials[x].K0Secondary)
  #print(g_i.Materials[x].SoilRatioSmall)
  #print(g_i.Materials[x].SoilRatioMedium)
  #print(g_i.Materials[x].SoilRatioLarge)
  #print(g_i.Materials[x].PsiUnsat)
  #print(g_i.Materials[x].HydraulicModel)
  #print(g_i.Materials[x].FlowDataModel)
  #print(g_i.Materials[x].ThermalParameters)
  #print(g_i.Materials[x].Density)
  #print(g_i.Materials[x].SolidThermalExpansionX)
  #print(g_i.Materials[x].SolidThermalExpansionY)
  #print(g_i.Materials[x].SolidThermalExpansionZ)
  #print(g_i.Materials[x].VapourDiffusion)
  #print(g_i.Materials[x].VapourDiffusionEnhancementFactor)
  #print(g_i.Materials[x].ThermalInsulance)
  #print(g_i.Materials[x].DrainageConductivity)
  #print(g_i.Materials[x].DefaultValuesAdvanced)  
  #print(g_i.Materials[x].DataSetFlow)
  #print(g_i.Materials[x].SoilTypeFlow)
  #print(g_i.Materials[x].M50)
  #print(g_i.Materials[x].UseDefaultsFlow)
  #print(g_i.Materials[x].TablePsiPermSat)
  #print(g_i.Materials[x].SplinePsiPerm)
  #print(g_i.Materials[x].SplinePsiSat)
  #print(g_i.Materials[x].TensionCutOff)
 ## Uncomment the above lines for additional soil material details



## Update soil material properties
## Based on the material type
def update_materialParametrs():

 for x in range(counterMaterial): 
 
   if ((g_i.Materials[x].MaterialName) == '2E') :
    
    print("") 

   elif((g_i.Materials[x].MaterialName) == 'Foundation') :
    
    print("") 

   elif((g_i.Materials[x].MaterialName) == 'asphalt core') :
    
    print("") 

   elif((g_i.Materials[x].MaterialName) == '3P') :

    ###Eparameter = g_i.Materials[x].Eref
    #Gparameter = g_i.Materials[x].Gref 
    #Poissonparameter =  g_i.Materials[x].nu
    #GParameter = 25563.9098 # this ensures that there is a 15% change in E
    ###Eparameter = Gparameter * (2*(1 + Poissonparameter))
    #g_i.Materials[x].Gref = GParameter   
     g_i.Materials[x].cref = CohesionParameter
     g_i.Materials[x].phi =  FricAngleParameter 
     g_i.Materials[x].psi = DiltAngleParameter 
       
    
    print("")   
   

   elif((g_i.Materials[x].MaterialName) == '3O') :	 
   
   
    print("")    

   elif((g_i.Materials[x].MaterialName) == '3N') :	 
   
   
    print("") 

  
 
 
 


##########################Second Server Connection###################################

def CallSolver():

 
  
 #Call the solver, True for calculating all the phases
 g_i.calculate(True) 

 #For output details. 
 output_port_1=g_i.view(g_i.Phases[-1])

 #For output details with results in select mesh points. 
 #output_port_1=g_i.selectmeshpoints()

 s_o, g_o = new_server('localhost',output_port_1,password='6N4@X%Xngtg51/G$')

 #print(g_o.Nodes)

 return g_o




#########################################################################

def resultsINV(g_o):   	

 
 ##====================This is a different loop providing some basic ideas====================
 #counterForPhase = 0
 #iterate = g_o.Phases[:]
 
 #Fetch the results from Plaxis at specific points
 # here this is acheived at different phases
 # could be modified based on the requirements 
 # for future use
 
 #for phase in iterate:
  
 
  #print(phase.Name.value)
  
  #print(phase.Steps.value)
  
  ##Points at three different vertical points   
    
  #sigma1_low = g_o.getsingleresult(g_o.Phases[counterForPhase], g_o.ResultTypes.Soil.SigmaTotal1, (3.97, 136.50)) 
  #sigma3_low = g_o.getsingleresult(g_o.Phases[counterForPhase], g_o.ResultTypes.Soil.SigmaTotal3, (3.97, 136.50)) 
  #eps1_low = g_o.getsingleresult(g_o.Phases[counterForPhase], g_o.ResultTypes.Soil.Eps1, (3.97, 136.50))  
  
  
  
  ## To obtain deviatoric stress result at a particular point
  ##  Uncomment and modify as required
  #DeviStress = g_o.getsingleresult(g_o.Phases[counterForPhase], g_o.ResultTypes.Soil.DeviatoricStress, (3.97, 136.50))    
   
  
  ## To format the data fetched from Plaxis, apply the following approach
  ## the coder may modify based upon his/her requirement
  #sigma_low = -(float(sigma1_low.replace('\U00002013', '-')) - float(sigma3_low.replace('\U00002013', '-')))  
  #sigma_mid = -(float(sigma1_mid.replace('\U00002013', '-')) - float(sigma3_mid.replace('\U00002013', '-')))
  #sigma_high = -(float(sigma1_high.replace('\U00002013', '-')) - float(sigma3_high.replace('\U00002013', '-')))
  #eps1_low = -(float(eps1_low.replace('\U00002013', '-'))) 
  #eps1_mid = -(float(eps1_mid.replace('\U00002013', '-'))) 
  #eps1_high = -(float(eps1_high.replace('\U00002013', '-')))  
  
 
  #try:

   #sigma_low = g_o.getsingleresult(g_o.Phases[counterForPhase], g_o.ResultTypes.Soil.DeviatoricStress, (3.97, 136.50))   
   #deviatoricstressesLow.append(float(sigma_low))
   #print ("")
   
  #except:
    	  
   #sigma_low = 0
   #deviatoricstressesLow.append(sigma_low)  
   #print("")
   
  #try:
   
   #eps1_low = -(float(eps1_low.replace('\U00002013', '-'))) 
   #axialepsilonsLow.append(eps1_low)   
   #print("")
   
  #except:	  
   
   #eps1_low = 0
   #axialepsilonsLow.append(eps1_low)  
   #print("")
  
    
  ## To fetch resut details such as SigmaTMin2, ESum2, Eps2 use the following lines
  ## they are being fetched at specific points
  
  #print(g_o.getsingleresult(g_o.Phases[counterForPhase], g_o.ResultTypes.Soil.SigmaTMin2, (3.97, 136.50)))    
  #print(g_o.getsingleresult(g_o.Phases[counterForPhase], g_o.ResultTypes.Soil.SigmaESum2, (0.74, 248.30))) 
  #print(g_o.getsingleresult(g_o.Phases[counterForPhase], g_o.ResultTypes.Soil.Eps2, (0.74, 248.30))) 
  
  #counterForPhase = counterForPhase + 1   
  
  ##====================This is a different loop providing some basic ideas. Ends here=================
  
  ## ================================================================
  ##========== Displacement INV02 - For Vertical inclinometers=========================
  
 
 try:
      
   Uy_INV02_one = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.83, 246.20)))
   print('****Total displacement INV02_one=' + str(Uy_INV02_one ))
   totaldisplacementY_INV02.append(Uy_INV02_one)
   coordinatesY_INV02.append(246.20)     
   
 except:
   
   Utot_INV02_one  = 0 # Or do nothing      
 
 try: 

   Uy_INV02_two  = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 234.90)))
   print('****Total displacement INV02_two=' + str(Uy_INV02_two))
   totaldisplacementY_INV02.append(Uy_INV02_two)
   coordinatesY_INV02.append(234.90)  
   
 except:
   
   Utot_INV02_two  = 0    # Or do nothing    
       
 try:
  
   Uy_INV02_three  = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 214.90)))   
   print('****Total displacement INV02_three=' + str(Uy_INV02_three))
   totaldisplacementY_INV02.append(Uy_INV02_three)
   coordinatesY_INV02.append(214.90)  
      
 except:   
 
    Utot_INV02_three = 0   

 try:
    
    Uy_INV02_four = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 199.90)))   
    print('****Total displacement INV02_four=' + str(Uy_INV02_four))   
    totaldisplacementY_INV02.append(Uy_INV02_four)
    coordinatesY_INV02.append(199.90)    
 
 except:    

    Utot_INV02_four = 0 

 try:
    
    Uy_INV02_five = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 196.10)))   
    print('****Total displacement INV02_five=' + str(Uy_INV02_five))   
    totaldisplacementY_INV02.append(Uy_INV02_five)
    coordinatesY_INV02.append(196.10)    
 
 except:    

    Utot_INV02_five = 0 

 try:
    
    Uy_INV02_six = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 194.90)))   
    print('****Total displacement INV02_six=' + str(Uy_INV02_six))   
    totaldisplacementY_INV02.append(Uy_INV02_six)
    coordinatesY_INV02.append(194.90)    
 
 except:    

    Utot_INV02_six = 0 

 try:
    
    Uy_INV02_seven = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 191.10)))   
    print('****Total displacement INV02_seven=' + str(Uy_INV02_seven))   
    totaldisplacementY_INV02.append(Uy_INV02_seven)
    coordinatesY_INV02.append(191.10)    
 
 except:    

    Utot_INV02_seven = 0 

 try:
    
    Uy_INV02_eight = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 189.90)))   
    print('****Total displacement INV02_eight=' + str(Uy_INV02_eight))   
    totaldisplacementY_INV02.append(Uy_INV02_eight)
    coordinatesY_INV02.append(189.90)    
 
 except:    

    Utot_INV02_eight = 0 


 try:
    
    Uy_INV02_nine = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 186.10)))   
    print('****Total displacement INV02_nine=' + str(Uy_INV02_nine))   
    totaldisplacementY_INV02.append(Uy_INV02_nine)
    coordinatesY_INV02.append(186.10)    
 
 except:    

    Utot_INV02_nine = 0         

 try: 

    Uy_INV02_ten = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 174.90)))   
    print('****Total displacement INV02_ten=' + str(Uy_INV02_ten))  
    totaldisplacementY_INV02.append(Uy_INV02_ten)
    coordinatesY_INV02.append(174.90)      

 except:    	 

    Utot_INV02_ten = 0    
 
 try: 

    Uy_INV02_eleven = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (5.73, 154.90)))   
    print('****Total displacement INV02_eleven=' + str(Uy_INV02_eleven))    
    totaldisplacementY_INV02.append(Uy_INV02_eleven)
    coordinatesY_INV02.append(154.90)      
     
 except:    	 

    Utot_INV02_eleven = 0             

 try: 

    Uy_INV02_twelve = float(g_o.getsingleresult(g_o.Phases[counterPhases - 1], g_o.ResultTypes.Soil.Uy, (6.38, 135.30)))   
    print('****Total displacement INV02_twelve=' + str(Uy_INV02_twelve))    
    totaldisplacementY_INV02.append(Uy_INV02_twelve)
    coordinatesY_INV02.append(135.30)      
 
 except:    	 

    Utot_INV02_twelve = 0   
 

##================ Displacement INV02 ends here=========================



##============== Displacement INV01 - For Vertical inclinometers=================
 
 try:
     
   Uy_INV01_one = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.74, 247.10)))
   print('****Total displacement INV01_one=' + str(Uy_INV01_one))
   totaldisplacementY_INV01.append(Uy_INV01_one)
   coordinatesY_INV01.append(247.10)
   
 except:
   
   print("")   
 
 try: 

   Uy_INV01_two  = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 234.90)))
   print('****Total displacement INV01_two=' + str(Uy_INV01_two))
   totaldisplacementY_INV01.append(Uy_INV01_two)
   coordinatesY_INV01.append(234.90)      
      
 except:
         
   print("") # Or do nothing     
   
 try:
       
   Uy_INV01_three  = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 214.90)))   
   print('****Total displacement INV01_three=' + str(Uy_INV01_three))
   totaldisplacementY_INV01.append(Uy_INV01_three)
   coordinatesY_INV01.append(214.90)
   
 except:   
 
    print("")
    
 try:
      
    Uy_INV01_four = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 199.90)))   
    print('****Total displacement INV01_four=' + str(Uy_INV01_four))   
    totaldisplacementY_INV01.append(Uy_INV01_four)
    coordinatesY_INV01.append(199.90) 	    

 except:    
  
    print("") # Or do nothing         

 try:
      
    Uy_INV01_five = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 197.90)))   
    print('****Total displacement INV01_five=' + str(Uy_INV01_five))   
    totaldisplacementY_INV01.append(Uy_INV01_five)
    coordinatesY_INV01.append(197.90) 	    

 except:    
  
   print("") # Or do nothing  


 try:
      
    Uy_INV01_six = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 194.90)))   
    print('****Total displacement INV01_six=' + str(Uy_INV01_six))   
    totaldisplacementY_INV01.append(Uy_INV01_six)
    coordinatesY_INV01.append(194.90) 	    

 except:    
  
    print("") # Or do nothing  

 try:
      
    Uy_INV01_seven = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 191.90)))   
    print('****Total displacement INV01_seven=' + str(Uy_INV01_seven))   
    totaldisplacementY_INV01.append(Uy_INV01_seven)
    coordinatesY_INV01.append(191.90) 	    

 except:    
  
    print("") # Or do nothing  

 try:
      
    Uy_INV01_eight = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 189.90)))   
    print('****Total displacement INV01_eight=' + str(Uy_INV01_eight))   
    totaldisplacementY_INV01.append(Uy_INV01_eight)
    coordinatesY_INV01.append(189.90) 	    

 except:    
  
    print("") # Or do nothing  

 try:
      
    Uy_INV01_nine = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 186.10)))   
    print('****Total displacement INV01_nine=' + str(Uy_INV01_nine))   
    totaldisplacementY_INV01.append(Uy_INV01_nine)
    coordinatesY_INV01.append(186.10) 	    

 except:    
  
    print("") # Or do nothing  

 try:
      
    Uy_INV01_ten = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 184.90)))   
    print('****Total displacement INV01_ten=' + str(Uy_INV01_ten))   
    totaldisplacementY_INV01.append(Uy_INV01_ten)
    coordinatesY_INV01.append(184.90) 	    

 except:    
  
    print("") # Or do nothing  

 try: 

    Uy_INV01_eleven = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 174.90)))   
    print('****Total displacement INV01_eleven=' + str(Uy_INV01_eleven))  
    totaldisplacementY_INV01.append(Uy_INV01_eleven)
    coordinatesY_INV01.append(174.90)     

 except:    	 

    print("")

 try: 

    Uy_INV01_twelve = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.67, 154.90)))   
    print('****Total displacement INV01_twelve=' + str(Uy_INV01_twelve))    
    totaldisplacementY_INV01.append(Uy_INV01_twelve)
    coordinatesY_INV01.append(154.90)  
     
 except:    	 
     
    print("")  # Do nothing   

 try: 

    Uy_INV01_thirteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (-5.45, 134.20)))   
    print('****Total displacement INV01_thirteen=' + str(Uy_INV01_thirteen))    
    totaldisplacementY_INV01.append(Uy_INV01_thirteen)
    coordinatesY_INV01.append(134.20)     
 
 except:    	 
   
   print("") # Or do nothing 




##================ Displacement INV01 ends here=========================
 
 ## Uncomment to debug
 #print(totaldisplacementY_INV02)
 #print(coordinatesY_INV02)
 #print(totaldisplacementY_INV01)
 #print(coordinatesY_INV01)

 
 return totaldisplacementY_INV01, coordinatesY_INV01, totaldisplacementY_INV02, coordinatesY_INV02, 
 
#for step in phase.Steps.value:	 

 ##To print the curve results
 #for step in g_o.Steps[1:]: 
 
  #print('Curve result') 
  ##print(g_o.getcurveresults(g_o.Nodes[0], step, g_o.ResultTypes.Soil.Utot))
  #print(g_o.getcurveresults(g_o.Node_A, step, g_o.ResultTypes.Soil.Utot))
 


def resultsINH(g_o):

 ##============== Displacement INH01 - For Horizontal inclinometers=================
 ##===The values are being assigned a negative value in the list only for the purpose of plotting====
 ##===Depending on the situation the negative value could be removed based on requirement=====
 
 try:
     
   Uy_INH01_one = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (5.73, 194.90)))
   print('****Total displacement INH01_one=' + str(Uy_INH01_one))
   totaldisplacementY_INH01.append(Uy_INV01_one)
   coordinatesY_INH01.append(5.73)
   
 except:
  print("")
  
 try:
     
   Uy_INH01_two = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (12.28, 194.90)))
   print('****Total displacement INH01_two=' + str(Uy_INH01_two))
   totaldisplacementY_INH01.append(Uy_INH01_two)
   coordinatesY_INH01.append(12.28)
   
 except:
  print("")
  
 try:
     
   Uy_INH01_three = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (19.34, 194.90)))
   print('****Total displacement INH01_three=' + str(Uy_INH01_three))
   totaldisplacementY_INH01.append(Uy_INH01_three)
   coordinatesY_INH01.append(19.34)
   
 except:
  print("")
 
 try:
     
   Uy_INH01_four = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (21.25, 194.90)))
   print('****Total displacement INH01_four=' + str(Uy_INH01_four))
   totaldisplacementY_INH01.append(Uy_INH01_four)
   coordinatesY_INH01.append(21.25)
   
 except:
  print("")
  
 try:
     
   Uy_INH01_five = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (26.95, 194.90)))
   print('****Total displacement INH01_five=' + str(Uy_INH01_five))
   totaldisplacementY_INH01.append(Uy_INH01_five)
   coordinatesY_INH01.append(26.95)
   
 except:
  print("")
 
 try:
     
   Uy_INH01_six = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (31.05, 194.90)))
   print('****Total displacement INH01_six=' + str(Uy_INH01_six))
   totaldisplacementY_INH01.append(Uy_INH01_six)
   coordinatesY_INH01.append(31.05)
   
 except:
  print("") # Do nothing

 try:
     
   Uy_INH01_seven = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (35.15, 194.90)))
   print('****Total displacement INH01_seven=' + str(Uy_INH01_seven))
   totaldisplacementY_INH01.append(Uy_INH01_seven)
   coordinatesY_INH01.append(35.15)
   
 except:
  print("") # Do nothing
   
 try:
     
   Uy_INH01_eight = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (37.11, 194.90)))
   print('****Total displacement INH01_eight=' + str(Uy_INH01_eight))
   totaldisplacementY_INH01.append(Uy_INH01_eight)
   coordinatesY_INH01.append(37.11)
   
 except:
  print("")
 
 try:
     
   Uy_INH01_nine = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (39.07, 194.90)))
   print('****Total displacement INH01_nine=' + str(Uy_INH01_nine))
   totaldisplacementY_INH01.append(Uy_INH01_nine)
   coordinatesY_INH01.append(39.07)
   
 except:
  print("") # Do nothing
  
 try:
     
   Uy_INH01_ten = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (43.00, 194.90)))
   print('****Total displacement INH01_ten=' + str(Uy_INH01_ten))
   totaldisplacementY_INH01.append(Uy_INH01_ten)
   coordinatesY_INH01.append(43.00)
   
 except:
  print("")
  
 try:
     
   Uy_INH01_eleven = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (46.94, 194.90)))
   print('****Total displacement INH01_eleven=' + str(Uy_INH01_eleven))
   totaldisplacementY_INH01.append(Uy_INH01_eleven)
   coordinatesY_INH01.append(46.94)
   
 except:
  print("")
 
 try:
     
   Uy_INH01_twelve = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (50.89, 194.90)))
   print('****Total displacement INH01_twelve=' + str(Uy_INH01_twelve))
   totaldisplacementY_INH01.append(Uy_INH01_twelve)
   coordinatesY_INH01.append(50.89)
   
 except:
  print("")
 
 try:
     
   Uy_INH01_thirteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (52.87, 194.90)))
   print('****Total displacement INH01_thirteen=' + str(Uy_INH01_thirteen))
   totaldisplacementY_INH01.append(Uy_INH01_thirteen)
   coordinatesY_INH01.append(52.87)
   
 except:
  print("")
 
 try:
     
   Uy_INH01_fourteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (54.85, 194.90)))
   print('****Total displacement INH01_fourteen=' + str(Uy_INH01_fourteen))
   totaldisplacementY_INH01.append(Uy_INH01_fourteen)
   coordinatesY_INH01.append(54.85)
   
 except:
  print("")

 try:
     
   Uy_INH01_fifteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (58.82, 194.90)))
   print('****Total displacement INH01_fifteen=' + str(Uy_INH01_fifteen))
   totaldisplacementY_INH01.append(Uy_INH01_fifteen)
   coordinatesY_INH01.append(58.82)
   
 except:
  print("") # Do nothing
 
 try:
     
   Uy_INH01_sixteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (60.81, 194.90)))
   print('****Total displacement INH01_sixteen=' + str(Uy_INH01_sixteen))
   totaldisplacementY_INH01.append(Uy_INH01_sixteen)
   coordinatesY_INH01.append(60.81)
   
 except:
  print("") # Do nothing
  
 try:
     
   Uy_INH01_seventeen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (62.80, 194.90)))
   print('****Total displacement INH01_seventeen=' + str(Uy_INH01_seventeen))
   totaldisplacementY_INH01.append(Uy_INH01_seventeen)
   coordinatesY_INH01.append(62.80)
  
 except:
  print("")
  
 try:
     
   Uy_INH01_eighteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (66.79, 194.90)))
   print('****Total displacement INH01_eighteen=' + str(Uy_INH01_eighteen))
   totaldisplacementY_INH01.append(Uy_INH01_eighteen)
   coordinatesY_INH01.append(66.79)
   
 except:
  print("")
 
 try:
     
   Uy_INH01_nineteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (72.80, 194.90)))
   print('****Total displacement INH01_nineteen=' + str(Uy_INH01_nineteen))
   totaldisplacementY_INH01.append(Uy_INH01_nineteen)
   coordinatesY_INH01.append(72.80)
   
 except:
  print("")
 
  
 try:
     
   Uy_INH01_twenty = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (74.80, 194.90)))
   print('****Total displacement INH01_twenty=' + str(Uy_INH01_twenty))
   totaldisplacementY_INH01.append(Uy_INH01_twenty)
   coordinatesY_INH01.append(74.80)
   
 except:
  print("")
  
 try:
     
   Uy_INH01_twentyone = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (78.83, 194.90)))
   print('****Total displacement INH01_twentyone=' + str(Uy_INH01_twentyone))
   totaldisplacementY_INH01.append(Uy_INH01_twentyone)
   coordinatesY_INH01.append(78.83)
   
 except:
  print("")
 
 


 ##================ Displacement INH01 ends here=========================
 
 
 ##============== Displacement INH02 - For Horizontal inclinometers===============
 
 
 try:
     
   Uy_INH02_one = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (5.73, 171.10)))
   print('****Total displacement INH02_one=' + str(Uy_INH02_one))
   totaldisplacementY_INH02.append(Uy_INH02_one)
   coordinatesY_INH02.append(5.73)
   
 except:
  print("") # Do nothing
  
 try:
     
   Uy_INH02_two = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (7.11, 171.10)))
   print('****Total displacement INH02_two=' + str(Uy_INH02_two))
   totaldisplacementY_INH02.append(Uy_INH02_two)
   coordinatesY_INH02.append(7.11)
   
 except:
  print("")
  
 try:
     
   Uy_INH02_three = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (11.47, 171.10)))
   print('****Total displacement INH02_three=' + str(Uy_INH02_three))
   totaldisplacementY_INH02.append(Uy_INH02_three)
   coordinatesY_INH02.append(11.47)
   
 except:
  print("") # Do nothing
 
 try:
     
   Uy_INH02_four = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (17.47, 171.10)))
   print('****Total displacement INH02_four=' + str(Uy_INH02_four))
   totaldisplacementY_INH02.append(Uy_INH02_four)
   coordinatesY_INH02.append(17.47)
   
 except:
  print("")
  
 try:
     
   Uy_INH02_five = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (25.36, 171.10)))
   print('****Total displacement INH02_five=' + str(Uy_INH02_five))
   totaldisplacementY_INH02.append(Uy_INH02_five)
   coordinatesY_INH02.append(25.36)
   
 except:
  print("") # Do nothing
 
 try:
     
   Uy_INH02_six = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (30.37, 171.10)))
   print('****Total displacement INH02_six=' + str(Uy_INH02_six))
   totaldisplacementY_INH02.append(Uy_INH02_six)
   coordinatesY_INH02.append(30.37)
   
 except:
  print("")

 try:
     
   Uy_INH02_seven = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (32.03, 171.10)))
   print('****Total displacement INH02_seven=' + str(Uy_INH02_seven))
   totaldisplacementY_INH02.append(Uy_INH02_seven)
   coordinatesY_INH02.append(32.03)
   
 except:
  print("")  # Do nothing
   
 try:
     
   Uy_INH02_eight = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (37.29, 171.10)))
   print('****Total displacement INH02_eight=' + str(Uy_INH02_eight))
   totaldisplacementY_INH02.append(Uy_INH02_eight)
   coordinatesY_INH02.append(37.29)
   
 except:
  print("")
 
 try:
     
   Uy_INH02_nine = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (39.03, 171.10)))
   print('****Total displacement INH02_nine=' + str(Uy_INH02_nine))
   totaldisplacementY_INH02.append(Uy_INH02_nine)
   coordinatesY_INH02.append(39.03)
   
 except:
  print("")
  
 try:
     
   Uy_INH02_ten = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (44.54, 171.10)))
   print('****Total displacement INH02_ten=' + str(Uy_INH02_ten))
   totaldisplacementY_INH02.append(Uy_INH02_ten)
   coordinatesY_INH02.append(44.54)
   
 except:
  print("")
  
 try:
     
   Uy_INH02_eleven = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (46.32, 171.10)))
   print('****Total displacement INH02_eleven=' + str(Uy_INH02_eleven))
   totaldisplacementY_INH02.append(Uy_INH02_eleven)
   coordinatesY_INH02.append(46.32)
   
 except:
  print("")
 
 try:
     
   Uy_INH02_twelve = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (48.21, 171.10)))
   print('****Total displacement INH02_twelve=' + str(Uy_INH02_twelve))
   totaldisplacementY_INH02.append(Ux_INH02_twelve)
   coordinatesY_INH02.append(48.21)
   
 except:
  print("")
 
 try:
     
   Uy_INH02_thirteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (51.99, 171.10)))
   print('****Total displacement INH02_thirteen=' + str(Uy_INH02_thirteen))
   totaldisplacementY_INH02.append(Uy_INH02_thirteen)
   coordinatesY_INH02.append(51.99)
   
 except:
  print("")
 
 try:
     
   Uy_INH02_fourteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (53.78, 171.10)))
   print('****Total displacement INH02_fourteen=' + str(Uy_INH02_fourteen))
   totaldisplacementY_INH02.append(Uy_INH02_fourteen)
   coordinatesY_INH02.append(53.78)
   
 except:
  print("") # Do nothing

 try:
     
   Uy_INH02_fifteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (57.57, 171.10)))
   print('****Total displacement INH02_fifteen=' + str(Uy_INH02_fifteen))
   totaldisplacementY_INH02.append(Uy_INH02_fifteen)
   coordinatesY_INH02.append(57.57)
   
 except:
  print("")
 
 try:
     
   Uy_INH02_sixteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (61.25, 171.10)))
   print('****Total displacement INH02_sixteen=' + str(Uy_INH02_sixteen))
   totaldisplacementY_INH02.append(Uy_INH02_sixteen)
   coordinatesY_INH02.append(61.25)
   
 except:
  print("")
  
 try:
     
   Uy_INH02_seventeen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (65.04, 171.10)))
   print('****Total displacement INH02_seventeen=' + str(Uy_INH02_seventeen))
   totaldisplacementY_INH02.append(Uy_INH02_seventeen)
   coordinatesY_INH02.append(65.04)
  
 except:
  print("")
  
 try:
     
   Uy_INH02_eighteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (68.73, 171.10)))
   print('****Total displacement INH02_eighteen=' + str(Uy_INH02_eighteen))
   totaldisplacementY_INH02.append(Uy_INH02_eighteen)
   coordinatesY_INH02.append(68.73)
   
 except:
  print("")
 
 try:
     
   Uy_INH02_nineteen = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (74.44, 171.10)))
   print('****Total displacement INH02_nineteen=' + str(Uy_INH02_nineteen))
   totaldisplacementY_INH02.append(Uy_INH02_nineteen)
   coordinatesY_INH02.append(74.44)
   
 except:
  print("")
 
  
 try:
     
   Uy_INH02_twenty = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (76.23, 171.10)))
   print('****Total displacement INH02_twenty=' + str(Uy_INH02_twenty))
   totaldisplacementY_INH02.append(Uy_INH02_twenty)
   coordinatesY_INH02.append(76.23)
   
 except:
  print("")
  
 try:
     
   Uy_INH02_twentyone = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (81.95, 171.10)))
   print('****Total displacement INH02_twentyone=' + str(Uy_INH02_twentyone))
   totaldisplacementY_INH02.append(Uy_INH02_twentyone)
   coordinatesY_INH02.append(81.95)
   
 except:
  print("")
 
  
 try:
     
   Uy_INH02_twentytwo = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (83.75, 171.10)))
   print('****Total displacement INH02_twentytwo=' + str(Uy_INH02_twentytwo))
   totaldisplacementY_INH02.append(Uy_INH02_twentytwo)
   coordinatesY_INH02.append(83.75)
   
 except:
  print("")
 
  
 try:
     
   Uy_INH02_twentythree = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (89.47, 171.10)))
   print('****Total displacement INH02_twentythree=' + str(Uy_INH02_twentythree))
   totaldisplacementY_INH02.append(Uy_INH02_twentythree)
   coordinatesY_INH02.append(89.47)
   
 except:
  print("")
 
  
 try:
     
   Uy_INH02_twentyfour = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (91.27, 171.10)))
   print('****Total displacement INH02_twentyfour=' + str(Uy_INH02_twentyfour))
   totaldisplacementY_INH02.append(Uy_INH02_twentyfour)
   coordinatesY_INH02.append(91.27)
   
 except:
   print("")
  
 try:
     
   Uy_INH02_twentyfive = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (97.01, 171.10)))
   print('****Total displacement INH02_twentyfive=' + str(Uy_INH02_twentyfive))
   totaldisplacementY_INH02.append(Uy_INH02_twentyfive)
   coordinatesY_INH02.append(97.01)
   
 except:
  print("") # Do nothing
  
  
 try:
     
   Uy_INH02_twentysix = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (102.60, 171.10)))
   print('****Total displacement INH02_twentysix=' + str(Uy_INH02_twentysix))
   totaldisplacementY_INH02.append(Uy_INH02_twentysix)
   coordinatesY_INH02.append(102.60)
   
 except:
   print("")
  
 try:
     
   Uy_INH02_twentyseven = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (106.40, 171.10)))
   print('****Total displacement INH02_twentyseven=' + str(Uy_INH02_twentyseven))
   totaldisplacementY_INH02.append(Uy_INH02_twentyseven)
   coordinatesY_INH02.append(106.40)
   
 except:
  print("")
 
 
 try:
     
   Uy_INH02_twentyeight = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (110.20, 171.10)))
   print('****Total displacement INH02_twentyeight=' + str(Uy_INH02_twentyeight))
   totaldisplacementY_INH02.append(Uy_INH02_twentyeight)
   coordinatesY_INH02.append(110.20)
   
 except:
  print("")
 
 try:
   
   Uy_INH02_twentynine = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (113.90, 171.10)))
   print('****Total displacement INH02_twentynine=' + str(Uy_INH02_twentynine))
   totaldisplacementY_INH02.append(Uy_INH02_twentynine)
   coordinatesY_INH02.append(113.90)
   
 except:
  print("")
 
 try:
     
   Uy_INH02_thirty = float(g_o.getsingleresult(g_o.Phases[counterPhases-1], g_o.ResultTypes.Soil.Uy, (117.80, 171.10)))
   print('****Total displacement INH02_thirty=' + str(Uy_INH02_thirty))
   totaldisplacementY_INH02.append(Uy_INH02_thirty)
   coordinatesY_INH02.append(117.80)
   
 except:
  print("")
 
 ##================ Displacement INH02 ends here=========================

 ## Uncomment to debug
 #print(totaldisplacementY_INH02)
 #print(coordinatesY_INH02)
 #print(totaldisplacementY_INH01)
 #print(coordinatesY_INH01)

 return totaldisplacementY_INH01, coordinatesY_INH01, totaldisplacementY_INH02, coordinatesY_INH02, 





# Plot Vertical inclinometer results and compare with actual data
def plotfunction_INV(dispY_INV01, cordY_INV01, dispY_INV02, cordY_INV02): 


 ##=====Subplot approaches=========
 
 #plt.subplot(311)
 #plt.plot(argStnL,argStrsL,'r--')
 #plt.loglog(argStnL,argStrsL,'r--')
 #plt.xlabel('Strain')
 #plt.semilogy(argStnL,argStrsL,'r--')
 #plt.ylabel('Stress')
 #plt.title('Lowest level')
 #plt.grid(True)

##=====Subplot approaches=======================

##+++++++++Experimental Data for Comparison+++++++++++
##+++++++++++Refer the excel files++++++++++++++++++

 ExpData_INV02 = []
 CordData_INV02= []
 
 ExpData_INV01 =[]
 CordData_INV01=[]
 
 
 
 ExpData_INV02.append(-0.355)
 ExpData_INV02.append(-0.339)
 ExpData_INV02.append(-0.292)
 ExpData_INV02.append(-0.252) 
 ExpData_INV02.append(-0.239)
 ExpData_INV02.append(-0.236)
 ExpData_INV02.append(-0.221)
 ExpData_INV02.append(-0.218)
 ExpData_INV02.append(-0.203)
 ExpData_INV02.append(-0.160)
 ExpData_INV02.append(-0.082) 
 ExpData_INV02.append(0) 

 CordData_INV02.append(246.19)
 CordData_INV02.append(235.19)
 CordData_INV02.append(215.19)
 CordData_INV02.append(200.19)
 CordData_INV02.append(196.19)
 CordData_INV02.append(195.19)
 CordData_INV02.append(191.19)
 CordData_INV02.append(190.19)
 CordData_INV02.append(186.19)
 CordData_INV02.append(175.19)
 CordData_INV02.append(154.19)
 CordData_INV02.append(135.30)
 
 ExpData_INV01.append(-0.277)
 ExpData_INV01.append(-0.260)
 ExpData_INV01.append(-0.206)
 ExpData_INV01.append(-0.155)
 ExpData_INV01.append(-0.148)
 ExpData_INV01.append(-0.215)
 ExpData_INV01.append(-0.212)
 ExpData_INV01.append(-0.209)
 ExpData_INV01.append(-0.199)
 ExpData_INV01.append(-0.194)
 ExpData_INV01.append(-0.157)
 ExpData_INV01.append(-0.072)
 ExpData_INV01.append(-0.00001)
  
 CordData_INV01.append(247.38)
 CordData_INV01.append(234.88)
 CordData_INV01.append(214.88)
 CordData_INV01.append(199.88)
 CordData_INV01.append(197.88)
 CordData_INV01.append(194.88)
 CordData_INV01.append(191.88)
 CordData_INV01.append(189.88)
 CordData_INV01.append(186.38)
 CordData_INV01.append(184.88)
 CordData_INV01.append(174.88)
 CordData_INV01.append(154.88)
 CordData_INV01.append(134.38)
  
   
 
##+++++++++Experimental Data for Comparison+++++++++++ 

 plt.figure(1)
 plt.plot(dispY_INV01,cordY_INV01, 'g-', label='INV01') 
 plt.plot(dispY_INV02,cordY_INV02,'r-', label='INV02')
 plt.plot(ExpData_INV02, CordData_INV02, 'm--', label='Exp_INV02')
 plt.plot(ExpData_INV01, CordData_INV01, 'b--', label='Exp_INV01')
 plt.xlabel('Displacement in m')
 plt.ylabel('Elevation in m')
 #plt.legend()
 plt.legend(loc = 'lower left')
 
 interactive(True)
 plt.show()



def plotfunction_INH(dispY_INH01, cordY_INH01, dispY_INH02, cordY_INH02): 
 

##++++++++++++++++ Experimental Data for Comparison+++++++++++++++
##++++++++++++++ Refer the Excel files +++++++++++++++++++++++++



 ExpData_INH02 = []
 CordData_INH02= []
 
 ExpData_INH01 =[]
 CordData_INH01=[]
 
 
 
 
 # The values have been assigned a negative value
 # for the plot.
 ExpData_INH01.append(-0.006)
 ExpData_INH01.append(-0.023)
 ExpData_INH01.append(-0.042)
 ExpData_INH01.append(-0.046)
 ExpData_INH01.append(-0.058)
 ExpData_INH01.append(-0.065)
 ExpData_INH01.append(-0.072)
 ExpData_INH01.append(-0.075)
 ExpData_INH01.append(-0.076)
 ExpData_INH01.append(-0.085)
 ExpData_INH01.append(-0.095)
 ExpData_INH01.append(-0.099)
 ExpData_INH01.append(-0.0996)
 ExpData_INH01.append(-0.101)
 ExpData_INH01.append(-0.103)
 ExpData_INH01.append(-0.105)
 ExpData_INH01.append(-0.106)
 ExpData_INH01.append(-0.102)
 ExpData_INH01.append(-0.082)
 ExpData_INH01.append(-0.076)
 ExpData_INH01.append(-0.047)
 
 
 CordData_INH01.append(5.87)
 CordData_INH01.append(12.37)
 CordData_INH01.append(19.37)
 CordData_INH01.append(21.37)
 CordData_INH01.append(26.87)
 CordData_INH01.append(30.87)
 CordData_INH01.append(35.37)
 CordData_INH01.append(37.37)
 CordData_INH01.append(38.87)
 CordData_INH01.append(42.87)
 CordData_INH01.append(46.87)
 CordData_INH01.append(50.87)
 CordData_INH01.append(52.87)
 CordData_INH01.append(54.87)
 CordData_INH01.append(58.87)
 CordData_INH01.append(60.87)
 CordData_INH01.append(62.87)
 CordData_INH01.append(66.87)
 CordData_INH01.append(72.87)
 CordData_INH01.append(74.87)
 CordData_INH01.append(78.87)
 
 
 
 
 # The values have been assigned a negative value
 # for the plot. (Values that were positive earlier are
 # negative now and those that were negative are positive
 # now. Be careful if the convention is being altered here)
 
 ExpData_INH02.append(-0.0017)
 ExpData_INH02.append(-0.003)
 ExpData_INH02.append(-0.009)
 ExpData_INH02.append(-0.016)
 ExpData_INH02.append(-0.0227)
 ExpData_INH02.append(-0.0233)
 ExpData_INH02.append(-0.0227)
 ExpData_INH02.append(-0.0215)
 ExpData_INH02.append(-0.0208)
 ExpData_INH02.append(-0.0205)
 ExpData_INH02.append(-0.0216)
 ExpData_INH02.append(-0.0219)
 ExpData_INH02.append(-0.0239)
 ExpData_INH02.append(-0.0243)
 ExpData_INH02.append(-0.024)
 ExpData_INH02.append(-0.0223)
 ExpData_INH02.append(-0.022)
 ExpData_INH02.append(-0.020)
 ExpData_INH02.append(-0.013)
 ExpData_INH02.append(-0.010)
 ExpData_INH02.append(-0.005)
 ExpData_INH02.append(-0.0008)
 ExpData_INH02.append(0.005)
 ExpData_INH02.append(0.007)
 ExpData_INH02.append(0.008)
 ExpData_INH02.append(0.013)
 ExpData_INH02.append(0.019)
 ExpData_INH02.append(0.023)
 ExpData_INH02.append(0.027)
 ExpData_INH02.append(0.029)
 
 
 
 CordData_INH02.append(5.91)
 CordData_INH02.append(7.41)
 CordData_INH02.append(11.41)
 CordData_INH02.append(17.41)
 CordData_INH02.append(25.41)
 CordData_INH02.append(30.41)
 CordData_INH02.append(31.91)
 CordData_INH02.append(37.41)
 CordData_INH02.append(38.91)
 CordData_INH02.append(44.41)
 CordData_INH02.append(46.41)
 CordData_INH02.append(48.41)
 CordData_INH02.append(51.91)
 CordData_INH02.append(53.91)
 CordData_INH02.append(57.41)
 CordData_INH02.append(61.41)
 CordData_INH02.append(64.91)
 CordData_INH02.append(68.91)
 CordData_INH02.append(74.41)
 CordData_INH02.append(76.41)
 CordData_INH02.append(81.91)
 CordData_INH02.append(83.91)
 CordData_INH02.append(89.41)
 CordData_INH02.append(91.41)
 CordData_INH02.append(96.91)
 CordData_INH02.append(102.41)
 CordData_INH02.append(106.41)
 CordData_INH02.append(110.41)
 CordData_INH02.append(113.91)
 CordData_INH02.append(117.41)
 
 
 ## ++++++++++++++++Experimental Data for Comparison+++++++++++++++
 
 plt.figure(2)
 plt.plot(cordY_INH01, dispY_INH01, 'g-', label='INH01') 
 plt.plot(cordY_INH02, dispY_INH02,'r-', label='INH02')
 plt.plot(CordData_INH02, ExpData_INH02, 'm--', label='Exp_INH02')
 plt.plot(CordData_INH01, ExpData_INH01, 'b--', label='Exp_INH01')
 plt.xlabel('Distance to the right from center in m')
 plt.ylabel('Displacement in m')
 #plt.legend()
 #plt.legend(loc = 'upper left')
 plt.legend(loc = 'lower right')
 
 interactive(False)
 plt.show()











## =============Call various functions======================================
## ++++++++++++++Get phase and material details+++++++++++++++++++++++++++++
## ++++++++++++++Obtain the results after solver call+++++++++++++++++++++++++++
##+++++++++++++++++ Plot the results++++++++++++++++++++++++++++++++++++
get_phasedetails()
get_soilmaterials()
update_materialParametrs()


# Call the solver. Be careful on commenting on this function
# as it may affec the functions that are being called subsequently
g_o = CallSolver()

# Vertical  displacement data
dispY_INV01, cordY_INV01, dispY_INV02, cordY_INV02  = resultsINV(g_o)  

# Horizontal dispalcement data 
dispY_INH01, cordY_INH01, dispY_INH02, cordY_INH02  = resultsINH(g_o) 												

plotfunction_INV(dispY_INV01, cordY_INV01, dispY_INV02, cordY_INV02)

plotfunction_INH(dispY_INH01, cordY_INH01, dispY_INH02, cordY_INH02)




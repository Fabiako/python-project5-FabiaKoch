#Project 5 with compressed dataset (other dataset crashed my laptop) by Fabia Koch 

#read input file
#only name of file needed in this case the 'global_data_compressed.txt file' 
data1= input('Please put in the global_data_compressed.txt file ')
data= open(data1)

#import dataframe with panda where every column is seperated by a 'comma' and every new row indicated by a '\n'

import pandas as pd
df = pd.read_csv(data, delimiter=',', lineterminator='\n', header= None)

# it is only the data right now without header -> created after with x.columns = [..]

df.columns = [ 'elevation [m]', 'local relief [m]', 'slope [° *10]','precipitation [mm/a]','temperature [°C *10]','NDVI average [0-255]','NDVI maximum [0-255]','ksn','tetrapod','amphibian','mammal', 'Köppen-Geiger Climate Zone', 'Geologic unit', 'Landcover', 'strain rate [10e-9/yr]']           

#some datapoints are at -9999 which stands for 0 
df= df.replace(-9999, 0) 

#create a scatter plot (using matplot) with specific data

import matplotlib.pyplot as plt

#specific data is extracted from file in seperated variables
#datapoints starts at 1 (0 is empty)

tetrapod = df.loc[1:,['tetrapod']]
amphibia = df.loc[1:,['amphibian']]
mammal = df.loc[1:,['mammal']]
Geological_unit = df.loc[1:,['Geologic unit']]

#scatter plot of tetrapods
fig_tetrapod= plt.figure()
plt.scatter(Geological_unit, tetrapod, color= 'orange')
plt.xlabel("Geological unit")
plt.ylabel("Number of tetrapod species")
plt.title("Tetrapod species at different geological units")
plt.show()

#save plot as figure (png) for further use 
fig_tetrapod.savefig('fig.tetrapod.png')

#scatter plot of amphibian
fig_amphibian = plt.figure()
plt.scatter(Geological_unit, amphibia, color= 'green')
plt.xlabel("Geological unit")
plt.ylabel("Number of amphibian species")
plt.title("Amphibian species at different geological units")
plt.show()

fig_amphibian.savefig('fig.amphibian.png')

#scatter plot of mammal
fig_mammal = plt.figure()
plt.scatter(Geological_unit, mammal, color= 'blue')
plt.xlabel("Geological unit")
plt.ylabel("Number of mammal species")
plt.title("Mammal species at different geological units")
plt.show()

fig_mammal.savefig('fig.mammal.png')

#scatter plot all three together
fig_all = plt.figure()
plt.scatter(Geological_unit, tetrapod, label= 'Tetrapod', color= 'orange')
plt.scatter(Geological_unit, amphibia, label= 'Amphibia', color= 'green')
plt.scatter(Geological_unit, mammal, label= 'Mammal', color= 'blue')
plt.xlabel("Geological unit")
plt.ylabel("Number of species")
plt.title("Species at different geological units")
plt.legend()
plt.show()

fig_all.savefig('fig.all.png')

print('\n Scatter plots will be saved as name.png in your folder \n')

data.close()
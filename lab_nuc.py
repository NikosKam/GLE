# -*- coding: utf-8 -*-
#"""
#Created on Thu Oct 13 15:37:57 2022

#@author: MGeront
#"""

# Nuclear Lab
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

#import csv data
#data_all = pd.read_csv('C:/Users/a-sta/OneDrive/ANEMOS/nuclear_lab/nmdb_data2.csv')
data_all = pd.read_csv(r'C:/Users/nicho/data_askhsh1.csv',delimiter=";")
data_all['date']=pd.to_datetime(data_all['date'])
dates=data_all["date"]
thul=data_all["THUL"].values
sopb=data_all["SOPB"].values
sopo=data_all["SOPO"].values

#plotting THUL station
plt.figure(num=1,dpi=120)
plt.plot(dates,thul)
plt.xticks(rotation=80)
#plt.show()

#plotting SOPB station
plt.figure(num=1,dpi=120)
plt.plot(dates,sopb)
plt.xticks(rotation=80)
#plt.show()

#plotting SOPO station
plt.figure(num=1,dpi=120)
plt.plot(dates,sopo)
plt.xticks(rotation=80)
#plt.show()

####filtering####
start_date="20-1-2005 0:00"
end_date="20-1-2005 23:59"
data_all['date']=pd.to_datetime(data_all['date'])
filtered_data=data_all.loc[(data_all['date']>start_date) & (data_all['date']<end_date) ]
dates_filtered=filtered_data['date']
thul_filtered=filtered_data['THUL'].values
sopb_filtered=filtered_data['SOPB'].values
sopo_filtered=filtered_data['SOPO'].values

#filtering THUL
plt.figure(num=2,dpi=120)
plt.plot(dates_filtered,thul_filtered)
plt.xticks(rotation=80)
plt.grid()
plt.show()

#filtering SOPB
plt.figure(num=2,dpi=120)
plt.plot(dates_filtered,sopb_filtered)
plt.xticks(rotation=80)
plt.grid()
plt.show()

#filtering SOPO
plt.figure(num=2,dpi=120)
plt.plot(dates_filtered,sopo_filtered)
plt.xticks(rotation=80)
plt.grid()
plt.show()


#selection for mean value
selection_start="20/1/2005 0:00"
selection_end="20/1/2005 23:59"
nmdb_sel=filtered_data.loc[(filtered_data['date']>selection_start) & (filtered_data['date']<selection_end) ]
thul_selected=nmdb_sel["THUL"].values
sopb_selected=nmdb_sel["SOPB"].values
sopo_selected=nmdb_sel["SOPO"].values

#mean_val=np.mean(thul_selected)
#results=(thul_filtered-mean_val)/mean_val

results_thul=(thul_filtered-np.mean(thul_selected))/np.mean(thul_selected)
results_sopb=(sopb_filtered-np.mean(sopb_selected))/np.mean(sopb_selected)
results_sopo=(sopo_filtered-np.mean(sopo_selected))/np.mean(sopo_selected)

#plotting THUL station filtered
plt.figure(num=3,dpi=120)
plt.title("GLE 69")
plt.plot(dates_filtered,results_thul)
plt.xlabel("date")
plt.ylabel("platos")
plt.xticks(rotation=80)
plt.grid()
plt.show()

#plotting SOPB station filtered
#plt.figure(num=3,dpi=120)
#plt.title("GLE 69")
#plt.plot(dates_filtered,results_sopb)
#plt.xlabel("date")
#plt.ylabel("platos")
#plt.xticks(rotation=80)
#plt.grid()
#plt.show()

#plotting SOPO station filtered
#plt.figure(num=3,dpi=120)
#plt.title("GLE 69")
#plt.plot(dates_filtered,results_sopo)
#plt.xlabel("date")
#plt.ylabel("platos")
#plt.xticks(rotation=80)
#plt.grid()
#plt.show()
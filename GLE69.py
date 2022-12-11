import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

#import csv data
data_CALG = pd.read_csv(r'C:\Users\nicho\OneDrive\Έγγραφα\Φυσικό Αθήνας\Εργαστήριο Κατεύθυνσης\Άσκηση 1\CALG.csv',delimiter=";")
data_ROME = pd.read_csv(r'C:\Users\nicho\OneDrive\Έγγραφα\Φυσικό Αθήνας\Εργαστήριο Κατεύθυνσης\Άσκηση 1\ROME.csv',delimiter=";")
data_INVK = pd.read_csv(r'C:\Users\nicho\OneDrive\Έγγραφα\Φυσικό Αθήνας\Εργαστήριο Κατεύθυνσης\Άσκηση 1\INVK.csv',delimiter=";")
data_THUL = pd.read_csv(r'C:\Users\nicho\OneDrive\Έγγραφα\Φυσικό Αθήνας\Εργαστήριο Κατεύθυνσης\Άσκηση 1\THUL.csv',delimiter=";")
data_SOPO = pd.read_csv(r'C:\Users\nicho\OneDrive\Έγγραφα\Φυσικό Αθήνας\Εργαστήριο Κατεύθυνσης\Άσκηση 1\SOPO.csv',delimiter=";")
data_TERA = pd.read_csv(r'C:\Users\nicho\OneDrive\Έγγραφα\Φυσικό Αθήνας\Εργαστήριο Κατεύθυνσης\Άσκηση 1\TERA.csv',delimiter=";")

data_CALG['date']=pd.to_datetime(data_CALG['date'])
data_THUL['date']=pd.to_datetime(data_THUL['date'])
data_SOPO['date']=pd.to_datetime(data_SOPO['date'])    
data_TERA['date']=pd.to_datetime(data_TERA['date'])
data_ROME['date']=pd.to_datetime(data_ROME['date'])
data_INVK['date']=pd.to_datetime(data_INVK['date'])

#plotting CALG station
plt.figure(num=1,dpi=120)
plt.plot(data_CALG['date'].values,data_CALG['CALG'].values)
plt.xticks(rotation=80)
plt.savefig("CALG.pdf")
plt.show()
    
#plotting THUL station
plt.figure(num=1,dpi=120)
plt.plot(data_THUL['date'].values,data_THUL['THUL'].values)
plt.xticks(rotation=80)
plt.savefig("THUL.pdf")
plt.show()
    
#plotting SOPO station
plt.figure(num=1,dpi=120)
plt.plot(data_SOPO['date'].values,data_SOPO['SOPO'].values)
plt.xticks(rotation=80)
plt.savefig("SOPO.pdf")
plt.show()
    
#plotting TERA station
plt.figure(num=1,dpi=120)
plt.plot(data_TERA['date'].values,data_TERA['TERA'].values)
plt.xticks(rotation=80)
plt.savefig("TERA.pdf")
plt.show()
    
#plotting ROME station
plt.figure(num=1,dpi=120)
plt.plot(data_ROME['date'].values,data_ROME['ROME'].values)
plt.xticks(rotation=80)
plt.savefig("ROME.pdf")
plt.show()
    
#plotting INVK station
plt.figure(num=1,dpi=120)
plt.plot(data_INVK['date'].values,data_INVK['INVK'].values)
plt.xticks(rotation=80)
plt.savefig("INVK.pdf")
plt.show()

####filtering####
results_calg=(data_CALG['CALG'].values-np.mean(data_CALG['CALG'].values))/np.mean(data_CALG['CALG'].values)
results_tera=(data_TERA['TERA'].values-np.mean(data_TERA['TERA'].values))/np.mean(data_TERA['TERA'].values)
results_sopo=(data_SOPO['SOPO'].values-np.mean(data_SOPO['SOPO'].values))/np.mean(data_SOPO['SOPO'].values)
results_thul=(data_THUL['THUL'].values-np.mean(data_THUL['THUL'].values))/np.mean(data_THUL['THUL'].values)
results_rome=(data_ROME['ROME'].values-np.mean(data_ROME['ROME'].values))/np.mean(data_ROME['ROME'].values)
results_invk=(data_INVK['INVK'].values-np.mean(data_INVK['INVK'].values))/np.mean(data_INVK['INVK'].values)
    
#plotting CALG station
plt.figure(num=1,dpi=120)
plt.title("GLE 69 CALG")
plt.plot(data_CALG['date'].values,results_calg)
plt.xlabel("date")
plt.ylabel("platos")
plt.xticks(rotation=80)
plt.grid()
plt.savefig("CALG_filtered.pdf")
plt.show()
    
#plotting THUL station
plt.figure(num=1,dpi=120)
plt.title("GLE 69 THUL")
plt.plot(data_THUL['date'].values,results_thul)    
plt.xlabel("date")
plt.ylabel("platos")
plt.xticks(rotation=80)
plt.grid()
plt.savefig("THUL_filtered.pdf")
plt.show()
    
#plotting SOPO station
plt.figure(num=1,dpi=120)
plt.title("GLE 69 SOPO")
plt.plot(data_SOPO['date'].values,results_sopo)
plt.xlabel("date")
plt.ylabel("platos")
plt.xticks(rotation=80)
plt.grid()
plt.savefig("SOPO_filtered.pdf")
plt.show()
    
#plotting TERA station
plt.figure(num=1,dpi=120)
plt.title("GLE 69 TERA")
plt.plot(data_TERA['date'].values,results_tera)
plt.xlabel("date")
plt.ylabel("platos")
plt.xticks(rotation=80)
plt.grid()
plt.savefig("TERA_filtered.pdf")
plt.show()
    
#plotting ROME station
plt.figure(num=1,dpi=120)
plt.title("GLE 69 ROME")    
plt.plot(data_ROME['date'].values,results_rome)
plt.xlabel("date")
plt.ylabel("platos")
plt.xticks(rotation=80)
plt.grid()
plt.savefig("ROME_filtered.pdf")
plt.show()
    
#plotting INVK station
plt.figure(num=1,dpi=120)
plt.title("GLE 69 INVK")
plt.plot(data_INVK['date'].values,results_invk)
plt.xlabel("date")
plt.ylabel("platos")
plt.xticks(rotation=80)
plt.grid()
plt.savefig("INVK_filtered.pdf")
plt.show()
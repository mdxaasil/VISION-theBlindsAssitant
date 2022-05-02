

import pickle
f=open(r"F:\Cs project\data\fav.dat","wb")

l1=[['1','aasil','aasil2003@gmail.com'],['2','harish','harish@gmail.com']]

pickle.dump(l1,f)
f.close()


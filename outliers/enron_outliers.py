#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

from operator import itemgetter
l = sorted(data, key=itemgetter(0), reverse=True)
print (l);
#l = sorted(data_dict.items(), key=lambda (k, v): v['salary'], reverse=True)[:100]
#for p in l:
#    print(p[0] +":"+ str(p[1]['salary']))
#print(sorted( enron_data.items(), key=itemgetter('total_payments')))


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

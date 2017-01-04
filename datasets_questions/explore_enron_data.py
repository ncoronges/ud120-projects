#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import operator

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print ("total people: ",len(enron_data))
print ("num features: ",len(enron_data["SKILLING JEFFREY K"]))
print ("num poi: ", sum([1 for p in enron_data if enron_data[p]["poi"] == True]))
print ("James Prentice: ", enron_data["Prentice James".upper()])
print ("Wesley Colwell to poi emails : ", enron_data["Colwell Wesley".upper()]["from_this_person_to_poi"])
print (" Jeffrey K Skilling options exercised : ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print (type(enron_data))
print (type(enron_data["SKILLING JEFFREY K"]))
l = sorted(enron_data.items(), key=lambda (k, v): v['total_payments'], reverse=True)[:100]
#for p in l:
#    print(p[0] +":"+ str(p[1]['total_payments']))
#print(sorted( enron_data.items(), key=itemgetter('total_payments')))

print ("num with salary: ", sum([1 for p in enron_data if enron_data[p]["salary"] != "NaN"]))
print ("num with email: ", sum([1 for p in enron_data if enron_data[p]["email_address"] != "NaN"]))
print ("num without payment info: ", sum([1 for p in enron_data if enron_data[p]["total_payments"] == "NaN"]))
print ("num poi without payment info: ", sum([1 for p in enron_data if enron_data[p]["total_payments"] == "NaN" and enron_data[p]["poi"]==True]))

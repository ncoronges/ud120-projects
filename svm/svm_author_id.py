#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# 1% slide
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###

#########################################################

from sklearn.svm import SVC
clf = SVC(C=10000.0, kernel="rbf", verbose=True)

print ("start train")
t0 = time()
clf.fit(features_train,labels_train)
print ("training time:", round(time()-t0, 3), "s")

t0 = time()
y_pred = clf.predict(features_test)
print ("predict time:", round(time()-t0, 3), "s")
print (y_pred[10], y_pred[26], y_pred[50])
num_chris = sum([1 for x in y_pred if x > 0])
print ("num chris: ",num_chris)

#Accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, y_pred)

print (accuracy)

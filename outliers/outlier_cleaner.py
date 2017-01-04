#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    print("** cleaning data **")


    for i, v in enumerate(predictions):
        age = ages[i][0]
        net_worth = net_worths[i][0]
        error = net_worth - v[0]
        #print ("age:",age)
        cleaned_data.append((age, net_worth, error))

    cleaned_data = sorted(cleaned_data, key=lambda tup: abs(tup[2]))[:81]
    #print ("sorted:", l)

    return cleaned_data


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header= None)

# creating a list of lists for input to apriori

transactions = []
for i in range(0,7501):
	transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

print transactions	


# min 2 products in basket
# min_support = 3*7/7500
from apyori import apriori
rules = apriori(transactions, min_support= 0.003, min_confidence= 0.2, min_lift= 3, min_length = 2) 

# visualising the results
results = list(rules)
print results[0]
print results[0][2]

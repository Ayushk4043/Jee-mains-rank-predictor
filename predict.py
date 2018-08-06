import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def Mains(marks):
	jee_18 = pd.read_csv('Jee_main_2k18.csv')
	X = jee_18.iloc[:, 0:1].values
	y = jee_18.iloc[:, 1:2].values
	# Importing the JEE Main 2017 Dataset
	jee_17 = pd.read_csv('Jee_main_2k17.csv')
	A = jee_17.iloc[:, 0:1].values
	b = jee_17.iloc[:, 1:2].values
	regressor1 = RandomForestRegressor(n_estimators = 500, random_state = 130)
	regressor1.fit(X, y)
	regressor2 = RandomForestRegressor(n_estimators = 200, random_state = 0)
	regressor2.fit(A, b)
	s = regressor1.predict(marks)
	t = regressor2.predict(marks)
	avg = int((s+t)/2)
	max_avg = avg + 1000
	min_avg = avg - 1000
	if min_avg < 1502 :
		min_avg = 1
		max_avg = avg + 300

	print("Your rank between ",max_avg," and ",min_avg)





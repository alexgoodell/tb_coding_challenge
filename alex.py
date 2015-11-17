import pandas as pd
import random as random

# create map for state names
converter = [0] * 3
converter[0] = "Uninfected"
converter[1] = "LTBI"
converter[2] = "Active TB"

# create old state -> new state function
def get_new_state(old_state):
	new_state = 0
	if old_state == 0 and random.randint(1, 100) == 1:
		new_state = 1
	elif old_state == 1 and random.randint(1, 100) == 1:
		new_state = 2
	elif old_state == 2:
		new_state = 1
	else:
		new_state = old_state
	return new_state

# create list of people in states
people_states = [0] * 900 + [1] * 90 + [2] * 10 

# create dataframe with people's states as rows and years as columns
df = pd.DataFrame(columns=range(0,20))

# add people to column 0
df = df.append(people_states)

# for each person, determine next state
for year in range(0,20):
	for person in range(0,1000):
		df.loc[person, year+1] = get_new_state(df.loc[person, year])

# put in csv
df.to_csv("results.csv")
"""
File: .py
Author: AlexString
Description:
Algorithm that simply implements the knapsack problem with maximum and minimum weight criterion.
"""

def KnapSack_Min_weight(KW, it_w, it_v, method='max'):
	"""
	Parameters:
		KW: Knapsack maxweight 
		it_w: items weight 
		it_v: items values
		it_n: number of total items in list
		method: 'max', 'min'
	"""
	# Checking if length is correct
	if (len(it_w) != len(it_v)):
		print("Error: Discrepancy between items weight length and items values length, does not match.")
		return

	it_n = len(it_w)	

	# Defining max/min method.
	if ( method == 'max' ):
		discarder = -1
		knapSackCriterion = max
	elif ( method == 'min' ):
		discarder = max(it_w) + 1000
		knapSackCriterion = min
	else:
		print("Error in KnapSackMethod: invalid method input.")
		return

	dummy_array = [0] * it_n # Creating an array of it_n length filled with 0's
	dummy_weightArray = list(it_w) # Using a copy of the it_w array

	current_weight = 0
	minimum_weight_list = [] # Final array

	# [ KnapSack alorithm ]
	while( current_weight < KW ):
		actual_min_value = knapSackCriterion(dummy_weightArray) # Using criterion to evaluate KnapSack algorithm
		actual_min_value_position = dummy_weightArray.index(actual_min_value) # Getting value position

		minimum_weight_list.append(actual_min_value) # Adding it to array
		dummy_weightArray[actual_min_value_position] = discarder # Discard that value
		
		# If the current weight + the next calculated item is still less than the KnapSack weight:
		if ( (current_weight + it_w[actual_min_value_position]) <= KW):
			current_weight += it_w[actual_min_value_position]
			dummy_array[actual_min_value_position] = 1
		else:
			break

	# Finished algorithm - Now printing results
	total_value = 0
	items_grabbed = list()

	for i in range(len(dummy_array)): # Getting data from auxiliar dummy_array
		if ( dummy_array[i] != 0 ):
			items_grabbed.append(it_v[i])
			total_value += it_v[i]

	print("Grabbed values are:")
	print(items_grabbed)

	print("Calculated minimum weight list:")
	print(minimum_weight_list)

	print("Total weight is: " + str(current_weight))
	print("Value items sumatory is: " + str(total_value))


def Main():
	# VALUES HERE
	knapSack_MaximumWeight = 100
	items_weight = [10,20,30,40,50] 
	items_values = [20,30,66,40,60] 

	# Printing items data
	print("Items weight:")
	print(items_weight)

	print("Items values:")
	print(items_values)

	print("\n\n")

	KnapSack_Min_weight(knapSack_MaximumWeight,
		items_weight, 
		items_values, 
		"min")

Main()
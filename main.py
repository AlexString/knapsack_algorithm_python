"""
File: .py
Author: AlexString
Description:
Algorithm that simply implements the knapsack problem with maximum and minimum weight criterion.
"""

def KnapSack(KW, it_w, it_v, method='max'):
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
		print("Error in KnapSack function: Discrepancy between items weight length and items values length, does not match.")
		return

	it_n = len(it_w)	

	# Defining max/min method to KnapSackCriterion.
	if ( method == 'max' ):
		message = "maximum"
		discarder = -1
		knapSackCriterion = max
	elif ( method == 'min' ):
		message = "minimum"
		discarder = max(it_w) + 1000
		knapSackCriterion = min
	else:
		print("Error in KnapSack function: invalid method input.")
		return

	dummy_array = [0] * it_n # Creating an array of it_n length filled with 0's
	dummy_weightArray = list(it_w) # Using a copy of the it_w array

	current_weight = 0
	final_weight_values_list = list() # Final values will end in this list

	# [ KnapSack alorithm ]
	while( current_weight < KW ):
		actual_value = knapSackCriterion(dummy_weightArray) # Using criterion from KnapSack algorithm
		actual_value_position = dummy_weightArray.index(actual_value) # Getting value position

		# If the current weight + the next calculated item is still less than the KnapSack weight:
		if ( (current_weight + it_w[actual_value_position]) <= KW):
			current_weight += it_w[actual_value_position]
			dummy_array[actual_value_position] = 1
		else:
			break
		
		final_weight_values_list.append(actual_value) # Adding it to array
		dummy_weightArray[actual_value_position] = discarder # Discard that value

	# Finished algorithm - Now printing results
	total_value = 0
	items_grabbed = list()

	for i in range(len(dummy_array)): # Getting data from auxiliar dummy_array
		if ( dummy_array[i] != 0 ):
			items_grabbed.append(it_v[i])
			total_value += it_v[i]

	print("Grabbed values are:")
	print(items_grabbed)

	print("Calculated " + message + " weight list:")
	print(final_weight_values_list)

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

	KnapSack(knapSack_MaximumWeight,
		items_weight, 
		items_values, 
		"max")

if __name__ == 'main':
    Main()
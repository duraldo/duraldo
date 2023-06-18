#practice solution with notes from Tuples video.
def skip_elements(elements):
	result = []   #Code starts here, defining the new list as 'result, using the brackets'.
	for index, word in enumerate (elements):   #iterate over index & element of given list
	   if index % 2 == 0:   #checks odd/even, if the index (Modulus operators are hard for me to grasp,  but index is a variable, x. So, X/2 == 0 right, and 0 is where the index starts, not 1, this is how it checks for odd/even, correct me I am wrong here).
	      result.append(word)  #is word the paremeter? (yes, took me foreeverto figure this out)
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach'] because the goal is to skip the even "elements"

#prints out the desired results, green answer!

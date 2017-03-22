def binary_search(key,array, lmin, umax):
    if umax < lmin:
        return -1
    else:
        midpoint = int((lmin + umax)/2)

    if array[midpoint] < key:
        return binary_search(key, array, midpoint + 1,umax)
    elif array[midpoint] > key:
        return binary_search(key, array, lmin, midpoint - 1)
    else:
        return midpoint

# testing... 

test_array = ["Aadvark", "Badger","Cat","Dog","Eagle","Frog","Gecko",
              "Honey Badger","Iguana","Jackal","Kid","Llama","Monkey",
              "Narwhal","Ostrich","Penguin","Quail","Rhinocereos","Snake",
              "Tapir","Upupa","Viper","Whale","Xenon","Yellow Mongoose","Zebra"]
test_cases = ["Viper","Buffalo","Hedgehog","Jackal","Kid","Seahorse","Penguin"]
##test_cases = ["jackal"]


for case in test_cases:
    position = binary_search(case, test_array, 0, len(test_array) - 1) + 1
    if position > 0:
        print(case, "found at position", position)
    else:
        print(case, "not found")
    

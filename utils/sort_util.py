import json

# array_object = {
#     "array" : [],
#     "sorted_array": [],
#     "iter_loc": 0,
#     "current" : 0,
#     "swap": [0],
#     "sorted": False
# }

#Function to perform 1 single sort step
def sort_one(array_object, sortType):
    
    print("inside sort one")
    print(json.dumps(array_object))

    #All elements already sorted
    if len(array_object['sorted_array']) == len(array_object['array'])  or array_object['sorted'] == True:
        print("array has been completly sorted")
        array_object['sorted'] = True
        return array_object
    #Perform 1 single swap
    elif array_object['swap'] :
        x, y = array_object['swap'][0], array_object['swap'][1]
        print("swapping locations " +str(x)+ ", "+str(y))
        array_object['array'][x], array_object['array'][y] = array_object['array'][y], array_object['array'][x]
        array_object['swap'] = None
        return array_object

    if sortType == "1":
        print("Bubble sort..")
        bubblesort_one(array_object)


    return array_object

#One step in bubble sort
def bubblesort_one(array_object):
    
    current = array_object['current']
    iter_loc = array_object['iter_loc']
    outer = len(array_object['array'])-1-iter_loc
    array = array_object['array']
    
    print("Current iteration details : ")
    print("outer loc :" +str(outer))
    print("current loc :" +str(current))

    if current >= outer:
        print("iteration over.. marking last element sorted and.. resetting current to 0 and outer to "+str(outer-1))
        array_object['sorted_array'].append(current)
        current = 0
        outer = outer-1
        array_object['current']=0
        array_object['iter_loc']+=1

    
    if outer <=0:
        print("All iterations over.. marking array as sorted")
        array_object['sorted'] = True
        return array_object

    if array[current] > array[current+1]:
        print("Marking elements for swap")
        array_object['swap'] = []
        array_object['swap'].extend([current,current+1])
    
    array_object['current']+=1
    return array_object

    
    
    
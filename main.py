values = [100, 30, 40, 500]
weights = [10, 3, 20, 50]
capacity = 40
n = len(values)

def backpack(values, weights, capacity, n):
   
    # base case: no items left or no remaining capacity 
    if n == 0 or capacity == 0:
        return 0

    # skip current item if it doesn't fit
    if weights[n-1] > capacity:
        return backpack(values, weights, capacity, n-1)

    # recursive call: try both posibilities
    else:
        
        # case 1: include current item
        include = values[n-1] + backpack(values, weights, capacity - weights[n-1], n-1)

        # case 2: exclude current item (explore other combinations) 
        exclude = backpack(values, weights, capacity, n-1)

        # return better option
        return max(include, exclude)


print(backpack(values, weights, capacity, n))

# Chapter 7 final review code
# 1/21/2025

def main():
    # my_list = [47, 8, 71, 70, 14, 22]
    # by_seven_list = [item for item in my_list if item % 7 == 0 ]
    # by_seven_list = [item if item % 7 == 0 else 0 for item in my_list ]
    # by_seven_list = [item for item in my_list if item % 7 == 0 if item == 70]
    # print(by_seven_list)

    # create our 2d list
    matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

    sum = 0
    row = 0
    
    # assume all lists have the same number of elements
    for num in range(len(matrix[0])): # cols
        total = 0
        for aList in matrix: # access element in row
            total += aList[num]
        print(total)

    
    # for x in matrix: # for each row
    #     for y in x[row:]:  # for each element in the row
    #         sum += y
    #         break; # get out after we read the first element
    #     row += 1
    # print(sum)

    # our tuple to play around
    tpl = (10, 20, [33, 24, 18])
    print(len(tpl))
    print(tpl[0])

    #tpl[0] = 100 cannot do with tuple
    #tpl.append(100) also cannot do 

    # Get reference to list
    theList = tpl[2]
    print(theList)
    # we can update the list values
    theList[0] = 77

    # or can get by using nested list syntax
    tpl[2][0] = 77 
    tpl[2].append(100)
    print(tpl)

    # create two new tuples
    tpl1 = (10, 32, 43, 78, 101)
    tpl2 = (34, 56, 67, 123, 6)

    # call our comparison function
    print(find_diff(tpl1, tpl2))
    return

def find_diff(one, two):
    return max(one) - max(two)

if __name__ == '__main__':
    main()

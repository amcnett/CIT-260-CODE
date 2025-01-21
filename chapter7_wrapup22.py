# Chapter 7 final review code
# 1/21/2025

def main():
    my_list = [47, 8, 71, 70, 14, 22]
    div_by_seven = [item for item in my_list if item % 7 == 0]
    #div_by_seven = [item % 7 == 0 for item in my_list if item % 7 == 0]
    div_by_seven = [item for item in my_list if item % 7 == 0 if item % 10 == 0] 
    div_by_seven = [item if item % 7 == 0 else 0 for item in my_list]
    print(div_by_seven)
    
    matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

    print(matrix[1:])
    # sum = 0
    # for alist in matrix: # each list 
    #     for item in alist: # each item in the list
    #         sum += item
    asum = 0
    for alist in matrix: # each list  
            asum += sum(alist)

    print(asum)

    matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

    sum1 = 0
    sum2 = 0
    sum3 = 0
    for list in matrix:  # get me each row/list in matrix
         sum1 += list[0]
         sum2 += list[1]
         sum3 += list[2]
    print(sum1, sum2, sum3)


    # need to use list comprehension instead for slicing with both rows
    # and columns
    print(matrix[1:])

    new_list = [item[:2] for item in matrix[1:]]
    print(new_list)

    #cannot create tuple like this
    #tpl = (1) # thinks it is just an int... Python is confused
    tpl = (1,) # need to do this instead

    tpl = (1, 2, 100, [12, 14, 23])
    print(tpl[0])
    #tpl[0] = 100 # this not allowed
    #tpl.append(100) # this is also not allowed

    # but we can modify the list
    alist = tpl[3]
    alist[0] = 0
    print(tpl) #worked!
  
if __name__ == '__main__':
    main()

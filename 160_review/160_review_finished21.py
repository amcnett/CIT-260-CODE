'''
CIT160 REVIEW, Activity 0
'''

def main():
    #call get_principle_investment
    print(get_principle_investment(rate=0.5, future_value=10000))

    #call stairs
    stairs()

    #call print_c_to_f
    print_c_to_f()

    #call print_average_from_file
    print(print_average_from_file())

    courses = ["CIT160", "CIT260", "CIT360"]
    print(courses)
    print(courses[0])
    courses.append("EET145")
    print(courses)
    courses[-1] = "EET247"
    print(courses)
    print(courses[1::2])
    # print(courses[7])  # throws index error exception

    for item in courses:
        print(item)

    list1 = [1, 2, 3, 4]

    list2 = [item + 1 for item in list1]   #[]
    print(list2)

    #for item in list1:

    #    list2.append(item + 1)


    return


'''
# 1
'''


def get_principle_investment(*, future_value=0, rate=0.01, years=1):
    #put your arithmetic here
    return future_value/(1+rate)**years
    return 


'''
# 2
'''


def stairs():
    #write your stairs code here
    for stair in range(6):
        print("#", end="")
        for _ in range(stair):
            print(" ", end="")
        print("#")
    return


'''
# 3
'''


def print_c_to_f():
    #Write the C to F conversion here
    #celcius = range(21)
    for n in range(21): #celcius: # [0, 1, 2, 3, ... ,20]
        fahren = (9/5)*n + 32
        print(f"{n} <-> {fahren:.1f}")
    return


'''
#4
'''


def print_average_from_file():
  #Write your code to open and calculate the average of the values in the file
    average = 0
    try:
        with open("160_review_data.txt", "r") as rfile:
            total = 0
            count = 0
            for x in rfile:
                print(x)
                x = float(x)
                total += x
                count += 1
            average = total / count
    except FileNotFoundError:
        print ("Error: file not found")
    return average


if __name__ == '__main__':
    main()
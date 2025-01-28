'''
CIT160 REVIEW, Activity 0
'''

def main():
    #call get_principle_investment
    print(get_principle_investment(rate=0.05, years=10, future_value=20000))
    #call stairs
    stairs()
    #call print_c_to_f
    print_c_to_f()
    #call print_average_from_file
    print_average_from_file()

    courses = ["CIT160", "CIT260", "CIT360"]
    print(courses)

    courses.append("EET145")
    print(courses)

    courses[3] = "EET247"
    print(courses)

    for course in courses[:2]: # assumes 0 for first
        print(course)
    
    
    courses.append("CIT180")
    courses.append("CIT230")
    print(courses)
    for course in courses[::2]:  # print every other course
        print(course)

    courses[-1]  # gets value at the end of the list
    return


'''
# 1
'''


def get_principle_investment(*, future_value=0, rate=0.01, years=1):
    #put your arithmetic here
    needed = future_value/(1+rate)**years
    return needed


'''
# 2
'''


def stairs():
    #write your stairs code here
    # counter = 0
    # while counter < 6:
    #     space = ""
    #     for spaces in range(counter):
    #         space += " "
    #     print("#" + space + "#")
    #     counter += 1

    for i in range(6):
        print("#" + " " * i + "#")

    return


'''
# 3
'''


def print_c_to_f():
    #Write the C to F conversion here
    for c in range(0, 21):
        print(c, end=": ")
        f = ((9/5)*c)+32
        print(f"{f:.2f}")
    return


'''
#4
'''


def print_average_from_file():
  #Write your code to open and calculate the average of the values in the file
    try:
        sum = 0
        count = 0
        with open(r"160_review_data.txt", "r") as review:
            for line in review:
                newline = line.strip()
                linenum = float(newline)
                sum += linenum
                count +=1
        average = sum/count
        print(f"{average:.2f}")
    
    except Exception:
        print("Error in code")
        
    return 


if __name__ == '__main__':
    main()
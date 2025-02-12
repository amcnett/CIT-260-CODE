import re

# 1. 6 letter words that end with “ly” with no other data allowed
# Really is okay, so is really, or REALLY
test_string = "really"
# [a-z] \w
matches = re.findall(r"^[a-z]{4}ly$", test_string.lower())
print(matches)

# 2. Prescription number: 3 letters x, j, or k followed by 6 numbers with no 
# other data allowed
# x123456 is okay, so is J123456
# \d instead of [0-9]
test_string = "j123946"
matches = re.findall(r"^[xjk]\d{6}$", test_string.lower())
print(matches)

# 3. Match number 0 – 99 with no other data allowed
# 5 is okay, so is 05
#\d?\d
test_string = "900"
matches = re.findall(r"^([0-9][0-9])|([0-9])$", test_string)
print(matches)

# 4. IP Address (v4) with no other data allowed
# 4 triplets ranging from 0-255 separated by “.”
# 12.2.1.23 is okay, but 12.02.01.23 is not
test_string = "127.0.0.1"
matches = re.findall(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", test_string)
print(matches)


courses = {
    "CIT160": 12,
    "CIT180": 20,
    "EET145": 16
}
print(courses)

#courses = {}
courses["CIT160"] = 100
print(courses)
print(courses["CIT160"])

for key in courses:
    print(key)

print(courses.keys())

for key, value in courses.items():
    print(key, " ", value)

#print(courses["CIT260"])  # throws error
print(courses.get("CIT260"))
print(courses.get("CIT260", 0))

del courses["CIT160"]
print(courses)
print(len(courses))

late_courses = {
    "EET247": 20,
    "CSC124": 30,
    "CIT180": 200
}

#all_courses = courses | late_courses
courses |= late_courses
print(courses)

del courses["EET145"]
print(courses)

#courses.clear()
#print(courses)

#large_classes = {item:courses[item] for item in courses if courses[item] > 20}
large_classes = {k:v for k,v in courses.items() if v > 20}
print(large_classes)

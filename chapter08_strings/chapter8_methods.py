# Explore the wonderful world of string methods!

# input validation
# check type before casting!
# What is someone's age in dog years
age = input("Enter your age: ")
if age.isdigit():
    dog_age = int(age) * 7
    print("The dog age is ", dog_age)
else:
    print("This is not a valid age")

# input validation -- consider use of upper() or lower()
# remove leading or trailing whitespace
# have someone state Y or N (perform input validation)
response = input("Please enter Y or N: ")
response = response.upper().strip()
while response != "Y" and response != "N":
    response = input("Please enter Y or N: ")

# update date formats
# replace() can be used to update - in date with /
adate = "1-28-2025"
adate = adate.replace("-" , "/")
print(adate)

# cross site scripting removal
# Is called sanitizing input
# remove harmful < and > with &gt; and &lt; (in one line) with replace()
# Example <script>alert('Hello')</script>
reply = '''<script>alert('Hello')</script>'''
reply = reply.replace("<", "&lt;").replace(">", "&gt;")
print(reply)

# file validation
# did they give us the right file type
# check extension with endswith()
filename = input("Give me a .csv file: ")
if not filename.endswith(".csv"):
    print("this is not a CSV")
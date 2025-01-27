import hashlib

'''
To use this file
1. import this into your file
2. call the appropriate method for the CASE and the STEP and provide the string
    a. for the last step, send the first english word to the proper function
'''

def case_one_step_zero(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "aab4f403fcbc9f702fe04bcbf37c3e0d"

def case_one_step_one(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "bbe236e220f76657a59fcebbd5c565e5"

def case_one_step_two(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "1df06ba2809b448acb5dee2e60a9237c"

def case_one_step_three(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "8b94c294983ad968eb3c8266c4bf3893"

def case_one_step_four(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "696046ae19e080f7a0b7a49a9b86cfb3"

def case_one_step_five(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "5b42bec30d7d1c39bdc163e61c271c5d"

def case_one_step_six(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "6435dc6338167ffdeb5cfff735f25dab"

def case_one_step_seven_first_word(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "e5d7cffe25654f7e3a1e334118c71549"

def case_two_step_zero(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == '62bdc6fc9d5d2244c98b0ec85fd78bfc'

def case_two_step_one(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "98c540c69a43a6377000eabc424e6024"

def case_two_step_two(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "6265940a441899ee0e5cf88c856c426c"

def case_two_step_three(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "0654ecbc6f3e269d7ce0af23c25c8920"

def case_two_step_four(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "61fea6533416b0a896be1aeab60d16ca"

def case_two_step_five(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "6d432f5170c08af31a56f21d683bb6a8"

def case_two_step_six(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "86aea98ded3c391069c13c3fcba7af88"

def case_two_step_seven_first_word(word : str) -> bool:
    return hashlib.md5(word.encode()).hexdigest() == "70068080f13c92cc4ef2d1ed3f5218f4"
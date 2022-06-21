#Password generator
#Create a random alphanumeric string of length ten that must contain at least four digits. For example, the output can be anything like 1
import random
import string
digits = string.digits
letter_digit_list = list(string.digits + string.ascii_letters)
# shuffle random source of letters and digits
random.shuffle(letter_digit_list)

#first generate 4 random digits
sample_str = ''.join((random.choice(digits) for i in range (4)))

# Now create random string of length 6 which is a combination of letters and digits
# Next, concatenate it with sample_str
sample_str += ''.join((random.choice(letter_digit_list) for i in range (6)))
aList = list(sample_str)
random.shuffle(aList)

final_str = ''.join(aList)
print("Random String:", final_str)
# Output ~ 810YQ6D430
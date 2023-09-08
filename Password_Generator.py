#password generator using only RANDOM & STRING module
import random
import string

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

length = int(input("Enter length of the password: "))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)
password1 = "".join(s[0:length])
print(f"Your password is {password1}")

password2 = "".join(random.sample(s,length))
print(f"Your password is {password2}")




# #password generator using only RANDOM module
# import random
# password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+`?><,./;;"
# length = int(input("Enter the length of the password: "))
# if length > len(password):
#     print(f"Length of the password must be lessthan equal to {len(password)}")
# else:
#     p = "".join(random.sample(password,length))
#     print(f"Your password is {p}")
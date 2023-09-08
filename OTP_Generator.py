#OTP generator using RANDOM module
import random
lt = ["0","1","2","3","4","5","6","7","8","9"]
otp = "".join(random.sample(lt,6))
print("One Time Password(OTP):",otp)

import math, random 
def OTPgenerator():
	digits="0123456789"
	OTP=""
	for i in range(6): 
		OTP+=digits[math.floor(random.random()*10)] 
	return OTP 

# Main function 
print("Your six digit OTP is: ",OTPgenerator()) 	

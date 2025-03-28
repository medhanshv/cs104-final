message = "1"
str = ""

def func(message="hello"):
	message+="Bye. "
	message+="From the function. "
	return message

message += func("Calling ")
print("this is printed")
print(message)

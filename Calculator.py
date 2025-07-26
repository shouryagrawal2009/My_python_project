# My first calculator of two numbers
while True:
	 first_number = float(input("Enter first number :   "))
	 second_number = float(input("Enter second number:     "))
	 operation = input("Enter operation   ")
	 if (operation =="+")  :
	      sum = first_number + second_number
	      print("The answer is :", sum)
	 elif (operation =="-") :
          sum= first_number - second_number
          print("The answer is :", sum)
	 elif (operation == ">" and ">="):
	 	sum = first_number >= second_number
	 	print("The answer is :", sum)
	 elif (operation == "<" or "<="):
	 	sum = first_number <= second_number
	 	print("The answer is :", sum)
	 elif (operation == "**"):
	 	sum = first_number ** second_number
	 	print("The answer is :", sum)
	 elif (operation == "//"):
	 	sum = first_number // second_number
	 	print("The answer is :", sum)
	 elif (operation =="%") :
	 	sum = first_number % second_number
	 	print("The answer is :", sum)
	 elif (operation =="/") :
	 	sum = first_number / second_number
	 	print("The answer is :", sum)
	 elif (operation =="*") :
	 	sum = first_number * second_number
	 	print("The answer is :", sum)
	 else :
	 	print("Invalid operation")

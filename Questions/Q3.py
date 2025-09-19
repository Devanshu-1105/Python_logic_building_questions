# question here
Question = """Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers."""
 #swed
# #taking the user input 

input_1 = int(input("Number 1: "))
input_2 = int(input("Number 2: "))

# #making the code more modular and reuseable. 

def add_1():
    return (input_1 + input_2)

def diff_2():
    return (input_1 - input_2)

def pro_3():
    return (input_1 * input_2)

print(add_1())
print(diff_2())
print(pro_3())

#optimised version of the code.
# Optimized and modular code

def add(a, b):
    return a + b

def diff(a, b):
    return a - b

def pro(a, b):
    return a * b

def main():
    # Taking user input
    input_1 = int(input("Number 1: "))
    input_2 = int(input("Number 2: "))

    # Operations and results
    operations = {  # we are refrencing the function here,
        "Addition": add,
        "Difference": diff,
        "Product": pro
    }

    for operation, func in operations.items():
        print(f"{operation}: {func(input_1, input_2)}")

if __name__ == "__main__":
    main()
    

#refrencing function through a varaiable.
def hello( name):
    return (f"Hello,{name}")

var = hello

print(var("Devanshu"))


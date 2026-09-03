def calculator(num_1, num_2):
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    op = int(input("Enter the num for Operation: "))
    
    if op == 1:
        return num_1 + num_2
    elif op == 2:
        return num_1 - num_2
    elif op == 3:
        return num_1 * num_2
    elif op == 4:
        return num_1 / num_2
    else:
        return "Error"

num_1 = int(input("Enter the num_1: "))
num_2 = int(input("Enter the num_2: "))
ans = calculator(num_1, num_2)
print("Result:", ans)

def collatz(number):
    if number % 2 == 0:
        print(int(number/2))
        return (int(number/2))
    else:
        print (int(3*number+1))
        return (int(3*number+1))

while True:
    print("\nType an integer: ")
    try:
        int_number = int(input())
        if collatz(int_number) == 1:
            break
    except ValueError:
        print("Please enter an integer number.")

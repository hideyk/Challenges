# Enter your code here. Read input from STDIN. Print output to STDOUT
def divideNumbers(a, b):
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

noInputs = int(input())
for i in range(noInputs):
    divideNumbers(*input().split())
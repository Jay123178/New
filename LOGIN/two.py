def myfun(n):
 
    return str(n) == str(n)[::-1]

n = int(input("enter any string for checking the palindrome:  "))
if myfun(n):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")

# def myfun(n):
#     return str(n) == str(n)[::-1]

# start=int(input("enter the starting value: "))
# end=int(input("enter the last value: "))
# print(f"prime number between {start} and {end} are:  ")
# for i in range(start,end+1):
#     if myfun(i):
#         print(i , end=' ')


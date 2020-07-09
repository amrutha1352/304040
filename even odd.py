In [122]:
start=int(input("Enter the starting number of the sequence: "))
end=int(input("Enter the ending number of the sequence: "))
count_even=0
count_odd=0
for num in range(start,end+1):
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1
print("The number of even numbers:",count_even)
print("The number of odd numbers",count_odd)
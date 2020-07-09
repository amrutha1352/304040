In [ ]:
binary_num=list (input('enter a binary number'))
value=0
for i in range(len(binary_num)):
 digit=binary_num.pop()
if digit=='1':
 value=value+pow(2,i)
print("decimal value of the num is",value)
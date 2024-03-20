
def loop_fact(num):
    total = 1 
    for i in range (num,1,-1):
        total = total*i
    return total
        
        

print (loop_fact(1))
print(loop_fact(4))
print(loop_fact(5))
print(loop_fact(6))
print(loop_fact(9))


def factorial(num):
    if num != 1:
        num = num * factorial(num-1)
    return num
print (factorial(2))
print (factorial(1))
print (factorial(4))
print (factorial(6))
print (factorial(9))

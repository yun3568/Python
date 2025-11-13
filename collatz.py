def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return(number)
    else:
        number = 3 * number + 1
        print(number)
        return(number)

print("输入一个整数")
i = int(input())
while i != 1:
    i = collatz(i)   #不重新赋值给i会进入无限循环
print('end')
    

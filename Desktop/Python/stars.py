n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))
    
for i in range(1, n+1):
    print(' ' * (n - i), end='')
    print('*' * i)
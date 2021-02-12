
#user's input
fib = int(input('How many numbers to you want? '))

x, y = 0, 1
z = 0


# for x in range(fib):
while z < fib:
    print(x)
    a = x + y
    x = y
    y = a
    z += 1

    print(z)
    
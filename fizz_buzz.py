# Small: add_func(1, 2) --> outputs: __
# More Complex: add_func(500, 999) --> outputs: __
# Edge Cases: add_func() or add_func(null) or add_func(undefined) --> outputs: ___

# Take a user's input for a number, and then print out all of the numbers from 1 to that number.
            #startFrom = int(input('Start From (1-10): ')) not needed
            #x = 1
            # endOn = int(input('End On (any number): '))
            # while(x <= endOn):
            # print(x)
            # x +=1
# For any number divisible by 3, print 'fizz'
            # for i in range(lower, upper+1):
            #     if((i%3==0):
            #     print(i)
# For any number divisible by 5, print 'buzz'
            # for i in range(lower, upper+1):
            #   (i%5==0)):
            #   print(i)
# For any number divisible by 3 and 5, print 'fizzbuzz'
            # for i in range(lower, upper+1):
            #     if((i%3==0) & (i%5==0)):
            #     print(i)

#print 1 to user's input NOT NEEDED
# while(x <= endOn):
#     print(x)
#     x += 1

# HAD TO COMBINE CODE AND REPLACE SYNTAX AND ORDER OF EVALUATION

#Starting range
x = 1
#user's input
endOn = int(input('End On (any number): '))

#for loop and if statment
for x in range(x, endOn):
    if x % 3 == 0 and x % 5 == 0:
        print('fizzbuzz')
        continue
    elif x % 3 == 0:
        print("fizz")
        continue
    elif x % 5 == 0:
        print("buzz")
        continue
    print(x)



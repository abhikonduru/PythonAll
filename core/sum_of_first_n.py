#print the sum of the range of numbers from 0 to an input

#inefficient way (uses more of the computer's brain)
end = input("What is the ending value: ")
endint  = int(end)
sum = 0

for x in range(endint+1):
    sum = x+sum
print(f"The sum on the numbers in the range 0 to {x} is: {sum}")

#smart way (uses less of the computer's brain)
endval = input("What is the ending value: ")
y = int(endval)
print(f"The sum of the numbers in the range 0 to {y} is {y*(y+1)/2}")
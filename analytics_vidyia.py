# Operators
print(3 * 5)
print(32 // 5)
print(27 % 5)
print("salam" * 5)
print(54 > 85)

# Odd or Even
x = int(input('give us the Number:'))
if x % 2 == 0:
    print("Even")
else:
    print("odd")

# Grade Classification
y = int(input('Enter Variable : '))
if y > 90:
    print('grade A')
elif 90 >= y > 60:
    print('Grade B')
else:
    print('Grade F')

# Loop for numbers between 10-50
for i in range(10, 50):
    print(i)
# Loop for Odd numbers between 10 -50
for i in range(10, 50):
    if i % 2 != 0:
        print(i)
# or
for i in range(11, 50, 2):
    print(i)


# Function of area of circle
def area_circle(radius):
    area = 3.14 * radius * radius
    return area


print(area_circle(3))


# compare
def gratter_function(x, y):
    if x > y:
        s = x
    else:
        s = y
    return s


print(gratter_function(3, 7))

# list

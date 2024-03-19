num = 5
new_num = num * (10 - 3) # Add parenthesis to make new_num to be 35
print(f"Exercise 1's new_num is: {new_num}")

dividend = 10
divisor = 3
decimal_quotient = dividend / divisor 
quotient = dividend // divisor # The quotient should be 3
remainder = dividend % divisor # The remainder should be 1
print(f"Exercise 2's quotient is: {quotient}, remainder is: {remainder}.")


rectangular_width = 5
rectangular_length = 3
perimeter = 2* (rectangular_width + rectangular_length) # Modify it to calculate perimeter
area = rectangular_width * rectangular_length # Modify to calculate area
print(f"Exercise 3's rectangular has perimeter of: {perimeter}, area of: {area}.")

marks = [80.5, 86.5]
mark_mid = marks[0]
mark_final = marks[1]
mark_average = (mark_mid + mark_final) /2 # Modify to get the correct average score of mark_mid and mark_final
print(f"Exercise 4's average mark is: {mark_average}")

words = ["apple", "pear"]
if len(words[0]) > len(words[1]): 
    longer_word = words[0]
else:
    longer_word = words[1]

print(f"Exercise 5's longer word is: {longer_word}")


increase = 0.2
increase_percentage = increase * 100
print(f"Exercise 6's increase percentage is: {increase_percentage}%")

x = 2
count = 0
while count < 8: 
    print(x)
    x = x + 2
    count = count + 1

def first_even_natural_nums(total):
    x = 2
    count = 0
    while count < total: 
        print(x)
        x = x + 2
        count = count + 1


first_even_natural_nums(8)

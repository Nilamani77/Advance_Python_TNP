# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# num = int(input("Enter a number: "))
# result = check_even_odd(num)
# print("The number is:", result)


# def sum_and_difference(a, b):
#     total = a + b
#     difference = a - b
#     return total, difference

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# sum_result, diff_result = sum_and_difference(num1, num2)

# print("Sum:", sum_result)
# print("Difference:", diff_result)


# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3

# print("The largest number is:", largest)

# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)

# num = int(input("Enter a number: "))
# print_numbers(num)

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# num = int(input("Enter a number: "))
# print("Factorial is:", factorial(num))

# def get_even_numbers(numbers):
#     even_list = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_list.append(num)
#     return even_list

# sample_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print("Even numbers:", get_even_numbers(sample_list))

# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
    
#     for char in text:
#         if char in vowels:
#             count += 1
            
#     return count

# sentence = input("Enter a string: ")
# print("Number of vowels:", count_vowels(sentence))

# def reverse_string(text):
#     reversed_text = ""
#     for char in text:
#         reversed_text = char + reversed_text
#     return reversed_text
# string = input("Enter a string: ")
# print("Reversed string:", reverse_string(string))

# def multiplication_table(n):
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")
# num = int(input("Enter a number: "))
# multiplication_table(num)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print("The number is Prime")
# else:
#     print("The number is Not Prime")

# def sum_of_list(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# sample_list = [10, 20, 30, 40]
# print("Sum of elements:", sum_of_list(sample_list))

# def print_dictionary(data):
#     for key, value in data.items():
#         print("Key:", key, "| Value:", value)

# sample_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }

# print_dictionary(sample_dict)

# def fibonacci_series(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# num = int(input("Enter number of terms: "))
# fibonacci_series(num)

# def find_max_min(numbers):
#     if len(numbers) == 0:
#         return None, None   
    
#     maximum = numbers[0]
#     minimum = numbers[0]
    
#     for num in numbers:
#         if num > maximum:
#             maximum = num
#         if num < minimum:
#             minimum = num
            
#     return maximum, minimum

# sample_list = [34,4,234,53,354,98]
# max_val, min_val = find_max_min(sample_list)

# print("Maximum:", max_val)
# print("Minimum:", min_val)

def is_palindrome(text):
    reversed_text = ""
    
    for char in text:
        reversed_text = char + reversed_text
    
    if text == reversed_text:
        return True
    else:
        return False

word = input("Enter a string: ")
if is_palindrome(word):
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")

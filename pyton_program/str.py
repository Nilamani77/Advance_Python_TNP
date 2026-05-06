# str=input("Enter a string:-")
# print(str[::-1])

# str=input("Enter a string:-")
# print(str.isupper())
# print(str.islower())

# s = input("Enter a string: ")

# if s.isdigit():
#     print("The string contains only digits.")
# else:
#     print("The string does not contain only digits.")


#4.
# s = input("Enter a string: ")

# result = s.replace(" ", "_")

# print("Modified string:", result)

#5.
# s = input("Enter string: ").lower()
# freq = {}

# for ch in s:
#     if ch != " ":
#         freq[ch] = freq.get(ch, 0) + 1

# print(freq)


#6.
# s = input("Enter a string: ")
# print("1st occurance",s[0])
# print("last occurance",s[len(s)-1])


#7.
# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"

# result = ""
# for ch in s:
#     if ch not in vowels:
#         result += ch

# print("String without vowels:", result)

# 8.
# s1=input("Enter first string:-")
# s2=input("Enter second string:-")
# if sorted(s1)==sorted(s2):
#     print("The string are anagrams")
# else:
#     print("The string not a anagrams")


#9.
# str = input("Enter a string: ")
# print(str.title())

# 10.
str = input("Enter a string: ")
if str==str[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")

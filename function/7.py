def is_palindrome(str1):
    if str1 == str1[-1::-1]:
        return True
    return False


s = input()
if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")
# str1 = "abcdefghijkl"
# print(str1[-3])
# print(str1[-1::-1])

# range(start, end, step)

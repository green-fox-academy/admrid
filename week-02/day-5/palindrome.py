# SOLUTION 1
# def create_palindrome(impi):
#     palindrome = impi
#     for charachter in impi[::-1]:
#         palindrome += charachter
#     return palindrome

# print(create_palindrome('string'))

# SOLUTION 2
def create_palindrome(impi):
    palindrome = ''
    palindrome = impi + impi[::-1]
    return palindrome

print(create_palindrome('string'))
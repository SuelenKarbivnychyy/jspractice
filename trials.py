"""Python functions for JavaScript Trials 1."""


def output_all_items(items):    
    """ 
    Print each item in the given array.

    Ex.:
    >>> output_all_items([52, 40, 78, "hi"])
    52
    40
    78
    hi

    """

    for item in items:
        print(item)    


def get_all_evens(nums):
    """
    Given an array of numbers, return an array of all even numbers.

    Ex.:
    >>> get_all_evens([20, 7, 10, 1, 2, 8, 46])
    [20, 10, 2, 8, 46]
    
    """
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums        



def get_odd_indices(items):
    """
    Given an array, return all elements at odd numbered indices.

    Ex.:
    >>> get_odd_indices([1, 'hello', True, 500])
    ['hello', 500]
   
    """
    odd_index_item = []

    for index, item in enumerate(items):
        if index %2 != 0:
            odd_index_item.append(item)

    return odd_index_item         


def print_as_numbered_list(items):
    """
    Given an array, output a numbered list.

    Ex.:
    >>> print_as_numbered_list([1, 'hello', "true"])
    1. 1
    1. hello
    1. true
    
    """

    counter = 1

    for item in items:
        print(f"{counter}. {item}")



def get_range(start, stop):
    """
    Return an array of numbers in a certain range.

    Ex.:
    >>> get_range(1, 5)
    [1, 2, 3, 4]
    
    """

    numbers = [start]
    num = start

    while num < stop -1:
        numbers.append(num + 1)
        num += 1

    return numbers    



def censor_vowels(word):
    """
    Given a string, return a string where vowels are replaced with '*'.

    Ex:    
    """

    chars = []

    for letter in word:
        if letter in "aeiouAEIOU":
            chars.append("*")
        else:
            chars.append(letter)

    return " ".join(chars)  



def snake_to_camel(string):
    """
    Given a string in snake case, return a string in upper camel case.

    Ex.:
    >>> snake_to_camel('hello_world')
    'HelloWorld'
    
    """

    camelCase = []

    words = string.split("_")

    for word in words:
        camelCase.append(word.title())
        

    return "".join(camelCase)           



def longest_word_length(words):
    """    
    Return the length of the longest word in the given array of words.

    Ex.:
    >>> longest_word_length(['jellyfish', 'zebra'])
    9

    """

    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest        


def truncate(string):
    """
    Truncate repeating characters into one character.

    Ex.:    
    >>> truncate('hi***!!!! wooow')
    'hi*! wow'
    
    """

    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result)-1]:
            result.append(char)

    return "".join(result)       



def has_balanced_parens(string):
    """
    Return true if all parentheses in a given string are balanced.

    Ex.:
    >>> has_balanced_parens('((This) (is) (good))')
    True
    >>> has_balanced_parens('(Oh no!)(')
    False

    """

    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1

        if parens < 0:
            return False    

    return parens == 0



def compress(string):
    """Return a compressed version of the given string.

    Ex.:
    >>> compress('Hello, world! Cows go moooo...')
    'Hel2o, world! Cows go mo4.3'

    """

    compressed = []

    current_char = ""
    counter = 0

    for char in string:
        if char != current_char:
            compressed.append(current_char)

            if counter > 1:
                compressed.append(str(counter))

            current_char = char
            counter = 0

        counter += 1

    compressed.append(current_char)
    if counter > 1:
        compressed.append(str(counter))

    return "".join(compressed)
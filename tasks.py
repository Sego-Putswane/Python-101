# Task 1
def get_user_info():
    """
    Ask the user for their name, age, and favorite color.
    Return a dictionary with the following structure:
    {
        "name": <user's name>,
        "age": <user's age>,
        "favorite_color": <user's favorite color>
    }
    """
    user_details= {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "favorite color": input("Enter your favorite color: ")}
    return user_details
    pass

# Task 2
def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) using the formula:
    BMI = weight (kg) / (height (m) ** 2)
    Return the BMI rounded to 2 decimal places.
    """
    BMI = weight  / (height ** 2)
    return round (BMI, 2)
    pass

# Task 3
def create_shopping_list(items):
    """
    Given a list of items, create a shopping list.
    Return a dictionary where the keys are the items and the values are the quantities (default to 1).
    Example:
    Input: ["apple", "banana", "apple"]
    Output: {"apple": 2, "banana": 1}
    """
    
    Dic_shopping_list ={}
    for item in items:
        if not isinstance(item, str):
            return TypeError(f"{item} is not a string")
        if item in Dic_shopping_list:
            Dic_shopping_list[item] += 1
        else:
            Dic_shopping_list[item] = 1
    return Dic_shopping_list
# items= ["apple", "banana", "apple", "apple", "orange", "banana"]
# shopping_list= create_shopping_list(items)
# print(shopping_list)
            
            
    
    # pass

# Task 4
def count_word_frequency(text):
    """
    Given a string, count the frequency of each word.
    Return a dictionary where the keys are the words and the values are their frequencies.
    Example:
    Input: "hello world hello"
    Output: {"hello": 2, "world": 1}
    """
    word_frequency= {}
    words= text.split()
    for word in words:
        if not isinstance(word, str):
            raise ValueError(f"{word} is not a string")
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency
# text= "hello world hello"
# frequency= count_word_frequency(text)
# print(frequency)
    
    # pass

# Task 5
def check_number(num):
    """
    Given a number, return:
    - "Positive" if the number is greater than 0.
    - "Negative" if the number is less than 0.
    - "Zero" if the number is 0.
    """
    if num > 0:
        return "Positive"
    if num < 0:
        return "Negative"
    if num == 0:
        return "Zero"
    return num
    pass

# Task 6
def sum_even_numbers(numbers):
    """
    Given a list of numbers, return the sum of all even numbers.
    """
    count= 0
    for num in numbers:
        if num % 2 == 0:
            count += num
    return count
    pass

# Task 7
def find_first_negative(numbers):
    """
    Given a list of numbers, use a while loop to find the first negative number.
    Return the first negative number or None if there are no negative numbers.
    """
    index= 0
    while index < len(numbers):
        if numbers[index] <0:
            return numbers[index]
        index += 1
    return None
    pass

# Task 8
def analyze_text(text):
    """
    Given a string, perform the following tasks:
    1. Count the number of words.
    2. Count the number of vowels (a, e, i, o, u).
    3. Return a dictionary with the results.
    Example:
    Input: "Hello world"
    Output: {"word_count": 2, "vowel_count": 3}
    """


    vowels= ["a", "e", "i", "o", "u"]
    word_count= 0
    vowels_count= 0

    words= text.split()

    word_count= len(words)

    for char in text.lower():
        if char in vowels:
            vowels_count += 1
    return{"word_count": word_count, "vowels_count":vowels_count}
# results= analyze_text("hello world")
# print(results)
    



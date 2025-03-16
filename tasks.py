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
    name = input("Enter your name: ").capitalize()
    age = input("Enter your age: ")
    favorite_color = input("Enter your favorite color: ").capitalize()
    
    return {"name" : name,
            "age" : age,
            "favorite_color" : favorite_color}

# Task 2
def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) using the formula:
    BMI = weight (kg) / (height (m) ** 2)
    Return the BMI rounded to 2 decimal places.
    """
    bmi = weight / (height**2)
    bmi = round(bmi, 2)
    return bmi

# Task 3
def create_shopping_list(items):
    """
    Given a list of items, create a shopping list.
    Return a dictionary where the keys are the items and the values are the quantities (default to 1).
    Example:
    Input: ["apple", "banana", "apple"]
    Output: {"apple": 2, "banana": 1}
    """
    
    shopping_list = {}
    for item in items:
        if item in shopping_list:
            shopping_list[item] += 1
        else:
            shopping_list[item] = 1
    return shopping_list

# Task 4
def count_word_frequency(text):
    """
    Given a string, count the frequency of each word.
    Return a dictionary where the keys are the words and the values are their frequencies.
    Example:
    Input: "hello world hello"
    Output: {"hello": 2, "world": 1}
    """

    words = text.lower().split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

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
    elif num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    else:
        return "Invalid Input. Enter a valid number"

# Task 6
def sum_even_numbers(numbers):
    """
    Given a list of numbers, return the sum of all even numbers.
    """
    even_numbers = 0
    
    for number in numbers:
        if number % 2 == 0:
            even_numbers += number
    return even_numbers

# Task 7
def find_first_negative(numbers):
    """
    Given a list of numbers, use a while loop to find the first negative number.
    Return the first negative number or None if there are no negative numbers.
    """
    index_num = 0
    
    while index_num < len(numbers):
        if numbers[index_num] < 0:
            return numbers[index_num]
        index_num += 1
    
    return None
            

# Task 8
def analyze_text(text):
    """
    Given a string, perform the following tasks:
    1. Count the number of words.
    2. Count the number of vowels (a, e, i, o, u).
    3. Return a dictionary with the results.
    Example:
    Input: "Hello world"
    Output: {"split_words": 2, "vowel": 3}
    """
    
    
    vowel = 0
    split_words = text.split()

    for item in text:
        if item in ["a","A","e","E","i","I","o","O","u","U"]:
            vowel += 1
    
    return {"word_count": len(split_words), "vowel_count": vowel}

print(analyze_text("Python is fun"))

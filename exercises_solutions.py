# 1. Girilen bir sayının faktöriyelini hesaplayan bir program yazın (Write a program that calculates the factorial of a given number).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
print("Factorial of", num, "is", factorial(num))

# 2. Verilen bir listenin en büyük elemanını bulan bir program yazın (Write a program to find the largest element of a given list).

def find_largest_element(lst):
    largest = lst[0]
    for item in lst:
        if item > largest:
            largest = item
    return largest

numbers = [3, 4, 1, 0, 4, 8]
largest_num = find_largest_element(numbers)
print(largest_num)

# 3. İki sayının en büyük ortak bölenini bulan bir program yazın (Write a program to find the greatest common divisor of two numbers).

def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

print(gcd(24, 36))

# 4. Bir dizinin elemanlarını tersten yazdıran bir program yazın (Write a program that prints the elements of an array in reverse order).

def reverse_array(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])

my_array = [1, 2, 3, 4, 5]
reverse_array(my_array)

# 5. Bir dizinin elemanlarını küçükten büyüğe sıralayan bir program yazın (Write a program that sorts the elements of an array in ascending order).

def sort_array(arr):
    return sorted(arr)

my_list = [3, 6, 1, 8, 2, 0, 5]
sorted_list = sort_array(my_list)
print(sorted_list)

# 6. Bir cümledeki kelimelerin sayısını hesaplayan bir program yazın (Write a program that counts the number of words in a sentence).

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "This is a test sentence."
num_words = count_words(sentence)
print("Number of words:", num_words)

# 7. Verilen bir listedeki çift sayıların toplamını hesaplayan bir program yazın (Write a program that calculates the sum of even numbers in a given list).

def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(my_list)
print(result)

# 8. İki matrisi çarpan bir program yazın (Write a program that multiplies two matrices).

import numpy as np

def matris_carpimi(matris1, matris2):
    return np.dot(matris1, matris2)

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
m = matris_carpimi(m1, m2)
print(m)

# 9. Verilen bir listedeki elemanları tekrar etmeden sıralayan bir program yazın (Write a program that sorts the elements of a list without duplicates).

def sort_list_without_repeats(lst):
    return list(sorted(set(lst)))

numbers = [1,4,6,8,4,3,2,2,5,7,8,9,1,2,0,2,4]
print(sort_list_without_repeats(numbers))

# 10. Verilen bir sayının asal olup olmadığını kontrol eden bir program yazın (Write a program that checks whether a given number is prime or not).

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(10))
print(is_prime(17))

# 11. İki sayı arasındaki asal sayıları listeleyen bir program yazın (Write a program that lists the prime numbers between two given numbers).

def prime_numbers(start, end):
    prime_nums = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(num)
    return prime_nums

start_num = 3
end_num = 99
prime_nums_res = prime_numbers(start_num, end_num)
print(f"Prime numbers between {start_num} and {end_num} are: {prime_nums_res}")

# 12. Bir cümleyi tersine çeviren bir program yazın (Write a program that reverses a sentence).

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_sentence("If your code works fine don't touch it"))

# 13. Bir sayının ikilik tabandaki karşılığını hesaplayan bir program yazın (Write a program that calculates the binary representation a number).

def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

print(decimal_to_binary(3410))

# 14. İki sayıyı toplayan bir program yazın (Write a program that adds two numbers).

def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(3, -5))

# 15. Bir dizideki her elemanın karesini hesaplayan bir program yazın (Write a program that calculates the square of each element in an array).

def square_elements(lst):
    return [x**2 for x in lst]

numbers = [1,2,3,4,5]
print(square_elements(numbers))

# 16. Bir listedeki elemanların ortalamasını hesaplayan bir program yazın (Write a program that calculates the average of the elements in a list).

def calculate_average(lst):
    return sum(lst) / len(lst)

numbers = [1,2,3,4,5]
print(calculate_average(numbers))

# 17. Verilen bir cümledeki en sık tekrar eden kelimeyi bulan bir program yazın (Write a program that finds the most frequently occurring word in a given sentence).

from collections import Counter

def most_common_word(sentence):
    words = sentence.split()
    word_count = Counter(words)
    return word_count.most_common(1)[0][0]

sentence = "Next time there won't be a next time." #Phil Leotardo, in The Sopranos
print(most_common_word(sentence))

# 18. Verilen bir metindeki kelime sayısını ve frekanslarını hesaplayan bir program yazın (Write a program that calculates the word frequency and counts in a given text).

import string

def word_count(text):
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.lower().split()

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return len(words), word_freq

text = "This is a sample text for testing word count. It should count each word and show its frequency."
print(word_count(text))

# 19. Bir dizi elemanını rastgele sıraya dizmek için bir program yazın (Write a program to shuffle the elements of an array randomly).

import random

def shuffle_array(arr):
    shuffled_arr = arr.copy()
    random.shuffle(shuffled_arr)
    return shuffled_arr

arr = [1, 2, 3, 4, 5]
print(shuffle_array(arr))

# 20. Verilen bir sayıyı verilen üsle hesaplayan bir program yazın (Write a program that calculates a given number raised to a given power).

def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

print(power(2,7))

# 21. İki sayı arasındaki Fibonacci sayılarını listeleyen bir program yazın (Write a program that lists the Fibonacci numbers between two given numbers).

def fibonacci(start, end):
    fibonacci_list = []
    a, b = 0, 1
    while b < end:
        if b >= start:
            fibonacci_list.append(b)
        a, b = b, a + b
    return fibonacci_list

print(fibonacci(0,100))

# 22. Bir metnin harf frekansını hesaplayan bir program yazın (Write a program that calculates the letter frequency of a text).

def letter_frequency(text):
    frequency = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

print(letter_frequency("pneumonoultramicroscopicsilicovolcanoconiosis"))

# 23. Verilen bir listedeki elemanların çarpımını hesaplayan bir program yazın (Write a program that calculates the product of the elements in a given list).

def calculate_product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [1,2,3,4,5]
print(calculate_product(numbers))

# 24. Verilen bir cümledeki her kelimenin ilk harfini büyük harfe çeviren bir program yazın (Write a program that capitalizes the first letter of each word in a given sentence).

def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

print(capitalize_first_letter("hello world !"))

# 25. Verilen bir metindeki kelime sayısını bulan bir program yazın (Write a program that counts the number of words in a given text).

def count_words(text):
    words = text.split()
    return len(words)

text = "This is a sample text for testing word count. It should count each word and show its frequency."
print(count_words(text))

# 26. Verilen bir dizideki elemanların toplamını bulan bir program yazın (Write a program that calculates the sum of the elements in a given list).

def sum_list(lst):
    return sum(lst)

numbers = [1,2,3,4,5]
print(sum_list(numbers))

# 27. Verilen bir sayının üslü kuvvetini bulan bir program yazın (Write a program that calculates the power of a given number).

def power(base, exponent):
    return base ** exponent

print(power(3,9))

# 28. Verilen bir metindeki en sık kullanılan 2 kelimeyi bulan bir program yazın (Write a program that finds the top 2 most frequently used words in a given text).

def top_2_words(text):
    words = text.lower().split()

    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    return [word[0] for word in sorted_dict[:2]]

text = "Almost nothing was more annoying than having our wasted time wasted on something not worth wasting it on." #Joshua Ferris, Then We Came to the End
print(top_2_words(text))

# 29. Verilen bir sayıda bulunan rakamların toplamını hesaplayan bir program yazın (Write a program that calculates the sum of digits in a given number).

def sum_of_digits(num):
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)
    return digit_sum

num = 99
print(sum_of_digits(num))

# 30. Verilen bir listedeki elemanların toplamını ve ortalamasını hesaplayan bir program yazın (Write a program that calculates the sum and average of elements in a given list).

def calculate_sum_avg(lst):
    total = sum(lst)
    avg = total / len(lst)
    return total, avg

my_list = [1, 2, 3, 4, 5]
total, avg = calculate_sum_avg(my_list)
print("Sum:", total)
print("Average:", avg)

# 31. Verilen bir metindeki en uzun kelimeyi bulan bir program yazın (Write a program that finds the longest word in a given text).

def find_longest_words(text):
    words = text.split()
    max_length = len(max(words, key=len))
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words

my_text = "One two three four five six seven eight nine"
longest_word = find_longest_words(my_text)
print("Longest word(s):", longest_word)

# 32. Verilen bir sayıdan küçük veya eşit olan tüm asal sayıları listeleyen bir program yazın (Write a program that lists all prime numbers less than or equal to a given number).

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def list_primes(num):
    primes = []
    for i in range(2, num+1):
        if is_prime(i):
            primes.append(i)
    return primes

my_num = 20
prime_list = list_primes(my_num)
print("Prime numbers less than or equal to", my_num, ":", prime_list)

# 33. Verilen bir listenin elemanlarını tek veya çift sayı olma durumuna göre ayrı ayrı listelerde saklayan bir program yazın (Write a program that separates the elements of a given list into two different lists according to whether they are odd or even).

def separate_odds_evens(lst):
    odds = []
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return odds, evens

numbers = [1,2,3,4,5,6,7,8,9]
print(separate_odds_evens(numbers))

# 34. Verilen bir listenin elemanlarının toplamını ve en küçük/en büyük elemanını hesaplayan bir program yazın (Write a program that calculates the sum and the smallest/largest element of a given list).

def calculate_stats(lst):
    total = sum(lst)
    minimum = min(lst)
    maximum = max(lst)
    return total, minimum, maximum

numbers = [1,2,3,4,5,6,7,8,9]
print(calculate_stats(numbers))

# 35. Verilen bir metindeki kelime sayısını ve sayıların toplamını hesaplayan bir program yazın (Write a program that counts the number of words and the sum of the numbers in a given text).

def count_words_and_numbers(text):
    words = text.split()
    word_count = len(words)
    number_sum = sum(int(word) for word in words if word.isdigit())
    return word_count, number_sum

text = "My journey to becoming a web developer from scratch without a CS degree. 3 2 1 go!"
print(count_words_and_numbers(text))

# 36. Verilen bir sayının çarpanlarını listeleyen bir program yazın (Write a program that lists the factors of a given number).

def list_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

print(list_factors(12))

# 37. Verilen bir listenin her elemanının faktöriyelini hesaplayan bir program yazın (Write a program that calculates the factorial of each element in a given list).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calculate_factorials(lst):
    result = []
    for i in lst:
        result.append(factorial(i))
    return result

print(calculate_factorials([3, 4, 5]))

# 38. Verilen bir metindeki en sık kullanılan harfi bulan bir program yazın (Write a program that finds the most frequently used letter in a given text).

def most_frequent_letter(text):
    letter_count = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    max_count = max(letter_count.values())
    most_frequent_letters = [k for k, v in letter_count.items() if v == max_count]
    return most_frequent_letters

print(most_frequent_letter("Internationalization is an important aspect for companies looking to expand their business globally."))

# 39. İki sayı arasındaki Armstrong sayılarını listeleyen bir program yazın (Write a program that lists the Armstrong numbers between two given numbers).

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**num_digits
    return sum == n

def armstrong_numbers_between(start, end):
    armstrongs = []
    for n in range(start, end+1):
        if is_armstrong(n):
            armstrongs.append(n)
    return armstrongs

print(armstrong_numbers_between(100, 500))

# 40. Verilen bir listenin her elemanını 10'dan büyükse 10'a eşitleyen bir program yazın (Write a program that sets each element of a given list to 10 if it is greater than 10).

def set_to_ten_if_greater_than_ten(lst):
    for i in range(len(lst)):
        if lst[i] > 10:
            lst[i] = 10

my_list = [5, 12, 3, 18, 7, 9]
set_to_ten_if_greater_than_ten(my_list)
print(my_list)

# 41. Verilen bir metindeki kelime frekanslarına göre kelime sayısını ve frekansları listesini oluşturan bir program yazın (Write a program that creates a list of word frequencies and word counts in a given text).

def get_word_frequencies(text):
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    word_frequencies = []
    for word, count in word_counts.items():
        word_frequencies.append((word, count))
    return word_frequencies

text = "Peter Piper picked a peck of pickled peppers; A peck of pickled peppers Peter Piper picked; If Peter Piper picked a peck of pickled peppers, Where's the peck of pickled peppers Peter Piper picked?"
word_frequencies = get_word_frequencies(text)
print(word_frequencies)

# 42. Verilen bir dizinin elemanlarını ikili sayı sisteminde gösteren bir program yazın (Write a program that displays the elements of a given list in binary number system).

def binary_list(lst):
    return [bin(x)[2:] for x in lst]

print(binary_list([3, 7, 9, 12]))

# 43. Verilen bir cümledeki her kelimenin son harfini büyük harfe çeviren bir program yazın (Write a program that converts the last letter of each word in a given sentence to uppercase).

def upper_last(sentence):
    words = sentence.split()
    for i in range(len(words)):
        words[i] = words[i][:-1] + words[i][-1].upper()
    return ' '.join(words)

print(upper_last("hello world !"))

# 44. İki diziyi birleştirerek tek bir dizi oluşturan bir program yazın (Write a program that merges two arrays to create a single array).

def merge_arrays(arr1, arr2):
    merged_arr = arr1 + arr2
    return merged_arr

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(merge_arrays(arr1, arr2))

# 45. Verilen bir sayı dizisindeki elemanların karelerinin toplamını hesaplayan bir program yazın (Write a program that calculates the sum of the squares of the elements in a given numerical array).

def sum_of_squares(arr):
    square_sum = 0
    for num in arr:
        square_sum += num**2
    return square_sum

arr = [1, 2, 3, 4, 5]
print(sum_of_squares(arr))

# 46. Verilen bir öğe kümesinin tüm olası kombinasyonlarını içeren bir liste oluşturan bir program yazın. Program öğe kümesini girdi olarak almalı ve tüm olası kombinasyonları içeren bir tuple listesi döndürmelidir (Write a program that generates a list of all possible combinations of a given set of elements. The program should take the set of elements as input and return a list of tuples containing all possible combinations).

from itertools import combinations

elements = [1, 2, 3, 4]
combinations_list = []

for i in range(len(elements)+1):
    combinations_list += list(combinations(elements, i))

print(combinations_list)

# 47. Verilen bir öğe kümesinin tüm olası permütasyonlarını içeren bir liste oluşturan bir program yazın. Program öğe kümesini girdi olarak almalı ve tüm olası permütasyonları içeren bir tuple listesi döndürmelidir (Write a program that generates a list of all possible permutations of a given set of elements. The program should take the set of elements as input and return a list of tuples containing all possible permutations).

from itertools import permutations

elements = [1, 2, 3]
permutations_list = list(permutations(elements))
print(permutations_list)

# 48. Verilen bir metindeki sesli harflerin tamamını istenilen tek bir sesli harfe çeviren bir program yazın (Write a program that converts all the vowels in a given text into a single desired vowel).

def replace_vowels(text, desired_vowel):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            if char.isupper():
                result += desired_vowel.upper()
            else:
                result += desired_vowel
        else:
            result += char
    return result

text = "A Bottle of Water"
desired_vowel = "o"
new_text = replace_vowels(text, desired_vowel)
print(new_text)

# 49. Verilen kelimedeki harflerin alfabedeki sıralarını yazdıran bir program yazın (Write a program that prints the alphabetical positions of the letters in a given word).

word = "Internet"

for letter in word:
    if letter.isupper():
        position = ord(letter) - 64
    else:
        position = ord(letter) - 96

    print(f"{letter}: {position}")

# 50. Verilen bir cümlede bazı harflerin yerine * işaretini koyacak bir program yazın (Write a program that will place * marks in place of some letters in a given sentence).

def replace_letters(sentence, letters):
    new_sentence = ""
    for char in sentence:
        if char.lower() in letters.lower():
            new_sentence += "*"
        else:
            new_sentence += char
    return new_sentence

sentence = "What the fuck!"
letters = "aeiou"
new_sentence = replace_letters(sentence, letters)
print(new_sentence)

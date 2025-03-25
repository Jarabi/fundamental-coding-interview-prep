# Applying Simple Looping in Practice with Python

## Requirements

### Manipulating Strings: Reversing Words in a Sentence

1. Rotating Characters in Words of a 
    > You are given a string of `n` characters, with `n` varying from `1` to `1000`, inclusive.
   > Your task is to write a Python function that takes this string as input, applies the following
   > operations, and finally returns the resulting string.

    > 1. Split the given string into individual words, using a space as the separator.
    > 2. Convert each word into a list of its constituent characters, and shift each list once to the
    > right (with the last element moving to the first position).
    > 3. After the rotations, reassemble each word from its list of characters.
    > 4. Join all the words into a single string, separating adjacent words with a single space.
    > 5. Return this final string as the function's output.

    > The constraints for the problem are as follows:
   > - The input string will neither start nor end with a space, nor will it have multiple consecutive
   > spaces.
   > - Each word will contain only alphabets and digits, and its length will range from `1` to `10`.
   > - The words are case-sensitive; for example, `'word'` and `'Word'` are considered distinct.

   > Your program should output a single string with the words rotated by their lengths while preserving
   > their original order.

    > As an illustration, consider the input string `"abc 123 def"`. Applying the stated operations results
   > in the output `"cab 312 fde"`.

2. Transforming Words with English Alphabet's Opposite Characters
    >    Given a string consisting of words separated by whitespace, your task is to write a Python function
   >    that accepts this string. It then replaces each character in the words with the corresponding character
   >    opposite in the English alphabet and stitches them all together to form a new string.

    >    Here's what you need to consider:
   > - The input string will include between 1 and 100 words.
   > - Each word consists of characters separated by white space.
   > - A word is composed of characters ranging from `a` to `z` or `A` to `Z`. So, if a word contains a lowercase
   > 'a', for instance, it should be replaced with 'z', 'b' with 'y', 'c' with 'x', and so on, maintaining the
   > same case. For words with an uppercase 'A', it should be replaced with 'Z', 'B' with 'Y', 'C' with 'X', and
   > so forth, while preserving the uppercase.
   > - The given string will not start or end with a space, and there will be no occurrence of double spaces.
   > - After transforming the characters of the words, form a new string by taking the last word first and appending
   > the remaining words in their original order, each separated by spaces.
   
   > **Note**: The opposite letter mappings are as follows: `a` ↔ `z`, `b` ↔ `y`, `c` ↔ `x`, ..., `m` ↔ `n`,
   > `n` ↔ `m`, ..., `x` ↔ `c`, `y` ↔ `b`, `z` ↔ `a`. The mapping is case-sensitive.

    > <strong>Example</strong>: For the input string `"CapitaL letters"`, the output should be `"ovggvih XzkrgzO"`.

3. Capitalizing and Lowercasing String Words
   > You are given a string filled with words. Your task is to write a Python function that takes this string as
   > input. Your function should then capitalize the first letter of each word while making the rest of the letters
   > lowercase. Finally, it should recombine the words into a new string where every word starts with a capital
   > letter.

   > Here's what to keep in mind:

   > - The input string will contain between 1 and 100 words.
   > - Each word is a sequence of characters separated by white space.
   > - Words consist of characters ranging from `a` to `z`, `A` to `Z`, `0` to `9`, or even an underscore `_`.
   > - The provided string will not start or end with a space, and it will not contain double spaces.
   > - After capitalizing the first character of each word and converting the rest to lowercase, the program
   > should return a single string in which the words maintain their original order.
   > - If the first character of a word is not a letter (like a number or an underscore), keep it as is.
   
   > Ignore cases where punctuation marks are attached to words (such as "Hello," or "world!"). Words and
   > punctuation should retain their original places in your final output. You are not required to separate
   > punctuation marks from the words in your solution.
   
   > **Example**  
   For the input string `"SoME rAndoM _TeXT"`, the output should be `"Some Random _text"`.

### Parsing and Multiplying Numeric Values in Strings

1. Parsing and Converting Words in a String
   > Let's imagine you are given a string that contains a series of words separated by a hyphen ("-"). Each
   > word in the string can be a lowercase letter from 'a' to 'z' or a set of digits representing a number from
   > 1 to 26. Your task is to parse this string and swap the type of each word: convert numbers into their
   > corresponding English alphabet letters, and letters into their numerical equivalents. This means '1' should
   > convert to 'a', and 'a' should convert to '1'.

   > You need to return a new string with the converted words, rejoined with hyphens.

   > Ensure you maintain the original order of the words from the input string in your output string.

   > The input string's length should range from 1 to 1000 for this exercise. The string will never be empty,
   > always containing at least one valid lowercase letter or numerical word.

   > Remember, the transformation of words should be limited to converting numbers from 1 to 26 into their
   > corresponding letters from 'a' to 'z', and vice versa.

   > **Example**  
   For the input string `"1-a-3-c-5"`, the output should be `"a-1-c-3-e"`.

2. Parsing Sports Records: Calculating Sum of Scores
   > You are given a string `s` of length `n`, with `n` ranging from `1` to `500` inclusive. This string 
   > represents the complex and jumbled record of a sports game. It combines player names and scores but lacks
   > a uniform structure. The player names consist of words made up of lowercase English alphabets (`a`-`z`),
   > while the scores are integers ranging from 1 to 100 inclusive.

   > Your mission involves writing a Python function that should parse the given string, isolate the integers
   > representing player scores, and return the sum of these scores.

   > For instance, for the input string, `"joe scored 5 points, while adam scored 10 points and bob scored 2,
   > with an extra 1 point scored by joe"`, your function should return the sum `5 + 10 + 2 + 1`, which totals 18.

3. Shifting Characters within a String Following Numerical Values
   > You are provided with a string of alphanumeric characters in which each number, regardless of the number of
   > digits, is always followed by at least one alphabetic character before the next number appears. The task
   > requires you to return a transformed version of the string wherein the first alphabetic character following
   > each number is moved to a new position within the string and characters in between are removed.

   > Specifically, for each number in the original string, identify the next letter that follows it, and then
   > reposition that character to directly precede the number. All spaces and punctuation marks between the
   > number and the letter are removed.

   > The length of the string `s` ranges from 3 to 10^6 (inclusive), and the string contains at least one number.
   > The numbers in the string are all integers and are non-negative.

   > Here is an example for better understanding:  
   > Given the string:
   > 
   > `"I have 2 apples and 5! oranges and 3 grapefruits."`  
   > 
   > The function should return:
   >
   > `"I have a2pples and o5ranges and g3rapefruits."`
   
   > In this instance, the character 'a' following the number 2 is moved to come before the 2, the 'o' succeeding
   > the 5 is placed before the 5, and the 'g' subsequent to the 3 is repositioned to precede the 3. Punctuation
   > marks and spaces in between are removed.
   
   > Please note that the operation should maintain the sequential order of the numbers and the rest of the text.
   > Considering this, the task is not solely about dividing a string into substrings but also about modifying
   > them. This will test your expertise in Python string operations and type conversions.

### Parsing and Calculating Seconds from Time Strings in Python

1. Adding Seconds to Time Points
2. Calculating the Length of a Time Period in Minutes
3. Calculating New Date Given Number of Days

### Exploring Substring Search in Python Strings

1. Replacing Substring in a Text
2. Reverse Word Instances in Sentences
3. Spotting Swapped Characters in Strings


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
2. Parsing Sports Records: Calculating Sum of Scores
3. Shifting Characters within a String Following Numerical Values

### Parsing and Calculating Seconds from Time Strings in Python

1. Adding Seconds to Time Points
2. Calculating the Length of a Time Period in Minutes
3. Calculating New Date Given Number of Days

### Exploring Substring Search in Python Strings

1. Replacing Substring in a Text
2. Reverse Word Instances in Sentences
3. Spotting Swapped Characters in Strings


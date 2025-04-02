# Practicing String Operations and Type Conversions in Python

## Requirements

### Manipulating Strings: Reversing Words in a Sentence

1. Rotating Characters in Words of a 
   > You are given a string of `n` characters, with `n` varying from `1` to `1000`, inclusive.
   > Your task is to write a Python function that takes this string as input, applies the following
   > operations, and finally returns the resulting string.
   >
   > 1. Split the given string into individual words, using a space as the separator.
   > 2. Convert each word into a list of its constituent characters, and shift each list once to the
   > right (with the last element moving to the first position).
   > 3. After the rotations, reassemble each word from its list of characters.
   > 4. Join all the words into a single string, separating adjacent words with a single space.
   > 5. Return this final string as the function's output.
   >
   > The constraints for the problem are as follows:
   > - The input string will neither start nor end with a space, nor will it have multiple consecutive
   > spaces.
   > - Each word will contain only alphabets and digits, and its length will range from `1` to `10`.
   > - The words are case-sensitive; for example, `'word'` and `'Word'` are considered distinct.
   >
   > Your program should output a single string with the words rotated by their lengths while preserving
   > their original order.
   >
   > As an illustration, consider the input string `"abc 123 def"`. Applying the stated operations results
   > in the output `"cab 312 fde"`.

2. Transforming Words with English Alphabet's Opposite Characters
   > Given a string consisting of words separated by whitespace, your task is to write a Python function
   > that accepts this string. It then replaces each character in the words with the corresponding character
   > opposite in the English alphabet and stitches them all together to form a new string.
   >
   > Here's what you need to consider:
   > - The input string will include between 1 and 100 words.
   > - Each word consists of characters separated by white space.
   > - A word is composed of characters ranging from `a` to `z` or `A` to `Z`. So, if a word contains a lowercase
   > 'a', for instance, it should be replaced with 'z', 'b' with 'y', 'c' with 'x', and so on, maintaining the
   > same case. For words with an uppercase 'A', it should be replaced with 'Z', 'B' with 'Y', 'C' with 'X', and
   > so forth, while preserving the uppercase.
   > - The given string will not start or end with a space, and there will be no occurrence of double spaces.
   > - After transforming the characters of the words, form a new string by taking the last word first and appending
   > the remaining words in their original order, each separated by spaces.
   >
   > **Note**: The opposite letter mappings are as follows: `a` ↔ `z`, `b` ↔ `y`, `c` ↔ `x`, ..., `m` ↔ `n`,
   > `n` ↔ `m`, ..., `x` ↔ `c`, `y` ↔ `b`, `z` ↔ `a`. The mapping is case-sensitive.
   >
   > **Example**: For the input string `"CapitaL letters"`, the output should be `"ovggvih XzkrgzO"`.

3. Capitalizing and Lowercasing String Words
   > You are given a string filled with words. Your task is to write a Python function that takes this string as
   > input. Your function should then capitalize the first letter of each word while making the rest of the letters
   > lowercase. Finally, it should recombine the words into a new string where every word starts with a capital
   > letter.
   >
   > Here's what to keep in mind:
   >
   > - The input string will contain between 1 and 100 words.
   > - Each word is a sequence of characters separated by white space.
   > - Words consist of characters ranging from `a` to `z`, `A` to `Z`, `0` to `9`, or even an underscore `_`.
   > - The provided string will not start or end with a space, and it will not contain double spaces.
   > - After capitalizing the first character of each word and converting the rest to lowercase, the program
   > should return a single string in which the words maintain their original order.
   > - If the first character of a word is not a letter (like a number or an underscore), keep it as is.
   >
   > Ignore cases where punctuation marks are attached to words (such as "Hello," or "world!"). Words and
   > punctuation should retain their original places in your final output. You are not required to separate
   > punctuation marks from the words in your solution.
   >
   > **Example**
   >
   > For the input string `"SoME rAndoM _TeXT"`, the output should be `"Some Random _text"`.

### Parsing and Multiplying Numeric Values in Strings

1. Parsing and Converting Words in a String
   > Let's imagine you are given a string that contains a series of words separated by a hyphen ("-"). Each
   > word in the string can be a lowercase letter from 'a' to 'z' or a set of digits representing a number from
   > 1 to 26. Your task is to parse this string and swap the type of each word: convert numbers into their
   > corresponding English alphabet letters, and letters into their numerical equivalents. This means '1' should
   > convert to 'a', and 'a' should convert to '1'.
   >
   > You need to return a new string with the converted words, rejoined with hyphens.
   >
   > Ensure you maintain the original order of the words from the input string in your output string.
   >
   > The input string's length should range from 1 to 1000 for this exercise. The string will never be empty,
   > always containing at least one valid lowercase letter or numerical word.
   >
   > Remember, the transformation of words should be limited to converting numbers from 1 to 26 into their
   > corresponding letters from 'a' to 'z', and vice versa.
   >
   > **Example**
   >
   > For the input string `"1-a-3-c-5"`, the output should be `"a-1-c-3-e"`.

2. Parsing Sports Records: Calculating Sum of Scores
   > You are given a string `s` of length `n`, with `n` ranging from `1` to `500` inclusive. This string 
   > represents the complex and jumbled record of a sports game. It combines player names and scores but lacks
   > a uniform structure. The player names consist of words made up of lowercase English alphabets (`a`-`z`),
   > while the scores are integers ranging from 1 to 100 inclusive.
   >
   > Your mission involves writing a Python function that should parse the given string, isolate the integers
   > representing player scores, and return the sum of these scores.
   >
   > For instance, for the input string, `"joe scored 5 points, while adam scored 10 points and bob scored 2,
   > with an extra 1 point scored by joe"`, your function should return the sum `5 + 10 + 2 + 1`, which totals 18.

3. Shifting Characters within a String Following Numerical Values
   > You are provided with a string of alphanumeric characters in which each number, regardless of the number of
   > digits, is always followed by at least one alphabetic character before the next number appears. The task
   > requires you to return a transformed version of the string wherein the first alphabetic character following
   > each number is moved to a new position within the string and characters in between are removed.
   >
   > Specifically, for each number in the original string, identify the next letter that follows it, and then
   > reposition that character to directly precede the number. All spaces and punctuation marks between the
   > number and the letter are removed.
   >
   > The length of the string `s` ranges from 3 to 10^6 (inclusive), and the string contains at least one number.
   > The numbers in the string are all integers and are non-negative.
   >
   > Here is an example for better understanding:  
   > Given the string:
   > 
   > `"I have 2 apples and 5! oranges and 3 grapefruits."`  
   > 
   > The function should return:
   >
   > `"I have a2pples and o5ranges and g3rapefruits."`
   >
   > In this instance, the character 'a' following the number 2 is moved to come before the 2, the 'o' succeeding
   > the 5 is placed before the 5, and the 'g' after the 3 is repositioned to precede the 3. Punctuation
   > marks and spaces in between are removed.
   >
   > Please note that the operation should maintain the sequential order of the numbers and the rest of the text.
   > Considering this, the task is not solely about dividing a string into substrings but also about modifying
   > them. This will test your expertise in Python string operations and type conversions.

### Parsing and Calculating Seconds from Time Strings in Python

1. Adding Seconds to Time Points
   > You are given two input arguments: an array of strings `time_points` and an integer `added_seconds`. Each string
   > in `time_points` is in the `HH:MM:SS` format, representing a valid time from `"00:00:00"` to `"23:59:59"`
   > inclusive. The integer `added_seconds` represents a number of seconds, ranging from 1 to 86,400. Your task is to
   > create a new function, `add_seconds_to_times(time_points, added_seconds)`, which takes these two arguments and
   > returns a new array of strings. Each string in the returned array is the new time, calculated by adding the
   > provided `added_seconds` to the corresponding time in `time_points`, formatted in `HH:MM:SS`.
   >
   > The array `time_points` contains `n` strings, where `n` can be any integer from 1 to 100 inclusive. The time
   > represented by each string in `time_points` is guaranteed to be valid. The total time, after adding
   > `added_seconds`, can roll over to the next day.
   >
   > **Example**
   > 
   > For `time_points = ['10:00:00', '23:30:00']` and `added_seconds = 3600`, the output should be
   > `['11:00:00', '00:30:00']`.

2. Calculating the Length of a Time Period in Minutes
   > You are given a time period formatted as a string in the `HH:MM:SS - HH:MM:SS` format. HH:MM:SS represents
   > the time in hours, minutes, and seconds form, and the hyphen (-) separates the start time from the end time
   > of the period.
   >
   > Your task is to calculate how many minutes pass from the start time until the end time.
   >
   > Here are some guidelines:
   >
   > - The input times are always valid time strings in the `HH:MM:SS` format, with `HH` ranging from 00 to 23,
   > and `MM` and `SS` from 00 to 59.
   > - The output should be an integer, representing the total length of the time period in minutes.
   > - The start time of the period will always be earlier than the end time, so periods that cross over midnight
   > (like 23:00:00 - 01:00:00) are not considered.
   > - We are interested in the number of times the time passes some `HH:MM:00` after the start time until the end
   > time. Any remaining seconds should be disregarded; for instance, a period of `"12:15:00 - 12:16:59"` represents
   > 1 minute, not 2, and a period of `"12:14:59 - 12:15:00"` also represents 1 minute.
   > 
   > **Example**
   >
   > `"12:15:30 - 14:00:00"` should return `105`

3. Calculating New Date Given Number of Days
   > You are given an initial date as a string in the format `YYYY-MM-DD`, along with an integer `n` which represents
   > a number of days. Your task is to calculate the date after adding the given number of days to the initial date
   > and return the result in the `YYYY-MM-DD` format.
   > 
   > Keep these points in mind when resolving the task:
   > 
   > - The initial date string is always valid, formatted as `YYYY-MM-DD`, where `YYYY` denotes the year, `MM` the
   > month, and `DD` the day.
   > - The given integer `n` is the number of days you have to add to the initial date and will be up to **50,000**.
   > - The output should be a string showcasing the final date after adding `n` days, in the `YYYY-MM-DD` format.
   >
   > Your function will be in the form `add_days(date: str, n: int) -> str`.
   >
   > **Constraints**
   > - `date` = the date string in the `YYYY-MM-DD` format. The year `YYYY` will be from 1900 to 2100, inclusive.
   > The month `MM` and the day `DD` will be valid for the given year.
   > - `n` = the integer representing the number of days you have to add to the initial date. `n` ranges from 1 to
   > **50,000**, inclusive.
   > - You should consider leap years in the calculation. A year is a leap year if it is divisible by 4, but century
   > years (years divisible by 100) are not leap years unless they are divisible by 400. This means that the year
   > 2000 was a leap year, although 1900 was not.
   > - The month and day result should always be two digits long, padding with a 0 if necessary. For example, July
   > 9th should be formatted as `"07-09"`.
   > 
   > **Example**
   > 
   > For `date = '1999-01-01'` and `n = 365`, the output should be `'2000-01-01'`.

### Exploring Substring Search in Python Strings

1. Replacing Substring in a Text
   > Imagine you are working on a new feature for a text processing application. The feature requires you to provide
   > users with the option to replace all occurrences of a certain substring in the entered text with a new substring.
   >
   > You are tasked with writing a function, `replace_substring(text: str, old: str, new: str) -> str`, that does the
   > following:
   >
   > - Accepts as input `text` (a string of length `n`, where `1 ≤ n ≤ 500`, which includes only lowercase alphabets
   > and spaces), `old` (a string of length `k`, where `1 ≤ k ≤ n`, which includes only lowercase alphabets), and `new`
   > (a string of length `m`, where `1 ≤ m ≤ 500`, which includes only lowercase alphabets).
   >
   > - Replaces every occurrence of the string `old` in `text` with the string `new`.
   >
   > - Returns the updated `text` string with all replaced substrings.
   >
   > Please ensure that the case of the letters remains consistent during the process, meaning an uppercase letter
   > should be replaced with an uppercase letter, and a lowercase letter should be replaced with a lowercase one.
   >
   > For instance, your function might be called as follows:
   >
   > ```python
   > replace_substring("hello world", "world", "friend")
   > ```
   > In this case, the output would be:
   > ```
   > "hello friend"
   > ```
   > This is because there is one occurrence of the substring 'world' in the string. This occurrence is replaced by
   > 'friend', resulting in the return value "hello friend".

2. Reverse Word Instances in Sentences
   > You are given two lists, `sentences` and `words`, each comprising `n strings`, where n ranges from  **1** to
   > **100** inclusive. Each string in the `sentences` list has a length ranging from **1** to **500** inclusive.
   > Each `word` in the `words` list is a single lowercase English alphabet word of length *1* to **10** inclusive.
   > 
   > Your task is to find all instances of each word in the corresponding sentence from the `sentences` list and
   > replace them with the reverse of the word. The words and sentences at the same index in their respective lists
   > are deemed to correspond to each other.
   > 
   > Return a new list comprising `n strings`, where each `string` is the sentence from the `sentences` list at the
   > corresponding index, with all instances of the word from the `words` list at the same index replaced with its
   > reverse.
   > 
   > If the `word` is not found in the respective sentence, keep the sentence as it is.
   > 
   > Remember, while replacing the instances of `word` in the sentence, you should preserve the case of the initial
   > letter of the word. If a word starts with a capital letter in the sentence, its reversed form should also start
   > with a capital letter.
   > 
   > **Example**
   >
   > For `sentences = ['this is a simple example.', 'the name is bond. james bond.', 'remove every single e']` and
   > `words = ['simple', 'bond', 'e']`, the output should be `['this is a elpmis example.', 'the name is dnob. james
   > dnob.', 'remove every single e']`.

3. Spotting Swapped Characters in Strings
   > Humans often make mistakes when they are typing quickly. In some cases, they may press two keys simultaneously,
   > resulting in swapped characters in the text. Your task is to craft a Python function that helps identify such
   > typos. Specifically, you are asked to construct a function called s`pot_swaps(source: str, target: str) -> 
   > List[Tuple[int, str, str]]` that behaves as follows:
   > 
   > Given two strings, `source` and `target`, of the same length `n` (1 ≤ `n` ≤ 500), inclusive, both comprise only
   > lowercase English letters. The function should return a list of tuples. Each tuple should contain three elements:
   > the zero-based index of the swap in the `source` string, the character (a string of length 1) at that index in
   > `source`, and the character that swapped places with the source character in `target`.
   > 
   > In other words, go over both strings simultaneously and, for each character from `source` and `target` at
   > position i, find situations when `source[i] != target[i]` and `source[i+1] = target[i]` and `source[i] =
   > target[i+1]`. This implies that the characters at positions `i` and `i+1` in the `source` string swapped places
   > in the `target` string.
   > 
   > **Note:**
   > 
   > - Characters can be swapped at most once.
   > - The swapped character pairs should be returned in a list in the order they were found (from the string start
   > - to end).
   > - Don't check for swaps at the last position of a string, since there is no character with which to swap.
   >
   > **Example**
   > 
   > For `source = "hello"` and `target = "hlelo"`, the output should be `[(1, 'e', 'l')]`.
   > 
   > Good luck!


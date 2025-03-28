# Applying Simple Looping in Practice with Python

## Requirements

### Manipulating Arrays to Find Opposite Element Pairs

1. Creating Geometric Mean Pairs from an Array

    > You are given an input array consisting of n integers ranging from 0 to 100, inclusive,
   > where n represents the length of the array. Your task is to return a new array of tuples.
   > Each tuple should consist of an element from the input array paired with its geometrical
   > mean with the 'opposite' element. The 'opposite' element of any element in the array is
   > defined as the element at the corresponding position from the end of the array.

    > Assume that the geometrical mean of two numbers, a and b, is calculated as: `sqrt(a×b)`.

    > Notes:
    > - If the length of the array, n, is odd, the middle element is considered to be its own 'opposite'.
    > - The elements of the input array will be in the range from 0 to 100, inclusive.
    > - Calculate the geometrical mean to two decimal places. For example, the geometrical mean of 2 and 8 is 4.00 (since `sqrt(2×8)=4`).
    > - Round down to two decimal places. For instance, the geometrical mean of 2 and 8 is 4.00, not 4.472.

    >  For example, for `numbers = [1, 2, 3, 4, 5]`, the output should be `solution(numbers) = [(1, 2.24), (2, 2.83), (3, 3.0), (4, 2.83), (5, 2.24)]`.

2. Pairing Numbers with their Reverse Counterparts in a List
    > You are provided with a list of n integers, where n ranges from 2 to 200, inclusive.
   > The task is to return a list of tuples, each containing a pair of an integer and its reverse counterpart.

    > In this context, the reverse counterpart of a number is the number with its digits reversed.
   > For example, the reverse counterpart of `123` is `321`.

    > You must iterate through the list to find the reverse counterpart for each integer.
   > If this reversed number exists in the list, create a tuple with the original number and its reverse counterpart. If not, skip it.

    > Your output should be a list of tuples with the original numbers and their reverse counterparts.
   > The integers in the given list will range from 10 to 9999, inclusive, and each integer in the list is unique.

    > Note: The reverse counterpart of a single digit number is the same number. For numbers that result in
   > leading zeros when reversed (e.g., 100 becomes 001, which is 1), consider only the integer value (i.e., 1).
   > It's guaranteed that the original list will not contain integers with leading zeros.

    > For example, for `numbers = [12, 21, 34, 43, 56, 65]`, the output should be
   > `solution(numbers) = [(12, 21), (21, 12), (34, 43), (43, 34), (56, 65), (65, 56)]`.

3. Summing Up Opposite Elements in an Array
   > You are given an array of `n` integers, where n ranges from 2 to 200, inclusive. The elements in the
   > array range from -200 to 200, inclusive. Your task is to return an array in which each element is the
   > sum of a pair composed of an element and its 'opposite' element.

   > By 'opposite', we mean that in an array of n elements, the first and last elements are paired, the
   > second and second-to-last elements are paired, and so on. If the array is of odd length, the middle
   > element pairs with itself.

   > The function should handle both positive and negative integers and be capable of dealing with an odd
   > number of elements in the list.

   > For example, given an input array `[1, 2, 3, 4, 5]`, your function should return `[6, 6, 6]`. This is
   > because the first element 1 plus the last element 5 equals 6, the second element 2 plus the second-to-last
   > element 4 equals 6, and the middle element 3 plus itself equals 6.

### Traversing and Summing Even Digits in an Integer

1. Calculating Product of Odd Digits in a Number
   > You are given an integer `n` where n ranges from 1 to 10^8, inclusive. Your task is to write a function
   > that calculates and returns the product of the odd digits of n, `without converting n into a string`.

   > For example, if n equals `43172`, the output should be `21`, because the product of the odd digits
   > `3`, `1`, and `7` is `21`.

   > Please note that if n has no odd digits, your function should return `0`.

   > You are expected to solve this task by using a while loop. Good luck!

2. Reversing Integer Digits with a While Loop
   > Your task is to construct a function that accepts an integer `n` and returns the integer with
   > the same digits as `n`, but in `reverse` order. You should implement your solution using a `while loop`.

   > For instance, if the input is `12345`, the output should be `54321`.

   > Keep in mind that n will always be a positive integer between 1 and 10^8.

   > Do not use built-in functions that convert the integer to another data type, such as a string,
   > to reverse it. Solve the problem purely using mathematical operations and loop constructs.

   > Note that when the result has leading zeros, you should consider only the integer value
   > (e.g., `1230` becomes `321` after the operation).

3. Duplicating Digits in an Integer
   > Your task is to implement a function that duplicates every digit in a given non-negative integer number,
   > `n`. For example, if `n` equals `1234`, the function should return `11223344`.

   > To prevent possible integer overflow, it is guaranteed that n will be a non-negative integer that does
   > not exceed 10^4. Solve this task `without converting n into a string or performing any other type of
   > casting`. Your job is to work strictly with integer operations.

   > **Keynote:**
   > Focus on the essence of the problem, which is processing each digit of the number independently while
   > maintaining the digit order. There is no need to look for mathematical patterns or clever simplifications;
   > plain and straightforward processing will suffice. Utilize the toolbox of basic programming skills:
   > loops, conditions, and mathematical operations. Good luck!

4. Counting Groups of Consecutive Equal Digits in a Number
   > You are tasked with writing a function that takes a positive integer, `n`, as an input and returns the
   > number of consecutive equal digits in the number. Specifically, your function should identify pairs of
   > digits in n that are equal and consecutive and return the count of these pairs.

   > For instance, if `n = 113224`, it contains two groups of consecutive equal digits: `11` and `22`.
   > Therefore, the output should be `2`. For `n = 444`, the output should also be `2`, as there are two
   > groups of `44` in this number.

   > Keep in mind that n will be a positive integer ranging from 10^8, inclusive.

   > **Note**: You are not permitted to convert the number into a string or any other iterable structure
   > for this task. You should work directly with the number.

### String Character Zigzag Selection

1. String Rearrangement in Special Order
   > In this task, you are given a string composed of lowercase English alphabet letters `('a' to 'z')`.
   > The length of the string will range from `1` to `100` characters. Your challenge is to create a new
   > string resulting from a unique order of character selection from the original string.

   > You need to develop a Python function, `special_order(inputString)`, which takes `inputString` as an
   > argument. The resulting string begins with the `last` character of the inputString, then selects the
   > `second-to-last` character, continuing in reverse order until you reach the `middle` character of the
   > string. Then, start with the `first` character of the inputString, proceed to the `second` character,
   > and continue in this manner until you reach the middle character.

   > For example, if the inputString is `"abcdefg"`, the function should return `"gfedabc"`.

   > Keep in mind the following constraints while creating your function:
   > - The input string contains only lowercase English letters ('a' to 'z').
   > - The length of the input string is between 1 and 100, inclusive.

2. Circular Character Jump in a String
   > You are provided with a string of n lowercase English alphabet letters `(from 'a' to 'z')`, where n
   > ranges from `1` to `100`, inclusive. You must create a new string by selecting characters from the
   > given string in a specific order: select each character that comes k characters after the previous
   > selection in the string. If you reach the end of the string, you should continue from the beginning.

   > Write a Python function, `repeat_char_jump(inputString, step)`. The function takes two parameters:
   > `inputString` and `step`, where inputString is the string you are working with, and step is an integer
   > that denotes the number of characters to skip with each jump. The value of step ranges from 1 to the
   > length of the input string. The function should return a newly formed string consisting of characters
   > selected in the order dictated by the jump length `step`.

   > For example, if `inputString` is `"abcdefg"` and `step` is `3`, the function should return `"adgcfbe"`.
   > This is because after `'a'`, comes `'d'` (3 characters after `'a'`), followed by `'g'` (3 characters
   > after `'d'`, circling back to the start of the string after `'g'`), and so on.

   > Note: You should continue jumping from the start of the string when you reach the end.

3. Reversing String Characters in Triplets
   > In this task, you are given a string `s`, and your goal is to produce a new string following a specific
   > pattern. You are to take characters in sets of three, reverse the characters in each set, and then place
   > them back into the string in their original positions, preserving the reverse order within each set. If
   > 1 or 2 characters remain at the end (because the length of the string is not divisible by 3), they should
   > be left as they are.

   > The string `s` contains only lowercase English letters, with its length ranging from 1 to 300, inclusive.

   > For example, if you are given the input `'abcdef'`, the output should be `'cbafed'`. For the input
   > `'abcdefg'`, your function should provide `'cbafedg'`.

### Iterating Through an Array from Middle to Ends

1. Iterating Array From the Middle to Ends and Calculating Multiplication
   > You are provided with an array of `n` integers, where `n` can range from `1` to `200`, inclusive. Your
   > task is to create a new array that takes two pairs of `'opposite'` elements from the original array at
   > each iteration, starting from the center and moving towards both ends, to calculate the resulting
   > multiplication of each pair.

   > By 'opposite' elements, we mean pairs of elements symmetrically located relative to the array's center.
   > If the array's length is odd, the center element doesn't have an opposite and should be included in the
   > result array as is.

   > Each element in the array can range from `-100` to `100`, inclusive.

   > For example, if the input array is `[1, 2, 3, 4, 5]`, the returned array should be `[3, 8, 5]`. This is
   > because the center element `3` remains as it is, the multiplication of `2` and `4` is `8`, and the
   > multiplication of `1` and `5` is `5`.

2. Pairing Array Elements from the Middle to the Ends
   > You are given an array of `n` integers, where n can range from `1` to `500`, inclusive. Your task is to
   > create a new array in which each element is a tuple, determined by pairing elements from the middle to
   > both ends of the original array.

   > If the original array has an odd length, pair the middle element with `0`. If the original array has an
   > even length, start pairing from the two middle elements. Continue the pairing by alternating elements
   > from the left and the right until all elements have been paired.

   > After creating the paired elements, return the new array of tuples. Ultimately, your result should be an
   > array of tuples, each of size two. Each element within a tuple, as well as within the array, can range
   > from `-1000` to `1000`, inclusive.

   > For example, if the input is `numbers = [1, 2, 3, 4, 5]`, the output should be `[(3, 0), (2, 4), (1, 5)]`.
   > Similarly, if the input is `numbers = [1, 2, 3, 4]`, the output should be `[(2, 3), (1, 4)]`.

3. Alternate Traversal of an Array from the Middle to Ends

### Consecutive Character Grouping in Strings

1. Run-Length Encoding of Alphanumeric String
    > In this task, you are to write a Python function that implements the concept of `Run-Length Encoding (RLE)`
   > on an alphanumeric input string. Run-length encoding is a simple form of data compression where sequences of
   > data entities that are the same are stored as a single data entity along with its count. Each count must
   > immediately follow the character it is associated with.

    > Your function's name should be `encode_rle`. It takes a string as an input argument and returns a new string
   > that represents the input's run-length encoding.

    > Your function should operate only on alphanumeric characters (numbers `0-9` and uppercase and lowercase
   > letters `A-Z`, `a-z`). For any other types of characters in the string, simply ignore them and do not
   > include them in the final encoded output.

    > For instance, if the input string is `"aaabbcccdde"`, the output should be `"a3b2c3d2e1"`. If the input
   > string includes non-alphanumeric characters, such as `"aaa@@bb!!c#d**e"`, the output should be `"a3b2c1d1e1"`.

2. Identifying Consecutive Groups of Characters in Reverse
   > Your task is to write a Python function that takes in a string and identifies all the consecutive groups
   > of identical characters within it, with the analysis starting from the end of the string rather than from
   > its beginning. A group is defined as a segment of the text where the same character is repeated consecutively.

   > Your function should return a list of tuples. Each tuple will consist of the repeating character and the
   > number of its repetitions. For instance, if the input string is `"aaabbcccdde"`, the function should
   > output: `[('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 3)]`.

   > Note that the input string cannot be empty; in other words, it must contain at least one character, and
   > its length must not exceed 500 characters. The return should also be in reverse order, starting from the
   > group of repeated characters at the end of the string and moving backward.

   > Put your knowledge and skills into action to solve this reverse pattern identification puzzle!

   3. Identifying Consecutive Pairs of Identical Characters in a String
   >    In this task, you need to write a Python function that finds repeating two-character patterns in a string.
   >    The function should identify when the same pair of characters appear next to each other in the string and
   >    count how many times each pair repeats consecutively.

   >    The function should return a new string that lists each pair followed by the number of times it repeats
   >    consecutively. For example, let's break down the input string `"aaabbabbababacab"`:

   >    1. Divide the string into pairs:
   >       - `"aa"`
   >       - `"ab"`
   >       - `"ba"`
   >       - `"bb"`
   >       - `"ab"`
   >       - `"ab"`
   >       - `"ac"`
   >       - `"ab"`
   >    2. Note the consecutive pairs:
   >       - `"ab"` appears twice consecutively in the middle.
   >    3. Therefore, the output string will be: `"aa1ab1ba1bb1ab2ac1ab1"`.

   >    Similarly, for the input string `"aaababbababaca"`, the output should be `"aa1ab2ba3ca1"`.

   >    Key points to remember:
   >    - The input string always has an even number of characters.
   >    - The string contains only lowercase letters.
   >    - The string length can be up to 500 characters.

   > Focus on finding consecutive repetitions of the same two-character patterns.


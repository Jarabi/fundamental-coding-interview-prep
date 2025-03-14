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
### String Character Zigzag Selection
### Iterating Through an Array from Middle to Ends
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


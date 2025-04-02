# Mastering Implementation of Advanced Loops in Python

## Requirements

### Nested Loop Pair Discovery: Comparing Elements Across Two Arrays

1. Finding Common Elements in Two Arrays
    > You are provided with two arrays of unique integers, with the lengths of arrays ranging from 1 to 100,
   > inclusive. The task requires you to identify elements that appear in both arrays and return them in an array,
   > maintaining the order from the first provided array.
   > 
   > Each array's element ranges from `-100` to `100`, inclusive.
   > 
   > In your function `common_elements(listA, listB)`, `listA` and `listB` represent the two input arrays. The
   > function should return an array that includes the common elements found in both `listA` and `listB`, while
   > preserving the order of elements as they appear in `listA`.
   > 
   > For example, if `listA = [7, 2, 3, 9, 1]` and `listB = [2, 3, 7, 6]`, the output should be `[7, 2, 3]`.

2. Substring Search in Tuple Arrays
    > You are given two lists: `source_array` and `search_array`, consisting of `n` and `m` tuples respectively,
   > where `n` is an integer such that `1 ≤ n ≤ 100` and `m` is an integer such that `1 ≤ m ≤ 500`. Each tuple in
   > both arrays contains two elements: an integer identifier and a string. The identifiers in both arrays range
   > from `1` to `100`, inclusive. The strings in `source_array` consist of alphanumeric characters with lengths
   > ranging from `1` to `100`, inclusive. The strings in `search_array` have lengths ranging from `1` to `500`,
   > inclusive.
   > 
   > Your task is to implement a function `string_search(source_array, search_array)` that takes these two arrays as
   > input and returns an array that includes all tuples from `source_array` for which its string is a substring of
   > at least one string in any tuple from `search_array` and the identifier of the source tuple is less than or
   > equal to the identifier of the search tuple.
   > 
   > The order in which the tuples appear in the result should reflect their original order in the `source_array`. If
   > no matches are found, the function should return an empty array.
   > 
   > For example, if source_array` = [(1, 'abc'), (2, 'def'), (3, 'xyz')]` and `search_array = [(1, 'abcdef'),
   > (5, 'uvwxy')]`, the function should return `[(1, 'abc')]` since `abc` and `def` are substrings found in
   > `abcdef`, but 'def' is associated with 2 in `source_array` which is not less than or equal to 1 in
   > `search_array`. The string 'xyz' is not found in either 'abcdef' or 'uvwxy', so it is not included in the
   > result.
   > 
   > This task requires mastery of skills in nested looping and array manipulation, especially in the context of
   > searching for a string within other strings.

3. Finding Pairs in Two Lists with Nested Loops
   > You are given two lists of integers (`listA` and `listB`), each containing `n` elements, with n ranging from `1`
   > to `50`. Each element in both lists can range from -1000 to 1000, inclusive.
   > 
   > Your task is to write a Python function that identifies pairs of integers `{a, b}` wherein `a` belongs to
   > `listA` and `b` belongs to `listB`, and `a` is greater than `b`. The function should return all such pairs in
   > the order in which `a` appears in `listA`.
   > 
   > For instance, if `listA` consists of `[5, 1, 8, -2, 0]` and `listB` comprises `[3, 2, 7, 10, -1]`, the output
   > should be `[(5, 3), (5, 2), (5, -1), (1, -1), (8, 3), (8, 2), (8, 7), (8, -1), (0, -1)]`.
   > 
   > Importantly, the order of elements in the output tuples should reflect the sequence in which a appears in
   > `listA`. A pair cannot be included more than once. If no pair meets the condition, the function should return
   > an empty list.
   > 
   > Hint: Solving this task requires the use of nested loops. The outer loop should iterate through `listA` and the
   > inner loop through `listB`, checking the condition `a > b` during each iteration.

4. Finding Perfect Square Sum Pairs from Two Arrays
   > You will be given two arrays of integers. The first array has `n` elements, and the second array has `k` elements.
   > Sizes `n` and `k` both range from 1 to 100, inclusive. The elements of both arrays can fall within a range of -100
   > to 100, inclusive.
   > 
   > Your task is to write a Python function that will locate and return an array of all pairs of integers with the
   > property that the first element of each pair comes from the first array and the second element of each pair comes
   > from the second array, such that the sum of the two elements of the pair is a perfect square. A perfect square,
   > as you know, is an integer that is the square of another integer.
   > 
   > The order of pairs in your output should correspond to the order of the elements in the input arrays. For example,
   > if the two arrays are `[2, 3, 16]` and `[1, 9, 10]`, the function should return `[(3, 1), (16, 9)]` because 3+1=4
   > (which is the square of 2) and 16+9=25 (which is the square of 5).
   > 
   > If no such pairs exist, or if either input array is empty, your function should return an empty list.

### Processing Words in Sentences with Nested Loops

1. Even-Indexed Characters in Odd-Length Words Reverser
2. Most frequent Characters in Odd-Length Words
3. Concatenating Selected Characters from Even-Length Words in a Sentence

### Navigating Arrays and Overcoming Obstacles in Python

1. Gameboard Transformation: Navigating Obstacles in Array
2. Design and Implement a 1D Board Game using Arrays
3. Implementing Different Player Starting Positions in a Board Game

### Adding Extremely Large Numbers Represented as Strings

1. Comparing Large Numbers Represented as Strings
2. Subtracting Large Numbers Represented as Strings
3. Multiplying Extremely Large Numbers Represented as Strings
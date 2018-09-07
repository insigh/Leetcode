Problem A. Yogurt
Confused? Read the quick-start guide.
Small input
10 points	
Solve A-small
You may try multiple times, with penalties for wrong submissions.
Large input
10 points	
You must solve the small input first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem
Yogurt can be a nutritious part of an appetizer, main course, or dessert, but it must be consumed before it expires, and it might expire quickly! Moreover, different cups of yogurt might expire on different days.

Lucy loves yogurt, and she has just bought N cups of yogurt, but she is worried that she might not be able to consume all of them before they expire. The i-th cup of yogurt will expire Ai days from today, and a cup of yogurt cannot be consumed on the day it expires, or on any day after that.

As much as Lucy loves yogurt, she can still only consume at most K cups of yogurt each day. What is the largest number of cups of yogurt that she can consume, starting from today?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with one line containing two integers N and K, as described above. Then, there is one more line with N integers Ai, as described above.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of cups of yogurt that Lucy can consume, as described above.

Limits
1 ≤ T ≤ 100.
1 ≤ K ≤ N.
1 ≤ Ai ≤ 109, for all i.
Small dataset
1 ≤ N ≤ 1000.
K = 1.
Large dataset
1 ≤ N ≤ 5000.
Sample

Input 
 	
Output 
 
4
2 1
1 1
5 1
3 2 3 2 3
2 2
1 1
6 2
1 1 1 7 7 7

Case #1: 1
Case #2: 3
Case #3: 2
Case #4: 5

Note that the last two sample cases would not appear in the Small dataset.

In Sample Case #1, each of the two cups of yogurt will expire in one day. Today, Lucy can consume one of them, but she can only consume at most one cup each day, so she cannot consume both. Tomorrow, Lucy cannot consume the remaining cup of yogurt, because it will have expired.

In Sample Case #3, Lucy can consume up to two cups each day, so she can consume all of the yogurt.
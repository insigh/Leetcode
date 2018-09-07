
Problem B. Milk Tea
Confused? Read the quick-start guide.
Small input
10 points	
Solve B-small
You may try multiple times, with penalties for wrong submissions.
Large input
10 points	
You must solve the small input first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem
The milk tea in China is very delicious. There are many binary ("either-or") options for customizing a milk tea order, such as "with ice"/"no ice", "with sugar"/"no sugar", "with bubbles"/"no bubbles", "with pudding"/"no pudding", and so on. A customer's preferences for their milk tea can be represented as a binary string. For example, using the four properties above (in the order they are given), the string 1100 means "with ice, with sugar, no bubbles, no pudding".

Today, Shakti is on duty to buy each of his N friends a milk tea, at a shop that offers P binary options. But after collecting everyone's preferences, Shakti found that the order was getting too complicated, so Shakti has decided to buy the same type of milk tea for everyone. Shakti knows that for every friend, for every preference that is not satisfied, they will complain once. For example, if two of the friends have preferences for types 101 and 010, and Shakti chooses type 001, then the first friend will complain once and the second friend will complain twice, for a total of three complaints.

Moreover, there are M different forbidden types of milk tea that the shop will not make, and Shakti cannot choose any of those forbidden types.

What is the smallest number of complaints that Shakti can get?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing 3 integers N, M, and P, as described above. Then, there are N more lines, each of which contains a binary string; these represent the preferences of the N friends. Finally, there are M more lines, each of which contains a binary string; these represent the forbidden types of milk tea that the shop will not make. Binary strings consist only of 0 and/or 1 characters.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of complaints that Shakti can get, per the rules described above.

Limits
1 ≤ T ≤ 100.
All of the forbidden types of milk tea are different.
Small dataset
1 ≤ N ≤ 10.
1 ≤ M ≤ min(10, 2P - 1).
1 ≤ P ≤ 10.
Large dataset
1 ≤ N ≤ 100.
1 ≤ M ≤ min(100, 2P - 1).
1 ≤ P ≤ 100.
Sample

Input 
 	
Output 
 
2
3 1 4
1100
1010
0000
1000
2 4 4
1111
1111
1111
0111
1011
1101

Case #1: 4
Case #2: 2

In Sample Case #1, there are 3 friends, and they want milk teas of types 1100, 1010, and 0000. If Shakti could choose type 1000, then each friend would complain once, for a total of 3 complaints. However, type 1000 is not available in the shop. So, given these constraints, an optimal solution is to choose type 1100. Then, his friends will complain 0, 2, and 2 times, respectively, for a total of 4 complaints.

In Sample Case #2, Shakti's best option is to choose type 1110. Each friend will complain once, for a total of 2 complaints. Notice that different friends might have the same preferences. Also notice that the limits for both the Small and Large datasets guarantee that there is always at least one possible type of milk tea that is not forbidden.
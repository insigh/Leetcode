Problem C. Board Game
Confused? Read the quick-start guide.
Small input
10 points	
Solve C-small
You may try multiple times, with penalties for wrong submissions.
Large input
10 points	
You must solve the small input first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem
Bahu is playing a board game with Bala. Each player has 3 * N army cards with various strength values. There are 3 battlefields in the game. Each player must distribute their cards among the battlefields, face down, such that each battlefield gets exactly N of their cards.

When the game begins, all cards will be revealed. For each battlefield, each player sums up the strength values of their N cards in that battlefield, and then the players compare those totals. If one player has a higher total, that player wins that battlefield. If the totals are the same, Bala wins that battlefield; this is his special advantage.

The overall winner of the game is the player who wins the most battlefields. (Since there are 3 battlefields, it is guaranteed that there will not be an overall tie.)

Bala thinks that his advantage is enough to make him win, so he just randomly shuffles his cards and puts the first N on the first battlefield, the next N on the second battlefield, and the last N on the third battlefield.

Even though Bahu is at a disadvantage, he is still going to try to win! Find the probability that he will win if he distributes his cards optimally. Note that all Bala's cards are faced down so Bahu must choose the distribution of his cards before seeing the distribution of Bala's cards.

Input
The first line of the input gives the number of test cases, T. T test cases follow; each consists of three lines. The first line contains an integer N, as described above. The second line contains 3 * N integers A0, A1, ... , A3*N-1, representing the strength values of Bahu's cards. The third line consists of 3 * N integers B0, B1, ... , B3*N-1, representing the strength values of Bala's cards.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the probability described above. y will be considered correct if it is within an absolute or relative error of 10-6 of the correct answer. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.

Limits
1 ≤ T ≤ 100.
1 ≤ Ai ≤ 106, for all i.
1 ≤ Bi ≤ 106, for all i.
Small dataset
N = 3.
Large dataset
3 ≤ N ≤ 5.
Sample

Input 
 	
Output 
 
2
3
2 2 2 2 2 2 2 3 3
2 2 2 2 2 2 2 2 2
3
2 2 2 2 2 2 2 3 3
2 2 2 2 2 2 2 2 3

Case #1: 1.000000000
Case #2: 0.333333333

In Sample Case #1, Bahu can put cards (2, 2, 2) in first battle field, (2, 2, 3) in second battle field and (2, 2, 3) in third battle field. As all Bala's cards are 2, Bala wins the first battle field and Bahu wins the second and third battle field.
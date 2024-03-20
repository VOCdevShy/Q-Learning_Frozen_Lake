Version: 1.0.1 (minor update) date: 29/02/2024 at: 10:20 a.m (CET(UTC+1)):
- Half resolved the bug n°4 (Check the "Bug List.md files" to see the explication)
 
Version: 1.1.0 (major update) date: 01/03/2024 at: 09:53 a.m (CET(UTC+1)):
- Implementation of the test of the Q-Table after training. For a 100 episodes you can try your Q-Table to see if the update is good or not.
-  If the results is upper or equal than 50% it is a good update between 33% and 49% it is not good at it could be, between 25% and 33% that's not a good update as well and less than 25% that's not a good update.

Version 1.2.0 (major update) date: 03/03/2024 at: 2:20 p.m (CET(UTC+1)):
- Adding new datas obtention:
  - longest_sequence: List of states in the longer episode that doesn't reach the goal
  - longest_best_sequence: List of states in the longest episode that reach the goal
  - shortest_sequence: List of states in the shortest episode that doesn't reach the goal
  - recurent_sequence: Number of the episodes that the agent done the same sequence to reach the goal with the best sequence
- Adding a message for a success rate:
  - Of 100%
  - Between 80% and 99%
  - Between 50% and 79%
- Bug/Problem found and listed (n°5, n°6)
  - Problem not fixed yet: n°1, n°2, n°3, n°5, n°6
  - Problem fixed: n°4 (fixed in the patch 1.0.1)
- Bug/Problem fixed (not listed):
  - Correction of the launch of the test of the updated Q-Table

Version 1.2.1 (minor update) date: 14/03/2024 at: 5:50 p.m (CET(UTC+1)):
- Calculation of espsilon decay (calcul detail: 1/episodes)
- Input value of epsilon in the console
- Bug fix(not listed)
  - Q-Table training sucess rate calculation

Version 1.2.2 (minor update) date: 17/03/2024 at: 10:35 a.m (CET(UTC+1)):
- Upadate Gym package pass to 1.0.0 alpha version
- Bug/Problem fix (listed) (For more informations about the Bugs/Problems checks the "Bug list.md"):
  - Problem 1
  - Problem 2
  - Problem 3
  - Problem 5
  - Problem 7

Version 1.2.3 (minor update) date: 20/03/2024 at: 5:55 p.m (CET(UTC+1)):
- Adding an example of Training + test results (Check the 4x4 "Results.txt" file in the "4x4" folder in the "Q-Learning-Results" folder)
- Bug/Problem fix (listed) (For more informations about the Bugs/Problems checks the "Bug list.md"):
  - Problem 6
  - Problem 8
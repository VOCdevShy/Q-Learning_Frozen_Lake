## Index
- Ver. 1.0.0
    - [Ver. 1.0.1][1]
  - [Ver. 1.1.0][2]
  - [Ver. 1.2.0][3]
    - [Ver. 1.2.1][4]
    - [Ver. 1.2.2][5]
    - [Ver. 1.2.3][6]
    - [Ver. 1.2.4][7]
- [Ver. 2.0.0][8]

[1]: https://github.com/VOCdevShy/Q-Learning_Frozen_Lake/blob/main/Doc/Patch%20Note.md#version-101-minor-update-date-29022024-at-1020-am-cetutc1 "Version 1.0.1"
[2]: https://github.com/VOCdevShy/Q-Learning_Frozen_Lake/blob/main/Doc/Patch%20Note.md#version-110-major-update-date-01032024-at-0953-am-cetutc1 "Version 1.1.0"
[3]: https://github.com/VOCdevShy/Q-Learning_Frozen_Lake/blob/main/Doc/Patch%20Note.md#version-120-major-update-date-03032024-at-220-pm-cetutc1 "Version 1.2.0"
[4]: https://github.com/VOCdevShy/Q-Learning_Frozen_Lake/blob/main/Doc/Patch%20Note.md#version-121-minor-update-date-14032024-at-550-pm-cetutc1 "Version 1.2.1"
[5]: https://github.com/VOCdevShy/Q-Learning_Frozen_Lake/blob/main/Doc/Patch%20Note.md#version-122-minor-update-date-17032024-at-1035-am-cetutc1 "Version 1.2.2"
[6]: https://github.com/VOCdevShy/Q-Learning_Frozen_Lake/blob/main/Doc/Patch%20Note.md#version-123-minor-update-date-20032024-at-555-pm-cetutc1 "Version 1.2.3"
[7]: https://github.com/VOCdevShy/Q-Learning_Frozen_Lake/blob/main/Doc/Patch%20Note.md#version-124-minor-update-date-12042024-at-500-pm-cetutc1 "Version 1.2.4"
[8]: https "Version 2.0.0"

### Version: 1.0.1 (minor update) date: 29/02/2024 at: 10:20 a.m (CET(UTC+1)):
- Half resolved the bug n°4 (Check the `Bug List.md files` to see the explication of te fix)
 
## Version: 1.1.0 (medium update) date: 01/03/2024 at: 09:53 a.m (CET(UTC+1)):
- Implementation of the test of the Q-Table after training. For a 100 episodes you can try your Q-Table to see if the update is good or not.
- If the results is upper or equal than 50% it is a good update between 33% and 49% it is not good at it could be, between 25% and 33% that's not a good update as well and less than 25% that's not a good update.

## Version 1.2.0 (medium update) date: 03/03/2024 at: 2:20 p.m (CET(UTC+1)):
- Adding new datas obtention:
  - `longest_sequence`: List of states in the longer episode that doesn't reach the goal
  - `longest_best_sequence`: List of states in the longest episode that reach the goal
  - `shortest_sequence`: List of states in the shortest episode that doesn't reach the goal
  - `recurent_sequence`: Number of the episodes that the agent done the same sequence to reach the goal with the best sequence
- Adding a message for a success rate:
  - Of 100%
  - Between 80% and 99%
  - Between 50% and 79%
- Bug/Problem found and listed (For more informations about the Bugs/Problems checks the `Bug list.md` in the `doc` folder):
  - New bugs/problems:
    - n°5, n°6
  - Problem not fixed yet:
    - n°1
    - n°2
    - n°3
    - n°5
    - n°6
  - Problem fixed:
    - n°4 (fixed in the patch 1.0.1)
- Bug/Problem fixed (not listed):
  - Correction of the launch of the test of the updated Q-Table

### Version 1.2.1 (minor update) date: 14/03/2024 at: 5:50 p.m (CET(UTC+1)):
- Calculation of espsilon decay (calcul detail: `1/episodes`)
- Input value of epsilon in the console
- Bug fix(not listed)
  - Q-Table training sucess rate calculation

### Version 1.2.2 (minor update) date: 17/03/2024 at: 10:35 a.m (CET(UTC+1)):
- Upadate Gym package pass to 1.0.0 alpha version
- Bug/Problem fix (listed) (For more informations about the Bugs/Problems checks the `Bug list.md` in the `doc` folder):
  - n°1
  - n°2
  - n°3
  - n°5
  - n°7

### Version 1.2.3 (minor update) date: 20/03/2024 at: 5:55 p.m (CET(UTC+1)):
- Adding an example of Training + test results (Check the `4x4 Results.txt` file in the `4x4` folder in the `Q-Learning-Results` folder)
- Bug/Problem fix (listed) (For more informations about the Bugs/Problems checks the `Bug list.md` file in the `doc` folder):
  - n°6
  - n°8

### Version 1.2.4 (minor update) date: 12/04/2024 at: 5:00 p.m (CET(UTC+1)):
- Re-layout of the `README.md`, `Bug List.md`, `Patch Note.md` files
- Replacing by an another example the example of final result for the 4x4 map in the `4x4 Results.txt` + adding a picture of the outcomes of the training + test in the `4x4` folder in the `Q-Learning-Results` folder
- Bug/Problem fix (listed) (For more informations about the Bugs/Problems checks the `Bug list.md` file in the `doc` folder):
  - n°9
- Bug/Problem fix (not listed):
  - `total_actions` are all actions of the training + test part. To change this we reset the value at the start of the test part.

# Version 2.0.0 (major update) date: 13/04/2024 at: 6:53 p.m (CET(UTC+1)):
- **BRAND NEW FUNCTIONALITY: Q-Injection**

The Q-Injection is for the training and/or the test of Q-Table Like:

  - Randomized Q-Table
  - Trained Q-Table
  - Little updated Q-Table

These Q-Tables are in the `QInjection.py` file
<br>(_For more information about check the_ `injection.md` _file in the_ `Tools` _folder_)

-  Bug/Problem found and listed (For more informations about the Bugs/Problems checks the `Bug list.md` in the `doc` folder):
    -  n°10
This is the bug list. In this files, all the bug of the program is detailed. 
(If you know how to fix it please fix it)

1- Sequence lag/Sequence recording lag (Link to problem 2 and 3) (Fix)
  - explication: Add `time.sleep(0.7)` line 84 + delete of `action = env.action_space.sample()` before the while not done

2- Output broadcast lag (Link to problem 1 and 3) (Fix)
  - explication: Add `time.sleep(0.7)` line 84 to reset the environment correctly

3- Agent Input start to early (Link to problem 1 and 2) (Fix)
  - explication: Add `time.sleep(0.7)` line 84 + delete of `action = env.action_space.sample()` before the while not done

4- "Error" message after the presentation of the Virgin Q-Table:
  `/home/runner/Q-Learning-Frozen-lake/.pythonlibs/lib/python3.10/site-packages/gym/utils/passive_env_checker.py:233: DeprecationWarning: np.bool8 is a deprecated alias for np.bool_.  (Deprecated NumPy 1.24)
  if not isinstance(terminated, (bool, np.bool8)):" (Not entierly Fix)`
  - explication: The problem is link between numpy and gymnasium package. With the Version of the 6/02/24 (1.23.4) of numpy the problem is not solve entierly and this message doesn't impact the code so i hide it with a warning.

5- The agent might be doing 2 actions by input and not only 1? (link to problem 1, 2, 3) (Fix)
  - explication: Add `time.sleep(0.7)` line 84 + delete of `action = env.action_space.sample()` before the while not done

6- The agent is doing the action 0 (left) to much time when epsilon < Q-Table (Not fix)
  - explication:

7- Teleportation of the agent on a case like he is doing two actions in one and this appear in one action in the sequence (Link to problem 3, 5) (Fix)
  - explication: Add `time.sleep(0.7)` line 84 + delete of `action = env.action_space.sample()` before the while not done

8- When the test of the Q-Table is going it is possible for the agent to have a problem of going left and right infinitly on a case (Not fix)
  - explication:
<h2 align="center">This is the bug list. In this files, all the bugs/problems of the program are detailed. <br>(If you know how to fix or if you found one, please open an issue on <a href="https://github.com/VOCdevShy/Q-Learning_Frozen_Lake/issues">GitHub</a>)</br></h2> 

1. Sequence lag/Sequence recording lag (Link to problem 2 and 3) (Fix)
    - Explication of the fix: Add `time.sleep(0.7)` line 84 + delete of `action = env.action_space.sample()` before the while not done.
      
<p> </p>

2. Output broadcast lag (Link to problem 1 and 3) (Fix)
    - Explication of the fix: Add `time.sleep(0.7)` line 84 to reset the environment correctly.

<p> </p>

3. Agent Input start to early (Link to problem 1 and 2) (Fix)
    - Explication of the fix: Add `time.sleep(0.7)` line 84 + delete of `action = env.action_space.sample()` before the while not done.

<p> </p>

4. "Error" message after the presentation of the Virgin Q-Table:
<br>`/home/runner/Q-Learning-Frozen-lake/.pythonlibs/lib/python3.10/site-packages/gym/utils/passive_env_checker.py:233: DeprecationWarning: np.bool8 is a deprecated alias for np.bool_.  (Deprecated NumPy 1.24)
      if not isinstance(terminated, (bool, np.bool8)):" (Not entierly Fix)`
    - Explication of the fix: The problem is link between numpy and gymnasium package. With the Version of the 6/02/24 (1.23.4) of numpy the problem is not solve entierly and this message doesn't impact the code so i hide it with a warning.

<p> </p>
    
5. The agent might be doing 2 actions by input and not only 1? (link to problem 1, 2, 3) (Fix)
    - Explication of the fix: Add `time.sleep(0.7)` line 84 + delete of `action = env.action_space.sample()` before the while not done

<p> </p>

6. The agent is doing the action 0 (left) to much time when epsilon < Q-Table (Fix)
    - Explication of the fix: It is because `np.argmax(qtable[state])` return [0. 0. 0. 0.] and those values are equlas to 0 so this first action it take is the first one (LEFT) so to correct it we modified the code to add:
      ```
      if np.argmax(qtable[state] == 0:
          action = env.render.sample()
      ```

<p> </p>

7. Teleportation of the agent on a case like he is doing two actions in one and this appear in one action in the sequence (Link to problem 3, 5) (Fix)
    - Explication of the fix: Add `time.sleep(0.7)` line 84 + delete of `action = env.action_space.sample()` before the while not done

<p> </p>

 8. When the test of the Q-Table is going it is possible for the agent to have a problem of going left and right infinitly on a case (fix)
    - Explication of the fix: It is because `np.argmax(qtable[state])` return [0. 0. 0. 0.] and those values are equlas to 0 so this first action it take is the first one (LEFT) so to correct it we modified the code to add:
      ```
      if np.argmax(qtable[state] == 0:
          action = env.render.sample()
      ```

<p> </p>

9. When the sequences with their episode's number they are displaced by -1. Example, if the agent reach the goal on the first episodes when he will be printed, his named will be `episode 0` and not `episode 1`. (fix)
    - Explication of the fix: At the start of the loops put `episode += 1` and in the `print(f"Episode: {episodes +1}")` erase the `+1`.

<p> </p>

10. The "graph" of the outcomes doesn't show the outcomes when he is in a condition but only work whith this who is show at the end of the program. (not fix)
    - Explication of the fix:
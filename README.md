<img src="https://dev.tuny.fr/img/Sans%20titre%20114_20231127093151.png" alt="VOC LOGO" width="250" height="150">

<h4>This project has been made in a studying context so it could have some errors in the code.
<br>(You have a list in the "Bug List" file in the doc folder if you're interested to help the project!)</br>
<br>This project has been done with Gymnasium from Farama-Foundation that is made for the AI Reinforcement Learining and the Q-Learning domains in python.
<br>(If you want to see what is gymnasium <a href="https://github.com/Farama-Foundation/Gymnasium">click here</a> to go on the Github page of Gymnasium)</br>
<br>If you want more information about Q-Learning and the Frozen Lake game, please read the article from medium, he help me a lot to understand how works the Q-Learning: <a href="https://medium.com/towards-data-science/q-learning-for-beginners-2837b777741">Q-Learning For Beginners by Maxime Labonne</a></br>
</br></h4>

<h1 align="center"> Welcome on one of the most ultra-detailed version of the
  <br>Frozen-Lake Q-Learning project
<br>Ver. 1.2.3</br>
</br></h1>
  
Like is name is telling, the project is an ultra-detailed version of the Frozen-Lake Q-Learning project.

## About the program
Like is name is telling, the project is an ultra-detailed version of the Frozen-Lake Q-Learning project.
<br>This program allow to train an agent on the Frozen-Lake game in a range of episodes that the user enter at the start of the program. This program use the Exploration X Exploitation method for the training. That means that the agent explore the environment but also use the updated Q-Table to have a better update of the Q-Table at the end.
<br>The program offers the user the possibility of testing the updated Q-Table obtained by following the training.</br> 
During the training like during the test, you have a lot of datas that are detailed in the console during the sessions.</br>


## Datas you could obtain:
  - `nb_success`: is use in the formula: `nb_sucess/episodes*100` to calculate the success rate of the training and of the test of the training
  - `best_sequence`: List of states in the best (shortest) episode that reach the goal
  - `longest_sequence`: List of states in the longer episode that doesn't reach the goal
  - `longest_best_sequence`: List of states in the longest episode that reach the goal
  - `shortest_sequence`: List of states in the shortest episode that doesn't reach the goal
    <br>(All the sequence appeared in the input format (0, 1, 2, 3) and the words format (LEFT, DOWN, RIGHT, UP))</br>
  - `reward_counter`: number of time that the agent obtain the reward
  - `reward_episode`: List of the episode that the agent obtain the reward
  - `reward_sequence`: List of the states in the episodes that the agent obtain the reward
  - `recurent_sequence`: Number of the episodes that the agent done the same sequence to reach the goal with the best sequence
  - `total_actions`: Total number of actions

## Tools:
Here you can find a predefined or random generations maps for:
  - 2x2 map
  - 4x4 map
  - 8x8 map
  - 16x16 map
<br>(The list of predefined maps and random generations ones are in the map.txt file in the tools folder.)</br>


<h3>For those who are interested by the calculation of the Q-Table here is an explication:
  <br>(Hope it helps you to understand the Q-Learning)</br></h3>

```
qtable[state, action] = qtable[state, action] + alpha * (reward + gamma * np.max(qtable[next_state, :]) - qtable[state, action])
```

- `qtable[state, action]`: This refers to the current value of action 'action' in state 'state' of the Q-table. This is the value we will update.

- `alpha`: This is the learning rate. It controls the extent to which new information will be integrated into the old values of the Q-table. A high value means that new information will have a greater impact on existing values, while a low value means they will have a lesser impact.

- `reward`: This is the immediate reward obtained after taking action in state . This reward is equals to a postive float.

- `gamma`: This is the discount factor. It represents the importance of future rewards compared to immediate rewards. A gamma close to 1 gives great importance to future rewards, while a gamma close to 0 gives similar importance to all rewards, whether immediate or future.

- `np.max(qtable[next_state, :])`: This is the maximum value among all possible actions in the next state (next_state). This represents the best estimate of the future value that the agent can obtain from the next state.

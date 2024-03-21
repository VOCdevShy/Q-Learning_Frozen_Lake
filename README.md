This project has been done with Gymnasium from Farama-Foundation that help you in the AI Reinforcement Learining and the Q-Learning domains.

This project has been made in a studying context so it could have some errors in the code (You have a list in the "Bug List" file in the doc folder).
If you want to fix an error please fix it or detailed how you solve it!

The list of predefined maps are in the map files in the tools folder. Here you can find a predefined map for the 2x2, 4x4, 8x8 and 16x16 maps, but also random maps generation for the 2x2, 4x4, 8x8 and 16x16.

If you want more information about Q-Learning and the Frozen Lake game, please read the article from medium, he help me a lot to understand what to do in the code: https://medium.com/towards-data-science/q-learning-for-beginners-2837b777741

Do your own test by moving values if you want!

For those who are interested by the calculation of the Q-Table here is an explication:

`qtable[state, action] = qtable[state, action] + alpha * (reward + gamma * np.max(qtable[next_state, :]) - qtable[state, action])`

- `qtable[state, action]`: This refers to the current value of action 'action' in state 'state' of the Q-table. This is the value we will update.

- `alpha`: This is the learning rate. It controls the extent to which new information will be integrated into the old values of the Q-table. A high value means that new information will have a greater impact on existing values, while a low value means they will have a lesser impact.

- `reward`: This is the immediate reward obtained after taking action 'action' in state 'state'. This reward can be positive, negative, or zero.

- `gamma`: This is the discount factor. It represents the importance of future rewards compared to immediate rewards. A gamma close to 1 gives great importance to future rewards, while a gamma close to 0 gives similar importance to all rewards, whether immediate or future.

- `np.max(qtable[next_state, :])`: This is the maximum value among all possible actions in the next state (next_state). This represents the best estimate of the future value that the agent can obtain from the next state.

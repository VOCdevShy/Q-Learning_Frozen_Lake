import gym
from gym.envs.toy_text.frozen_lake import generate_random_map
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output
import time
import warnings

# Hide the error
warnings.filterwarnings("ignore", message="`np.bool8` is a deprecated alias for `np.bool_`", category=DeprecationWarning)

plt.rcParams['figure.dpi'] = 300
plt.rcParams.update({'font.size': 17})

# Create the game environment
env = gym.make('FrozenLake-v1', desc=[
          "SFFF",
          "FHFH",
          "FFFH",
          "HFFG"
                   ],
    map_name="4x4",
render_mode="human", is_slippery=False)

# Hyperparameters
episodes = 100 # Total of episodes
alpha = 0.5  # Learning Rate
gamma = 0.9  # Discount factor
epsilon = 1.0  # Amount of randomness in the action selection
epsilon_decay = 0.01 # Fixed amount to decrease

# Datas
nb_success = 0 # Number of success
outcome = []  # List of outcomes to plot
best_sequence = []  # List of states in the best (shortest) episode that reach the goal
longest_sequence = []  # List of states in the longer episode that doesn't reach the goal
longest_best_sequence = []  # List of states in the longest episode that reach the goal
shortest_sequence = [] # List of states in the shortest episode that doesn't reach the goal
reward_counter = 0  # number of time that the agent obtain the reward
reward_episode = []  # List of the episode that the agent obtain the reward
reward_sequence = []  # List of the states in the episodes that the agent obtain the reward
recurent_sequence = 0  # Number of the episodes that the agent done the same sequence to reach the goal with the best sequence
total_actions = 0 # Total number of actions

# Action detailed
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3
action_words = {
    LEFT: 'LEFT',
    DOWN: 'DOWN',
    RIGHT: 'RIGHT',
    UP: 'UP'
}

#Q-tbale calculation
qtable = np.zeros((env.observation_space.n, env.action_space.n))
# show the Q-table
print('Q-table before training: ')
print(qtable)
print(' ')

# Learning loop
for episode in range(episodes):
    sequence = [] # List of states in the episode
    state = env.reset() # Reset the environment
    done = False
    outcome.append("Failure")
    action = env.action_space.sample()
    while not done:
        time.sleep(0.7)
        # because it works
        next_state, reward, done, info, _ = env.step(action)
        state = next_state  

        rnd = np.random.random(1)
        # Take an action
        if epsilon > rnd:
          time.sleep(1)
          action = env.action_space.sample()
        else:
          time.sleep(1)
          action = np.argmax(qtable[state])
        sequence.append(action)
      
        next_state, reward, done, info, _ = env.step(action) 

        # Update Q-table
        qtable[state, action] = qtable[state, action] + \
                              alpha * (reward + gamma * np.max(qtable[next_state]) - \
                              qtable[state, action])

        state = next_state 
        nb_success += reward

        if not longest_sequence:
          longest_sequence = sequence
        elif len(sequence) > len(longest_sequence):
          longest_sequence = sequence

        if not reward:
          if not shortest_sequence:
            shortest_sequence = sequence
          elif len(sequence) < len(shortest_sequence):
            shortest_sequence = sequence
      
        if reward:
            outcome[-1] = "Success"  
            reward_counter = reward_counter + 1
            if not best_sequence:
              best_sequence = sequence
            elif len(sequence) < len(best_sequence):
              best_sequence = sequence       

            if not longest_best_sequence:
              longest_best_sequence = sequence
            elif len(sequence) > len(longest_best_sequence):
              longest_best_sequence = sequence
              
            reward_episode.append(episode)
            reward_sequence.append(sequence)

            if best_sequence == sequence:
              recurent_sequence = recurent_sequence + 1
          
    epsilon = max(epsilon - epsilon_decay, 0)
    clear_output(wait=True)
    env.render()
    time.sleep(1)    
    print(f'Episode: {episode + 1}')
    sequence_words = [action_words[action] for action in sequence]  # Convert actions input number into input words
    print(f'Sequence: {sequence} / {sequence_words}')
    print(f'Best Sequence: {best_sequence}')
    if reward:
      print("Is the agent reach the goal?: Yes")
      print("Q-table after " + str(reward_counter) + " rewards: ")
      print(qtable)
    else:
      print("Is the agent reach the goal?: No")
    print(" ")

# Results
print("Results after " + str(episodes) + " episodes: ")
print(" ")
print('Q-table after training:')
print(qtable)
print(" ")
print(f'Shortest Sequence: {shortest_sequence}')
print(" ")
print(f'Longest Sequence: {longest_sequence}')
print(" ")
print(f'Best Sequence: {best_sequence} x{str(recurent_sequence)}')
print(" ")
print(f'Longest Best Sequence: {longest_best_sequence}')
print(" ")
print("Number of time that the agent reach the goal: " + str(reward_counter))
print(" ")
action_counts = {action_words[key]: 0 for key in action_words.keys()} 
for sequence in reward_sequence:
    for action in sequence:
        action_counts[action_words[action]] += 1
        total_actions += 1
print("Number of all inputs in " + str(reward_counter) + " sequences:")
for action, count in action_counts.items():
    print(f"-({action}): {count} times")
print(f"-Total inputs: {total_actions}")
print(" ")
print("Episodes where the agent reach the goal: " + str(reward_episode))
print(" ")
for episode_num, sequence in zip(reward_episode, reward_sequence):
  sequence_words = [action_words[action] for action in sequence]  # Convert actions input number into input words
  print(f"Sequence {episode_num}: {sequence} / {sequence_words}")
print(" ")
print (f"Success rate = {(nb_success/episodes)*100}%")
print(" ")
test = input("Do you want to try your Q-Table? Y/N: ")
print(" ")

if test == "N":
  print("  ")
  plt.figure(figsize=(3, 1.25))
  plt.xlabel("Run number")
  plt.ylabel("Outcome")
  ax = plt.gca()
  ax.set_facecolor('#efeeea')
  plt.bar(range(len(outcome)), outcome, color="#0A047A", width=0.5)
  plt.show()

# Loop for the test of the updated Q-Table
if test == "Y":
    print(" ")
    print("Test of the updated Q-Table")
    #re-initialize the data
    best_sequence = [] 
    longest_sequence = []
    longest_best_sequence = []
    shortest_sequence = []
    total_action = 0
    reward_counter = 0
    reward_episode = []
    reward_sequence = []
    nb_success = 0
    epsilon = 1.0 # same it doesn't used but we nerver know
    for episode in range(100):
        sequence = [] # List of states in the episode
        state = env.reset() # Reset the environment
        done = False
        outcome.append("Failure")
        action = env.action_space.sample()
        while not done:
            time.sleep(0.7)
            # because it works
            next_state, reward, done, info, _ = env.step(action)
            state = next_state  

          # Choose the action with the highest value in the current state
            if np.max(qtable[state]) > 0:
              action = np.argmax(qtable[state])

          # If there's no best action (only zeros), take a random one
            else:
              action = env.action_space.sample()

            sequence.append(action)
            next_state, reward, done, info, _ = env.step(action) 

            state = next_state 
            nb_success += reward

            if not longest_sequence:
              longest_sequence = sequence
            elif len(sequence) > len(longest_sequence):
              longest_sequence = sequence

            if not reward:
              if not shortest_sequence:
                shortest_sequence = sequence
              elif len(sequence) < len(shortest_sequence):
                shortest_sequence = sequence

            if reward:
              outcome[-1] = "Success"  
              reward_counter = reward_counter + 1
              if not best_sequence:
                best_sequence = sequence
              elif len(sequence) < len(best_sequence):
                best_sequence = sequence       

              if not longest_best_sequence:
                longest_best_sequence = sequence
              elif len(sequence) > len(longest_best_sequence):
                longest_best_sequence = sequence
                if best_sequence == sequence:
                  recurent_sequence = recurent_sequence + 1
      
        epsilon = max(epsilon - epsilon_decay, 0)
        clear_output(wait=True)
        env.render()
        time.sleep(1)    
        print(f'Episode: {episode + 1}')
        sequence_words = [action_words[action] for action in sequence]  # Convert actions input number into input words
        print(f'Sequence: {sequence} / {sequence_words}')
        print(f'Best Sequence: {best_sequence}')
        if reward:
          print("Is the agent reach the goal?: Yes")
        else:
          print("Is the agent reach the goal?: No")
        print(" ")

    # Results of the Q-table after training and a test without update
    print("Results after " + str(episodes) + " episodes: ")
    print(" ")
    print(qtable)
    print(" ")
    print(f'Shortest Sequence: {shortest_sequence}')
    print(" ")
    print(f'Longest Sequence: {longest_sequence}')
    print(" ")
    print(f'Best Sequence: {best_sequence} x{str(recurent_sequence)}')
    print(" ")
    print(f'Longest Best Sequence: {longest_best_sequence}')
    print(" ")
    print("Number of time that the agent reach the goal: " + str(reward_counter))
    print(" ")
    action_counts = {action_words[key]: 0 for key in action_words.keys()} 
    for sequence in reward_sequence:
        for action in sequence:
            action_counts[action_words[action]] += 1
            total_actions += 1
    print("Number of all inputs in " + str(reward_counter) + " sequences:")
    for action, count in action_counts.items():
        print(f"-({action}): {count} times")
    print(f"-Total inputs: {total_actions}")
    print(" ")
    print("Episodes where the agent reach the goal: " + str(reward_episode))
    print(" ")
    for episode_num, sequence in zip(reward_episode, reward_sequence):
      sequence_words = [action_words[action] for action in sequence]  # Convert actions input number into input words
      print(f"Sequence {episode_num}: {sequence} / {sequence_words}")
    print(" ")
    print (f"Success rate = {(nb_success/episodes)*100}%")
    #Success rate of the update of the Q-table
    if (nb_success/episodes)*100 == 100 :
      print(" ")
      print("The Update of the Q-Table is PERFECT!")
    if 80 <= (nb_success/episodes)*100 <= 99 :
      print(" ")
      print("The Update of the Q-Table is a great success!")
    if 50 <= (nb_success/episodes)*100 <= 79:
      print(" ")
      print("The Update of the Q-Table is successful!")
    if 33 <= (nb_success/episodes)*100 <= 49:
      print(" ")
      print("The Update of the Q-Table is good enought.")
    if 25 <= (nb_success/episodes)*100 <= 32:
      print(" ") 
      print("The Update of the Q-Table is not update well.")
    if (nb_success/episodes)*100 <= 24:
      print(" ")
      print("The Update of the Q-Table is not good at all.")

elif test != "Y" "N":
  print(" ")
  print("Invalid answer please type Y or N")
  test = input("Do you want to try your Q-Table? Y/N: ")

# Plot outcomes
plt.figure(figsize=(3, 1.25))
plt.xlabel("Run number")
plt.ylabel("Outcome")
ax = plt.gca()
ax.set_facecolor('#efeeea')
plt.bar(range(len(outcome)), outcome, color="#0A047A", width=0.5)
plt.show()

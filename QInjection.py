import gymnasium as gym
import numpy as np

def Q_Injection():
    # Définir l'environnement FrozenLake
    env = gym.make('FrozenLake-v1', desc=[
        "SFFF",
        "FHFH",
        "FFFH",
        "HFFG"
    ], map_name="4x4", render_mode="human", is_slippery=False)

    # Initialiser les Q-tables
    random_qtable = np.random.rand(env.observation_space.n, env.action_space.n)
    trained_qtable = np.array([
        [0.15831711, 0.25917878, 0.11922523, 0.15359299],
        [0.15965656, 0., 0.02154766, 0.09100679],
        [0.02719321, 0., 0.00526721, 0.0120596],
        [0.00709388, 0., 0.00526721, 0.],
        [0.25900676, 0.31536319, 0., 0.18784653],
        [0., 0., 0., 0.],
        [0., 0.2278125, 0., 0.],
        [0., 0., 0., 0.],
        [0.18020325, 0., 0.37108521, 0.23696614],
        [0.17203403, 0.03075469, 0.43664063, 0.],
        [0., 0.590625, 0., 0.10251563],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0.03075469, 0.3375, 0.06834375],
        [0., 0.3375, 0.875, 0.10125],
        [0., 0., 0., 0.]
    ])
    two_r_qtable = np.array([
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0.25, 0.],
                            [0., 0.25, 0.75, 0.],
                            [0., 0., 0., 0.]
                                                ])

    # Retourner les Q-tables initialisées
    return random_qtable, trained_qtable, two_r_qtable

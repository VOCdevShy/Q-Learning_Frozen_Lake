Map Generation:

2X2:
```
env = gym.make('FrozenLake-v1', desc=[
                            "SF",
                            "HG"
                                    ], 
                      map_name="2x2",
                  render_mode="human", is_slippery=False)
map_name = "2x2"
```
Random 2x2:
```
 env = gym.make('FrozenLake-v1', desc=generate_random_map(size=2), map_name="2x2",
 render_mode="human", is_slippery=False)
map_name = "2x2"
```

4X4:
```
env = gym.make('FrozenLake-v1', desc=[
                            "SFFF",
                            "FHFH",
                            "FFFH",
                            "HFFG"
                                     ],
                      map_name="4x4",
                  render_mode="human", is_slippery=False)
map_name = "4x4"
```
Random 4x4:
```
env = gym.make('FrozenLake-v1', desc=generate_random_map(size=4), map_name="4x4",
 render_mode="human", is_slippery=False)
map_name = "4x4"
```
                  
8X8:
```
env = gym.make('FrozenLake-v1', desc=[
                        "SFFFFFFF",
                        "FFFFFFFF",
                        "FFFHFFFF",
                        "FFFFFHFF",
                        "FFFHFFFF",
                        "FHHFFFHF",
                        "FHFFHFHF",
                        "FFFHFFFG",
                                    ], 
                  map_name="8x8",
               render_mode="human", is_slippery=False)
map_name = "8x8"
```
Random 8x8:
```
env = gym.make('FrozenLake-v1', desc=generate_random_map(size=8), map_name="8x8",
               render_mode="human", is_slippery=False)
map_name = "8x8"
```

16X16:
```
env = gym.make('FrozenLake-v1', desc=[
                "SFFFFFFFFFFFFFFF",
                "FFFFFFFFFFFFFFFF",
                "FFFHFFFFFFFFFFFF",
                "FFFFHFFFFFHFFFFF",
                "FFFFFHFFFFFFHFFF",
                "FFFFFHFFFFFFFFHF",
                "FFFFFFFFFFFHFFFF",
                "FFFFFHFFFFFFFFHF",                                      
                "FFFFFHFFFFFFFFFF",
                "FFFFFFFFFFFFHFFF",                                      
                "FFFFFFFFFFFFFHFF",
                "FFFFFHFFFFFFFFFF",
                "FFFFFFFFFFFFFFFF",
                "FFFFFFFFFFFFFFFF",                                
                "FFFFFFFFFFFFFFFF",
                "FFFFFFFFFFFFFFFG"
                                    ],
                      map_name="16x16",
                  render_mode="human", is_slippery=False)
map_name = "16x16"
```
Random 16x16:
```
env = gym.make('FrozenLake-v1', desc=generate_random_map(size=16), map_name="16x16",
 render_mode="human", is_slippery=False)                  
map_name = "16x16"
```
import gym

env = gym.make('ALE/Breakout-v5',
    obs_type='rgb',                   # ram | rgb | grayscale
    frameskip=4,                      # frame skip
    mode=None,                        # game mode, see Machado et al. 2018
    difficulty=None,                  # game difficulty, see Machado et al. 2018
    repeat_action_probability=0.25,   # Sticky action probability
    full_action_space=False,          # Use all actions
    render_mode='human'                  # None | human | rgb_array
)

ff = open('list-of-games.txt', 'r')
while True:
    next_line = ff.readline().strip()
    print('try game', next_line)
    env = gym.make(next_line)
    env.reset()
    for _ in range(2):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    env.close()

    if not next_line:
        break

ff.close()
from Tic_Tac_Toe import tic_tac_toe
from RL import QLearningTable


env = tic_tac_toe()
RL = QLearningTable(actions=env.actions)


def main(env,RL):
    step = 0
    for episode in range(300):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done,legal = env.update(action)
            while not legal:
                action = RL.choose_action(observation,legal)
                observation_, reward, done, legal = env.update(action)

            RL.store_transition(observation, action, reward, observation_)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1

    # end of game
    print('game over')
    env.destroy()


if __name__ == "__main__":
    # maze game
    main()
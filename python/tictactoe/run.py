from Tic_Tac_Toe import tic_tac_toe
from RL import QLearningTable


env = tic_tac_toe()
RL_1 = QLearningTable(actions=env.actions,file="OO.csv")
RL_2 = QLearningTable(actions=env.actions,file="XX.csv")

def main(env,RL_1,RL_2):
    while True:
        # initial observation
        observation = env.reset().copy()


        while True:
            # fresh env

            # RL choose action based on observation
            action_1 = str(RL_1.choose_action(str(observation)))

            # RL take action and get next observation and reward
            observation_, reward_1, done_1,legal_1 = env.step(action_1,observation)

            while not legal_1:
                action_1 = RL_1.choose_action(str(observation),legal_1)
                observation_, reward_1, done_1, legal_1 = env.step(action_1,observation)

            # RL learn from this transition
            RL_1.learn(str(observation), action_1, reward_1, str(observation_),done_1)
            # swap observation
            observation = observation_
            env.render(observation)
            if done_1 :
                break
            action_2 = str(RL_2.choose_action(str(observation)))

            observation_, reward_2, done_2, legal_2 = env.step(action_2,observation)

            while not legal_2 :
                action_2 = RL_2.choose_action(str(observation),legal_2)
                observation_, reward_2, done_2, legal_2 = env.step(action_2,observation)

            RL_2.learn(str(observation), action_2, reward_2, str(observation_),done_2)

            observation = observation_
            env.render(observation)

            # break while loop when end of this episode
            if done_2 :

                break


    # end of game



if __name__ == "__main__":
    # maze game
    main(env,RL_1,RL_2)
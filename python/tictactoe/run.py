from Tic_Tac_Toe import tic_tac_toe
from RL import QLearningTable


env = tic_tac_toe()
RL_1 = QLearningTable(actions=env.actions)
RL_2 = QLearningTable(actions=env.actions)

def main(env,RL_1,RL_2):
    while True:
        # initial observation
        observation = env.reset()
        observation_1 = observation.copy()
        observation_2 = observation.copy()

        while True:
            # fresh env
            env.render(observation_1)
            for i in range(len(observation_2)):
                if observation_2[i]=='1':
                    observation_2[i] = '2'
                elif observation_2[i]=='2':
                    observation_2[i] = '1'
            # RL choose action based on observation
            action_1 = str(RL_1.choose_action(str(observation_1)))
            action_2 = str(RL_2.choose_action(str(observation_2)))

            # RL take action and get next observation and reward
            observation_1_, reward_1, done_1,legal_1 = env.update(action_1,observation_1)

            observation_2_, reward_2, done_2, legal_2 = env.update(action_2,observation_2)

            while not legal_1 and reward_1==0:
                action_1 = RL_1.choose_action(str(observation_1),legal_1)
                observation_1_, reward_1, done_1, legal_1 = env.update(action_1,observation_1)

            while not legal_2 and reward_2==0:
                action_2 = RL_2.choose_action(str(observation_2),legal_2)
                observation_2_, reward_2, done_2, legal_2 = env.update(action_2,observation_2)

            # RL learn from this transition
            RL_1.learn(str(observation_1), action_1, reward_1, str(observation_1_),done_1)
            RL_2.learn(str(observation_2), action_2, reward_2, str(observation_2_),done_2)
            # swap observation

            observation_1 = observation_1_
            observation_2 = observation_2_
            print(observation_1 == observation_1_,observation_2 == observation_2_)
            # break while loop when end of this episode
            if done_1 or done_2 or env.round==9:

                break


    # end of game



if __name__ == "__main__":
    # maze game
    main(env,RL_1,RL_2)
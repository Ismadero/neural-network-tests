import torch
import uuid

import sys, os
_base = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_base, "dqn"))
sys.path.insert(0, os.path.join(_base, "snake"))

import agent as agentLib
import game as gameLib
import constants

def save_state(dict, episodes, dir):
    save = {'model': dict,
            'episodes': episodes}
    torch.save(save, dir)
    print(f"Model saved into '{dir}' file" + "\n")

rows = constants.ROWS
columns = constants.COLUMNS

model = None
episodes = 0

dir = sys.argv[1] if len(sys.argv) > 1 else ""

if dir != "":
    if os.path.exists(dir):
        saved = torch.load(dir)
        model = saved['model']
        episodes = saved['episodes']
    else:
        print(f"{dir} is not a file, model will initiate whit random values")
else:
    dir = f"snake_dqn_{uuid.uuid4().hex[:8]}.pth"

agent = agentLib.DQNAgent(model = model, rows = rows, cols = columns)

while 1:
    #Loop that iterates over episodes
    done = False
    game = gameLib.Game(render = False)
    try:
        #Loop that completes one episode (session of the game)
        while not done:
            state = torch.tensor(game.get_state())
            action = agent.select_action(state)
            next_state = game.step(action)
            agent.store(state, action, next_state[1], next_state[0], next_state[2])
            agent.train_step()
            done = next_state[2]

        results = game.quit()
        episodes += 1

        #Save model
        if episodes % 10 == 0:
            print(f"{episodes} episodes completed" + "\n" +
                  "Last game results:" + "\n" +
                  "Score : " + str(results[0]) + "\n" +
                  "Max achievable : " + str(results[1]) + "\n" +
                  "Time : " + str(results[2]) + "sec")
            save_state(agent.get_state_dict(), episodes, dir)

    except KeyboardInterrupt:
        game.quit()
        print("\n" + f"{episodes} episodes completed")
        save_state(agent.get_state_dict(), episodes, dir)
        break


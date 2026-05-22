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

agent = agentLib.DQNAgent(rows = rows, cols = columns)
if dir != "":
    try:
        if os.path.exists(dir):
            saved = torch.load(dir)
            model = saved['model']
            episodes = saved['episodes']
            agent.import_model(model)
        else:
            print(f"{dir} is not a file, model will initiate whit random values")
    except KeyError:
        print("File given is no a trained model")
    
else:
    dir = f"snake_dqn_{uuid.uuid4().hex[:8]}.pth"
scores = []
steps = []

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

        steps.append(game.get_steps())
        results = game.quit()
        scores.append(results[0])
        episodes += 1

        #Save model
        if episodes % 100 == 0:
            print(f"{episodes} episodes completed" + "\n")
            print(f"min: {min(scores)}  max: {max(scores)}  avg: {sum(scores)/len(scores):.1f}")
            print(f"min: {min(steps)}  max: {max(steps)}  avg: {sum(steps)/len(steps):.1f}")
            scores = []
            steps = []
            print(f"Actual epsilon: {agent.get_epsilon()}")
            save_state(agent.export_model(), episodes, dir)

    except KeyboardInterrupt:
        game.quit()
        print("\n" + f"{episodes} episodes completed")
        save_state(agent.export_model(), episodes, dir)
        break


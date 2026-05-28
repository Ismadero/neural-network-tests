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
episodes_max = 3000

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

while episodes < episodes_max:
    #Loop that iterates over episodes
    done = False
    game = gameLib.Game(render = False)
    try:
        #Loop that completes one episode (session of the game)
        while not done:
            state = game.get_state()
            direction = state[1]
            action = agent.select_action(state, direction)
            next_state_tuple, reward, done_aux = game.step(action)
            next_state, next_dir = next_state_tuple
            agent.store(state, 
                        action,
                        direction,
                        reward, 
                        next_state,
                        next_dir, 
                        done_aux)
            agent.train_step()
            max_steps = 100 + 50*game.get_score()
            done = done_aux or game.get_steps() >= max_steps


        steps.append(game.get_steps())
        results = game.quit()
        scores.append(results[0])
        episodes += 1

        #Save model
        if episodes % 100 == 0:
            print(f"{episodes} episodes completed")
            print(f"Score min: {min(scores)}  max: {max(scores)}  avg: {sum(scores)/len(scores):.1f}")
            print(f"Steps min: {min(steps)}  max: {max(steps)}  avg: {sum(steps)/len(steps):.1f}")
            scores = []
            steps = []
            model = agent.export_model()
            print(f"Actual epsilon: {model['epsilon']}")
            save_state(model, episodes, dir)

    except KeyboardInterrupt:
        game.quit()
        print("\n" + f"{episodes} episodes completed")
        save_state(agent.export_model(), episodes, dir)
        break


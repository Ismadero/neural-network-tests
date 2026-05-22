import torch
import time

import sys, os
_base = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_base, "dqn"))
sys.path.insert(0, os.path.join(_base, "snake"))


import agent as agentLib
import game as gameLib
import constants

model = ""
episodes = 0
dir = sys.argv[1] if len(sys.argv) > 1 else ""
agent = agentLib.DQNAgent(epsilon_start = 0.0)

if dir != "":
    try:
        if os.path.exists(dir):
            saved = torch.load(dir)
            model = saved['model']
            episodes = saved['episodes']
            agent.import_model(model)
        else:
            raise ValueError(f"{dir} is not a file" + "\n")
            
    except (KeyError):
        print("File given is not a trained model")
    
    print(f"Charged file '{dir}' with {episodes} episodes." + "\n")
    done = False
    game = gameLib.Game()
    try:
        while not done:
            state = torch.tensor(game.get_state())
            action = agent.select_action(state)
            next_state = game.step(action)
            done = next_state[2]
            time.sleep(constants.MOVE_INTERVAL)
        results = game.quit()
        print("Score : " + str(results[0]) + "\n" +
            "Max achievable : " + str(results[1]) + "\n" +
            "Time : " + str(results[2]) + "sec" + "\n")
    except KeyboardInterrupt:
        results = game.quit()
        print("\n" + 
            "Score : " + str(results[0]) + "\n" +
            "Max achievable : " + str(results[1]) + "\n" +
            "Time : " + str(results[2]) + "sec" + "\n")
else:
    print("One parameter is needed." + "\n")

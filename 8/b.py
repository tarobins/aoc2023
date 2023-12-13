from absl import app
import numpy as np

def main(argv):
    filename = argv[1]
    
    with open(filename, 'r') as f:
        directions = f.readline().strip()
        f.readline()
        states = dict()
        while True:
            line = f.readline()
            if line == '':
                break
            line = line.strip()
            state = line.split('=')[0].strip()
            value = line.split('=')[1].strip()
            left = value[1:4]
            right = value[6:9]
            states[state] = [left, right]

    lcm = 1

    start_states = [key for key in states.keys() if key.endswith('A')]
    
    for start in start_states:
        transitions = 0
        current_direction_index = 0
        current_state = start
        while not current_state.endswith('Z'):
            options = states[current_state]
            if directions[current_direction_index] == 'L':
                current_state = options[0]
            else:
                current_state = options[1]
            current_direction_index = (current_direction_index + 1) % len(directions)
            transitions += 1
        print(transitions)
        lcm = np.lcm(lcm, transitions)
    
    print(lcm)
    

if __name__ == '__main__':
    app.run(main)
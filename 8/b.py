from absl import app

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

    transitions = 0
    current_direction_index = 0
    current_states = [key for key in states.keys() if key.endswith('A')]
    current_states = ['DBA']
    number_of_states = len(current_states)
    
    while len([key for key in current_states if key.endswith('Z')]) != number_of_states:
        print(f'{current_states} {len([key for key in current_states if key.endswith("Z")])}')
        new_states = []
        for state in current_states:
            options = states[state]
            if directions[current_direction_index] == 'L':
                new_states.append(options[0])
            else:
                new_states.append(options[1])
        current_direction_index = (current_direction_index + 1) % len(directions)
        transitions += 1
        current_states = new_states
    #     options = states[current_state]
    #     if directions[current_direction_index] == 'L':
    #         current_state = options[0]
    #     else:
    #         current_state = options[1]
    #     current_direction_index = (current_direction_index + 1) % len(directions)
    #     transitions += 1

    print(transitions)

if __name__ == '__main__':
    app.run(main)
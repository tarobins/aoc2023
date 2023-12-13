from absl import app
import numpy as np

def main(argv):
    filename = argv[1]
    total = 0
    with open(filename, 'r') as f:
        for string_line in f:
            lines = [np.array(list(map(int, string_line.strip().split(' '))))]
            last_line = lines[-1]  
            while not np.all(last_line == 0):
                lines.append(last_line[1:] - last_line[:-1])
                last_line = lines[-1]
            value = 0
            for line in reversed(lines):
                value = line[0] - value
            total += value
    print(total)

if __name__ == '__main__':
    app.run(main)
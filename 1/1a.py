from absl import app
from absl import flags

def main(argv):
    filename = argv[1]
    sum = 0
    with open(filename, 'r') as file:
        for line in file:
            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next((char for char in reversed(line) if char.isdigit()), None)
            sum = sum + int(first_digit) * 10 + int(last_digit)

    print(sum)

if __name__ == '__main__':
    app.run(main)   

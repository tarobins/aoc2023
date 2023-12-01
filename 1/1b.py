from absl import app
from absl import flags

digit_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def main(argv):
    keys = list(digit_map.keys())
    values = list(digit_map.values())
    filename = argv[1]
    sum = 0
    with open(filename, 'r') as file:
        for line in file:
            first_locs = [line.find(key) for key in keys]
            min_loc = min(i for i in first_locs if i >= 0)
            min_loc_arg = first_locs.index(min_loc)
            first_digit = values[min_loc_arg]
            last_locs = [line.rfind(key) for key in keys]
            max_loc = max(i for i in last_locs if i >= 0)
            max_loc_arg = last_locs.index(max_loc)
            last_digit = values[max_loc_arg]
            sum = sum + first_digit * 10 + last_digit

    print(sum)

if __name__ == '__main__':
    app.run(main)   

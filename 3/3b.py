from absl import app
import numpy as np



def main(argv):
    filename = argv[1]

    with open(filename, 'r') as f:
        lines = f.readlines()
    char_arr = np.array(list(map(lambda x: list(x.strip()), lines)))

    digit_array = np.where(np.char.isdigit(char_arr), char_arr, None)

    number_lookup = dict()
    id_array = np.full(digit_array.shape, None)

    id = 0

    for row in range(digit_array.shape[0]):
        col = 0
        while col < digit_array.shape[1]:
            if digit_array[row][col] is not None:
                first_col = col
                # get the number
                num = int(digit_array[row][col])
                while col < digit_array.shape[1] - 1 and digit_array[row][col+1] is not None:
                    num = num * 10 + int(digit_array[row][col+1])
                    col = col + 1
                col = col + 1
                last_col = col
                number_lookup[id] = num
                id_array[row][first_col:last_col] = id
                id = id + 1
            else:
                col = col + 1

    # find the *s
    sum = 0
    for row in range(char_arr.shape[0]):
        for col in range(char_arr.shape[1]):
            if char_arr[row][col] == '*':
                neighbor_ids = id_array[max(0, row-1):min(row+2, id_array.shape[0]), max(0, col-1):min(col+2, id_array.shape[1])]
                neighbor_ids = neighbor_ids[neighbor_ids != None]
                unique_neighbor_ids = np.unique(neighbor_ids)
                if len(unique_neighbor_ids) == 2:
                    sum = sum + number_lookup[unique_neighbor_ids[0]] * number_lookup[unique_neighbor_ids[1]]
    print(sum)     

if __name__ == '__main__':
    app.run(main)
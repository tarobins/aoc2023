from absl import app
import numpy as np



def main(argv):
    filename = '3/test_data.txt'

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

    


    # n = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # print(n)

    # value_array = np.full(number_array.shape, None)

    # value_array[0][0] = 

    # symbol_array = np.where(np.logical_and(np.logical_not(np.char.isdigit(char_arr)), np.logical_not(char_arr == '.')), char_arr, None)
    
    # neighbor_array = np.full(symbol_array.shape, None)
    
    # for row in range(symbol_array.shape[0]):
    #     for col in range(symbol_array.shape[1]):
    #         if symbol_array[row][col] is not None:
    #             neighbor_array[max(0, row-1):min(row+2, symbol_array.shape[0]), 
    #                            max(0, col-1):min(col+2, symbol_array.shape[1])] = symbol_array[row][col]
    part_sum = 0
    # for row in range(symbol_array.shape[0]):
    #     col = 0
    #     while col < symbol_array.shape[1]:
    #         if char_arr[row][col].isdigit():
    #             isPart = neighbor_array[row][col] is not None
    #             num = int(char_arr[row][col])   
    #             col = col + 1
    #             while col < symbol_array.shape[1] and char_arr[row][col].isdigit():
    #                 isPart = isPart or neighbor_array[row][col] is not None
    #                 num = num * 10 + int(char_arr[row][col])
    #                 col = col + 1
    #             if isPart:
    #                 part_sum = part_sum + num
    #         else:
    #             col = col + 1
    #     row = row + 1
    
    # print(part_sum) 


if __name__ == '__main__':
    app.run(main)
from absl import app

def main(argv):
    filename = argv[1]
    sum = 0
    for line in open(filename, 'r'):
        l = line.split(':')
        game_number = int(l[0].split(' ')[1])
        sum = sum + game_number
        turns = l[1].split(';')
        for turn in turns:
            color_count = dict(list(map(lambda x: [x[1], int(x[0])], list(map(lambda x: x.strip().split(' '), turn.split(','))))))
            if not 'red' in color_count:
                color_count['red'] = 0
            if not 'blue' in color_count:
                color_count['blue'] = 0
            if not 'green' in color_count:
                color_count['green'] = 0
            if color_count['red'] > 12 or color_count['blue'] > 14 or color_count['green'] > 13:
                sum = sum - game_number
                break
    print(sum)

if __name__ == '__main__':
    app.run(main)
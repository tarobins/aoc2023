from absl import app

def main(argv):
    filename = argv[1]
    power = 0
    for line in open(filename, 'r'):
        l = line.split(':')
        game_number = int(l[0].split(' ')[1])
        game_max = {'red':0, "blue": 0, 'green': 0}
        turns = l[1].split(';')
        for turn in turns:
            color_count = dict(list(map(lambda x: [x[1], int(x[0])], list(map(lambda x: x.strip().split(' '), turn.split(','))))))
            if not 'red' in color_count:
                color_count['red'] = 0
            if not 'blue' in color_count:
                color_count['blue'] = 0
            if not 'green' in color_count:
                color_count['green'] = 0
            game_max['red'] = max(game_max['red'], color_count['red'])
            game_max['blue'] = max(game_max['blue'], color_count['blue'])
            game_max['green'] = max(game_max['green'], color_count['green'])
        power = power + game_max['red'] * game_max['blue'] * game_max['green']
    print(power)

if __name__ == '__main__':
    app.run(main)
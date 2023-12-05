from absl import app

def main(argv):
    filename = argv[1]
    sum = 0
    with open(filename, 'r') as f:
        for line in f:
            card_content = line.split(':')[1]
            winning_numbers = list(filter(lambda x: x != '', card_content.split('|')[0].strip().split(' ')))
            my_numbers = list(filter(lambda x: x != '', card_content.split('|')[1].strip().split(' ')))
            intersection_count = len(set(winning_numbers) & set(my_numbers))
            if intersection_count > 0:
                sum += 2 ** (intersection_count - 1)
    
    print(sum)

if __name__ == '__main__':
    app.run(main)

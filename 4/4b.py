from absl import app

def main(argv):
    filename = argv[1]
    
    copies = dict()
    current = 1
    
    with open(filename, 'r') as f:
        for line in f:
            copies[current] = copies.get(current, 0) + 1
            card_content = line.split(':')[1]
            winning_numbers = list(filter(lambda x: x != '', card_content.split('|')[0].strip().split(' ')))
            my_numbers = list(filter(lambda x: x != '', card_content.split('|')[1].strip().split(' ')))
            intersection_count = len(set(winning_numbers) & set(my_numbers))
            for i in range(current + 1, current + 1 + intersection_count):
                copies[i] = copies.get(i, 0) + copies.get(current, 1)
            current = current + 1
            
    total_sum = sum(copies.values())

    print('Total sum: {}'.format(total_sum))
    

if __name__ == '__main__':
    app.run(main)

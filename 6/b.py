from absl import app
from math import sqrt, ceil, floor

def main(argv):
    filename = argv[1]
    prod = 1
    with open(filename) as f:
        times = [f.readline().split(':')[1].replace(' ', '').strip()]
        distances = [f.readline().split(':')[1].replace(' ', '').strip() ]

        for i in range(len(times)):
            T = int(times[i])
            D = int(distances[i])
            left_time = (- T + sqrt(T**2 - 4*D))/-2
            right_time = (- T - sqrt(T**2 - 4*D))/-2
            
            num = floor(right_time) - ceil(left_time) + 1
            if int(left_time) == left_time:
                num -= 1
            if int(right_time) == right_time:
                num -= 1
            # print(left_time, right_time, num)
            prod *= num
    
    print(prod)

if __name__ == '__main__':
    app.run(main)
from absl import app

class single_map:
    def __init__(self, source_start, dest_start, length):
        self.source_start = source_start
        self.dest_start = dest_start
        self.length = length

    def __getitem__(self, key):
        if key < self.source_start or key >= self.source_start + self.length:
            return -1
        return self.dest_start + key - self.source_start

class seed_map:
    def __init__(self, mappings):
        self.submaps = []
        for mapping in mappings:
            self.submaps.append(single_map(mapping[1], mapping[0], mapping[2]))
    
    def __getitem__(self, key):
        for submap in self.submaps:
            if key >= submap.source_start and key < submap.source_start + submap.length:
                return submap[key]
        return key

def main(argv):
    filename = argv[1]
    with open(filename, 'r') as f:
        seeds = f.readline().split(':')[1].strip().split(' ')
        
        seed_maps = []
        f.readline() # skip blank line
        while True:
            f.readline() # skip header
            next_line = f.readline()
            # print(next_line)
            # print(f' >>>> {len(next_line)}')
            seed_to_soil_arrays = []
            while len(next_line) > 0 and next_line[0].isdigit():
                next_line = next_line.strip().split(' ')
                seed_to_soil_arrays.append([int(next_line[0]), int(next_line[1]), int(next_line[2])])
                next_line = f.readline()
            
            seed_maps.append(seed_map(seed_to_soil_arrays))

            if len(next_line) == 0:
                break

    min_loc = None
    for seed_group in range(0, len(seeds), 2):
        seed_group_start = int(seeds[seed_group])
        seed_group_length = int(seeds[seed_group + 1])
        for seed in range(seed_group_start, seed_group_start + seed_group_length + 1):
            loc = seed
            for nseed_map in seed_maps:
                loc = nseed_map[int(loc)]
                
            if min_loc is None or loc < min_loc:
                min_loc = loc
    
    print(min_loc)


        

if __name__ == '__main__':
    app.run(main)
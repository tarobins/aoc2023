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
    
    def critical_range(self, critical_domain):
        result = []
        for i in range(0, len(critical_domain), 2):
            if (critical_domain[i] >= self.source_start + self.length 
                or critical_domain[i] + critical_domain[i + 1] <= self.source_start):
                return critical_domain
            start_domain = max(self.source_start, 
                             min(critical_domain[i], self.source_start + self.length - 1))
            start = self[start_domain]
            end_domain = min(self.source_start + self.length - 1, 
                             critical_domain[i] + critical_domain[i + 1] - 1)
            end = self[end_domain] - start + 1
            if critical_domain[i] < start_domain:
                result.extend([critical_domain[i], start_domain - critical_domain[i]])
            result.extend([start, end])
            if critical_domain[i] + critical_domain[i + 1] > end_domain + 1:
                result.extend([end_domain + 1, critical_domain[i] + critical_domain[i + 1] - end_domain - 1])
        return result
    
    def pre_range(self, critical_domain):
        result = []
        for i in range(0, len(critical_domain), 2):
            if (critical_domain[i] + critical_domain[i + 1] <= self.source_start):
                return critical_domain
            start_domain = max(self.source_start, 
                             min(critical_domain[i], self.source_start + self.length - 1))
            if critical_domain[i] < start_domain:
                result.extend([critical_domain[i], start_domain - critical_domain[i]])
    
        return result
    
    def map_range(self, critical_domain):
        result = []
        for i in range(0, len(critical_domain), 2):
            if (critical_domain[i] >= self.source_start + self.length 
                or critical_domain[i] + critical_domain[i + 1] <= self.source_start):
                return []
            start_domain = max(self.source_start, 
                             min(critical_domain[i], self.source_start + self.length - 1))
            start = self[start_domain]
            end_domain = min(self.source_start + self.length - 1, 
                             critical_domain[i] + critical_domain[i + 1] - 1)
            end = self[end_domain] - start + 1
            result.extend([start, end])
        return result
    

    def post_range(self, critical_domain):
        result = []
        for i in range(0, len(critical_domain), 2):
            if (critical_domain[i] >= self.source_start + self.length):
                return critical_domain
            start_domain = max(self.source_start, 
                             min(critical_domain[i], self.source_start + self.length - 1))
            start = self[start_domain]
            end_domain = min(self.source_start + self.length - 1, 
                             critical_domain[i] + critical_domain[i + 1] - 1)
            if critical_domain[i] + critical_domain[i + 1] > end_domain + 1:
                result.extend([end_domain + 1, critical_domain[i] + critical_domain[i + 1] - end_domain - 1])
        return result
        
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

    def critical_range(self, critical_domain):
        unmapped = critical_domain.copy()
        mapped = []
        for submap in self.submaps:
            for_next_map = []
            for i in range(0, len(unmapped), 2):
                sub_domain = unmapped[i:i + 2]
                for_next_map.extend(submap.pre_range(sub_domain))
                mapped.extend(submap.map_range(sub_domain))
                for_next_map.extend(submap.post_range(sub_domain))
            unmapped = for_next_map
        mapped.extend(unmapped)
        return mapped

    
def main(argv):
    pass
    # filename = argv[1]                    
    # with open(filename, 'r') as f:
    #     seeds = list(map(int, f.readline().split(':')[1].strip().split(' ')))
        
        
    #     seed_maps = []
    #     f.readline() # skip blank line
    #     while True:
    #         f.readline() # skip header
    #         next_line = f.readline()
    #         # print(next_line)
    #         # print(f' >>>> {len(next_line)}')
    #         seed_to_soil_arrays = []
    #         while len(next_line) > 0 and next_line[0].isdigit():
    #             next_line = next_line.strip().split(' ')
    #             seed_to_soil_arrays.append([int(next_line[0]), int(next_line[1]), int(next_line[2])])
    #             next_line = f.readline()
            
    #         seed_maps.append(seed_map(seed_to_soil_arrays))

    #         if len(next_line) == 0:
    #             break
    
    # cd = seeds
    # print(cd)
    # for vseed_map in seed_maps:
    #     cd = vseed_map.critical_range(cd)
    #     print(cd)
    
    # print(cd)


if __name__ == '__main__':
    app.run(main)
import s_map

def test_single_map():
    s = s_map.single_map(2, 5, 4)
    assert s[2] == 5
    assert s.critical_range([2, 2]) == [5, 2]
    assert s.critical_range([3, 2]) == [6, 2]
    assert s.critical_range([2, 4]) == [5, 4]
    assert s.critical_range([1, 1]) == [1, 1]
    assert s.critical_range([1, 2]) == [1, 1, 5, 1]
    assert s.critical_range([4, 4]) == [7, 2, 6, 2]
    assert s.critical_range([0, 10]) == [0, 2, 5, 4, 6, 4]

    assert s.map_range([2, 2]) == [5, 2]
    assert s.map_range([3, 2]) == [6, 2]
    assert s.map_range([2, 4]) == [5, 4]
    assert s.map_range([1, 1]) == []
    assert s.map_range([1, 2]) == [5, 1]
    assert s.map_range([4, 4]) == [7, 2]
    assert s.map_range([0, 10]) == [5, 4]

    assert s.pre_range([2, 2]) == []
    assert s.pre_range([3, 2]) == []
    assert s.pre_range([2, 4]) == []
    assert s.pre_range([1, 1]) == [1, 1]
    assert s.pre_range([1, 2]) == [1, 1]
    assert s.pre_range([4, 4]) == []
    assert s.pre_range([0, 10]) == [0, 2]

    assert s.post_range([2, 2]) == []
    assert s.post_range([3, 2]) == []
    assert s.post_range([2, 4]) == []
    assert s.post_range([1, 1]) == []
    assert s.post_range([1, 2]) == []
    assert s.post_range([6, 4]) == [6,4]
    assert s.post_range([4, 4]) == [6, 2]
    assert s.post_range([0, 10]) == [6, 4]

def test_seed_map():
    seed_to_soil = s_map.seed_map([[50, 98, 2], [52, 50, 48]])
    seeds = [79, 14, 55, 13]

    soil = seed_to_soil.map(seeds) 

    assert soil == [81, 14, 57, 13]




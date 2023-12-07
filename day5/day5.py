import pandas as pd


def map_converter_dict(seeds, map_dict):
    # part 1
    data = {}
    # destination, source, range
    # soil       , seed
    keys = ["seed"] + list(map_dict.keys())
    for seed in seeds:
        data[seed] = {"seed": seed}
        for i, name in enumerate(map_dict):
            for prop in map_dict[name]:
                if prop[1] <= data[seed][keys[i]] < (prop[1] + prop[2]):
                    data[seed][name] = data[seed][keys[i]] - prop[1] + prop[0]
                    break
            if not name in data[seed]:
                data[seed][name] = data[seed][keys[i]]
    return data


def map_converter(seeds, map_dict):
    # part 1
    # destination, source, range
    # soil       , seed
    min_location = 1756229080
    for seed in seeds:
        last_value = seed
        for name in map_dict:
            for prop in map_dict[name]:
                if prop[1] <= last_value < (prop[1] + prop[2]):
                    last_value = last_value - prop[1] + prop[0]
                    break
        if last_value < min_location:
            min_location = last_value
    return min_location


def get_ranges(init_ranges, mappings):
    final_ranges = []
    if isinstance(init_ranges, list):
        ranges_to_check = init_ranges
    else:
        ranges_to_check = [init_ranges]
    while ranges_to_check:
        range1 = ranges_to_check[0]
        prev_checked = ranges_to_check.copy()
        for dest_start, source_start, range_len in mappings:
            range2 = (source_start, source_start + range_len)
            dest = (dest_start, dest_start + range_len)
            if range1[0] >= range2[0]:  # 2,3,5
                if range1[1] <= range2[1]:  # 2
                    mapped_start = dest[0] + range1[0] - source_start
                    mapped = (mapped_start, mapped_start + range1[1] - range1[0])
                    final_ranges.append(mapped)
                    ranges_to_check.pop(0)
                    break
                if range1[0] >= range2[1]:  # 3
                    continue
                if range1[1] > range2[1]:  # 5
                    if range1[0] < range2[1]:
                        mapped_start = dest[0] + range1[0] - range2[0]
                        mapped = (mapped_start, dest[1])
                        final_ranges.append(mapped)
                    ranges_to_check.append((range2[1], range1[1]))
                    ranges_to_check.pop(0)
                    break
            if range1[1] <= range2[0]:  # 1
                continue
            if range1[1] <= range2[1]:  # 4
                mapped = (dest[0], dest[0] + range1[1] - range2[1])
                final_ranges.append(mapped)
                ranges_to_check.append((range1[0], range2[0]))
                ranges_to_check.pop(0)
                break
            else:  # 6
                ranges_to_check.append((range1[0], range2[0]))
                ranges_to_check.append((range2[1], range1[1]))
                final_ranges.append(dest)
                ranges_to_check.pop(0)
                break
        if ranges_to_check and ranges_to_check[0] == range1:
            ranges_to_check.pop(0)
            final_ranges.append(range1)
        if prev_checked == ranges_to_check:
            break

    final_ranges.extend(ranges_to_check)
    return final_ranges


def map_converter_by_ranges(seeds, map_dict):
    # part 2
    # destination, source, range
    # soil       , seed

    sorted_seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    sorted_seeds.sort(key=lambda x: x[0])
    [map_dict[name].sort(key=lambda x: x[1]) for name in map_dict]
    ranges = [
        (range_start, range_start + range_len)
        for range_start, range_len in sorted_seeds
    ]

    for mappings in map_dict.values():
        ranges = get_ranges(ranges, mappings)
    min_location = min(ranges)
    return min_location[0]


def one_star(filename):
    coded_input = open(filename, "r").read().split("\n\n")
    coded_input = [line.split(":") for line in coded_input]
    seeds = list(map(lambda x: int(x), coded_input[0][1].split()))

    map_dict = {
        line[0]: list(
            map(lambda x: [int(el) for el in x.split()], line[1].strip().split("\n"))
        )
        for line in coded_input[1:]
    }
    # dict solution
    # data = map_converter_dict(seeds, map_dict)
    # df = pd.DataFrame([el[1] for el in list(data.items())])
    # print(df)
    # print(f'Part 1 minimum location is: {df.min()["humidity-to-location map"]}')

    data = map_converter(seeds, map_dict)
    print(data)
    print(f"Part 1 minimum location is: {data}")


def two_stars(filename):
    coded_input = open(filename, "r").read().split("\n\n")
    coded_input = [line.split(":") for line in coded_input]

    seeds = list(map(lambda x: int(x), coded_input[0][1].split()))
    map_dict = {
        line[0]: list(
            map(lambda x: [int(el) for el in x.split()], line[1].strip().split("\n"))
        )
        for line in coded_input[1:]
    }
    min_location = map_converter_by_ranges(seeds, map_dict)
    print(f"Part 2 minimum location is: {min_location}")


# one_star("day5_input.txt")
# two_stars("day5_input.txt")

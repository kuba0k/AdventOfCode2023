import pandas as pd
from collections import deque


def map_converter(seeds, toSoil, toFert, toWater, toLight, toTemp, toHumid, toLoc):
    data = {}
    # destination, source, range
    # soil       , seed
    for seed in seeds:
        data[seed] = {}
        # seed to soil
        for soil in toSoil:
            if soil[0] <= seed < soil[0] + soil[2]:
                data[seed]["soil"] = seed - soil[0] + soil[1]
        if not "soil" in data[seed]:
            data[seed]["soil"] = seed

    # soil to fertilizer

    # fertilizer to water

    # water to light

    # light to temperature

    # temperature to humidity

    # humidity to location

    return data


def map_converter(seeds, map_dict):
    data = {}
    # destination, source, range
    # soil       , seed
    keys = ["seed"] + list(map_dict.keys())
    # print(keys)
    for seed in seeds:
        data[seed] = {"seed": seed}
        for i, name in enumerate(map_dict):
            # print(f"{i=}")
            for prop in map_dict[name]:
                # print(f"{prop=}")
                if prop[1] <= data[seed][keys[i]] < (prop[1] + prop[2]):
                    data[seed][name] = data[seed][keys[i]] - prop[1] + prop[0]
                    # print(
                    #     f"{data[seed][keys[i]]=}, {data[seed][name]=}, {prop[0]=}, {prop[1]=}, {prop[2]=}"
                    # )
                    # print(f"{keys[i+1]=}")
                    break
            if not name in data[seed]:
                data[seed][name] = data[seed][keys[i]]
                # print(f"{keys[i+1]=}")
    return data


def map_converter2(seeds, map_dict):
    # destination, source, range
    # soil       , seed
    min_location = 1756229080
    for i in range(0, len(seeds) // 2 + 1, 2):
        for j in range(seeds[i + 1]):
            last_value = seeds[i] + j
            for name in map_dict:
                for prop in map_dict[name]:
                    if prop[1] <= last_value < (prop[1] + prop[2]):
                        last_value = last_value - prop[1] + prop[0]
                        break
                    # print(f"{keys[i+1]=}")
            if last_value < min_location:
                min_location = last_value
    return min_location


def map_converter3(seeds, map_dict):
    # destination, source, range
    # soil       , seed
    min_location = 1756229080
    # sort values bo source in mapdict
    # sort seeds in pairs
    # take first value from mapdict, if in range and checked at least once pop first element and take next
    sorted_seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds) // 2 + 1, 2)]
    sorted_seeds.sort(key=lambda x: x[0])
    [map_dict[name].sort(key=lambda x: x[1]) for name in map_dict]

    seeds.sort()
    for seed in [79]:
        print(f"Checking seed {seed}")
        prev_value = seed

        # for seed in sorted_seeds:
        #     print(f"Checking seed {seed[0]}")
        #     for seed_range in range(seed[1]):
        #         prev_value = seed[0]  + seed_range
        for name in map_dict:
            if map_dict[name]:
                source_range_end = map_dict[name][0][1] + map_dict[name][0][2]
                if prev_value >= source_range_end:
                    print(f"{name=}, {source_range_end=}")
                    map_dict[name].pop(0)
                    # break
                elif map_dict[name][0][1] <= prev_value:
                    prev_value = (
                        prev_value - map_dict[name][0][1] + map_dict[name][0][0]
                    )
        if prev_value < min_location:
            print(f"{seed=}")
            min_location = prev_value
    return min_location


def map_converter3(seeds, map_dict):
    # destination, source, range
    # soil       , seed
    min_location = 1756229080
    # sort values bo source in mapdict
    # sort seeds in pairs
    # take first value from mapdict, if in range and checked at least once pop first element and take next
    sorted_seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    sorted_seeds.sort(key=lambda x: x[0])
    [map_dict[name].sort(key=lambda x: x[1]) for name in map_dict]
    print(f"{sorted_seeds=}")

    for seed in sorted_seeds:
        print(f"Checking seed {seed[0]}")
        for seed_range in range(seed[1]):
            prev_value = seed[0] + seed_range
            for name in map_dict:
                while map_dict[name]:
                    source_range_end = map_dict[name][0][1] + map_dict[name][0][2]
                    if prev_value > source_range_end:
                        # print(f"{name=}, {source_range_end=}")
                        map_dict[name].pop(0)
                    elif map_dict[name][0][1] <= prev_value:
                        prev_value = (
                            prev_value - map_dict[name][0][1] + map_dict[name][0][0]
                        )
                        break
                    else:
                        break
            if prev_value < min_location:
                # print(f"{seed=}")
                min_location = prev_value
        print(f"Current minimum: {min_location}")
    return min_location


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

    data = map_converter(seeds, map_dict)
    df = pd.DataFrame([el[1] for el in list(data.items())])
    print(df.min()["humidity-to-location map"])


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

    min_location = map_converter3(seeds, map_dict)
    print(f"Minimum location is: {min_location}")


# one_star("day5_input.txt")
two_stars("day5_input2.txt")

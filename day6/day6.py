def calc_possibilities(times, distances):
    result = 1
    if isinstance(times, int):
        times, distances = [times], [distances]
    for time, dist in zip(times, distances):
        range_start = 0
        range_end = 0
        for wind_up in range(
            0,
            time + 1,
        ):
            time_left = time - wind_up
            dist_travelled = time_left * wind_up
            if dist_travelled > dist:
                range_start = wind_up
                break
        for wind_up in range(time, -1, -1):
            time_left = time - wind_up
            dist_travelled = time_left * wind_up
            if dist_travelled > dist:
                range_end = wind_up
                break
        result *= range_end - range_start + 1
    print(result)


def one_star(filename):
    times = open(filename).read().split("\n")
    times, distances = [
        list(map(lambda x: int(x), time.split(":")[1].split())) for time in times
    ]
    calc_possibilities(times, distances)


def two_stars(filename):
    times = open(filename).read().split("\n")
    time, distance = [int(time.split(":")[1].replace(" ", "")) for time in times]
    calc_possibilities(time, distance)


# one_star("day6_input.txt")
# two_stars("day6_input.txt")

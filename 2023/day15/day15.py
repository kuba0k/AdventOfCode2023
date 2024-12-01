def one_star(filename):
    lines = open(filename).readlines()[0].split(",")
    result = 0
    for step in lines:
        step_result = 0
        for char in step:
            step_result = ((step_result + ord(char)) * 17) % 256
        result += step_result

    print(f"Result part 1: {result}")


def two_stars(filename):
    lines = open(filename).readlines()[0].split(",")
    boxes = {f"Box {i}": [] for i in range(256)}
    for step in lines:
        label_result = 0
        split = step.split("=")
        sign = "=" if len(split) > 1 else "-"
        if sign == "=":
            label = split[0]
        else:
            label = split[0][:-1]
        for char in label:
            label_result = ((label_result + ord(char)) * 17) % 256
        box_str = f"Box {label_result}"
        if sign == "=":
            changed = 0
            for i, lens in enumerate(boxes[box_str]):
                if lens[0] == label:
                    changed = 1
                    boxes[box_str][i] = [split[0], split[1]]
            if not changed:
                boxes[box_str].append([split[0], split[1]])
        else:
            if box_str in boxes:
                for i, lens in enumerate(boxes[box_str]):
                    if lens[0] == label:
                        del boxes[box_str][i]
    result = 0
    for i, box in enumerate(boxes.values()):
        for j, lens in enumerate(box, 1):
            result += (1 + i) * j * int(lens[1])

    print(f"Result part 2: {result}")


one_star("day15_input.txt")
two_stars("day15_input.txt")

import re



reg = re.compile(r"""(\d+)-(\d+) ([a-z]): ([a-z]+)""")





with open("/workspace/aoc2020/input/day02_input") as f:
    c = 0
    d = 0
    for p in f:
        m = reg.match(p)
        lower, upper, letter, string = m.groups()
        lower = int(lower)
        upper = int(upper)
        if string.count(letter) in range(lower, upper + 1):
            c += 1
    # print(c)
        # Part 2
        if (string[lower - 1] == letter) != (string[upper - 1] == letter):
            d += 1
    print(c,d)




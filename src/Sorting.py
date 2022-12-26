from Usage import usage


def sort(args):
    # check for errors
    if len(args) == 0:
        usage(error="Too few arguments", tool="sort")

    # put together all lines from all given files
    lines = []
    for i in range(len(args)):
        file = open(args[i])
        while True:
            line = file.readline()
            if not line:
                break
            lines.append(line)
        file.close()

    lines.sort()

    for i in range(len(lines)):
        print(lines[i], end="")

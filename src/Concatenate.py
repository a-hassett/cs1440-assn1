from Usage import usage


def cat(args):
    # if no arguments -> error
    if len(args) == 0:
        usage(error="Too few arguments", tool="cat")

    # repeats for every given file
    for i in range(len(args)):
        file = open(args[i])
        while True:
            line = file.readline()
            if not line:
                break
            print(line, end="")
        file.close()


def tac(args):
    # if no arguments -> error
    if len(args) == 0:
        usage(error="Too few arguments", tool="tac")

    # add lines to the list for each given file
    for i in range(len(args)):
        lines = []
        file = open(args[i])
        while True:
            line = file.readline()
            if not line:
                break
            lines.append(line)
        file.close()

        # print lines list backwards
        for j in range(len(lines), 0, -1):
            print(lines[j - 1], end="")

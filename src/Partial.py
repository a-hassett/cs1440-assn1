from Usage import usage


def head(args):
    # check for errors
    if len(args) == 0:
        usage(error="Too few arguments", tool="head")
    elif args[0] == "-n":  # not default
        if len(args) == 1 or not args[1].isnumeric():
            usage(error="Number of lines is required", tool="head")

    # number of lines is specified
    numPrintedLines = 10  # default
    if args[0] == "-n":
        numPrintedLines = int(args[1])
        args = args[2:]

    for i in range(len(args)):
        lines = []
        file = open(args[i])
        while True:
            line = file.readline()
            if not line:
                break
            lines.append(line)
        file.close()

        # avoid "index out of range" errors
        if numPrintedLines > len(lines):
            numPrintedLines = len(lines)

        # format for multiple files
        if len(args) > 1:
            print("==> ", args[i], " <==")

        for j in range(numPrintedLines):
            if j < len(lines):
                print(lines[j], end="")
        print()


def tail(args):
    # check for errors
    if len(args) == 0:
        usage(error="Too few arguments", tool="tail")
    elif args[0] == "-n":  # not default
        if len(args) == 1 or not args[1].isnumeric():
            usage(error="Number of lines is required", tool="tail")

    # number of lines is specified
    numPrintedLines = 10  # default
    if args[0] == "-n":
        numPrintedLines = int(args[1])
        args = args[2:]

    for i in range(len(args)):
        lines = []
        file = open(args[i])
        while True:
            line = file.readline()
            if not line:
                break
            lines.append(line)
        file.close()

        # avoid "index out of range" errors
        if numPrintedLines > len(lines):
            numPrintedLines = len(lines)

        # format for multiple files
        if len(args) > 1:
            print("==> ", args[i], " <==")

        for j in range(len(lines) - numPrintedLines, len(lines)):
            if j < len(lines):
                print(lines[j], end="")
        print()

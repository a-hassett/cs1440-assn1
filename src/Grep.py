from Usage import usage


def grep(args):
    # check for errors
    if len(args) < 2:
        usage(error="Please provide a pattern and at least one filename", tool="grep")

    # whether it prints opposite
    thereIsOption = False
    if args[0] == "-v":
        keyword = args[1]
        thereIsOption = True
        args = args[2:]
    else:
        keyword = args[0]
        args = args[1:]

    for i in range(len(args)):
        lines = []
        file = open(args[i])
        while True:
            line = file.readline()
            if not line:
                break
            lines.append(line)
        file.close()

        for j in range(len(lines)):
            if not thereIsOption and keyword in lines[j]:  # searching for keyword
                print(lines[j], end="")
            elif thereIsOption and keyword not in lines[j]:  # searching for lack of keyword
                print(lines[j], end="")

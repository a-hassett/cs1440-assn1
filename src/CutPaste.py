from Usage import usage


def cut(args):
    # check for errors
    if len(args) == 0:
        usage(error="Too few arguments", tool="cut")
    elif args[0] == "-f" and len(args) < 2:
        usage(error="A comma-separated field specification is required", tool="cut")

    field = []
    if args[0] == "-f":  # if there's an option
        field = args[1].split(",")

        for i in range(len(field)):
            # check for errors
            if field[i].isalpha() or int(field[i]) < 1:
                usage(error="A comma-separated field specification is required", tool="cut")

            field[i] = int(field[i])
        field.sort()  # will print fields in order of original file
        args = args[2:]
    else:
        field.append(1)  # default is 1

    # repeats for every file
    for i in range(len(args)):
        lines = []
        file = open(args[i])
        while True:
            line = file.readline()
            if not line:
                break
            lines.append(line.split(","))  # split line into words

        file.close()

        for ln in range(len(lines)):  # ln means line number for readability
            for j in range(len(field)):
                fn = field[j] - 1  # fn means field number for readability

                # avoid "index out of range" errors
                if fn + 1 > len(lines[ln]):
                    print("", end="")

                else:
                    # take out newline character from word
                    if (lines[ln][fn])[len(lines[ln][fn]) - 1] == "\n":
                        word = (lines[ln][fn])[:len(lines[ln][fn]) - 1]
                    else:
                        word = lines[ln][fn]

                    print(word, end="")

                    # if last word in field, no comma
                    if j < len(field) - 1:
                        print(",", end="")
            print()


def paste(args):
    # check for errors
    if len(args) == 0:
        usage(error="Too few arguments", tool="paste")

    lines = []
    fileNum = 0
    for i in range(len(args)):
        file = open(args[i])
        lines.append([])  # each file fills a list element

        while True:
            line = file.readline()
            if not line:
                break
            lines[fileNum].append(line)  # for file element, add lines

        fileNum += 1
        file.close()

    # will print as many lines as longest file
    longest = 0
    for i in range(len(lines)):
        if len(lines[i]) > longest:
            longest = len(lines[i])

    for i in range(longest):
        for j in range(len(lines)):
            if i < len(lines[j]):  # avoid "index out of range" error
                compactLine = (lines[j][i])[:len(lines[j][i]) - 1]  # line without newline character at end
                print(compactLine, end="")

                # if last file item to be pasted, no comma
                if j != len(lines) - 1:
                    print(",", end="")
            else:
                # if index out of range, print an empty string & make sure comma is in right spot
                print("", end="")
                if j != len(lines) - 1:
                    print(",", end="")
        print()

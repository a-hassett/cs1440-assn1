from Usage import usage


def wc(files):
    # check for errors
    if len(files) == 0:
        usage(error="Too few arguments", tool="wc")

    # variables used in case of multiple files
    totalLines = 0
    totalWords = 0
    totalChar = 0

    for i in range(len(files)):
        file = open(files[i])

        # variables reset and reused per file
        lines = []
        numWords = 0
        numChar = 0

        while True:
            line = file.readline()
            if not line:
                break
            lines.append(line)
        file.close()

        # count characters by counting length of words in line
        for j in range(len(lines)):
            numChar += len(lines[j])

        # count words by counting length of line
        for k in range(len(lines)):
            lines[k] = lines[k].split()
            numWords += len(lines[k])

        # format what gets printed
        print(format(len(lines), ">6d"), format(numWords, ">6d"), format(numChar, ">6d"), "\t", files[i])

        # prepare in case of multiple files
        totalWords += numWords
        totalChar += numChar
        totalLines += len(lines)

    # format what gets printed in case of multiple files
    if len(files) > 1:
        print(format(totalLines, ">6d"), format(totalWords, ">6d"), format(totalChar, ">6d"), "\t total")

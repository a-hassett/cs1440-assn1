# Software Development Plan
## Phase 0: Requirements Specification *(10%)*

**Deliver:**

This program will be imitating built-in command line commands for text files.
We will be making concatenate(cat), backwards concatenate(tac), cut, paste, 
grep, head, tail, sort, and word count.\
\
__Concatenate (cat)__: I will be printing each line of the file in the order it appears in
the original file, with the same spacing and capitalization and everything. The file
will be opened, read from, and printed out. I'm not sure whether I can just use
something like print(read(file)). I'll have to test that out in the REPL.\
\
__Back concatenate (tac)__: I think I'll open the file and then make a list with
each line as an item. Then I'll print starting at the last line item in the list
and continue from there. I'll think there's a method called readline() that I could
use or maybe I'll use a for loop this way: "for line in file:" and then put each
line in the list that way.\
\
__Cut__: This one breaks a line of text separated by commas into different groups
called fields. I can choose which fields get printed by entering "-f _number_" where
number is the number field I want to show up. If the number is larger than the
number of fields, the field is treated as empty. If there is a different number of
elements in every field then there will be as many lines printed as the greatest
number of elements. If the fields are empty, print out the same number of lines,
just let them be blank. I'm not sure how I will break the lines into fields using
commas. I'll have to find the commas somehow. I might be able to use text.split(",")
where a comma is the parameter to break it up. I will use text.split() for every
line, which makes a list. I'll use a for loop to repeat this for every line. Then
When a number argument gets passed at the command line, I'll have to check if it's
in that list's range. If not, I'll print a blank line. Close file.\
\
__Paste__: This one seems a little hard. I'll have to have two open files at a
time and might have to make a new file. I'm hoping python automatically makes its
own new file when you do "_oldfile_ > _newfile_", but if it doesn't I'll have to
figure it out. I'll have to read each file and make a list of lists containing
each file's lines. I'll print the first one's first line, then a comma, then the
second file's first line. There should be no spaces, tabs, or new lines in between.
Then I'll continue for the greatest number of lines among the files on the argument
line.\
\
__Grep__: This one prints lines that contain a character or word of your choice.
It is case-sensitive. I think this one will put every line as an element of a
list. Then we will read through every item in the list for a match of the command
line argument (remember this argument is a character or word). I think I'll be
able to do this with "if _character/word_ is in line[i]" then print the line.\
\
__Head__: This is where we'll put every line back in a list and print the first
few lines, based on the number put as the command line argument. We'll start at
index 0 and go from there.\
\
__Tail__: We'll put every line in the text file back in a list, and this time
we'll print a few line, but we'll start at the last possible index and then go
backwards until we print as many lines as the command line argument that goes after
"-n".\
\
__Sort__: We will print the lines of at least one text file in order. First, we'll
have to open any and all files presented to the command line and put their lines in a 
list again. But this time we have to read the characters in the line and compare them
to each other. I might be able to make a new list. I'll slowly add each new line from the old list
to it after comparing them. I think I can insert a list item at a certain index in
python using _list_.insert(_index_, _element_). I'll put them into the new list 
by their first character, but then I have to compare the second character without
reordering the first organization. I think the best way to do this would be to 
compare the first few items of the string. Like if line1[:3] = line2[:3], then I
can compare line1[4] to line2[4]. I think I'll use a for loop to increase the length
of the string I'm comparing. I'll figure out the pseudocode in a different phase.\
\
__Word Count__: This one should be easy. I'll just put the lines of the file back
into a list and then I'll use the _string_.split() to make a 2x2 array. Then I'll use
nested for loops to count the number of items in each line's list and add them
all up. I'll use one of the nested for loops to count the number of lines and
a similar process to count the number of bytes/characters. I must format it so 
the numbers are right justified and the words are left justified. I'll be printing
the number of lines, then words, then bytes, then the sys.argv string (so the file
name). I don't know how to figure out the number of bytes of a word or file. I
Googled it, and I think I might be able to use len(_file_) or _file_.length(). I
also might be able to use len(_of the line lengths_) added together. 

## Phase 1: System Analysis *(10%)*

**Deliver:**

These programs will take arguments from the command line. I'll need to analyze the
number and type of arguments. I can't just count the number of arguments, because
the cut command could have the same number of arguments whether it uses -f or 
two file names. And I'll have to see which argument starts with a dash. If the
files don't exist, I don't have to deal with that. I'll just let it crash, especially
because I can't import the os library. I'll read arguments from the command line
using sys.argv. I must import the sys library. The output will be either printed
text or a new file, in which case the shell will make it for me when I use ">".
I think I'll be able to make most of the commands using a list technique. I'll
open the file, process it in the specific way for that command, then print it
in the appropriate format. I might need to set the working directory permanently
to be cs1440-hassett-ally-assn1. Based on the first argument, tt.py (the driver)
will send the code to run in a command's module. The next argument might be an
option. Then I have to see, with the combination of the command and option if the
next sys.argv will be a file or an extension of the option. The only commands with
an option and then an argument for the option are Cut and Head. The option extension
for Head just needs to be passed to an integer variable, but the Cut option
extension needs to be _x_.split() and then the parts of that list should be
passed to integer variables as well. Then we use those integers when we pick
what to print.

## Phase 2: Design *(30%)*

**Deliver:**

I thought we were supposed to assume the command line got perfect input until I double
checked the requirements during my implementing phase. So none of my error messages
are in the pseudocode.
```python
# found in the "else" section of tt.py
# will run this code given that there are at least two arguments from user
arguments = sys.argv.split()
tool = arguments[1]
arguments = arguments[2:]
if tool == "cat":
    cat(arguments)
elif tool == "tac":
    tac(arguments)
elif tool == "paste":
    paste(arguments)
elif tool == "cut":
    cut(arguments)
elif tool == "grep":
    grep(arguments)
elif tool == "head":
    head(arguments)
elif tool == "tail":
    tail(arguments)
elif tool == "sort":
    sort(arguments)
elif tool == "wc":
    wc(arguments)
else:
    usage(error="invalid tool")
```
```python
# found in Concatenate.py
def cat(args):
    # must concatenate more than one file if needed; for loop for repeats
    for file in args:  # repeats for every given argument
        file.open()
        lines = []
        for lines in file:
            lines.append(file.readline())
        # or
        print(file.readline())  # repeat somehow
        # or 
        print(file)
        file.close()
```
```python
# found in Concatenate.py
def tac(args):
    # doesn't print each line of first file then the second
    # put them together then go backwards
    lines = []
    for file in args:  # repeats for every given argument
        file.open()
        lines.append(file.readline())
        file.close()
    for i in range (len(lines), 0, -1):  # prints backwards, starting from biggest index
        print(lines[i - 1])
```
```python
# found in CutPaste.py
def paste(args):
    # combine the items of different files
    lines = []
    fileNum = 0
    for file in args:
        file.open()
        lines.append([])  # there will be as many elements in list as files
        lines[fileNum].append(file.readline())  # for list element, put lines
        fileNum += 1
    longest = 0  # we will print as many lines as most amount of lines
    for i in range (len(lines)):
        if len(lines[i]) > longest:
            longest = len(lines[1])
    for i in range (longest):
        for j in range (len(lines)):
            if lines[j][i] exists:
                print(lines[j][i], end=",")  # separate by a comma
            else:
                print("", end=",")
        print()  # new line   
    for file in args:
        file.close()

```
```python
def cut(args):
    field = []
    if args[0] == "-f":  # if there's an option 
        field = args[1].split(",")
        for i in range (len(field)):
            field[i] = int(field[i])  # make a list of every integers of each number the user enters
        # put all the files from the argument line into a list
    else:
        field.append(1)  # default as 1
    lines = []
    for file in args:  # repeats for every given argument
        file.open()
        line = file.readline()
        lines.append(line.split(","))  # split each line into sections based on the commas
        file.close()
    for i in range (len(field)):  # repeat for every number in argument
        for j in range (len(lines)):
            if field[i] <= len(lines[i]):  # if it doesn't exist
                print(lines[j][field[i] - 1], end=",")
            else:
                print("", end=",")
        print()
```
```python
# found in Grep.py
def grep(args):
    thereIsOption = False  # will it print opposite?
    if args[0] == "-v":
        keyword = args[1]
        thereIsOption = True
        args = args[2:]  # set file list here
    else:
        keyword = args[0]
        args = args[1:]  # set file list here
    lines = []
    for file in args:  # repeats for every given argument
        file.open()
        lines.append(file.readline())
        file.close()
    for i in range (len(lines)):
        if not thereIsOption and keyword in lines[i]:  # searching for keyword
            print(lines[i])
        elif thereIsOption and keyword not in lines[i]:  # searching for lack of keyword
            print(lines[i])
```
```python
# found in Partial.py
def head(args):
    numPrintedLines = 10  # default
    if args[0] == "-n":  # not default
        numPrintedLines = int(args[1])
        args = args[2:]
    lines = []
    fileNum = 0
    for file in args:
        file.open()
        lines.append([])
        lines[fileNum].append(file.readline())
        file.close()
        fileNum += 1
    for i in range (len(lines)):
        if numPrintedLines < len(lines[i]):
            numPrintedLines = len(lines[i])
        for j in range (numPrintedLines):
            print(lines[i][j])
```
```python
# found in Partial.py
def tail(args):
    numPrintedLines = 10  # default
    if args[0] == "-n":  # not default
        numPrintedLines = int(args[1])
        args = args[2:]
    lines = []
    fileNum = 0
    for file in args:
        file.open()
        lines.append([])
        lines[fileNum].append(file.readline())
        file.close()
        fileNum += 1
    for i in range (len(lines)):
        if numPrintedLines < len(lines[i]):
            numPrintedLines = len(lines[i])
        if len(lines) > 1:
            print("==> ", args[i], " <==")
        for j in range (len(lines[i]), len(lines[i]) - numPrintedLines, -1):
            print(lines[i][j - 1])
        print()
```
```python
# found in Sorting.py
def sort(args):
    [lines = []
    for file in args:
        file.open()
        lines.append(file.readline())
        file.close()
    '''compare chuck of first line to second
    if they don't match, compare them:
        put whichever has a higher order second
    if they match:
        increase the size of the chunk'''
    lines.sort()
    for i in range (len(lines)):
        print(lines[i])]
```
```python
# found in WordCount.py
# will print the number of lines, then words, then characters, then the file name
def wc(args):
    args = args.split()
    totalLines = 0
    totalWords = 0
    totalChar = 0
    for file in args:
        file.open()
        lines = []
        numWords = 0
        numChar = 0
        # do this appending for every line
        lines.append(file.readline())
        numLines = len(lines)
        for i in range (len(lines)):
            numChar += len(lines[i])
        for i in range (len(lines)):
            lines[i] = lines[i].split()
            numWords += len(lines[i])
        print(format(numLines, ">10d", numWords, ">10d", numChar, ">10d"), args[file])
        totalWords += numWords
        totalChar += numChar
        totalLines += numLines
        file.close()
    if len(args) > 1:
        print(format(totalLines, ">10d", totalWords, ">10d", totalChar, ">10d"), "total")
```

## Phase 3: Implementation *(15%)*

**Deliver:**

I thought sys.argv would give me a string, not a list, so I had to change a few
things because of that. I also couldn't figure out for the life of me how to get
the text from the files to become a string, but one line at a time. I had to use
a while loop. My cut function was formatted completely wrong so I basically had
to rewrite the entire thing. I had a hard time with cut and paste when they would
print with the new line characters at the end, so I had to figure out how to cut
that part off the string before printing. I also had to add a bunch of error
messages for different error situations. In tail, I accidentally printed the last
few lines backwards. So I had to change it so that the first line printed would be
N - totalLinesInFile where N is the integer put after the -n option on the command
line. My formatting in wordcount was a little bit funky.\
\
I learned that I should
check what format things we be in before I code. I thought I knew that sys.argv 
returned a string, but it was a list. Thankfully, a list is actually easier to work
with. I learned about the different ways to read from a file. I used readline()
because it was easiest to reformat text that way, but the other ones are useful in
different situations and for different needs.\
\
I like to have readable code as well, so after I got all the methods working I
went back and organized the code. I put all the error messages at the beginning
of the function even though it takes more lines. Then I rewrote the for loop
variables, so it makes more sense to someone who didn't write it. It also makes
it easier for me, so that's a plus. Then I went back and deleted all the DuckieCorp
text at the top of the file. I also deleted the tips and print statements at the 
beginning of the function. It was just cluttered.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

I ran "python src/tt.py paste data/let3 data/names10" and it worked perfectly
fine and then I ran "python src/tt.py paste data/names10 data/let3" and it only
printed as many lines as the second file entered. I figured out the issue when
I ran "python src/tt.py paste data/names10" and it didn't print anything because
lines[1] was out of range. I had forgotten to generalize this as lines[i] so it 
only printed as many lines as the second file had, instead the greatest number of
lines between all the files. I got a bug when I tried to run "cut" on three files.
The first and last were actual files but the middle one didn't exist. I
immediately got an error message instead of running the first file's bit and then
quitting. I fixed this by putting all of the printing part of my code in the for
loop that repeats for each file. Before, I put every file into a big long list
but this time I made a new list for every file, but I ran each list before making
the next one. I got a bug in head and tail when I ran the program. I accidentally
told the program to print the greater number of lines between the number of lines
in the file and the number from the user's input. I just changed it so it would
print the smaller number. When I went back over my code to make it more readable,
I rearranged some lines in cut and then it stopped working. Somehow I read an
extra line into my lines list and it screwed it up so I appended the line to the
lines list after preparing to read again.

## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

* I think it was sloppy of me to use i and j as the for loop variables most often. I tried to go back and change them into something better but nothing made sense without making the code look messy and unreadable.
* I'm not sure why the line "if not line" will produce either true or false. I get that it will be false when it's done reading but I don't know how that happens.
* I have a pretty good understanding of where everything is and what lines can cause what problems, so I think it would take me a couple of hours max.
* My documentation is pretty organized until Phase 4, where it's just a big jumble. The rest of it is organized by command line method.
* I think this will make plenty of sense later on.
* It will be really easy to add onto this, because I can just import a new module, and update tt.py and Usage.py to match.
* I only import the sys library, so I doubt new software would mess with very much of my code. If variable types change, though, that could be an issue.
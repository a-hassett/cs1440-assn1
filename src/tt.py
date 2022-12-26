import sys

from Concatenate import cat, tac                                    	         	  
from CutPaste import cut, paste                                     	         	  
from Grep import grep                                               	         	  
from Partial import head, tail                                      	         	  
from Sorting import sort                                            	         	  
from WordCount import wc                                            	         	  
from Usage import usage


if len(sys.argv) < 2:                                               	         	  
    usage()                                                         	         	  
    sys.exit(1)                                                     	         	  
else:                                                               	         	  
    tool = sys.argv[1]
    arguments = sys.argv[2:]

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

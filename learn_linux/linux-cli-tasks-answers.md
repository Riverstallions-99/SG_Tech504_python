(If time) Solution to task: Linux - Streams
Trainees will hopefully learn that:

A stream is a flow of data to/from programs to hardware (e.g. to the screen)
3 data streams:
STDIN - Standard input
Data that is fed in to your program
Could come from the file you give to the program or another other stream
Code 0
STDOUT - Standard output
Data that comes out of your program and, by default, gets printed to the terminal for you to see
Code 1
STDERR - Standard error
If a program encounters an error it will write a message to Standard Error
May not feel like a different stream sometimes because, by default, it also gets printed to the terminal
Code 2
STDOUT is directed to a file by default
Example of re-directing only STDOUT to a file:
Create new.txt
ls missing_directory new.txt >msg.txt OR ls missing_directory new.txt 1>msg.txt (STDERR should still print to the screen because it's not being re-directed)
Example of re-directing only STDERR to a file:
Create new.txt
ls missing_directory new.txt 2>msg.txt (STDOUT should still print to the screen because it's not being re-directed)
Example of re-directing both STDOUT and STDERR to a file:
Create new.txt
ls missing_directory new.txt >msg.txt 2>&1 (neither STDOUT or STDERR should print to the screen)
&1 is needed so it understands it is a stream code (without the & it will think 1 is a file)


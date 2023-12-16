# hello.py

Preface
---

in hello.py at the top of the file you can see the following

`#!/usr/bin/env python3` this is called a shebang which is what allows us to run
./hello.py from the terminal

before you are able to do this, you have to run `chmod +x *.py` on the file you run
in the Makefile you can see that we target the name of the command
which should be the same as the file, and is noted as `@.py` we then continue
to run the `chmod +x` command in addition to running the file directly in the same command.

This file specifically shows a simple, and easy print statement
there may be some interest in looking to dynamically linking and compiling python files together
where this Makefile could truly come in handy for bigger projects.
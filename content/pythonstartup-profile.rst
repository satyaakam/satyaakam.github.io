PYTHONSTARTUP == .profile
#########################
:date: 2009-06-04 14:20
:author: satya
:category: python, tips
:tags: python
:slug: pythonstartup-profile
:status: published

When you use Python interactively, it is frequently handy to have some
standard commands executed every time the interpreter is started. You
can do this by setting an environment variable named PYTHONSTARTUP to
the name of a file containing your start-up commands. This is similar to
the .profile feature of the Unix shells.

This file is only read in interactive sessions, not when Python reads
commands from a script, and not when /dev/tty is given as the explicit
source of commands (which otherwise behaves like an interactive
session). It is executed in the same namespace where interactive
commands are executed, so that objects that it defines or imports can be
used without qualification in the interactive session. You can also
change the prompts sys.ps1 and sys.ps2 in this file.

If you want to read an additional start-up file from the current
directory, you can program this in the global start-up file using code
like if os.path.isfile('.pythonrc.py'): execfile('.pythonrc.py'). If you
want to use the startup file in a script, you must do this explicitly in
the script:

| import os
|  filename = os.environ.get('PYTHONSTARTUP')
|  if filename and os.path.isfile(filename):
|  execfile(filename)

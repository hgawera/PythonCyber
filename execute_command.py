import subprocess

# Subprocess allows us to execute system commands

command = "msg * You have been Hacked bro"
# Popen executes command and keeps programme running (does not wait for command to finish)
subprocess.Popen(command, shell=True)
# So invoking the shell invokes a program of the user's choosing and is platform-dependent.

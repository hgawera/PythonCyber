import subprocess

# Subprocess allows us to execute system commands

# command = "wmic product get name"
message = "'You have been hacked!'"
commandone = "PowerShell -Command "
commandtwo = '"Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]'
commandthree = '::Show(' + str(message) + ')"'

commands = commandone + commandtwo + commandthree
# Popen executes command and keeps programme running (does not wait for command to finish)
print(commands)
subprocess.Popen(commands, shell=True)
# So invoking the shell invokes a program of the user's choosing and is platform-dependent.

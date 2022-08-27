# Shutdown.py helps shutdown your Windows computer using PowerShell and Python
import socket
import os

# Obtains Computer Hostname, Designate Shell Environment, Establishes Command
hostname = socket.gethostname()
shell = "powershell.exe"
command = "Stop-Computer -ComputerName " + hostname + " -Force"

# Executes PowerShell command Stop-Computer -ComputerName [ hostname ] -Force
os.system(shell + " " + command)

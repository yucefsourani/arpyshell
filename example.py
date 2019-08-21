from arpyshell import ArPyShell

shell = ArPyShell()
print(shell.ls("~/vlc.py ",output=True,utf8=False,shell="bash -c "))
print(shell.ls("~/vlc.py ",output=True,utf8=True))


print(shell.ls("~/vlc.py ",output=True,utf8=False))
print(shell.ls("~/vlc.py ",output=False,utf8=True))

print(shell.ls("~/vlc ",output=True))
print(shell.ls("~/vlc ",output=False))

print(shell.ls("fortest",output=True))
print(shell.mkdir("-p fortest",output=True))
print(shell.ls("fortest ",output=False))

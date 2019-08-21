from arpyshell import ArPyShell

bash = ArPyShell(shell="bash -c ")
print(bash.ls("~/vlc.py ",output=True,utf8=False))
print(bash.ls("~/vlc.py ",output=True,utf8=True))


print(bash.ls("~/vlc.py ",output=True,utf8=False))
print(bash.ls("~/vlc.py ",output=False,utf8=True))

print(bash.ls("~/vlc ",output=True))
print(bash.ls("~/vlc ",output=False))

print(bash.ls("fortest",output=True))
print(bash.mkdir("-p fortest",output=True))
print(bash.ls("fortest ",output=False))

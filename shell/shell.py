z=0 #While this is equal to zero...
print("ninetyeightOS cmdline v0.1")
a=raw_input(">")
while z == 0: #It forms a loop that can be stopped until the program is stopped!
  if a == 'commands':
    print("sudo - superuser; use this when downloading something or changing settings.")
    print("apt-get - get an app; you must list an apps name after this command or it will not work.")
    print("about - displays information about this terminal.")
    print("current packages - prints all of the current packages that are available for download.")
    a=0
    
  if a == 0:
    a=raw_input(">")

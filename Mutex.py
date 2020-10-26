n = int(input("Enter the number of processes: "))
l = []
while True:
    print("1.Request\n2.Release\n3.Exit")
    i = int(input())
    if i == 3:
        break
    if i == 1:
        p = int(input("Enter the process number: "))
        if len(l) == 0:
          l.append(p)
        else:
            print("Process {0} already in the critical section.".format(l[0]))
            l.append(p)
        print("Processes waiting are: ",l[1:])
    if i== 2:
        if len(l) != 0:
            l.pop(0)
            if len(l) == 0:
                print("No processes are waiting.")
            else:
                print("Critical section currently has: ",l[0])
        else:
            print("No processes are waiting.")
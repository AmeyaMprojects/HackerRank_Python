if __name__ == '__main__':
    N = int(input())
    x=[]
    for i in range(N):
        command = input()
        if "insert" in command:
            command = command.split(" ")
            x.insert(int(command[1]), int(command[2]))
            
        elif command == "print":
            print(x)
            
        elif "remove" in command:
            command = command.split(" ")
            x.remove(int(command[1]))
            
        elif "append" in command:
            command = command.split(" ")
            x.append(int(command[1]))
            
        elif command == "sort":
            x.sort()
            
        elif command == "pop":
            x.pop()
            
        elif command == "reverse":
            x.reverse()
            
            
            

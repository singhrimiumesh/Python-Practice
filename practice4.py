print("Start\n")
f = open("file1.txt", "r")

while True:
    line = f.readline()
    if not line:
        break 
    print(line.split(",")[0])  # Print the first element before the comma i.e 1st column.
    print(line.split(",")[1])
    print(line.split(",")[2])
print("\nEnd")



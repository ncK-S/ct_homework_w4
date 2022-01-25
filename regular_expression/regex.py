

with open("regular_expression/regex.txt") as f:
    for line in f:
        if line.index == 2:
            print(line.split()[-1])
    

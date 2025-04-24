with open ("q2-input.txt","r") as file:
    global ans
    ans=set()
    for line in file:
        input=set(line.strip("\n"))
        print(input)
        ans=ans.union(input)
    ans.remove(",")
    print(len(ans))


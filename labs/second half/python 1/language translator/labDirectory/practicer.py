import sys
import numpy as np
var=0
finalist=[]
with open ("translations.csv","r") as file:
    for line in file:
        var+=1
        given=line.strip("\n")
        listed=list(given.split(','))
        finalist.append(listed)
    np.array(finalist).reshape(var,4)

desired = np.full((var, 3), None, dtype=object)
for i in range(var):
    if(finalist[i][0]=="punjabi"):
        if(finalist[i][2]=="english"):
            if((finalist[i][1] not in desired) and (finalist[i][3] not in desired)):
                desired[i][1]=finalist[i][3]
                desired[i][2]=finalist[i][1]
            else:
                if(finalist[i][1] in desired):
                    loc=np.where(desired==finalist[i][1])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]-1]=finalist[i][3]
                else:
                    loc=np.where(desired==finalist[i][3])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]+1]=finalist[i][1]                   
    if(finalist[i][0]=="english"):
        if(finalist[i][2]=="punjabi"):
            if((finalist[i][1] not in desired) and (finalist[i][3] not in desired)):
                desired[i][2]=finalist[i][3]
                desired[i][1]=finalist[i][1]
            else:
                if(finalist[i][1] in desired):
                    loc=np.where(desired==finalist[i][1])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]+1]=finalist[i][3]
                else:
                    loc=np.where(desired==finalist[i][3])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]-1]=finalist[i][1]                   
    if(finalist[i][0]=="hindi"):
        if(finalist[i][2]=="english"):
            if((finalist[i][1] not in desired) and (finalist[i][3] not in desired)):
                desired[i][1]=finalist[i][3]
                desired[i][0]=finalist[i][1]
            else:
                if(finalist[i][1] in desired):
                    loc=np.where(desired==finalist[i][1])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]+1]=finalist[i][3]
                else:
                    loc=np.where(desired==finalist[i][3])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]-1]=finalist[i][1]                   
    if(finalist[i][0]=="english"):
        if(finalist[i][2]=="hindi"):
            if((finalist[i][1] not in desired) and (finalist[i][3] not in desired)):
                desired[i][0]=finalist[i][3]
                desired[i][1]=finalist[i][1]
            else:
                if(finalist[i][1] in desired):
                    loc=np.where(desired==finalist[i][1])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]-1]=finalist[i][3]
                else:
                    loc=np.where(desired==finalist[i][3])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]+1]=finalist[i][1]                   
    if(finalist[i][0]=="punjabi"):
        if(finalist[i][2]=="hindi"):
            if((finalist[i][1] not in desired) and (finalist[i][3] not in desired)):
                desired[i][0]=finalist[i][3]
                desired[i][2]=finalist[i][1]
            else:
                if(finalist[i][1] in desired):
                    loc=np.where(desired==finalist[i][1])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]-2]=finalist[i][3]
                else:
                    loc=np.where(desired==finalist[i][3])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]+2]=finalist[i][1]                   
    if(finalist[i][0]=="hindi"):
        if(finalist[i][2]=="punjabi"):
            if((finalist[i][1] not in desired) and (finalist[i][3] not in desired)):
                desired[i][2]=finalist[i][3]
                desired[i][0]=finalist[i][1]
            else:
                if(finalist[i][1] in desired):
                    loc=np.where(desired==finalist[i][1])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]+2]=finalist[i][3]
                else:
                    loc=np.where(desired==finalist[i][3])
                    desired[loc[0].flatten()[0]][loc[1].flatten()[0]-2]=finalist[i][1]                   
  
ans1=[]
if(sys.argv[1]=="1"):
    if(sys.argv[2]=="english"):
        for i in range(var):
            if(desired[i][1] is not None ):
                ans1.append(desired[i][1])
        print(sorted(ans1, reverse=True))
    if(sys.argv[2]=="hindi"):
        for i in range(var):
            if(desired[i][0] is not None ):
                ans1.append(desired[i][0])
        print(sorted(ans1, reverse=True))
    if(sys.argv[2]=="punjabi"):
        for i in range(var):
            if(desired[i][2] is not None ):
                ans1.append(desired[i][2])
        print(sorted(ans1, reverse=True))
ans2=[]
if(sys.argv[1]=="2"):
    if(sys.argv[2]=="hindi" and sys.argv[3]=="english" ):
        for i in range(var):
            if(desired[i][0] is not None and desired [i][1] is not None):
                ans2.append(tuple(desired[i][0],desired[i][1]))
        ans = sorted(ans2, key=lambda x: x[0])
        print(ans)
    if(sys.argv[2]=="english" and sys.argv[3]=="hindi" ):
        for i in range(var):
            if(desired[i][0] is not None and desired [i][1] is not None):
                ans2.append(tuple(desired[i][1],desired[i][0]))
        ans = sorted(ans2, key=lambda x: x[0])
        print(ans)
    if(sys.argv[2]=="hindi" and sys.argv[3]=="punjabi" ):
        for i in range(var):
            if(desired[i][0] is not None and desired [i][2] is not None):
                ans2.append(tuple(desired[i][0],desired[i][2]))
        ans = sorted(ans2, key=lambda x: x[0])
        print(ans)
    if(sys.argv[2]=="punjabi" and sys.argv[3]=="hindi" ):
        for i in range(var):
            if(desired[i][2] is not None and desired [i][0] is not None):
                ans2.append(tuple(desired[i][2],desired[i][0]))
        ans = sorted(ans2, key=lambda x: x[0])
        print(ans)
    if(sys.argv[2]=="punjabi" and sys.argv[3]=="english" ):
        for i in range(var):
            if(desired[i][1] is not None and desired [i][2] is not None):
                ans2.append(tuple(desired[i][2],desired[i][1]))
        ans = sorted(ans2, key=lambda x: x[0])
        print(ans)
    if(sys.argv[2]=="english" and sys.argv[3]=="punjabi" ):
        for i in range(var):
            if(desired[i][1] is not None and desired [i][2] is not None):
                ans2.append(tuple(desired[i][1],desired[i][2]))
        ans = sorted(ans2, key=lambda x: x[0])
        print(ans)

if(sys.argv[1]=="3"):
    if(sys.argv[2]=="english"):
        found=False
        for i in range(var):
            if(desired[i][1]==sys.argv[4]):
                found=True
                if(sys.argv[3]=="hindi"):
                    print(desired[i][0] if desired[i][0] is not None else "UNK")
                if(sys.argv[3]=="punjabi"):
                    print(desired[i][2] if desired[i][2] is not None else "UNK")  
                if(sys.argv[3]=="english"):
                    print(desired[i][1] if desired[i][1] is not None else "UNK")   
        if(not found):
            print("UNK")
             
    if(sys.argv[2]=="hindi"):
        found=False
        for i in range(var):
            if(desired[i][0]==sys.argv[4]):
                found=True
                if(sys.argv[3]=="hindi"):
                    print(desired[i][0] if desired[i][0] is not None else "UNK")
                if(sys.argv[3]=="punjabi"):
                    print(desired[i][2] if desired[i][2] is not None else "UNK")  
                if(sys.argv[3]=="english"):
                    print(desired[i][1] if desired[i][1] is not None else "UNK")  
        if(not found):
            print("UNK")
                
    if(sys.argv[2]=="punjabi"):
        found=False
        for i in range(var):
            found=False
            if(desired[i][2]==sys.argv[4]):
                found=True
                if(sys.argv[3]=="hindi"):
                    print(desired[i][0] if desired[i][0] is not None else "UNK")
                if(sys.argv[3]=="punjabi"):
                    print(desired[i][2] if desired[i][2] is not None else "UNK")  
                if(sys.argv[3]=="english"):
                    print(desired[i][1] if desired[i][1] is not None else "UNK") 
        if(not found):
            print("UNK")
  
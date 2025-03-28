'''
    Olympics Medals
    Author: Saksham Rathi
'''

from argparse import ArgumentParser as ap
import os

parser = ap()
parser.add_argument('--path', type=str, required = True)
args = parser.parse_args()

# dictionary for the data
totalData = {}

# looping through the directory
for fileName in os.listdir(args.path):
    filePath = os.path.join(args.path, fileName)
    # read the file
    # loop through data of file and set the values for the data
    with open(filePath,"r") as file:
        for line in file:
            given=(line.strip("\n"))
            arr=list(given.split("-"))
            if(arr[0] in totalData):
                totalData[arr[0]][0]+=int(arr[1])
                totalData[arr[0]][1]+=int(arr[2])
                totalData[arr[0]][2]+=int(arr[3])
            else:
                totalData[arr[0]]=[int(arr[1]),int(arr[2]),int(arr[3])]

sorted_data = dict(sorted(totalData.items(), key=lambda x: (-x[1][0], x[0])))
print(sorted_data)

# sort as per gold medals and break ties lexicographically
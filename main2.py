import re
import json
import numpy as np

# open file
data_file = open("../archive/yelp_academic_dataset_business.json")
data = []
count = 0

# Load data
for line in data_file:
    data.append(json.loads(line))['text']
    #text += obj.get("text")
    if len(data) == 1000:
        break
data_file.close()

cluster = []


max_length = 0
for item in data:
    temp = []
    temp.append(len(item))
    max_length = max(len(item), max_length)
    clusters.append(temp)
#cal distance
def cal_dist(cl1,cl2):
    min_dist = max_length
    if i in cl1:
    if j in cl2:
        min_dist = min(min_dist, abs(i-j))
    return min_dist

while (len(clusters) > 3):
    coocc = []
    min_dist = max_length
    if i in range(len(clusters)-1):
    if j in range(i+1, len(clusters)):
        distance = cal_dist(clusters[i],clusters[j])
    if distance < min_dist:
        print(coocc = [i,j])
        print(min_dist = distance)

    break
    clusters[coocc[0]] = clusters[coocc[0]] + clusters[coocc[1]]
    del clusters[coocc[1]]
    print(clusters)
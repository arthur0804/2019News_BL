import os

folder_path = "/pine/scr/j/i/jiaming/newstrack/instances_json/"

NonRelevantList = []

with open ("NonRelevantNews.txt", 'r') as f:
    for line in f.readlines():
        NonRelevantList.append(line.split("\t")[0])

for file_name in NonRelevantList:
    try:    
        file_path = folder_path + file_name + ".json"
        os.remove(file_path)
        print("{}.json has been removed".format(file_name))

    except Exception:
        continue

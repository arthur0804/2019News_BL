folderpath = "instances_json/"
import json
count = 0
with open ("data/wapo.jl", "r") as f:
    for line in f.readlines():
        instance = json.loads(line)
        filepath = folderpath + instance["id"] + ".json"
        with open (filepath , "w") as fp:
            json.dump(instance, fp)
        count = count + 1
    f.close()
print(count)



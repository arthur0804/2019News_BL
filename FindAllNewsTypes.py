import os
import re
import json

type_set = set()

folder_path = "/pine/scr/j/i/jiaming/newstrack/instances_json/"

for file_name in os.listdir("/pine/scr/j/i/jiaming/newstrack/instances_json/"):

    # must be json file
    if file_name[-5:] == ".json":

        # read json file
        file_json = folder_path + file_name

        with open(file_json, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                news = json.loads(line)
                if "content" in news["contents"][0].keys():
                    if news["contents"][0]["type"] == "kicker":
                        news_category = news["contents"][0]["content"]
                    else:
                        news_category = None
                else:
                    news_category = None
                type_set.add(news_category)

for i in type_set:
    print(i)

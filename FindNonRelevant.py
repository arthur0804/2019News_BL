import os
import re
import json

folder_path = "/pine/scr/j/i/jiaming/newstrack/instances_json/"

NonRelevantTypes = ["Opinion", "Letters to the Editor", "The Post's View"]

for file_name in os.listdir("/pine/scr/j/i/jiaming/newstrack/instances_json/"):

    # must be json file
    if file_name[-5:] == ".json":

        # read json file
        file_json = folder_path + file_name

        with open(file_json, 'r') as f:
            for line in f.readlines():
                news = json.loads(line)
                news_id = news["id"]
                # get the news type in the "kicker" label which is the first content in the contents
                if "content" in news["contents"][0].keys():

                    news_type = news["contents"][0]["content"]

                else:

                    news_type = None

        if news_type in NonRelevantTypes:
            print(news_id + "\t" + news_type + "\n")

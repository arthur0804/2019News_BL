import os
import json

folder_path = "/pine/scr/j/i/jiaming/newstrack/instances_json/"

for file_name in os.listdir("/pine/scr/j/i/jiaming/newstrack/instances_json/"):

    if file_name[-5:] == ".json":

        file_json = folder_path + file_name

        with open(file_json, 'r') as f:

            for line in f.readlines():

                news = json.loads(line)

                if 'title' not in news.keys():
                    
                    print(file_name)

                else:

                    news_title = news['title']

                    if news_title is None:

                        print(file_name) 

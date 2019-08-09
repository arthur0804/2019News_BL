import os
import re
import json


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def ParseContent(ContentsList):
    contents_parsed = ""
    for c in ContentsList:
        # there might be NoneType in the contents
        if c is not None:
            if c["type"] == "sanitized_html":
                content_parsed = striphtml(c["content"])
                contents_parsed += content_parsed + "\n"
    return contents_parsed


folder_path = "/pine/scr/j/i/jiaming/newstrack/instances_json/"
new_folder_path = "/pine/scr/j/i/jiaming/newstrack/instances_json_parsed/"

for file_name in os.listdir("/pine/scr/j/i/jiaming/newstrack/instances_json/"):

    # must be json file
    if file_name[-5:] == ".json":

        # read json file
        file_json = folder_path + file_name

        with open(file_json, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                news = json.loads(line)
                # id, title, contens and category
                news_id = news["id"]
                news_title = news["title"]
                news_contents = news["contents"]

                if "content" in news["contents"][0].keys():
                    news_category = news["contents"][0]["content"]
                else:
                    news_category = None

                news_author = news["author"]
                news_date = news["published_date"]

        # parse the content
        news_contents_parsed = ParseContent(news_contents)

        # create a new news instance
        news_parsed = {}
        news_parsed["id"] = news_id
        news_parsed["title"] = news_title
        news_parsed["category"] = news_category
        news_parsed["author"] = news_author
        news_parsed["published_date"] = news_date
        news_parsed["content"] = news_contents_parsed

        # write into text file
        file_json_new = new_folder_path + news_id + ".json"

        with open(file_json_new, "w", encoding="utf-8") as fp:
            json.dump(news_parsed, fp, ensure_ascii=False)

import pandas as pd
import xml.etree.ElementTree as ET
import json
import os


def getNewsType(news_id):
    '''
    Get the type of a news
    Input: news id
    Output: news type
    '''
    folder_path = "/pine/scr/j/i/jiaming/newstrack/instances_json/"
    file_path = folder_path + news_id + ".json"
    file_name = news_id + ".json"

    if file_name in os.listdir(folder_path):

        with open(file_path, 'r') as f:
            file_json = json.load(f)

        if file_json["contents"][0]["type"] == "kicker":
            return  file_json["contents"][0]["content"]
        else:
            return "TypeNotKnown"

    else:
        return "TypeNotKnown"


# Parse the XML file of topics
tree = ET.parse("/pine/scr/j/i/jiaming/newstrack/topics/2018BL_topic.xml")

root = tree.getroot()

doc_id_list = []
for i in range(0, 50):
    doc_id_list.append(root[i][1].text)

topic_id_list = []
for i in range(0, 50):
    topic_id_list.append(int(root[i][0].text[-3:]))

# Read the correct answers
BL_answers = pd.read_csv(
    "/pine/scr/j/i/jiaming/newstrack/topics/2018BL_answer.txt", header=None, sep=" ")
BL_answers.columns = ["TOPIC_NO", "Q0", "DOC_ID", "REL"]

result_path = "/pine/scr/j/i/jiaming/newstrack/scripts/ReleventNewsTypes.txt"
f = open(result_path, 'a')

for i in range(0, 50):

    topic_no = topic_id_list[i]
    doc_id = doc_id_list[i]

    # header
    f.write("Topic No: {} \t Type: {} \n".format(
        topic_no, getNewsType(doc_id)))

    # Docs with 16 relevance score
    df_rel_16 = BL_answers[(BL_answers.TOPIC_NO == topic_no)
                           & (BL_answers.REL == 16)]
    f.write("{} 16-Rel docs\n".format(df_rel_16.shape[0]))

    for index, rows in df_rel_16.iterrows():
        answer_doc_id = df_rel_16.loc[index, "DOC_ID"]
        f.write("\t{}\n".format(getNewsType(answer_doc_id)))

    # Docs with 8 relevance score
    df_rel_8 = BL_answers[(BL_answers.TOPIC_NO == topic_no)
                          & (BL_answers.REL == 8)]
    f.write("{} 8-Rel docs\n".format(df_rel_8.shape[0]))

    for index, rows in df_rel_8.iterrows():
        answer_doc_id = df_rel_8.loc[index, "DOC_ID"]
        f.write("\t{}\n".format(getNewsType(answer_doc_id)))


    # Docs with 4 relevance score
    df_rel_4 = BL_answers[(BL_answers.TOPIC_NO == topic_no)
                           & (BL_answers.REL == 4)]

    f.write("{} 4-Rel docs\n".format(df_rel_4.shape[0]))

    for index, rows in df_rel_4.iterrows():
        answer_doc_id = df_rel_4.loc[index, "DOC_ID"]
        f.write("\t{}\n".format(getNewsType(answer_doc_id)))

    # Docs with 2 relevance score
    df_rel_2 = BL_answers[(BL_answers.TOPIC_NO == topic_no)
                           & (BL_answers.REL == 2)]

    f.write("{} 2-Rel docs\n".format(df_rel_2.shape[0]))

    for index, rows in df_rel_2.iterrows():
        answer_doc_id = df_rel_2.loc[index, "DOC_ID"]
        f.write("\t{}\n".format(getNewsType(answer_doc_id)))


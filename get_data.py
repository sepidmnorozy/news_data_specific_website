import csv
from pymongo import MongoClient

# with open('news_data.csv','r') as userFile:
#     userFileReader = csv.reader(userFile)
#     for row in userFileReader:
#         print(row)


# title = "سلام عنوان"
# url = "سلام لینک"
# sections = "سلام دسته بندی ها"
# summary = "سلام خلاصه"
# date = "سلام تاریخ"
# code = "سلام کد خبر"
# tags = "سلام برچسبها"
# text = "سلام متن"
# row_contents = [title, url, sections, summary, date, code, tags, text]




client = MongoClient()
db = client['newsdb_week']
articles = db.weekarticles

myquery = { "url": { "$regex": "https://namehnews.com/" } }
for a in articles.find(myquery):
    row_contents = [a["title"], a["url"], a["article_section"], a["summary"], a["date"],
                    a["code"], a["tags"], a["text"]]
    print("*******************************************************************************")
    print(row_contents)
    print("*******************************************************************************")
    # with open('news_data.csv', 'a') as data_file:
    #     newFileWriter = csv.writer(data_file)
    #     newFileWriter.writerow(row_contents)


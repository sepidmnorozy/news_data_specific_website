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

row_contents = ["title", "url", "article_section", "summary", "date", "code", "tags", "text"]
with open('news_data.csv', 'w') as data_file:
    newFileWriter = csv.writer(data_file)
    newFileWriter.writerow(row_contents)

count = 0
myquery = { "url": { "$regex": "http://www.akhbarbank.com" } }
for a in articles.find(myquery):
    if count > -1:
        row_contents = [" " if a["title"] is None else a["title"].replace('\t',''),
                        " " if a["url"] is None else a["url"].replace('\t', ''),
                        a["article_section"],
                        " " if a["summary"] is None else a["summary"].replace('\t', ''),
                        " " if a["date"] is None else a["date"].replace('\t', ''),
                        " " if a["code"] is None else a["code"].replace('\t', ''),
                        a["tags"],
                        " " if a["text"] is None else a["text"].replace('\t', '')]
        print("*******************************************************************************")
        print(row_contents)
        count += 1    
        with open('news_data.csv', 'a') as data_file:
            newFileWriter = csv.writer(data_file)
            newFileWriter.writerow(row_contents)
        data_file.close()
    else:
        break

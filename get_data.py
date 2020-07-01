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
    if count < 2:
        row_contents = [a["title"].replace('\t',''), a["url"].replace('\t',''), a["article_section"], a["summary"].replace('\t',''), a["date"].replace('\t',''),
                        a["code"].replace('\t',''), a["tags"], a["text"].replace('\t','')]
        print("*******************************************************************************")
        print(row_contents)
        count += 1    
        with open('news_data.csv', 'a') as data_file:
            newFileWriter = csv.writer(data_file)
            newFileWriter.writerow(row_contents)
        data_file.close()
    else:
        break

import csv

with open('news_data.csv','r') as userFile:
    userFileReader = csv.reader(userFile)
    for row in userFileReader:
        print(row)


title = "سلام عنوان"
url = "سلام لینک"
sections = "سلام دسته بندی ها"
summary = "سلام خلاصه"
date = "سلام تاریخ"
code = "سلام کد خبر"
tags = "سلام برچسبها"
text = "سلام متن"
row_contents = [title, url, sections, summary, date, code, tags, text]


# with open('news_data.csv', 'a') as data_file:
#     newFileWriter = csv.writer(data_file)
#     newFileWriter.writerow(row_contents)


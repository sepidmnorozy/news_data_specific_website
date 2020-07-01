import csv

with open('news_data.csv','r') as userFile:
    userFileReader = csv.reader(userFile)
    for row in userFileReader:
        print("***************************************")
        print(row)

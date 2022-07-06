import csv

from yw.ywSyDay import checkArgsAllMouth

date_rules_list = []


def runMouth():
    csvFile = open("config\\date_rules.csv", "r")
    reader = csv.reader(csvFile)
    global date_rules_list
    date_rules_list = list(reader)
    print(date_rules_list)
    for i in date_rules_list:
        print(i[0])
        checkArgsAllMouth(i[0], i[0][0:4])
    pass


if __name__ == '__main__':
    runMouth()
    pass




def sheet_data(sheet):

    out = list()

    sheetIndex = 0
    for X in range(1, s.nrows):
        learner = s.row_values(X)
        print(learner)
        average=sum(learner)
        out.append([learner[1], average])

    return out

def sum(learner):
    average = 0
    for score in range(2, len(learner)) :
        average = average+learner[score] // 2
        if debug>0:
            print(learner[score], average)
    return average

import xlrd

a = xlrd.open_workbook("БИОЛОГИ_ таблица успеваемости осень 2018.xlsx")
debug = 1

for s in a.sheets():
    if (s.name == 'Python') == True:
        out = sheet_data(s)
        if debug == 1:
            print(out)


class PRESENT_RESULT  :
    def __init__(self, a):
        self.a=a
    def __str__(self):
        return self.a




print("RESULT:")

resultat = ''

for _ in range(1, len(out)):
	resultat += str(out[_])

print(PRESENT_RESULT(resultat))
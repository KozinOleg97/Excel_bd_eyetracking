from os import listdir

from DataLoader import ProcessPerson
import pandas as pd
import openpyxl

path = "C:\Excel_Py\Готовые GDR"

dirList = listdir(path)

resList = []


def ReformDf(df):
    # ddd
    # ddd
    return df


def getPersonName(dir):
    dir = dir.replace(' ', '').replace(',', '.').replace('(2)', '')
    dir = dir[dir.rfind(".") + 1:dir.rfind(".") + 7]

    return dir


for dir in dirList:
    testDirList = listdir(path + "\\" + dir)

    person = getPersonName(dir)

    resList.append(ProcessPerson(path=path + "\\" + dir, testDirList=testDirList, personCode=person))

# for testFile in testDirList:
#     testFileList = listdir(path + "\\" + dir + "\\" + testFile)

df = pd.concat(resList, axis=1, ignore_index=True)
df = df.reindex(sorted(df.columns), axis=1)
df = df.T

df = ReformDf(df)

df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')

# df.to_csv('file_name.csv', sep=';', encoding='utf-8')

print("d")

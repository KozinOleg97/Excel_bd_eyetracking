from os import listdir

import numpy as np
import pandas as pd
from dataclasses import dataclass

from Data import *

mainDataList = []
resData = []


@dataclass
class resultForTest:
    meanList = []
    stdevList = []


def baseMath(currentTestFile):
    data = pd.read_csv(currentTestFile, sep=";", decimal=',', na_values=['(NA)']).fillna(0)

    result = resultForTest

    result.mean = data.mean()
    result.std = data.std()

    return result


def addData(res):
    i = 2
    for meanElem in res.mean:
        mainDataList[i].append(meanElem)
        i = i + 1

    for stdElem in res.std:
        mainDataList[i].append(stdElem)
        i = i + 1


def Affective_priming(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Visconsin_test(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Derie_Levald(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Metodika_NPA(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Multitask(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Switching(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Stop_signal(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Simon(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Stroop(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Flanker(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Corsy(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Demand_selection(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Go_nogo(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Iowa(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Nawon(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def PasatC(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def Visualsearch(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def RiskFactors(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def TAS(currentTestFile):
    res = baseMath(currentTestFile)
    addData(res)


def ProcessPerson(path, testDirList, personCode):
    mainDataList.clear()
    for i in range(62):
        list = []
        mainDataList.append(list)

    for testDir in testDirList:

        currentTestFiles = listdir(path + "\\" + testDir)

        pathToTest = path + "\\" + testDir + "\\" + currentTestFiles[0]

        testName = testDir

        # Есть проблемка с тем что коды и названия тестов записываются безусловно, а значения тестов условно (их
        # может не быть)
        mainDataList[0].append(personCode)
        mainDataList[1].append(testName)

        if testName.lower().find('аффективный') != -1:
            Affective_priming(pathToTest)

        elif testName.lower().find('висконсинский') != -1:
            Visconsin_test(pathToTest)

        elif testName.lower().find('дери') != -1:
            Derie_Levald(pathToTest)

        elif testName.lower().find('методика') != -1:
            Metodika_NPA(pathToTest)

        elif testName.lower().find('многозадачность') != -1:
            Multitask(pathToTest)

        elif testName.lower().find('переключение') != -1:
            Switching(pathToTest)

        elif testName.lower().find('стоп') != -1:
            Stop_signal(pathToTest)

        elif testName.lower().find('саймон') != -1:
            Simon(pathToTest)

        elif testName.lower().find('струп') != -1:
            Stroop(pathToTest)

        elif testName.lower().find('фланкер') != -1:
            Flanker(pathToTest)

        elif testName.lower().find('corsy') != -1:
            Corsy(pathToTest)

        elif testName.lower().find('demand') != -1:  # добавить вправо
            Demand_selection(pathToTest)

        elif testName.lower().find('go') != -1:
            Go_nogo(pathToTest)

        elif testName.lower().find('iowa') != -1:
            Iowa(pathToTest)

        elif testName.lower().find('nawon') != -1:
            Nawon(pathToTest)

        elif testName.lower().find('pasat') != -1:
            PasatC(pathToTest)

        elif testName.lower().find('visual') != -1:
            Visualsearch(pathToTest)

        elif testName.lower().find('tas') != -1:
            TAS(pathToTest)

        elif testName.lower().find('факторы') != -1:
            RiskFactors(pathToTest)

    print(personCode)

    return pd.DataFrame(mainDataList)

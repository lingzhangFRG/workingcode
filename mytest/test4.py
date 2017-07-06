import requests, pprint
import datetime
import numpy as np
import matplotlib.pyplot as plt
import re,random

import dataprocessing
import csv,os
from pathlib import Path

def check_output_file():

    for filename in ["AllTestSamplePath","new_index_name"]:
        myfile = Path(filename + ".csv")
        if myfile.is_file():
            print("Delete existing file:"+ filename +".csv")  
            os.remove(filename + ".csv")
        else:
            print("Create "+ filename+".csv")


def test_stp_service(Service_Name, Service_URL, Total_It):
    print(5*"--*--"+"Start Testing"+5*"--*--")

    SamplePath = np.array([])
    TEST_START = datetime.datetime.now()

    for it in range(Total_It):
        if (it+1)/Total_It*100%10 == 0:
            print("Testing "+ Service_Name+" Progress:" + str((it+1)/Total_It*100)+"%")
    # If the service is insert_var and upload_time_series, then need to generate data
        if Service_Name == "Insert_Variable":
            Service_URL = treat_InsertVariable(Service_Name, Service_URL)

        t_start = datetime.datetime.now()
        r = requests.get(Service_URL)
        t_end = datetime.datetime.now()
        duration = t_end - t_start
        SamplePath = np.append(SamplePath, [duration.total_seconds()])

    TEST_END = datetime.datetime.now()
    TOTAL_TIME = TEST_END - TEST_START
    print(5 * "--*--" + " The end " + 5 * "--*--")
    print("Testing window for " + Service_Name+ " : " + str(TEST_START.replace(second=0, microsecond=0))+" to "+ str(TEST_END.replace(second=0, microsecond=0)))
    print("Total elapsed time for : " +Service_Name + " : "+ str(TOTAL_TIME.total_seconds()) + "s")

    np.savetxt('output/'+Service_Name+'.csv', SamplePath, delimiter=',')  # X is an array

    outfile = open('AllTestSamplePath.csv', 'a+')
    writer = csv.writer(outfile, delimiter=',',lineterminator = '\n')
    # writer.writerow([SamplePath])
    writer.writerows([SamplePath])
    outfile.close()

    return SamplePath

def readService2Test(filename):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row[1])
            # print()

def treat_InsertVariable(Service_Name, Service_URL):
    if re.search(r'&name=[\w]+&', Service_URL):
        new_input_name = "test_FACTOR"+str(random.randint(1,100000))
        new_input = "&name="+new_input_name+"&"
        Service_URL = re.sub(r'&name=[\w]+&',new_input , Service_URL)
        # print(new_input_name)
        outfile = open('new_index_name.csv','a+')
        writer = csv.writer(outfile, delimiter=',',lineterminator = '\n')
        writer.writerow([new_input_name])
        outfile.close()
    else:
        raise Exception("No name= field found!")
    return Service_URL

def main(Total_It):
    check_output_file()

    ServiceList=[]
    AllSamplePath = np.array([])

    readCSV = readCSV = csv.reader(open("Service_List.csv"), delimiter=',')
    for row in readCSV:
        Service_Name = row[0]
        Service_URL = row[1]

        ServiceList.append(Service_Name) 
        print(row)
        test_stp_service(Service_Name,Service_URL,Total_It)
        dataprocessing.plotresult(Service_Name)

    print(4*"--*---"+"Complete Test List"+4*"--*---")
    print(ServiceList)

# def main():
#     TOTAL_IT = 10
#     SINGLE_IT = 1
#
#     print(10*"--*--")
#     SamplePath = np.array([])
#
#     TEST_START = datetime.datetime.now()
#
#     for it in range(TOTAL_IT):
#
#         if (it+1)/TOTAL_IT*100%10 == 0:
#             print("Progress:" + str((it+1)/TOTAL_IT*100)+"%")
#
#         t_start = datetime.datetime.now()
#         for _ in range(SINGLE_IT):
#             r = requests.get(myurl)
#
#         t_end = datetime.datetime.now()
#         duration = t_end - t_start
#         SamplePath = np.append(SamplePath,[duration.total_seconds()])
#         # print("Total time: "+ str(t_end - t_start) )
#     TEST_END = datetime.datetime.now()
#     TOTAL_TIME = TEST_END - TEST_START
#     print(5 * "--*--" + " The end " + 5 * "--*--")
#     print("Testing window: " + str(TEST_START.replace(second=0, microsecond=0))+" to "+ str(TEST_END.replace(second=0, microsecond=0)))
#     print("Total elapsed time: " + str(TOTAL_TIME.total_seconds()) + "s")
#
#     np.savetxt('fit_model_update.csv', SamplePath, delimiter=',')  # X is an array
#     dataprocessing.plotresult('fit_model_update.csv', "fit_model_update")



if __name__ == "__main__":
    # main(1)
    try:
        main(200)
    except Exception as e:
        print(e)
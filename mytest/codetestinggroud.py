import re,random
import csv

Service_Name = "Insert_Variable"
Service_URL = "http://app-dev.vor.frgrisk.com:7980/SASStoredProcess/do?_username=webrunner@saspw&_password=AsdF!23$&_program=%2FSystem%2FApplications%2FVOR+System%2FCommon%2Fstps%2FFactorModel%2Finsert_variable&_action=EXECUTE&name=test_index&description=Test%20Index&type=index&account_num=&formula=test-test2"
# Service_URL = "&name=dfasdf_sdfsdfs&"
# match = re.search(r'&name=[\w]+&', Service_URL)
if Service_Name == "Insert_Variable" and re.search(r'&name=[\w]+&', Service_URL):

	new_input_name = "test_index"+str(random.randint(1,100000))
	new_input = "&name="+new_input_name+"&"
	Service_URL = re.sub(r'&name=[\w]+&',new_input , Service_URL)
	print(Service_URL)
	outfile = open('new_index_name.csv','a+')
	writer = csv.writer(outfile, delimiter=',',lineterminator = '\n')
	print(new_input_name)
	print([new_input_name])
	writer.writerow([new_input_name])
	outfile.close()

else:
	print("Puff")
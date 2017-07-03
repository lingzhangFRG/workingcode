import requests, pprint
import datetime
import numpy as np
import matplotlib.pyplot as plt
myurl = "http://app-dev.vor.frgrisk.com:7980/SASStoredProcess/do?_username=stpservice@saspw&_password=%7BSAS002%7DF7A6FA3F175EB5A8504C13D1570D585D&_program=%2FSystem%2FApplications%2FVOR+System%2FCommon%2Fstps%2FFactorModel%2Ffit_model&_action=EXECUTE&start_dt=03Jun2008&end_dt=30Jun2017&freq=MONTH&fund=146&model_sk=168&factor=130&factor=131&restrict=.&restrict=3"



def main():
    TOTAL_IT = 50
    SINGLE_IT = 1

    print(10*"--*--")
    SamplePath = np.array([])

    TEST_START = datetime.datetime.now()

    for it in range(TOTAL_IT):

        if (it+1)/TOTAL_IT*100%10 == 0:
            print("Progress:" + str((it+1)/TOTAL_IT*100)+"%")

        t_start = datetime.datetime.now()
        for _ in range(SINGLE_IT):
            r = requests.get(myurl)

        t_end = datetime.datetime.now()
        duration = t_end - t_start
        SamplePath = np.append(SamplePath,[duration.total_seconds()])
        # print("Total time: "+ str(t_end - t_start) )
    TEST_END = datetime.datetime.now()
    TOTAL_TIME = TEST_END - TEST_START
    print(5 * "--*--" + " The end " + 5 * "--*--")
    print("Testing window: " + str(TEST_START.replace(second=0, microsecond=0))+" to "+ str(TEST_END.replace(second=0, microsecond=0)))
    print("Total elapsed time: " + str(TOTAL_TIME.total_seconds()) + "s")

    np.savetxt('fit_model_update.csv', SamplePath, delimiter=',')  # X is an array

    # Need to write a outlier remover

    SampleMean = np.mean(SamplePath)
    SampleVar = np.var(SamplePath)
    Report = "Sample Mean: " + str(np.around(SampleMean, decimals=2)) + " Sample Var: " + str(np.around(SampleVar, decimals=3))
    plt.figure()
    fig = plt.plot(SamplePath)
    plt.ylabel("Response Time(s)")
    plt.xlabel("Trial")
    plt.suptitle("fit_model", fontsize=14, fontweight='bold')
    plt.annotate(Report, xy=(0.05, 0.95), xycoords='axes fraction')
    plt.ylim(ymax = np.max(SamplePath)+0.05)
    # plt.text(1, 1,'matplotlib', horizontalalignment='center',
    #              verticalalignment='center',
    #              transform=fig.transAxes)

    plt.show()


if __name__ == "__main__":
    main()
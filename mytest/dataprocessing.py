import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def test_pring():
    print(10*"--*--")
    print("This is a test print")

def reject_outliers(data, m = 3.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return np.array(data[s<m])

def plotresult(Service_Name):
    # SamplePath = np.loadtxt("fit_model_update.csv")
    datafile = 'output/'+ Service_Name +'.csv'
    SamplePath = np.loadtxt(datafile)

    SampleMean = np.mean(SamplePath)
    SampleVar = np.var(SamplePath)

    Samplepath_processed = reject_outliers(SamplePath)
    SampleMean_processed = np.mean(Samplepath_processed)
    SampleVar_processed = np.var(Samplepath_processed)


    Report = "Raw data: Sample Mean: " + str(np.around(SampleMean, decimals=2)) + " Sample Std: " + str(np.around(np.sqrt(SampleVar), decimals=3))
    Report_processed = "No Outlier: Sample Mean: " + str(np.around(SampleMean_processed, decimals=2)) + " Sample Std: " + str(np.around(np.sqrt(SampleVar_processed), decimals=3))

    pp = PdfPages('output/'+Service_Name + '.pdf')

    plt.figure(np.ceil(np.random.rand(1)*1000))
    # plt.subplot(2,1,1)
    fig = plt.plot(SamplePath)
    plt.ylabel("Response Time(s)")
    plt.xlabel("Trial")
    plt.suptitle(Service_Name, fontsize=14, fontweight='bold')
    plt.annotate(Report, xy=(0.05, 0.95), xycoords='axes fraction')
    plt.annotate(Report_processed, xy=(0.05, 0.9), xycoords='axes fraction')


    plt.ylim(ymax = np.max(SamplePath)+0.05)
    pp.savefig()
    pp.close()
    # plt.show()



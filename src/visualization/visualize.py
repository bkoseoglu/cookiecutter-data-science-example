import matplotlib.pyplot as plt

def barPlot(pos=None,yvalues=None,x_ticks=None,y_label=None,title=None,figName=None):
    plt.bar(pos, yvalues, align='center', alpha=0.5)
    plt.xticks(pos, x_ticks)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig('reports/figures/'+str(figName))
    plt.show()

def plot(xValues=None,yValues=None,lineType=None,xLabel=None,yLabel=None,title=None,saveFig=None):
    plt.plot(xValues, yValues, lineType)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.savefig(saveFig)
    plt.show()

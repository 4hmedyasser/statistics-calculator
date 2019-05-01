from tkinter import *
from tkinter import messagebox
from builtins import *
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import scipy.stats as stats
import math
import statistics
import re

def pieChart(labels,sizes):
    plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()

def drawPieChart():
    dataArray=(re.split(',',dataVar.get()))
    dataNamesArray = (re.split(',', dataNamesVar.get()))
    desired_array = [int(numeric_string) for numeric_string in dataArray]
    pieChart(dataNamesArray,desired_array)


def histogram():

    HistoDataArray = (re.split(',', HistoDataVar.get()))
    desired_array_histo = [int(numeric_string) for numeric_string in HistoDataArray]

    n, bins, patches = plt.hist(desired_array_histo,int( histBarWidthVar.get()), facecolor='blue', alpha=0.5)
    plt.show()



def barChart():

    dataArray = (re.split(',', dataVar.get()))
    dataNamesArray = (re.split(',', dataNamesVar.get()))
    Bar_desired_array = [int(numeric_string) for numeric_string in dataArray]
    y_pos = np.arange(len(dataNamesArray))
    plt.bar(y_pos, Bar_desired_array, align='center', alpha=0.5)
    plt.xticks(y_pos, dataNamesArray)

    plt.show()


def mmm():

    mmmArray = (re.split(',', modmedian.get()))
    mmmdesired_array = [int(numeric_string) for numeric_string in mmmArray]

    df = pd.DataFrame({" rating1": mmmdesired_array, "dummy": range(len(mmmdesired_array))})

    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.2, 1)})
    mean = df[' rating1'].mean()
    median = df[' rating1'].median()
    mode = df[' rating1'].mode().get_values()[0]

    sns.boxplot(df[" rating1"], ax=ax_box)
    ax_box.axvline(mean, color='r', linestyle='--')
    ax_box.axvline(median, color='g', linestyle='-')
    ax_box.axvline(mode, color='b', linestyle='-')

    sns.distplot(df[" rating1"], ax=ax_hist)
    ax_hist.axvline(mean, color='r', linestyle='--')
    ax_hist.axvline(median, color='g', linestyle='-')
    ax_hist.axvline(mode, color='b', linestyle='-')

    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode})
    label = 'Mode=' + str(mode) + ', Median=' + str(median) + ', Mean=' + str(mean)

    ax_box.set(xlabel=label)
    if (stats(mmmdesired_array) == 0.0):
        ax_hist.set(xlabel="Symmetric (Zero Skewness)")
    elif (stats(mmmdesired_array) > 1):
        ax_hist.set(xlabel="Skewed to the Right (Positive Skewness)")

    else:
        ax_hist.set(xlabel="Skewed to the left (Negative Skewness)")

    plt.show()

def calc():


    zscoreArray = (re.split(',', zscroesVar.get()))
    zscoredesired_array = [int(numeric_string) for numeric_string in zscoreArray]
    arithmetic_mean = statistics.mean(zscoredesired_array)

    standard_deviation_population = statistics.pstdev(zscoredesired_array)

    zscores = []

    for item in zscoredesired_array:
        zscore = (item - arithmetic_mean) / standard_deviation_population
        zscores.append({"Value": item, "Z-Score": zscore})

    result = {"StandardDeviation": standard_deviation_population,
              "zscores": zscores}

    messagebox.showinfo( "Z-scores and Standard Deviation", result)


def estimate_coefficients(x, y):
    # size of the dataset OR number of observations/points
    n = np.size(x)

    # mean of x and y
    # Since we are using numpy just calling mean on numpy is sufficient
    mean_x, mean_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x - n * mean_y * mean_x)
    SS_xx = np.sum(x * x - n * mean_x * mean_x)

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = mean_y - b_1 * mean_x

    return (b_0, b_1)

    # x,y are the location of points on graph
    # color of the points change it to red blue orange play around


def plot_regression_line(x, y, b):
    # plotting the points as per dataset on a graph
    plt.scatter(x, y, color="m", marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels for x and y axis
    plt.xlabel("B0 = "+str(b[0])+"   "+"B1 = "+str(b[1]))
    plt.ylabel('Cost')

    # function to show plotted graph
    plt.show()


def regression ():
    # Datasets which we create
    regressionArray1 = (re.split(',', firstVar.get()))
    regressionArray2 = (re.split(',', secoundVar.get()))
    regressiondesired_array1 = [int(numeric_string) for numeric_string in regressionArray1]
    regressiondesired_array2 = [int(numeric_string) for numeric_string in regressionArray2]

    x = np.array(regressiondesired_array1)
    y = np.array(regressiondesired_array2)

    b = estimate_coefficients(x, y)

    # tkMessageBox.showinfo("Estimate Coefficients", "B0="+str(b[0])+"\n"+"B1="+str(b[1]))
    plot_regression_line(x, y, b)

def getrelation(corr):
    if corr >=(-0.3) and corr<(0):
        return "Negative Weak Correlation"
    elif corr<(-0.3) and corr>=(-0.6):
        return "Negative Moderate Correlation"
    elif corr<(-0.6) and corr>=(-0.9):
        return "Negative Strong Correlation"
    elif corr<(1) and corr>=(0.7):
        return "Positive Strong Correlation"
    elif corr<(0.7) and corr>=(0.4):
        return "positive moderate correlation"
    elif corr<(0.4) and corr>=(0.1):
        return "Positive Weak Correlation"
    else:
        return "Perfect Correlation"

def correlationCoefficient(X, Y, n):
    sum_X = 0
    sum_Y = 0
    sum_XY = 0
    squareSum_X = 0
    squareSum_Y = 0
    i = 0
    while i < n:
        # sum of elements of array X.
        sum_X = sum_X + X[i]
        # sum of elements of array Y.
        sum_Y = sum_Y + Y[i]
        # sum of X[i] * Y[i].
        sum_XY = sum_XY + X[i] * Y[i]
        # sum of square of array elements.
        squareSum_X = squareSum_X + X[i] * X[i]
        squareSum_Y = squareSum_Y + Y[i] * Y[i]
        i = i + 1
    # use formula for calculating correlation
    # coefficient.
    corr = (float)(n * sum_XY - sum_X * sum_Y) /(float)(math.sqrt((n * squareSum_X-sum_X * sum_X)* (n * squareSum_Y -sum_Y * sum_Y)))
    return corr

def showCorrelation():
    X_str = (re.split(',', firstVar.get()))
    X = [float(numeric_string) for numeric_string in X_str]
    Y_str = (re.split(',', secoundVar.get()))
    Y = [float(numeric_string) for numeric_string in Y_str]
    n = min(len(X), len(Y))
    messagebox.showinfo("Results" , "Correlation Coefficient: " + str( round( correlationCoefficient(X, Y, n) , 2 ) ) + "\n" + "Comment: " + getrelation(correlationCoefficient(X, Y, n)))

def mean_confidence_interval(n, mu,standardError, confidence=0.95):
    h = standardError * stats.t.ppf((1 + confidence) / 2., n - 1)
    return h

def normal_distribution_plot(mu, sigma , mu2 , sigma2):
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma))
    x = np.linspace(mu2 - 3 * sigma2, mu2 + 3 * sigma2, 100)
    plt.plot(x, stats.norm.pdf(x, mu2, sigma2))
    plt.show()

def standard_error(n, sigma):
    return sigma/math.sqrt(n)

def variance_of_x_bar(n, sigma):
    return math.pow(sigma , 2)/n

def show_plot():
    normal_distribution_plot(float(mean.get())
                             , float( sigma.get() )
                             , float(mean.get())
                             , standard_error(float(number.get())
                                              , float(sigma.get()) )  )
    mean_confidence_interval(float( number.get() )
                             , float( mean.get() )
                             , standard_error(float(number.get())
                                              ,float(sigma.get()) )  )

def show_data():
    try:
        messagebox.showinfo("Results" ,
                            "μ(x̅) = " + str(mean.get()) + "\n" +
                            "σ(x̅) = " + str(  round( standard_error(float(number.get()),float(sigma.get())) ,2 )  ) + "\n" +
                            "σ(x̅)² = " + str(  round( variance_of_x_bar(float(number.get()),float(sigma.get())) ,2 )  ) + "\n" +
                            "μ = " + str(mean.get()) + "±" + str(  round( mean_confidence_interval(float(number.get()),
                                                                                              float(mean.get()),
                                                                                              standard_error(float(number.get()),
                                                                                                             float(sigma.get())
                                                                                                             ),
                                                                                              float(confidence.get())
                                                                                              )
                                                                              , 2)
                                                                       ) + "\n" +
                            "μ ∈ [ " + str( float(mean.get()) - round( mean_confidence_interval(float(number.get()),
                                                                                   float(mean.get()),
                                                                                   standard_error(float(number.get()),
                                                                                                  float(sigma.get())
                                                                                                  ),
                                                                                   float(confidence.get()))
                                                                           , 2)
                                                ) +
                                            " , " + str( float(mean.get()) + round( mean_confidence_interval(float(number.get()),
                                                                                   float(mean.get()),
                                                                                   standard_error(float(number.get()),
                                                                                                  float(sigma.get())
                                                                                                  ),
                                                                                   float(confidence.get())
                                                                                            )
                                                                                    , 2)
                                                        ) +
                                            " ]" + "\n"
                            )
    except:
        messagebox.showinfo("Results",
                            "μ(x̅) = " + str(mean.get()) + "\n" +
                            "σ(x̅) = " + str( round( standard_error(float(number.get()), float(sigma.get())) ,2 )  ) + "\n" +
                            "σ(x̅)² = " + str( round( variance_of_x_bar(float(number.get()), float(sigma.get())) ,2 )  ) + "\n" +
                            "μ = " + str(mean.get()) + "±" + str( round( mean_confidence_interval(float(number.get()),
                                                                                              float(mean.get()),
                                                                                              standard_error(float(number.get()),
                                                                                                             float(sigma.get())
                                                                                                             )
                                                                                              )
                                                                             , 2 )
                                                                     ) + "\n" +
                            "μ ∈ [ " + str( float(mean.get()) - round( mean_confidence_interval( float(number.get()), float(mean.get()),
                                                                                              standard_error(float(number.get()),float(sigma.get()))
                                                                                              ) , 2 )
                                                ) +
                                   " , " + str( float(mean.get()) + round( mean_confidence_interval( float(number.get()), float(mean.get()),
                                                                                              standard_error(float(number.get()),float(sigma.get()))
                                                                                              ) , 2 )
                                                ) +
                                    " ]" + "\n"
                            )


root = Tk()
root.title("Statistical Analysis")

frame = Frame(root)

#--------------------------------------------PieChart and BarChart--------------------------------------------------------------

Label(frame,text=" ").pack()
Label(frame,text="Please Enter The Names of The Data That You Need to Visualize").pack()
Label(frame,text="'Separate the values by commas'").pack()

dataNamesVar = StringVar()
dataNamesEntry=Entry(frame, textvariable=dataNamesVar).pack()

Label(frame,text="Please Enter The Data That You Need to Visualize").pack()
Label(frame,text="'Separate the values by commas'").pack()

dataVar = StringVar()
dataEntry = Entry(frame, textvariable=dataVar).pack()

Button(frame,text="Show The Pie Chart ",command=drawPieChart).pack()
Button(frame,text="Show The Bar Chart ",command=barChart).pack()

#--------------------------------------------histogram--------------------------------------------------------------

Label(frame,text="Please Enter The Data That You Need to Visualize with Histogram").pack()
Label(frame,text="'Separate the values by commas'").pack()

HistoDataVar = StringVar()
HistoDataEntry = Entry(frame, textvariable=HistoDataVar).pack()

Label(frame,text="Please Enter Size of Bins").pack()

histBarWidthVar = StringVar()
histDataEntry = Entry(frame, textvariable=histBarWidthVar).pack()

Button(frame,text="Show The Histogram ",command=histogram).pack()

#--------------------------------------------mode median mean--------------------------------------------------------------

Label(frame,text="To Find Mean, Median, Mode, Skewness, Graph and Box Plot \n Please Enter The Data").pack()
Label(frame,text="'Separate the values by commas'").pack()

modmedian = StringVar()
modmedinaEntery = Entry(frame, textvariable=modmedian).pack()
Button(frame,text="Show",command=mmm).pack()

#-------------------------------------------- standard deviation z-scores --------------------------------------------------------------

Label(frame,text="To Find Z-Score and Standard Deviation \n Please Enter The Data").pack()
Label(frame,text="'Separate values by commas'").pack()

zscroesVar = StringVar()
zscroesEntry = Entry(frame, textvariable=zscroesVar).pack()

Button(frame,text="Show",command=calc).pack()
#-------------------------------------------- Correlation and Regression -------------------------------------------------------------

preform = Frame(root)

Label(preform,text="\n\nCorrelation and Regression").pack()
Label(preform,text="Please Enter The Data").pack()
Label(preform,text="'Separate the values by commas'").pack()

Label(preform,text="'First data table'").pack()

firstVar = StringVar()
firstEntry = Entry(preform, textvariable=firstVar).pack()

Label(preform,text="'Second data table'").pack()

secoundVar = StringVar()
secoundEntry = Entry(preform, textvariable=secoundVar).pack()

correlationButton = Button(preform,
                         text="Show Correlation Coefficient",
                         fg="black",
                         command=lambda: showCorrelation())
correlationButton.pack()

Button(preform,text="Show Regression \n and \n Scatter Chart",command=regression).pack()

#---------------------------------------------- Estimation and Inference ----------------------------------------------
bonus = Frame(root)

mainLable = Label(bonus,
                  text="Estimation and Inference",
                  fg="black")
mainLable.pack()

meanLable = Label(bonus,
                   text="Mean (μ)",
                   fg="black")
meanLable.pack()

mean = Entry(bonus)
mean.pack()

sigmaLable = Label(bonus,
                   text="Standard Deviation (σ)",
                   fg="black")
sigmaLable.pack()

sigma = Entry(bonus)
sigma.pack()

numberLable = Label(bonus,
                   text="Sample Size (n)",
                   fg="black")
numberLable.pack()

number = Entry(bonus)
number.pack()

confidenceLable = Label(bonus,
                   text="1-α (default: 0.95)",
                   fg="black")
confidenceLable.pack()

confidence = Entry(bonus)
confidence.pack()

showPlotButton = Button(bonus,
                         text=" Show Plot ",
                         fg="black",
                         command = lambda : show_plot())

showPlotButton.pack(side = RIGHT)

calculateButton = Button(bonus,
                         text="Show Results",
                         fg="black",
                         command=lambda: show_data())
calculateButton.pack(side = LEFT)

frame.pack(side=LEFT)
bonus.pack(side=RIGHT)
preform.pack(before=bonus)

root.mainloop()
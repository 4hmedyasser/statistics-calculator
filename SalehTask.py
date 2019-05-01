#import matplotlib.pyplot as plt; plt.rcdefaults()
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#import pandas as pd
#from scipy.stats import skew
#import statistics
#import numpy as np
#import matplotlib.pyplot as plt

"""""
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()



# observations
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# estimating coefficients
b = estimate_coef(x, y)
# plotting regression line
plot_regression_line(x, y, b)
print("Estimated coefficients:\nb_0 = {}  \ \nb_1 = {}".format(b[0], b[1]))
"""""


import Tkinter as tk
from Tkinter import *
import os
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import skew
import statistics
import numpy as np
import matplotlib.pyplot as plt
import re
import tkMessageBox

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

    BarDataArray = (re.split(',', BarDataVar.get()))
    BarDataNamesArray = (re.split(',', BarNamesDataVar.get()))
    Bar_desired_array = [int(numeric_string) for numeric_string in BarDataArray]
    y_pos = np.arange(len(BarDataNamesArray))
    plt.bar(y_pos, Bar_desired_array, align='center', alpha=0.5)
    plt.xticks(y_pos, BarDataNamesArray)

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
    if (skew(mmmdesired_array) == 0.0):
        ax_hist.set(xlabel="Symmetric (Zero Skewness)")
    elif (skew(mmmdesired_array) > 1):
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

    tkMessageBox.showinfo( "Z-scores and Standard Deviation", result)


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



root = Tk()
root.geometry('500x630')
root.title("Pie Chart Visualisation")

frame = Frame(root)
frame.pack()

#--------------------------------------------PieChart--------------------------------------------------------------

Label(frame,text=" ").pack()
Label(frame,text="Please Enter The Name of The Data you need to Visualize it").pack()
Label(frame,text="'Separated by Comma'").pack()

dataNamesVar = StringVar()
dataNamesEntry=Entry(frame, textvariable=dataNamesVar,width=500).pack()

Label(frame,text="Please Enter The Data you need to Visualize it using Pie Chart").pack()
Label(frame,text="'Separatede by Comma'").pack()

dataVar = StringVar()
dataEntry = Entry(frame, textvariable=dataVar,width=500).pack()

Button(frame,text="Show The Pie Chart ",command=drawPieChart).pack()

#--------------------------------------------histogram--------------------------------------------------------------

Label(frame,text="Please Enter The Data you need to Visualize it uisn Histogram").pack()
Label(frame,text="'Separatede by Comma'").pack()

HistoDataVar = StringVar()
HistoDataEntry = Entry(frame, textvariable=HistoDataVar,width=500).pack()

Label(frame,text="Please Enter Size of Bins").pack()

histBarWidthVar = StringVar()
histDataEntry = Entry(frame, textvariable=histBarWidthVar,width=500).pack()

Button(frame,text="Show The Histogram ",command=histogram).pack()

#----------------------------------barChart-----------------------------------------------------------

Label(frame,text= "Enter The Name of the Data you need to Visualize it uisn Bar Chart").pack()
Label(frame,text="'Separatede by Comma'").pack()

BarNamesDataVar = StringVar()
BarNamedDataEntry = Entry(frame, textvariable=BarNamesDataVar,width=500).pack()

Label(frame,text="Please Enter The Data you need to Visualize it uisn Bar Chart").pack()
Label(frame,text="'Separatede by Comma'").pack()

BarDataVar = StringVar()
BarDataEntry = Entry(frame, textvariable=BarDataVar,width=500).pack()

Button(frame,text="Show The Bar Chart ",command=barChart).pack()

#--------------------------------------------mode median mean--------------------------------------------------------------

Label(frame,text="To Find Mode, Median, Mean,Skewness,Graph and Box Plot Enter the Data").pack()
Label(frame,text="'Separatede by Comma'").pack()

modmedian = StringVar()
modmedinaEntery = Entry(frame, textvariable=modmedian,width=500).pack()
Button(frame,text="Show",command=mmm).pack()

#-------------------------------------------- standard deviation z-scores --------------------------------------------------------------

Label(frame,text="Enter The Data you need to find z-scores for its value and ").pack()
Label(frame,text="Standard Deviation 'Separatede by Comma'").pack()

zscroesVar = StringVar()
zscroesEntry = Entry(frame, textvariable=zscroesVar,width=500).pack()

Button(frame,text="Show",command=calc).pack()

#-------------------------------------------- Regression --------------------------------------------------------------

Label(frame,text="Enter The Data you need to perform Regression Analysis for them ").pack()
Label(frame,text="'Separatede by Comma'").pack()

Label(frame,text="'First Data'").pack()

firstVar = StringVar()
firstEntry = Entry(frame, textvariable=firstVar,width=500).pack()

Label(frame,text="'Secound Data'").pack()

secoundVar = StringVar()
secoundEntry = Entry(frame, textvariable=secoundVar,width=500).pack()

Button(frame,text="Show",command=regression).pack()


frame.mainloop()


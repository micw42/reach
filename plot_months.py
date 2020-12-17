import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plot_month_counts(month_list,counts_list,title):
    '''Pass in a list containing months, a list containing
    corresponding number of published paper counts, and a
    string for the graph title'''
    plt.plot(months,counts)
    plt.xlabel("Month")
    plt.ylabel("Number of Papers Published")
    plt.title(title)
    plt.show()

def get_list(file_name):
    '''read a single-column file into a list'''
    reader=open(file_name,"r")
    file_list=[]
    for line in reader:
        line=int(line)
        file_list.append(line)
    return file_list

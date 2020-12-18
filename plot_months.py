import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plot_month_counts(counts_list,title,save):
    '''Pass in a list containing months, a list containing
    corresponding number of published paper counts, and a
    string for the graph title'''
    month_list=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    plt.figure()
    plt.plot(month_list,counts_list)
    plt.xlabel("Month")
    plt.ylabel("Number of Papers Published")
    plt.title(title)
    plt.savefig(save)

def get_list(file_name):
    '''read a single-column file into a list'''
    reader=open(file_name,"r")
    file_list=[]
    for line in reader:
        line=int(line)
        file_list.append(line)
    return file_list


all_counts_lst=get_list("all_month_counts.txt")
count_lst_2020=get_list("new_2020_counts.txt")
plot_month_counts(all_counts_lst,"Monthly paper counts (all time)","all_counts_plot")
plot_month_counts(count_lst_2020,"Monthly paper counts (2020)","2020_counts_plot")

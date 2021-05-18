# importing the required module 
import matplotlib.pyplot as plt 

# x axis values 
x = [1,2,3,5,8,10] 
# corresponding y axis values 
y = [200,300,353,412,456,734] 
#colors=['g']
# plotting the points 
plt.figure(1)
plt.plot(x, y,'g',label='Latency') 

# naming the x axis 
plt.xlabel('No. of Clients') 
# naming the y axis 
plt.ylabel('Latency (in ms)') 

# giving a title to my graph 
plt.title('Performance Analysis') 
plt.legend(loc=4)

# function to show the plot 
#plt.show()
plt.savefig('PerformanceAnalysis.png')
activities = ['A', 'B', 'C', 'D', 'E', 'F'] 
  
# portion covered by each label 
slices = [50, 100, 28, 56, 230, 80] 
total=sum(slices) 
# color for each label 
colors = ['r', 'y', 'g', 'b', 'c', 'm'] 
plt.figure(2) 
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0, 0, 0, 0), 
        radius = 1.2, autopct = lambda p:'{:.0f}'.format(p * total / 100)) 
plt.title('Data Analysis')  
# plotting legend 
plt.legend(loc=3) 
plt.savefig('DataAnalysis.png')  
# showing the plot 


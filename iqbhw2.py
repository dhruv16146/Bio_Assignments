#Python Version:2.7
#Dhruv Bhagat
#B-Tech:CSE
#2016146
from subprocess import call
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.stats import pearsonr   
#open genedetail.csv having 20 records
file=open("genedetail.csv","r")
#my_lis is a list of list to hold columns
my_list=[]

row=0
col=0

for i in file.readline().split(","):
		new=[]
		my_list.append(new)
		col=col+1

#place the file pointer at start
file.seek(0, 0)
#read the file to make a list of list with each column corresponding to each list
for s in iter(file):
	n=0
	c=0
	row=row+1
	for i in s.split(","):	
		my_list[c].append(i.strip("\n"))
		n=n+1
		c=c+1

lis=[]

for i in my_list[3][1:]:
	lis.append(float(i))
	
lis2=[]
for i in my_list[6][1:]:
	lis2.append(float(i))

#l denotes zscores
#l1 denotes copy number

l=np.array(lis)
l1=np.array(lis2)
call('clear')
#print the correslation coefficient
print "Correlation Coefficient:",pearsonr(l,l1)[0]

print "Correlation Coefficient of 0.74 indicates a strong correlation between z score and copy number with positive value implying that as x increases so does y"


print "Mean for zscores:",np.mean(l)
print "Standard Deviation for zscores:",np.std(l)
#plot the histogram for z scores
plt.hist(l)
plt.xlabel('Z scores-->')
plt.title('------------Histogram for Zscores-----------')
plt.show()


from numpy import random

def CreateUniformDistribution():
	return random.randint(1,20,size=100)

def PlotDistribution(distribution):
	import matplotlib.pyplot as plt
	#import seaborn as sns
	plt.hist(distribution)
	plt.title('Frequency Distribution')
	plt.xlabel('x')
	plt.ylabel('values')
	plt.show()

def Sample(n,sampleDist):
	sampleSum=0
	for i in range(n):
		sampleSum+=random.choice(sampleDist)
	return float(sampleSum)/float(n)


def RunSampleDemo(n,sampleDist,plot=False,num_bins=None):
	means=[]
	for i in range(1000):
		means.append(Sample(n,sampleDist))
	if plot:
		print "Sample Mean Distribution with n=%s"%n
		PlotDistribution(means)
	return means


if __name__=='__main__':
	sampleDist=CreateUniformDistribution()

	#plot the original population distribution
	PlotDistribution(sampleDist)

	#plot a sampling distribution for values of N=2,3,10 and 30
	n_val=[2,3,10,30]
	for n in n_val:
		RunSampleDemo(n,sampleDist,True,40)
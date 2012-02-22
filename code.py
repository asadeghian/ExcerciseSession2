import inputdata
import numpy
import math
from scipy.stats.stats import pearsonr

data = inputdata.raw_scores
paperset=set()
papers=[]
stu=data.keys()
ratings=data.values()

def find_similarity_2norm(x,y,rates):
	tempmat=numpy.zeros((1,len(papers)), dtype=float)
	for i in range(len(papers)):
		if rates[x][i]!=0 and rates[y][i]!=0:
			tempmat[0][i]=rates[x][i]-rates[y][i]
		else:
			tempmat[0][i]=0
	return numpy.linalg.norm(tempmat, ord=2)

def p_correlation(x,y,rates):
	return pearsonr(rates[x], rates[y])[0]

def main():
	for i in ratings:
		temppaper=i.keys()
		for j in temppaper:
			paperset.add(j)
	for i in paperset:
		papers.append(i)
	rates=numpy.zeros((len(stu),len(papers)), dtype=float)

	for i,j in data.iteritems():
		for k,l in j.iteritems():
			rates[stu.index(i)][papers.index(k)]=float(l)
	
	similarity=numpy.zeros((len(stu),len(stu)), dtype=float)
	p_corr=numpy.zeros((len(stu),len(stu)), dtype=float)

	for i in range(len(stu)):
		for j in range(len(stu)):
			similarity[i][j]=find_similarity_2norm(i,j,rates)
	for i in range(len(stu)):
		for j in range(len(stu)):
			p_corr[i][j]=p_correlation(i,j,rates)
	

	print "************* student list ************"
	print stu
	print "\n\n************* papers list ************"
	print papers
	print "\n\n************* rates list ************"
	print rates
	print "\n\n************* similarity list ************"
	print similarity
	print "\n\n************* pearson correlation list ************"
	print p_corr

main()

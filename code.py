import inputdata
import numpy
import math
from scipy.stats.stats import pearsonr
from operator import itemgetter, attrgetter

data = inputdata.raw_scores
paperset=set()
papers=[]
stu=data.keys()
ratings=data.values()

def recommend_paper(x,similar,rates):
	# for each unread paper calculate the ans by sum of (similarity of the unread paper) times by (the given rate of the researcher to the unread paper) to the power of -1 and the less it gets the more wanted paper to the researcher
	tempmat=[]
	for i in range(len(rates[x])):
		if(rates[x][i]==0):
			ans=0.0
			for j in range(len(rates[x])):
				if(rates[x][j]!=0):
					ans+=1/(similar[i][j]*rates[x][j])
			tempmat.append((papers[i],ans))
	paper_sorted = sorted(tempmat,key=itemgetter(1,0))[0:5]
	return [paper_sorted[j][0] for j in range(len(paper_sorted))]



def find_similar_researcher(x,similarity):
	tempmat=numpy.ndarray((len(similarity[x])), dtype=object)
	for i in range(len(similarity[0])):
		tempmat[i]=(stu[i],similarity[x][i])
	researcher_sorted=sorted(tempmat,key=itemgetter(1,0))[1:6]
	print [researcher_sorted[j][0] for j in range(len(researcher_sorted))]

def find_similar_papers(x,similarity):
	tempmat=numpy.ndarray((len(similarity[x])), dtype=object)
	for i in range(len(similarity[0])):
		tempmat[i]=(papers[i],similarity[x][i])
	paper_sorted=sorted(tempmat,key=itemgetter(1,0))[1:6]
	return [paper_sorted[j][0] for j in range(len(paper_sorted))]



def find_similarity_2norm(x,y,rates):
	tempmat=numpy.zeros((1,len(rates[x])), dtype=float)
	for i in range(len(rates[x])):
		if rates[x][i]!=0 and rates[y][i]!=0:
			tempmat[0][i]=rates[x][i]-rates[y][i]
		else:
			tempmat[0][i]=0
	return numpy.linalg.norm(tempmat, ord=2)

def p_correlation(x,y,rates):
	a=[]
	b=[]
	for i in range(len(rates[x])):
		if rates[x][i]!=0 and rates[y][i]!=0:
			a.append(rates[x][i])
			b.append(rates[y][i])
	return pearsonr(a, b)[0]

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
	
	similarity_papers=numpy.zeros((len(papers),len(papers)), dtype=float)
	p_corr_papers=numpy.zeros((len(papers),len(papers)), dtype=float)

	for i in range(len(stu)):
		for j in range(len(stu)):
			similarity[i][j]=find_similarity_2norm(i,j,rates)
			p_corr[i][j]=p_correlation(i,j,rates)
	for i in range(len(papers)):
		for j in range(len(papers)):
			similarity_papers[i][j]=find_similarity_2norm(i,j,rates.transpose())
			p_corr_papers[i][j]=p_correlation(i,j,rates.transpose())


'''	print "************* student list ************"
	print stu
	print "\n\n************* papers list ************"
	print papers
	print "\n\n************* rates list ************"
	print rates
	print "\n\n************* similarity list of researchers ************"
	print similarity
	print "\n\n************* pearson correlation list of researchers  ************"
	print p_corr
	print "\n\n************* similarity list of papers ************"
	print similarity_papers
	print "\n\n************* pearson correlation list of papers ************"
	print p_corr_papers
	print "\n\n************* similar researcher to " + stu[0]
	print find_similar_researcher(0,similarity)
	print "\n\n************* similar paper to " + papers[0]
	print find_similar_papers(0,similarity_papers)
	print "\n\n************* recommended paper to " + stu[0]
	print recommend_paper(0,similarity_papers,rates)'''

main()

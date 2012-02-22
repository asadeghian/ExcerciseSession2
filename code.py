import inputdata
import numpy
data = inputdata.raw_scores

def main():
	paperset=set()
	papers=[]
	stu=data.keys()
	ratings=data.values()
	for i in ratings:
		temppaper=i.keys()
		for j in temppaper:
			paperset.add(j)
	for i in paperset:
		papers.append(i)
	rates=numpy.ndarray((len(stu),len(papers)), dtype=float)

	for i,j in data.iteritems():
		for k,l in j.iteritems():
			rates[stu.index(i)][papers.index(k)]=float(l)
		
	print stu
	print papers
	print rates

main()

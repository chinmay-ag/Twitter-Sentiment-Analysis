import csv
import sys

#reload(sys)  
#sys.setdefaultencoding('UTF8')

if len(sys.argv)!= 2:
	print "Provide the tweets input file"
	sys.exit(0)

with open(sys.argv[1],'rb') as f:			
	reader=csv.reader(f, delimiter='\t')
	l=list(reader)



# Remove the posts for which tweet is not available
out=[]
for i in l:
	if i[3]=="Not Available": 
		continue
	out.append(i)	

with open("../data/cleanedtesting.data", "wb") as f:		
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(out)

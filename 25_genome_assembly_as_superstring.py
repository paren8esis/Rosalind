edges = {}
outlinks = []
inlinks = []
DNA = []
reads = 0

def add_edge(s1, s2, overlap_index):
	''' Adds and edge to the overlap graph.
			The form of the each edge is: (target, overlap_index). '''
	ind1 = DNA.index(s1)
	ind2 = DNA.index(s2)
	outlinks[ind1] += 1
	inlinks[ind2] +=1
	edges[ind1]= (ind2, overlap_index)


def create_overlap_graph():
	''' Creates the overlap graph. 
			It basically consists of a dictionary of edges. '''
	for i in range(0, len(DNA)):
		s1 = DNA[i]
		for j in range(0, len(DNA)):
			if (i == j): continue
			s2 = DNA[j]
			mid = len(s1)//2
			# Find other strings that begin with s's suffix
			found = s2.find(s1[mid:])
			if ((found != -1) and (s1.endswith(s2[:found+len(s1)-mid]))):
				add_edge(s1, s2, found+len(s1)-mid)

def find_path(source, sink, path=[]):
	''' Finds the unique path from source to sink in the overlap graph. '''
	path.append(source)
	if (source == sink):
		return [path]
	if (edges[source][0] not in path):
		newpath = find_path(edges[source][0], sink, path)
		if (newpath): return newpath

	return None

# Open file for reading
f = open('rosalind_long.txt', 'r')

# Read the DNA strings
s = ''
for line in f:
	if (line[0] == '>'):	# Label
		if (s != ''):
			DNA.append(s.strip('\n'))
			s = ''
	else:
		s += line.strip('\n')

DNA.append(s.strip('\n'))	# add last string

# Update number of reads
reads = len(DNA)

# Initialize number of outlinks and inlinks for each node
for i in range(0, len(DNA)):
	outlinks.append(0)
	inlinks.append(0)
	edges[i] = []

# Create the overlap graph
create_overlap_graph()

# Find first (source) and last (sink) nodes of graph 
# and compute the path from source to sink
sink = outlinks.index(0)
source = inlinks.index(0)
path = find_path(source, sink, path=[])[0]

# Create the superstring
superstring = ''.join(DNA[path[0]])
start_index = edges[path[0]][1]
for i in range(1,len(path)):
	node = path[i]
	superstring += DNA[node][start_index:]
	if (edges[node] != []):
		start_index = edges[node][1]

# Print results
print(superstring)

# Close the file
f.close()

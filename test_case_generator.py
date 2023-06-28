import random

def write_file(filename: str, string: str):
    f = open(filename, "x")
    f.write(string)
    f.close()


'''
Generate testcases for
1514_Path_with_Maximum_Probability.py
'''
def get_testcase_random() -> int, list, list, int, int:
	n,edges,succProb,start,end = get_testcase_uniform()
	succProb = [random.random() for i in range(len(succProb))]
	return n,edges,succProb,start,end
	
def get_testcase_uniform() -> int, list, list, int, int:
	n = 10**4
	start = 0
	end = 10**4 - 1
	edges = []
	succProb = []
	max_edge_count = 2*n
	for i in range(max_edge_count):
		a = random.randint(start,end)
		b = a
		while b == a or [a,b] in edges or [b,a] in edges:
			b = random.randint(start,end)
		edges.append([a, b])
		succProb.append(1)
	return n,edges,succProb,start,end

def write_testcase(**kwargs):
	write_file("\n".join(kwargs))

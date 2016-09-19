import pdb

def test_pdb(arg):
	for i in range(1,10):
		print "n = %d" % (i*2)

pdb.run("test_pdb(5)")	
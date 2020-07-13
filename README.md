# Pet_Detective

This is a python script that uses a brute-force approach to solve the Lumosity pet-detecive game.

There is no optimization or any intelligence of any kind. It simply does a depth-first search

The car capacity is hard-coded to 4.

You set up and run the puzzle as :

def main() :

	pz = Puzzle( 5,3 )					# width, height
	pz.remove_branch( (2,0), (3,0) )	# no path between these two points
	pz.remove_branch( (1,0), (1,1) )
	pz.remove_branch( (2,0), (2,1) )
	pz.remove_branch( (4,0), (4,1) )
	pz.remove_branch( (1,1), (1,2) )
	pz.remove_branch( (0,2), (1,2) )
	pz.remove_branch( (3,2), (3,3) )
	pz.add_target( (4,0), (5,0) )		# there is a pet at (4,0) that needs to be
	pz.add_target( (3,1), (0,3) )		# dropped off at (5,0)
	pz.add_target( (5,1), (1,3) )
	pz.add_target( (2,3), (3,3) )

	# pdb.set_trace()
	pends = pz.targets.keys()			# the list of pets
	pz.solve( 14, (2,1), None, list( pends) , [], "")		# None is because there is no "from"
	# this is a recursive function that calls itself

main()

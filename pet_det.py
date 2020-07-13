# brute force solution to the Pet Detective game
# prints the first solution found and exits

import pdb

class Puzzle :
	# maintain the grid and the Target dict ( tuple --> tuple both points)
	def __init__(self, width, height) :
		self.width = width
		self.height = height	# both must be integers!
		self.absents = []
		self.targets = {}
		self.cargo = []
	
	def get_options( self, point ) :
		"""
		Given point, it will refer self.absents, self.width,height and 
		
		return the points that are accessible with a single branch (length 1)
		"""
		options = []
		poss =  [   (point[0]-1, point[1]  ),
					(point[0]+1, point[1]  ),
					(point[0]  , point[1]-1),
					(point[0]  , point[1]+1)
				]
		# now prune these based on width, height, self.absents (check_branch)
		for cand in poss :
			if cand[0] < 0 or cand[1] < 0 :
				continue
			if cand[0] > self.width or cand[1] > self.height :
				continue
			if self.check_branch( point, cand ) :
				options.append( cand )
		return options
			

	def check_branch( self, point1, point2 ) :
		"""returns True if the branch is NOT in the absents list"""
		for branch in self.absents :
			if branch[0] == point1 and branch[1] == point2 :
				return False
			if branch[0] == point2 and branch[1] == point1 :
				return False
		return True
	
	def add_target( self, p_point, d_point ) :
		self.targets[ p_point ] = d_point
	
	def remove_branch( self, point1, point2 ) :
		"""This will add [ point1, point2 ] to the absents list"""
		self.absents.append( (point1, point2 ) )
		
	def solve( self, fuel, point, origin, pending, cargo, log ) :
		"""This will call itself on each of the points returned by get_options(point)"""
		# if fuel == 0, then check if cargo, pending are both empty. Yes? Winner!
			# else, you lost
		# if cargo not empty, then check self.targets to see if you can drop off
		# it appends to the log.. which is just a string
		if len( cargo ) > 0 :
			for item in cargo :
				if point == self.targets[item] :
					cargo.remove( item )
					pending.remove( item )	# off the car and the to-do list :)
				
		if fuel >= 0 and len( cargo ) == 0 and len( pending ) == 0 :
			# congratulations - you won..
			log += str( point ) + " fuel : " + str( fuel ) + ". Done!\n\n"
			print( log )
			exit()
		elif 0 == fuel :
			# sorry matey
			# log += str( point ) + " fuel : " + str( fuel ) + ". Try again :)\n\n"
			# print( log )
			pass
		else :	# still playable
			options = self.get_options( point )
			if not origin is None :
				options.remove( origin )
				options.append( origin )	# make sure it's at the end :)
			for option in options :	# no pickup option
				self.solve( fuel-1, option, point, list(pending), list(cargo),
					log + str( point ) + " fuel : " + str( fuel ) +
						" remaining : " + str( pending ) + " on board : " + str(cargo) + "\n"
					)
			if point in pending :	# now the pickup options
				for option in options :
					if not point in cargo and len( cargo ) < 4 : 
						self.solve( fuel-1, option, point, list(pending), cargo + [point],
							log + str( point ) + " fuel : " + str( fuel ) +
							" remaining : " + str( pending ) + " on board : " + str(cargo + [point]) + "\n"
						)
					else :
						self.solve( fuel-1, option, point,  list(pending), list(cargo),
							log + str( point ) + " fuel : " + str( fuel ) +
							" remaining : " + str( pending ) + " on board : " + str(cargo) + "\n"
						)


def main() :
	# create a new puzzle, tell it what branches in the grid are to be removed
	# then add to the target dict
	# then call pz.solve( FUEL, starting_point, to_be_saved, [], "" )
	# pz = Puzzle( 1, 1 )
	# pz.remove_branch( (0,0), (1,0) )
	# pz.add_target( (1,0), (0,0) )
	# pdb.set_trace()
	# pz.solve( 4, (1,1), [(1,0)], [], "")
	
	# pz = Puzzle( 1, 2 )
	# pz.remove_branch( (0,0), (1,0) )
	# pz.remove_branch( (1,1), (1,2) )
	# pz.remove_branch( (0,2), (1,2) )
	# pz.add_target( (1,0), (0,0) )
	# pz.add_target( (0,1), (0,2) )
	# # pdb.set_trace()
	# pz.solve( 6, (1,1), [(1,0), (0,1)], [], "")

	# pz = Puzzle( 1, 2 )
	# pz.remove_branch( (0,0), (1,0) )
	# pz.remove_branch( (1,1), (1,2) )
	# pz.remove_branch( (0,2), (1,2) )
	# pz.add_target( (1,0), (0,0) )
	# pz.add_target( (0,1), (0,2) )
	# # pdb.set_trace()
	# pz.solve( 6, (1,1), None, pz.targets.keys() , [], "")
	
	# difficult one - probably will not complete in reasonable time
	# pz = Puzzle( 5,3 )
	# pz.remove_branch( (0,0), (1,0) )
	# pz.remove_branch( (1,2), (1,3) )
	# pz.remove_branch( (3,2), (3,3) )
	# pz.remove_branch( (4,2), (4,3) )
	# pz.remove_branch( (3,1), (4,1) )
	# pz.remove_branch( (4,1), (4,2) )
	# pz.remove_branch( (4,0), (5,0) )
	# pz.add_target( (0,0), (5,2) )
	# pz.add_target( (1,0), (0,2) )
	# pz.add_target( (1,1), (5,0) )
	# pz.add_target( (0,3), (3,1) )
	# pz.add_target( (2,2), (3,0) )
	# pz.add_target( (3,3), (1,3) )
	# pz.add_target( (4,3), (5,3) )
	# pz.add_target( (4,2), (4,0) )
	# pz.add_target( (4,1), (0,1) )
	# pz.add_target( (5,1), (1,2) )
	# # pdb.set_trace()
	# pends = pz.targets.keys()
	# pz.solve( 32, (3,2), list( pends) , [], "")

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

README for these files.  Scripts are kind of messy, sorry. Hopefully this helps to where we can both run it.

With these files in the wd you can run testing_comborun.py and it should interact with sgems and flash the variance maps + pathing points to the python console.

Make sure to:
	Manually enter your path in the comborun script, using forward slashes only.
	Check the sgems installation path in testing_alltogethernow.py (should be OK if you are on Windows)
	
Other notes:
	Right now I changed the distance weighting matrix to be uniform (ie. it will choose new points based on the variance map only, 	using the search for maximum and move 1 step in its direction.

	The point of maximum variance is also plotted on every iteration.

TODO list:
	Get the videos saving again 

	Get hard data input to SGEMS to work properly (currently it places hard data to a grid, but not at the correct x-y positions)
	
	Keep refining the pathing, either the distance matrix or the newpoint step logic.
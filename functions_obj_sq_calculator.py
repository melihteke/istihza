#!/bin/python3

select_operation = "1"
while select_operation != "q":
	select_operation = input("Select your operation\n 1-Triangle surface area\n 2-Square surface area \n 3-Circle surface area\n q-EXIT\n")
	print("---"*20)

	def triangle_surface_area(a_edge, h):
        	print("The triangle's a edge is ", a_edge)
        	print("The triangle's height is ", h)
        	print("The triangle's surface area is %s" %triangle_sq)

	def square_surface_area(a):
        	print("The square's a edge is ", a)
        	print("The square's surface area is %s" %square_sq)

	def circle_surface_area(r):
        	print("The circle's r is ", r)
        	print("The circle's area is %s" %circle_sq)


	if select_operation == "1":
		a_edge = input("Enter the edge A\n")
		h = input("Enter the height\n")
		triangle_sq = ( int(a_edge) * int(h) ) / 2
		triangle_surface_area(a_edge, h)
	elif select_operation == "2":
		a = input("Enter the a value\n")
		square_sq = int(a) * int(a)
		square_surface_area(a)
	elif select_operation == "3":
		r = input("Enter the r value\n")
		circle_sq = 3.14159 * int(r)
		circle_surface_area(r)
	else:
		print("Select correct operation value !!!")



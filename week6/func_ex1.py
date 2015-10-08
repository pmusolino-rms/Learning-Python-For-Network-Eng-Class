#!/usr/bin/env python

def product(x,y,z=1):
	print (x*y*z)

print "all positional"
product(5,10,20)
print "all named"
product(x=10,y=10,z=10)
print "Mixed assignment"
product(5,y=5,z=10)
print "2 arguments, default z"
product(5,10)

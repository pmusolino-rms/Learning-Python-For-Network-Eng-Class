#!/usr/bin/env python

def list_to_dictionary(a_list):
	a_dictionary={}
	for index,value in enumerate(a_list):
		a_dictionary.update({index:value})
	return(a_dictionary)

my_list = ['a','b','c','d','e']
print my_list
my_dict = list_to_dictionary(my_list)
print my_dict

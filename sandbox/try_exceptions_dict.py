#!/usr/bin/python

import os
import sys
import commands

from sets import Set
from sets import 

#what time is it
#what is the value of X - X is a string like (2+2)/1.5, report it's value
 
cmd_classes  = {  'open':read_file
		, 'execute':nix_cmd
		, 'credits':info_cmd
		, 'help':info_cmd
		, 'dic':my_cmd
		, 'geo':my_cmd
		, 'log':my_cmd
		, 'what':wh_q
		, 'how':wh_q
		}

legal_nix_cmd  = {'uptime':1, 'ls':1, 'ping':1}
py_what_cmd = ['time':1, 'is the value of':1]

me_inf  = [ 'name':foozy, 'family':boozy ]

all_cmd_len = len(all_cmd)

class nix_cmds:
	def ret(cmd):
		return commands.getoutput("cmd")

info_cmd_path_prefix = './canned/'
class info_cmd:
	def ret(info):
		f =  info_cmd_path_prefix + info
		for line in open(info.f, 'r'):
			info.ret += line
def classify(cmd):
	if cmd in cmd_classes:
		return cmd_classes[cmd]

def respond(message, sender=""):
	message = message.strip()
	#print "Got message",message
	words     = message.split()
	cmd       = words[0]
	cmd_class = classify(cmd)
	print cmd_class.ret(cmd)


respond('open    foo',    'me')

respond('execute uptime', 'me')
respond('execute ls',     'me')
respond('execute ping 127.0.0.1', 'me') # TODO: ask if they're gonna be throwing ipv6

respond('credit', 'me')
respond('help'  , 'me')

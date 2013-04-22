#!/usr/bin/python

import os
import sys
import commands

#what time is it
#what is the value of X - X is a string like (2+2)/1.5, report it's value
 

legal_nix_cmds  = {'uptime':1, 'ls':1, 'ping':1}
py_what_cmd = {'time':1, 'is the value of':1}

me_info  = { 'name':'foozy', 'family':'boozy' }

#all_cmd_len = len(all_cmd)

class cmds:
	def __init__(self, msg):
		self.cmd = msg[0]
		self.dcv = msg[1]
class py_cmds:
	def ret(cmd):
		return None
class nix(cmds):
	def ret(self, cmd):
		return commands.getoutput(cmd)

info_cmds_path_prefix = './canned/'
class info_cmds:
	def ret(self, info):
		f =  info_cmds_path_prefix + info[0]
		for line in open(f, 'r'):
			ret += line
		return ret
class my_cmds:
	def ret(my):
		return None
class wh_q:
	def ret(whq):
		return None
cmd_classes  = {  'open':py_cmds
		, 'execute':nix
		, 'credits':info_cmds
		, 'help':info_cmds
		, 'dic':my_cmds
		, 'geo':my_cmds
		, 'log':my_cmds
		, 'what':wh_q
		, 'how':wh_q
		}
def classify(msg):
	if msg[0] in cmd_classes:
		return cmd_classes[msg[0]]
def respond(message, sender=""):
	message   = message.strip()
	words     = message.split()
	cmd_class = classify(words)
	cmd_class_ins = cmd_class(words)
	print cmd_class_ins.ret(cmd_class_ins.dcv)
	#print cmd_class_ins.ret(words)

#respond('open    foo',    'me')

respond('execute uptime', 'me')
respond('execute ls',     'me')
#respond('execute ping 127.0.0.1', 'me') # TODO: ask if they're gonna be throwing ipv6

#respond('credits', 'me')
#respond('help'  , 'me')

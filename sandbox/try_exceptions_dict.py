#!/usr/bin/python

import os
import sys
import commands # TODO: use subprocess instead of commnads

#what time is it
from time import gmtime, strftime
#what is the value of X - X is a string like (2+2)/1.5, report it's value
 

legal_nix_cmds  = {'uptime':1, 'ls':1, 'ping':1}
py_what_cmd = {'time':1, 'is the value of':1}

me_info  = { 'name':'foozy', 'family':'boozy' }

#all_cmd_len = len(all_cmd)

class cmds(object):
	def __init__(self, msg):
		self.msg = msg
		self.cmd = self.msg[0]
		self.dcv = self.msg[1]
class nix(cmds):
	def ret(self):
		return commands.getoutput(self.dcv)

class canned_info(object):
	def __init__(self, msg):
		self.cmd = msg[0]
	prefix = './.canned/info/'
	def ret(self):
		f     = open(self.prefix + self.cmd, 'r')
		return f.read()

class py(cmds):
	def ret(self):
		f     = open(self.dcv, 'r')
		return f.read()
class my(cmds):
	def ret(self):
		return None
class whq(cmds):
	time = ['time', 'is', 'it?']
	val  = ['is', 'the', 'value', 'of']
	def ret(self):
		self.msg.pop(0)
		expresion = self.msg.pop()
		if self.msg == self.val:
			if expresion[-1] == '?':
				expresion.pop()
			eval(expresion)
		self.msg.append(expresion)
		if self.msg == self.time:
			#return strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
			return  strftime("%I:%M:%S %p")
			return 
cmd_classes  = {  'open':py
		, 'execute':nix
		, 'credits':canned_info
		, 'help':canned_info
		, 'dic':my
		, 'geo':my
		, 'log':my
		, 'what':whq
		, 'how':whq
		}
def classify(msg):
	if msg[0] in cmd_classes:
		return cmd_classes[msg[0]]
def respond(message, sender=""):
	message   = message.strip()
	words     = message.split()
	cmd_class = classify(words)
	cmd_class_ins = cmd_class(words)
	print cmd_class_ins.ret()
	#print cmd_class_ins.ret(words)

#respond('open    foo',    'me')

respond('execute uptime', 'me')
respond('execute ls',     'me')
#respond('execute ping 127.0.0.1', 'me') # TODO: ask if they're gonna be throwing ipv6

respond('open foo'  , 'me')
respond('credits', 'me')
#respond('help'  , 'me')
respond('what time is it?'  , 'me')
respond('what is the value of (2+2)/1.5?'  , 'me')

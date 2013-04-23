#!/usr/bin/python

import os
import sys
import subprocess # TODO: use subprocess instead of commnads
from collections import deque

#what time is it
from time import gmtime, strftime
#what is the value of X - X is a string like (2+2)/1.5, report it's value
 

legal_nix_cmds  = {'uptime':1, 'ls':1, 'ping':1}
py_what_cmd = {'time':1, 'is the value of':1}

me_info  = { 'name':'foozy', 'family':'boozy' }

class cmds(object):
	cls = 'cmds'
class nix(cmds):
	def __init__(self, msg):
		nix_cmd_args = {   'ls':''
				, 'uptime':''
				, 'ping':'-c 1'
				}
		msgq = deque(msg)
		self.dcv = msgq.popleft()
		self.cmd = msgq.popleft()
		self.switch = nix_cmd_args[self.cmd]
		# TODO: sanity check for ip format
		for arg in msgq:
			self.arg = self.arg + msgq.popleft()
	def ret(self):
		#return subprocess.check_output(["echo", self.cmd + self.switch + self.arg])
		return self.arg

class canned_info(object):
	cmd_args = {   'help':''
		     , 'credits':''
		   }
	def __init__(self, msg):
		msgq = deque(msg)
		msgq.appendleft('info')
		self.dcv = msgq.popleft()
		self.cmd = msgq.popleft()
		self.switch = cmd_args[self.cmd]
		self.arg = msg
	def ret(self):
		prefix = './.shelve'
		can    = prefix + '/' + self.dcv + '/' + self.cmd
		f     = open(can, 'r')
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
		self.msg.pop()
		if self.msg == self.val:
			if self.dcv[-1] == '?':
				self.dcv = self.dcv.rsplit('?', 1)[0]
			return eval(self.dcv) 
		self.msg.append(self.dcv)
		if self.msg == self.time:
			#return strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
			return  strftime("%I:%M:%S %p")
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
respond('execute ping 127.0.0.1', 'me') # TODO: ask if they're gonna be throwing ipv6

#respond('open foo'  , 'me')
#respond('credits', 'me')
#respond('help'  , 'me')
#respond('what time is it?'  , 'me')
#respond('what is the value of (2+2)/1.5?'  , 'me')
#respond('what is the value of (2+2)/1.5'  , 'me')


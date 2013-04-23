#!/usr/bin/python

import os
import sys
import shlex, subprocess # TODO: use subprocess instead of commnads
#import commands
from collections import deque


#what time is it
from time import gmtime, strftime
#what is the value of X - X is a string like (2+2)/1.5, report it's value
 

me_info  = { 'name':'foozy', 'family':'boozy' }

class cmds(object):
	cls = 'cmds'
ping_arg = ['-c', '1'] #, '|', 'tail', '-1']
cmd_args = {   'ls':''
		, 'uptime':''
		, 'ping':ping_arg
		, 'help':' '
		, 'credits':' '
	   }
class nix(cmds):
	def __init__(self, msg):
		msgq = deque(msg)
		self.dcv = msgq.popleft()
		self.cmd = msgq.popleft()
		self.switch = cmd_args[self.cmd]
		self.arg = ' '.join(msgq)
	def ret(self):
		wholeshbang = [self.cmd]
		if self.switch != '':
			wholeshbang.extend(self.switch)
		if self.arg != '':
			wholeshbang.append(self.arg)
		return subprocess.check_output(wholeshbang)

class canned_info(object):
	def __init__(self, msg):
		msgq = deque(msg)
		msgq.appendleft('info') # TODO: add this to class nix and abstrac __init__ in class cmds
		self.dcv = msgq.popleft()
		self.cmd = msgq.popleft()
		self.switch = cmd_args[self.cmd]
		self.arg = ' '.join(msg)
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

#respond('open foo'  , 'me')

respond('execute uptime', 'me')
respond('execute ls',     'me')
respond('execute ping 127.0.0.1', 'me')

respond('credits', 'me')
respond('help'  , 'me')
respond('what time is it?'  , 'me')
respond('what is the value of (2+2)/1.5?'  , 'me')
respond('what is the value of (2+2)/1.5'  , 'me')


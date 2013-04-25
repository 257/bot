#!/usr/bin/python

import subprocess
import random
#import commands
from collections import deque


#what time is it
from time import strftime
#what is the value of X - X is a string like (2+2)/1.5, report it's value

me_info  = { 'name':'foozy', 'family':'boozy' }
def me_info_var():
	ret = []
	for info in me_info:
		info_val = me_info[info]
		ret.append(info_val.upper())
		ret.append(info_val.lower())
		ret.append(info_val[0].upper() + info_val[1:])
	return ret
me_info_variations = me_info_var()

class cmds(object):
	def __init__(self, msg):
		msgq = deque(msg)
		if len(msgq) == 1:
			msgq.appendleft('info')
		msgq[-1] = msgq[-1].rsplit('?', 1)[0]
		self.dcv = msgq.popleft()
		self.cmd = msgq.popleft()
		try:
			self.switch = cmd_args[self.cmd]
		except KeyError:
			self.switch = 'generic'
		self.arg = msgq
ping_arg = ['-c', '1']
cmd_args = {   'ls':''
		, 'uptime':''
		, 'ping':ping_arg
		, 'help':' '
		, 'credits':' '
		, 'time':'is it'
		, 'is'  : 'the value of'
		, 'generic' : 'generic'
	   }
class nix(cmds):
	def ret(self):
		self.arg = ' '.join(self.arg)
		wholeshbang = [self.cmd]
		if self.switch != '':
			wholeshbang.extend(self.switch)
		if self.arg != '':
			wholeshbang.append(self.arg)
		# TODO: ugly pipes here man, use 're' for *'s sake
		nixp = subprocess.Popen(wholeshbang, stdout=subprocess.PIPE)
		if self.cmd == 'ping':
			grepp = subprocess.Popen(
					  ["grep", "transmitted"]
					, stdin=nixp.stdout
					, stdout=subprocess.PIPE)
			nixp.stdout.close()
			out = grepp.communicate()[0]
		else:
			out =  nixp.communicate()[0]
		return out
def cannon(dcv, cmd): # this cannon Sir, shoots beans :)
	prefix = './.shelve'
	can    = prefix + '/' + dcv + '/' + cmd
	with open(can, 'r') as beans:
		bag = beans.readlines()
		if dcv == 'info' and cmd == 'help':
			return '\n'.join(bag)
		else:
			return random.choice(bag)
class info(cmds):
	def ret(self):
		return cannon(self.dcv, self.cmd)
class py(cmds):
	def ret(self):
		with open(self.cmd, 'r') as f:
			return f.read()
import fgeoloc
# we go over the net here, only once
my_geoloc = fgeoloc.get() 
class my(cmds):
	def ret(self):
		return my_geoloc[self.cmd]


class whq(cmds):
	def ret(self):
		gen = 'generic'
		if self.dcv == 'what':
			if self.cmd == 'is':
				realarg = self.arg.pop()
				if ' '.join(self.arg) == self.switch:
					# cast to str here for .split
					return str(eval(realarg))
				else:
					return cannon(self.dcv, gen)
			elif self.cmd == 'time':
				if ' '.join(self.arg) == self.switch:
					return  strftime("%I:%M:%S %p")
				else:
					return cannon(self.dcv, gen)
			else:
				return cannon(self.dcv, gen)
		elif self.dcv == 'how':
			return cannon(self.dcv, gen)
		else:
			return 'how did you get here'
class non_cmds:
	def __init__(self, msg):
		self.dcv = 'non'
		self.cmd = 'generic'
	def ret(self):
		return cannon(self.dcv, self.cmd)

class with_my_name:
	def __init__(self, msg):
		self.dcv = 'with.my.name'
		self.cmd = 'generic'
	def ret(self):
		return cannon(self.dcv, self.cmd)
cmd_classes  = {  'open':py
		, 'execute':nix
		, 'credits':info
		, 'help':info
		, 'geo':my
		, 'weather':my
		, 'log':my
		, 'what':whq
		, 'how':whq
		, 'your':my
		}
def has_my_name(msg):
	ret = non_cmds
	for word in msg:
		for info in me_info:
			if word == me_info[info]:
				ret = with_my_name
	return ret

def classify(msg):
	try:
		return cmd_classes[msg[0]]
	except KeyError:
		return has_my_name(msg)

def respond(message, sender=""):
	message = message.lower()
	if message=="requested mark":
		return "100%"
	message   = message.strip()
	words     = message.split()
	# strip please out
	cmd_class = classify(words)
	cmd_class_ins = cmd_class(words)
	print cmd_class_ins.ret().strip()
	#return cmd_class_ins.ret().strip()

respond('What time is it?'  , 'me')
#respond('open foo'  , 'me')
#respond('execute uptime', 'me')
#respond('execute ls',     'me')
#respond('execute ping 127.0.0.1', 'me')
#respond('help'  , 'me')
#respond('credits', 'me')
#respond('what time is it?'  , 'me')
#respond('what time is it'  , 'me')
#respond('what time are you coming home?'  , 'me')
#respond('what is the value of (2+2)/1.5?'  , 'me')
#respond('what is the value of (2+2)/1.5'  , 'me')
#respond('how is the value of (2+2)/1.5'  , 'me')
#respond('how are you?'  , 'me')
#respond('how are yeah'  , 'me')
#respond('what are we'  , 'me')
#respond('what is this'  , 'me')
#respond('what the *'  , 'me')
#respond('is foozy home?', 'me')
#respond('is he home?', 'me')
#respond('your ip', 'me')
#respond('your longitude', 'me')
#respond('your latitude', 'me')
#respond('your city', 'me') # TODO: unicode problem
#respond('your country', 'me')
#respond('your province', 'me')
#respond('your zipcode', 'me')
#respond('weather', 'me')

#!/usr/bin/python

import os
import sys
import commands

from sets import Set
from sets import 

#what time is it
#what is the value of X - X is a string like (2+2)/1.5, report it's value
 
# legal words[0]
x_direct = {'open':read_file, 'execute':execute_nix_cmd}
info_cmd = {'credits':read_file, 'help':read_file}
me_cmd   = ['dic', 'geo', 'log']
wh_cmd   = ['what','how']
#wh_cmd  = ['who', 'what', 'when', 'where', 'how', 'why']

cmd_classes  = {'open':read_file
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

non_cmd     = () # for syncing the index for now
all_cmd_len = len(all_cmd)

#def is_nix_cmd(word):
#	try:
#		return nix_cmd.index(word)
#	except ValueError:
#		return 10
class nix_cmds:
	def __init__(cmd):
		cmd.ret = commands.getoutput("cmd")

info_cmd_path_prefix = './canned/'
class info_cmd:
	def __init__(info):
		f =  info_cmd_path_prefix + info
		for line in open(info.f, 'r'):
			info.ret += line

def do_cmd(cmd):
	if i == 0:
		return "no cmd!"
	elif i == 1:
		return run_signle_cmd(cmds)
	elif i == 2:
		return run_double_cmd(cmds)

def classifier(msg):

def respond(message, sender=""):
	message = message.strip()
	#print "Got message",message
	words   = message.split()
	cmd     = words[0]
	if is_legal(cmd):
		do(cmd)

respond('open    foo',    'me')
respond('execute uptime', 'me')
respond('execute ls',     'me')
respond('execute ping 127.0.0.1', 'me') # TODO: ask if they're gonna be throwing ipv6

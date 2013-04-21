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

cmd_classes  = {'open':read_file, 'execute':nix_cmds, 'credits':info_cmd, 'help':info_cmd, 'gdic':google_dictionary, 'geo':get_geoloc, 'log':log_conversation, 'what':parse_what, 'how':parse_how}

nix_cmd  = {'uptime':execute_nix_cmd, 'ls':execute_nix_cmd, 'ping':execute_nix_cmd}
what_cmd = ['time':commnads.getoutput, 'is the value of':.execute_nix_cmd]

me_inf  = [ 'name':'foozy', 'family':'boozy' ]

non_cmd     = () # for syncing the index for now
all_cmd_len = len(all_cmd)

#def is_nix_cmd(word):
#	try:
#		return nix_cmd.index(word)
#	except ValueError:
#		return 10
class nix_cmds:
	def nixit(cmd):
		cmd.ret = commands.getoutput("cmd")
info_cmd_path_prefix = './canned/'
class info_cmd:
	def __init__(info):
		f =  info_cmd_path_prefix + info
	def ret(info):
		for line in open(info.f, 'r'):
			info.ret += line
def do_cmd(i, msg, cmds):
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
	i = 0
	cmd     = words[i]
	i += 1
	cmd_len = len(all_cmd)
	while i < cmd_len:
		if cmd in all_cmd[i]:
			if i == cmd_len: # TODO: raise exception for ping
				retstr = do_cmd(i, message, words)
				return retstr
		i += 1
respond('open    foo',    'me')
respond('execute uptime', 'me')
respond('execute ls',     'me')
respond('execute ping 127.0.0.1', 'me') # TODO: ask if they're gonna be throwing ipv6

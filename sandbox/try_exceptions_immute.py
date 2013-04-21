#!/usr/bin/python

import commands
import os
import sys

from sets import Set
from sets import ImmutableSet

#what time is it
#what is the value of X - X is a string like (2+2)/1.5, report it's value
 
# legal words[0]
x_direct = ImmutableSet(['open', 'execute'])
info_cmd = ImmutableSet(['credits', 'help'])
me_cmd   = ImmutableSet(['dic', 'geo', 'log'])
wh_cmd   = ImmutableSet(['what','how'])
#wh_cmd  = ImmutableSet(['who', 'what', 'when', 'where', 'how', 'why'])

# legal words[1], not handling open here
nix_cmd  = ImmutableSet(['uptime', 'ls', 'ping'])
what_cmd = ImmutableSet(['time', 'eval'])
eval_str = 'is the value of'

me_inf  = ['peymane']

single_cmd  = info_cmd | me_cmd

legal_cmd   = nix_cmd | me_cmd | info_cmd
non_cmd     = Set() # for syncing the index for now
all_cmd     = [non_cmd, single_cmd, x_direct, wh_cmd]
all_cmd_len = len(all_cmd)

#def is_nix_cmd(word):
#	try:
#		return nix_cmd.index(word)
#	except ValueError:
#		return 10

def run_signle_cmd(cmds):
	if cmds[0] == 'help':
		hf = open('./canned/' + info_cmd[, 'r')
		print hf
	elif cmds[0] == 'credits': # TODO: double check, may not be necessary
		cf = open('./canned/credit', 'r')
		printf cf
def run_double_cmd(cmds):
	if cmds[0] == :
		f = open(

def do_cmd(i, msg, cmds):
	if i == 0:
		return "no cmd!"
	elif i == 1:
		return run_signle_cmd(cmds)
	elif i == 2:
		return run_double_cmd(cmds)


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

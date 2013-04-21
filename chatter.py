import commands
#what time is it
#what is the value of X - X is a string like (2+2)/1.5, report it's value
py_cmds  = ['open', 'time', 'eval']
nix_cmds = ['uptime', 'ls', 'ping']
wh_cmds  = ['who', 'what', 'when', 'where', 'how', 'why']
mis_cmds = ['credits', 'help']
my_cmds  = ['dic', 'geo', 'log']
my_name  = ['foo']
my_id    = ['123456']

single_cmds  = [nix_cmds, mis_cmds, my_cmds]
builtin_cmds = [py_cmds, nix_cmds, my_cmds]
nlp_cmds     = [wh_cmds, mis_cmds, my_name]
cmds         = [nlp_cmds, builtin_cmds]

#def is_builtin_cmds(cmd):
def is_nix_cmd(cmd):
	try:
		ret = nix_cmds.index(cmd)
	except LookupError:
		
def is_my_cmd(cmd):
def is_mis_cmds(cmd):

def parse_cmd(cmd):
	try:
		return commands.getoutput("")
def parse_msg(msg):
	msg_len = len(msg)
	if msg_len == 0:
		return msg_len
	elif msg_len == 1:
		is_cmd(words[0])

def respond(message, sender=""):
	message = message.strip()
	#print "Got message",message
	words   = message.split()
	parse_msg(words)


if __name__ == '__main__':
	respond("This is a test")

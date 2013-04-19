
def respond( message, sender=""):
    message = message.strip()
    print "Got message",message
    words = message.split()
    return words[1]

if __name__ == '__main__':
    respond("This is a test")

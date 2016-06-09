import socket,config
class MR9KBot:
	def __init__(self):
		self.server = config.SERVER
		self.port = config.PORT
		self.channels = config.CHANNELS
		self.nick = config.NICK
		self.password = config.PASS
		self.owner = config.OWNER

	def serve(self):
		self.irc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.irc.connect((self.server,self.port))
		self.irc.send("PASS "+self.password+"\r\n")
		self.irc.send("NICK {0}\r\n".format(self.nick))
		self.irc.send("USER {0} 8 * :MR9KBot reporting!".format(self.nick))
		for chan in self.channels:
			self.irc.send("JOIN #{}\r\n".format(chan))
		while True:
			data = self.irc.recv(4096)
			if data.find("PING") != -1:
				self.irc.send("PONG "+data.split(":")[1])
			elif data.find("PRIVMSG") != -1:
				self.irc.send("PRIVMSG MineRobber9000 :yo")

import paramiko

class SSH():
    def __init__(self, host, login, port=22, key_filename= None, passwd=None):
        self.host = host
        self.login=login
        self.passwd=passwd
        self.port = port
        self.key_filename=key_filename
        self.handle = None

    def connect(self):
        self.handle = paramiko.SSHClient()
        self.handle.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.handle.connect(self.host, username=self.login, key_filename=self.key_filename)
        print "Connected"

    def cmd(self,cmd):
        stdin,stdout,stderr=self.handle.exec_command(cmd)
        print stdin
        print stderr.read()
        return stdout.read()

#A = SSH('kc1', login="ubuntu", key_filename='/Users/srnukala/.ssh/id_rsa.key', passwd='')
#A.connect()
#print A.cmd("ls -l")





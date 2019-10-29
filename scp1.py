import paramiko
from scp import SCPClient

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

    def cpfiles(self):
        with SCPClient(ssh.get_transport()) as scp:
            scp.put('a.csv', 'b.csv')
            scp.get('23.txt')

if __name__=='__main__':
   A = SSH('35.229.63.233', login="srini7144", key_filename='/Users/srnukala/gcp/key', passwd='')
   A.connect()
   print A.cpfiles()





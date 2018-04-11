import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = raw_input("Qual arquivo voce deseja? -> ")
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("O arquivo existe, " + str(filesize) +" bytes, baixar? (y/n)? -> ")
            if message == 'y':
                s.send("OK")
                f = open('new_'+filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% concluido"
                print "Download Completo!"
                f.close()
        else:
            print "O arquivo nao existe!"

    s.close()
    

if __name__ == '__main__':
    Main()



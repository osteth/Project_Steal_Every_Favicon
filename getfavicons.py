for a in range(125, 135):
    for b in range(125, 135):
        for c in range(125, 135):
            for d in range(125, 135):
                ip = str(a)+"."+str(b)+"."+str(c)+"."+str(d)
                print "http://"+ip.strip(' \t\n\r')+"/favicon.ico"
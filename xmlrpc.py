import sys, os
import xmlrpc.client as client

def main():
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            path = os.path.join(root, file)
            with open(path, 'r') as i_file:
                for line in i_file.readlines():
                    uri = line.strip()
                    try:
                        with open(sys.argv[2], 'rb') as p:
                            rp = client.Binary(p.read())
                        with open(sys.argv[3], 'r') as hf:
                            for line in hf.readlines():
                                host = line.strip()
                                port = 443
                        server = client.Server('https://'+host+':443/xmlrpc'+uri)
                        server.register_function(rp)
                        response = server.recv(4096)
                        print(response)
                    except client.Error as e:
                        print(e)
                        pass

if __name__ == '__main__':
    main()
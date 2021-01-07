import socket #memasukan module socket
#Soket adalah titik akhir dari saluran komunikasi dua arah.
#Soket dapat berkomunikasi dalam suatu proses,
# antara proses pada mesin yang sama, atau antara proses di berbagai benua.

try:
    print """
    _                 _                    
   /_\  _ __  ___ _ _| |_ ___ __ __ _ _ _  
  / _ \| '_ \/ _ \ '_|  _(_-</ _/ _` | ' \ 
 /_/ \_\ .__/\___/_|  \__/__/\__\__,_|_||_|
       |_| Amikom Port Scan / Knock        
       """
    print ("  Information Gathering - Port scanning") #print text
    print  ("  Simple script Python3 Using library socket\n")
    ip = raw_input("  Enter IP addres target: ") #pembuat variable untuk penempatan hostname
except KeyboardInterrupt:
    sys.exit(1)

def scan(ip,port): #fungsi
 try: #penggunan  statement try .. except
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #membuat variable untuk module socket
    #socket.AF_INET : alamat format diambil dari host dan port number dimana menggunakan SOCK_STREAM (sebagai virtual sirkuit untuk stream)
    code = s.connect_ex((ip , port)) # connecting to the target
 except Exception, e:
     pass
 return code

for port in range(0,65535): #range port yang bakal di looping pada target
    try:#penggunan  statement try .. except
        call = scan(ip,port)
        if call==0:
            print("\n  Port Open is :  %d" % (port)) #output
    except Exception, e:
        pass

#try except digunakan untuk menangani error saat penggunaan IO, operasi database, atau pengaksesan indeks suatu list atau dictionary
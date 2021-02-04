# developed by mario diaz 01 30 2021
# reinicia la VPN l2tp unifi USG
# cuando algun usuario se queda logueado en el sistema

# This script restarts the VPN services,
# this is very useful when a user is already logged in the vpn,
# although it´s not, showing errors in windows or the OS

# this script avoids you to use ssh to do the job on the CLI

# pip install art
# pip3 install paramiko
# si da errores actualizar PIP
# si presenta error en pip de instalar c++  libraries usar el siguiente link
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# ese es el installer de  Microsoft Visual C++ una vez ahi ir a:
# -individual components
# compilers, build tools and run times
# chequear e instalar
# -C++ Universal Windows Platform runtime for v142 build tools
# escoger dependiendo de la version
# MSVC v142 - VS 2019 C++
# ARM64 build tools(v14.28)
# C++ Universal Windows Platform support for v142 b

from art import *
import paramiko
import time

host = "" #Unifi USG IP adress
company = "Xcodered" #Just your name
command1 = "show vpn ipsec sa" #Show users logged on
command2 = "sudo service xl2tpd restart"# restart services l2tp
command3 = "sudo ipsec restart"#restart Ipsec service
#the next info is available at unifi controller/settings/site/DEVICE AUTHENTICATION/SSH Authentication
usr = ""#Your SSH username
psw = ""#your SSH password

print(text2art(company))
print("VPN LP2TP / IPSEC  Reseter for unifi Soatvirtual VPN")
print("Pointing to USG " + host+".....")
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=usr, password=psw)

# functions


def execX(cmd):
    # This function executes the command that we need
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
        " /opt/vyatta/bin/vyatta-op-cmd-wrapper " + cmd)
    ssh_stdouta = ssh_stdout.readlines()
    outsterr = ssh_stderr.readlines()
    prconsole(ssh_stdouta, outsterr,cmd)
    
def execSudo(cmd):
    # This function executes sudo
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    ssh_stdouta = ssh_stdout.readlines()
    outsterr = ssh_stderr.readlines()
    prconsole(ssh_stdouta, outsterr,cmd)

def prconsole(ssh_stdouta, outsterr, cmd):
    # esta function prconsole imprime la consola de ssh ya sea
    # error o resultado
    # this function  prconsole prints the result from the console either
    # error or information
    print("\n ***************Command sent = "+cmd )
    if(any(ssh_stdouta)):
        print("CLI Results-----------------")
        print(ssh_stdouta)
        print("\n")
      
    elif(any(outsterr)):
        print("CLI errors--------------------")
        print(outsterr)
        print("\n")
    else:
        print("Not info returned")
        print("\n")    


# now lets execute the commands
# ejecutemos los comandos

execX(command1)
execSudo(command2)
execSudo(command3)
execX(command1)
ssh.close()
print("Connection closed")

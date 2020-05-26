import sys
import os
import crypt

def checkPass(hashedPassword):
    prefix = hashedPassword.split('$')[1]
    salt = hashedPassword.split('$')[2]
    dictionaryFile = open('dictionary.txt','r')
    for Pass in dictionaryFile.readlines():
        Pass = Pass.strip('\n')
        cryptPass = crypt.crypt(Pass, "$" + prefix + "$" + salt)
        if (cryptPass == hashedPassword):
            print "* Found Password: "+ Pass +"\n"
            return
    print "- Password Not Found.\n"
    return    
    
def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print '- ' + filename + ' does not exist.'
            exit(0)
        elif not os.access(filename, os.R_OK):
            print '- ' + filename + ' access denied.'
            exit(0)  
        else:
            passFile = open(filename,'r')
            for line in passFile.readlines():
                if ":" in line:
                    user = line.split(':')[0]
                    hashedPass = line.split(':')[1].strip(' ')
                    print "-> Cracking Password For: " + user
                    checkPass(hashedPass)    
    else:    
        print "- Please enter the name of file as argument via command line."
if __name__ == "__main__":
    main()

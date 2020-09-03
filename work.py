#!"C:\python\python.exe"
##
##print("content-type: text/html\n\n" )
##print("<br><B>hello python</B>")

print("content-type: text/html \n")
print("<div class='body' style='background-color:skyblue;height:100%;'>")

import cgi
import subprocess
import datetime

#args = ['cmd','calc','wmplayer','notepad']
def get_cmd(cmd):
    if cmd:        
        if (('google.com' in cmd) or ('github.com' in cmd) or ('stackoverflow.com' in cmd) or ('linkedin.com' in cmd) or ('facebook.com' in cmd)):
            x = subprocess.Popen(["firefox",cmd])          
            ##print(x)
            print("<div style='text-align:center'>")
            print("<h3 class='display: grid;place-items: center;'>Thank you.</h3>")
            print("<h3 class='display: grid;place-items: center;'>Visit Again.</h3>")    
            print ("<a href='https://localhost/pyapi/newtask/work.html'>Back </a>")
            print("</div>")
            
        elif(('cmd' in cmd) or ('calc' in cmd) or ('notepad' in cmd) or ('wmplayer' in cmd)):
            x = subprocess.run(cmd)           
            ##print(x)
            get = x.returncode
            if get >= 0:
                ##print(x)
                print("<div style='text-align:center'>")
                print("<h3 class='display: grid;place-items: center;'>Thank you</h3>")
                print("<h3 class='display: grid;place-items: center;'>Visit Again.</h3>")    
                print ("<a href='https://localhost/pyapi/newtask/work.html'>Back </a>")
                print("</div>")
            else:
                print("<div style='text-align:center'>")                
                print ("<a href='https://localhost/pyapi/newtask/work.html'>Back </a>")
                print("</div>")
        else:
            print("<div style='text-align:center'>")
            print("<h3 class='display: grid;place-items: center;'>Command Not Found</h3>")           
            print ("<a href='https://localhost/pyapi/newtask/work.html'>Back </a>")
            print("</div>")
    else:
        print("<div style='text-align:center'>")
        print("<h3 class='display: grid;place-items: center;'>Please Enter Something</h3>")
        print ("<a href='https://localhost/pyapi/newtask/work.html'>Back </a>")
        print("</div>")

        
form = cgi.FieldStorage()
now = datetime.datetime.now()
print("<div style='text-align:center;border:2px solid blue;margin:3px;padding:5px;'>")
print("<h1 style='font-family:Comic Sans MS;font-style: oblique;'>Mini Browser</h1>")
print(now.strftime("<h3 class='display: grid;place-items: center;'>%Y-%m-%d %H:%M:%S</h3>"))
print("</div>")
cmd = form.getvalue("get_cmd")
get_cmd(cmd)



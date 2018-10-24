import mechanize
import sys

Upload_Status = ""

url = sys.argv[1]

if url != "127.0.0.1:8000":
    Upload_Status = "Sorry, your file can't be uploaded due to incorrect server url"

else:

    login = "http://" + url + "/accounts/login"
    upload = "http://" + url + "/upload"
    
    with open('/home/pikachu/info.txt', 'r') as myfile:
        data = myfile.read().replace('\n',' ')

    arr = data.split()

    br = mechanize.Browser()
    br.open(login)
    br.select_form(nr=0)
    br.form['username'] = arr[0]
    br.form['password'] = arr[1]
    req = br.submit()
    
    br.open(login)

    counter = 0
    
    for f in br.forms():
        counter = counter + 1
    
    if counter != 0:
        Upload_Status = "Your file can't be uploaded due to bad login credentials"

    else:
        
        print "File is uploading"
        print "Please wait..."
        br.open(upload)

        filename = sys.argv[2]
        br.select_form(nr=0)
        br.form['filepath'] = filename
        br.form.add_file(open(filename), 'text/plain', filename)
        req = br.submit()
        Upload_Status = "Uploaded Successfully"

print Upload_Status

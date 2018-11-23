

                     BEST VIEWED IN FULL SCREEN MODE AND AT 1920*1080 RESOLUTION AND FONT 10 IN NOTEPAD


///////////////////////////////////////////////       DISCLAIMER        /////////////////////////////////////////////////////


This is the documentation of CCure - a Secure Personal Cloud made by Kalpit Veerwal, Nirmal Rajput and Kiran Dapkar, three second year students of Computer Science and Engineering at IIT Bombay for the CS251 project. All copyrights are reserved and proper references must be given while using the code for any purpose, otherwise you might face legal action. 

 

/////////////////////////////////////////////     REEFERENCES USED      /////////////////////////////////////////////////////


The following references were used while making this project, and we are highly thankful to evryone for contributing these articles:


1. GENERAL DJANGO REFERENCE - thenewboston's Django tutorial series (https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK)


2. DJANGO DOCUMENTATION - https://docs.djangoproject.com/en/2.1/


3. REFERENCES USED FOR MANAGING USERS, LOGIN, SIGNUP, ETC. - https://wsvincent.com/django-user-authentication-tutorial-login-                                                              and-logout/ for user login and authentication at                    https://wsvincent.com/django-user-authentication-tutorial-signup/ for creating new users.


4. PYTHON MECHANIZE LIBRARY - https://pypi.org/project/mechanize/  , a very useful library which enables form filling using Linux terminal (Bash Script).


5. STACK OVERFLOW  - Thanks for building this awesome community where we got many of our doubts resolved. It's tough to include them all, but it helped us upload files, use the mechanize library, encryption/decryption
                     make forms for uploading files, and debugging in general.


6. W3SCHOOLS  -  https://www.w3schools.com/  for JavaScript and other web client related stuff


////////////////////////////////////////////////////     FEATURES     ///////////////////////////////////////////////////////


CCure allows the users to use their Linux terminal to upload and download files from a server. You simply need to put the file's path as an argument with the file upload function (discussed later) and the file would be available to download for you. The data is stored in encrypted form (in development stage right now) in our servers, so you need not worry about security breaches. You would be able to make a profile for yourself, and upload files which no one except you (not even us) can view. The initial release consists of the upload/download and login facility, but we would be adding more features to make the product more powerful. CCure is currently available only for Ubuntu terminal, but we would try to make an Android app, website (a Web client already exists though) and a Windows product soon.


///////////////////////////////////////////////////////     USAGE     //////////////////////////////////////////////////////


1. INSTALLING CCURE - Untar the server tarball in your home directory (Server). type 'bash server.sh' on your terminal to 			install all modules. For clients, do the same with client tarball and type 'bash client.sh' to install all the required modules. You can now use usual commands (descibed below) to upload/login and use the web client for signup and download/view.


2. SIGNUP - Visit CCure's website and click on Signup. Choose an appropriate username and password and register yourself. Keep these credentials safe with you. We suggest making a strong password, although the password field won't allow you to signup unless you use a fairly strong password.
 

3. LOGIN - Type on the Terminal (make sure you are connected to the Internet) 'spc config edit'.
	   You would see prompts asking you for your username and password. Enter your (correct) login credentials and press Enter. If you see a prompt saying that you are logged in successfully- congrats, you            have made it! Otherwise you would be asked to enter your login credentials again until you c=enter them correctly. Go to step 2 if you haven't made an account on CCure yet.


4. UPLOADING FILES - First, signin successfully as above. 


5. DOWNLOADING FILES - After a successful login, you will view a portal showing the files uploaded by you. You can then click on them to view them in the browser (support provided for formats like pdf, jpg, txt, etc) or download them to your machine.

6. HELP - You can use 'man spc' command on terminal to see all the commands and their usage.


#################################################        THE END       ######################################################


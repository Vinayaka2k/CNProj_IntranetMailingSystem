# CNProj_IntranetMailingSystem
Building multiple-client server system using socket programming.  When a client tries to send a mail to other client,  the message doesnot directly go to the client. Instead, it first goes to the mail server, that stores the message in a sql database. And when a new client connects, server queries the database and retrieves all mails of that client (displays inbox of that client).

Technologies used :

HTML for GUI

Flask for rendering HTML using python

Socket Programming

MY SQL database

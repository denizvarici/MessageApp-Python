## MessageApp-Python
#### Python Chat App by socket library
---------------------------------------------------------------------------------------------------------------------------------------------
### WHAT CAN YOU DO WITH THIS 
-- You can create a server for chat with your friends
---------------------------------------------------------------------------------------------------------------------------------------------
### What to do ?
-- Firstly, clone this repository into a folder.
-- Inside MessageApp-Python/Program/ there are two python files. server.py and client.py
---------------------------------------------------------------------------------------------------------------------------------------------
### TEST CHATTING 
-- Open cmd and type "python server.py" after that on another cmd type "python client.py" write a username and join the chat. You can run multiple client.py (limit=5(you can change inside code server.py -> LISTENER_LIMIT constant)) and see if messaging successfull.
---------------------------------------------------------------------------------------------------------------------------------------------
### HOW TO CHAT ONLINE WITH YOUR FRIENDS ?
-- create an ngrok account -> https://ngrok.com/ and install ngrok.exe 
-- after auth tocken configuration type ngrok tcp 1234 (port must be same with server.py PORT constant)
-- then you will see "Forwarding -> tcp://x.tcp.eu.ngrok.io:yyyyy -> localhost:1234" this line. Change client.py HOST and PORT constants
-- example HOST = x.tcp.eu.ngrok.io, PORT = yyyyy
-- then you send client.py to your friends and start chatting !
---------------------------------------------------------------------------------------------------------------------------------------------
#### Contact me and see my other works
www.denizvarici.com.tr

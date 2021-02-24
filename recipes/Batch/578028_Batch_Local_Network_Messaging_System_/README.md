## Batch Local Network Messaging System   
Originally published: 2012-01-30 03:04:10  
Last updated: 2012-02-03 01:41:41  
Author: Alexander James Wallar  
  
This is a Batch Local Messaging System that can be used to send messages between computers that share the same file system.

There are three files in the code below. They are separated with dashed lines. There is a comment on the top of each segment of code indicating the file name that the code needs to be saved as. They need to be saved as three separate batch files in the same folder. 

The first file, MessengerMain.bat will ask you for your name and then an address. The name should be whatever you wish your screen name to be. The address needs to be the path of the FOLDER that is shared between you and the other computer that you are communicating with. Once these pieces of information are entered, two screens will appear. The first is the Sender screen and the other is the Receiver screen. 

How does it work?
The MessengerMain.bat file will create two text files, Name.txt and Address.txt, that will hold your user name and the common folder address. It will then use the START command to run Sender.bat and Receiver.bat. Sender.bat will create a text file named msgtext.txt in the address folder you specified in MessengerMain.bat. If there is already a file of this sort in existence in the address folder, it will overwrite it. Once this file is created, any message you enter will be saved in the msgtext.txt file after the name you entered (%name%: %msg%). Sender.bat the CLS (clears) the screen and asks you for another message continuously. Receiver.bat is very similar. Receiver.bat, first off, reads the Address.txt file and the Name.txt file to find your information given in MessengerMain.bat just like Sender.bat does. It will count the number of lines in the msgtext.txt file and will clear the whole screen and print out the whole contents of the file if the number of lines in msgtext.txt increases. So basically you are writing to a shared file and reading from a shared file. 

Example:

I have a folder called MSGFolder located in the folder as I have my MessengerMain.bat, Receiver.bat, and Sender.bat files. I then run MessengerMain.bat by double clicking on the icon. I enter Alex for my Name and MSGFolder as the Address. I then double click MessengerMain.bat again and enter the name Bob for Name and MSGFolder for Address. Once you do this you can type in either of the Sender.bat interfaces and it will show up as if you are talking.  
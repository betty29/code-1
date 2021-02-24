## Simple Example demonstrating Ajax Implementation using Perl  
Originally published: 2007-03-11 07:37:16  
Last updated: 2007-03-11 07:37:16  
Author: Rajkumar Jain  
  
In the example below, we have a table containing Student names and Marks. Every row has an Edit button, by which user can edit the information for that row. We have used Microsoft Access as the Database to keep things very simple.  In order to run the below example code you will have to create a table by the name “Student” in MS Access”. It should have the following columns.

Column Name	 Data type
Sl_No(Primary Key)	Number
Name	Text
Marks	Number

Also you need to create a DSN by the name “mydsn” pointing to the Access DB.

The basic logic here used in the example is that we have two separate rows for View and Edit (for every Student). Initially we hide the Edit row (by using style="display:none") and display the View Row(by using style="display:block").  When the user clicks on the “Edit” button, the View row becomes hidden and the Edit row is displayed. We have used JavaScript to toggle between the rows. Below is the code snippet used in files (AjaxExample.pl and student.js).
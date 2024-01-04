In this word counter building task, the following were the design choices, features and challenges that I faced.
Intially the project began with studying and analysing word counter websites and planing for the outline of the project. Once the intial phase was done, the next step was to determine the choices-->

1) Graphical User Interface: To enhance user experience and ease of use, I decided to implement a GUI using the tkinter library. 

2)Layout and Organization: The interface is divided into two main panels. The left panel is for text input and copy/cut/paste buttons, while the right panel displays the word count statistics and control buttons like Undo, Redo, Refresh, and Process.

3)Welcome Window: The welcome window includes a welcome message and a note explaining the functionality of the Word Counter program.

4)Button Placement and Styling: Buttons are placed logically near the text box for ease of use. They're color-coded for differentiation and follow a consistent design scheme.


Features are as follows-->

1)Error Handling: The program checks for empty input and displays an error message if no sentence or paragraph is entered.

2)Word Counting Functionality: The program accurately counts the number of words in the sentence or paragraph entered by the user using the split method and the len function.

3)Undo/Redo Functionality: Users can revert back and forth between changes made in the text input with the Undo and Redo buttons.

4)Copy/Cut/Paste Actions: Integrated buttons for copy, cut, and paste facilitate text manipulation.

5)Modular Code: The program is divided into functions for better code organization and reusability.

6)Refresh Button: It can be used to clear the window and have a fresh start.

Challenges that I faced are as followed:

1)Function Integration: Coordinating various functions like counting text, managing undo/redo history, and implementing copy/cut/paste features required careful synchronization to avoid conflicts or unexpected behavior.

2)User Input Handling: Ensuring the program handles potential errors, such as empty input, required careful consideration. Error handling was implemented to guide the user in case of invalid input.

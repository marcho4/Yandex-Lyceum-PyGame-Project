# Yandex-Lyceum-PyGame-Project
files:
README.md --> this file
requierements.txt --> list of libraries you need to install
main.py --> code
data --> all images, sounds and etc. you need to download

This game is written on Python 3.10 with the main use of 'pygame' library. Widget with the form to write down the name is made on 'PyQT5'. Working with 
the database for saving results uses 'sqlite3' library and SQL.

Game where player should catch falling apples colliding character with them. The player controls his character by putting down "<-" and "->" keys.
If the lives* end, the level is over. The result is saved to the database and the high-score among all the players updates and it is shown on level windows.
To switch to the next window player should put down the "SPACE" key. After passing two levels, player needs to write his name in the form and click the
button "Save" to save his result to the database, so, we can see all results and show the high-score.

*In first level player loses a "life" if he cathches a bad apple. In second one there are two situations: cathing a bad apple and missing a normal.

# Backend_task
Built a server that responds to mathematical operations sent via URL. It also maintains a history of the last 20 operations performed on the server.

|             | Get Request |   Response    |
| :---        |    :----:   |          ---: |
|  ENDPOINT   |      /      |  HTML:Welcome |
|             |   /history  | HTML:Lists the last 20 operations |
|     Eg1        |   /5/plus/3 |JSON{question:”5+3”,answer: 8}|
|     Eg2        | /3/minus/5  |JSON{question:”3-5”, answer: -2}|
|     Eg3        |/3/minus/5/plus/8|JSON{question:”3-5+8”, answer: 6}|
|     Eg4        |/3/into/5/plus/8/into/6|JSON{question:”3*5+8*6”, answer: 63}|
|....so on    |                      |                                     |


You can implement any amount of operators int it.


# Installing_SQLite:

SQLite is a lightweight, self-contained, and serverless SQL database engine that's widely used for embedded systems and local data storage.

1) For Windows, you can download the precompiled binaries of SQLite from the official website:

Visit the SQLite Download Page.
Scroll down to the "Precompiled Binaries for Windows" section.
Download the "sqlite-tools-win32-x86-xxxxxxx.zip" file.
Extract the contents of the ZIP file to a directory.
Add the directory to your system's PATH environment variable to access the sqlite3 command from anywhere.

For Verifying Installation
To verify that SQLite has been successfully installed, open a terminal or command prompt and run:

sqlite3 --version

This should display the version of SQLite installed on your system.

2) For macOS(homebrew)
If you're using macOS and have Homebrew installed, you can install SQLite with:

brew update
brew install sqlite

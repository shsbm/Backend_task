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


You can implement any amount of operators in it.

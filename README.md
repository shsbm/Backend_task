# Backend_task
Built a server that responds to mathematical operations sent via URL. It also maintains a history of the last 20 operations performed on the server.

_______________________________________________________________________________________________________________________

Let’s assume our server is at: localhost:5000. Here’s some sample requests:

|      |GET REQUEST | RESPONSE |
|------|------------|----------------------------------------------------|  
|Endpoint|/|HTML:Welcome|      
|       |/history|HTML:List the last 20 operations performed on the server| 
|       |/5/plus/3|JSON:"5+3"="8"|
|       |/3/minus/5|JSON:"3-5"="-2"|
|       |/3/minus/5/plus/8|JSON:"3-5+8"="6"|
|       | /3/into/5/plus/8/into/6|JSON:"3*5+8*6="63"|                                                                         .....SO ON                                                                                                                                                     
_______________________________________________________________________________________________________________________

You can implement any amount of operators int it.

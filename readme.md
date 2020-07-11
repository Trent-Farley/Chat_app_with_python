## A little Python application using SocketIO for chatting


### If you would like to run this application: 
1. clone this repository
2. run ```python 
pip install -r requirements.txt ```
3. run ```python
python -u main.py ```

#### You should have something like this: 

![Photo of chat app working](./Websocket_demo.jpg)

#### You can open up multiple tabs that all can communicate with each other in real time!
#### This requires no packet headers when the client and server have decided to upgrade. Websockets are great for increasing the speed that packets can be sent and received as well as being very secure. WIth browser support for almost every browser, it is certainly where the internet is heading. 
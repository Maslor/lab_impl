# lab_impl
<h5> server-client implementation </h5>

*General Description* :
Chat based on TFTP protocol.

*Usage* : The server is launched and it's supposed to process requests from the running clients. At the moment, it can only process requests form two users.
The first client that registers is able to choose Read or Write mode; the other client that registers is attributed the mode that's left. From then on, everytime a message is sent and read, the modes switch and allow communication in the opposite way (Read mode client receives the message, Write mode client sends it).

*Future changes* : Looking for someone to implement TCP mode, only runs on UDP at the moment.

**Help is more than welcome, don't hesitate to request a pull!**

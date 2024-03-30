# Reaper

```
      ____
     / __ \___  ____ _____  ___  _____
    / /_/ / _ \/ __ `/ __ \/ _ \/ ___/
   / _, _/  __/ /_/ / /_/ /  __/ /
  /_/ |_|\___/\__,_/ .___/\___/_/ v1
                  /_/                                   
```

Reaper is a powerful python doser that supports Layer 4/7 requests.

# Install
1. Run the command `git clone https://github.com/jwe0/reaper`
2. Run `pip install -r requirements.txt`
3. Run `python main.py`

# Modules
Explanation of each section and module.
## Layer 4
This is layer 4 of the iso model also know as the Transport Layer.
### ~ Tcp
Makes a tcp connection to the target server then sends data to the target in an attempt to overwhelm the server, It leaves the connections it makes open to confuse and overwhelm the server.
### ~ Udp
Same as tcp except with a udp connection instead of tcp.
### ~ Syn
Same as tcp and upd except it will use syn connections which in certain situations can be more powerful.

# Layer 7
This is layer 7 of the iso model also known as the Application Layer. Reaper also adds a random user agent so that the request looks legitimate server side.
### ~ Post
Sends post requests to the target url with custom headers and json data.

### ~ Get
Sends get requests to the target url with custom headers and json data.

### ~ Delete
Sends delete requests to the target url with custom headers and json data.

### ~ Patch
Sends patch requests to the target url with custom headers and json data.


# Tools
Reaper also includes a toolbox of useful tools relating to networking.
### ~ Reverse DNS
This module uses the Domain Naming System or DNS for short to turn a domain to a target IP address.
### ~ Portscanner
Scans the target ip address for common open ports that could be used in the dos attack.
### ~ Socket Server Debug
This is my personal favourite module. It allows you to connect to a server with an IP and PORT then allows you to send messages to a server and recieve the data the server returns with, this is great for debugging weak chat applications and general messing around.
### ~ Api Debugger
This allows you to get the response data for Get, Post, Put, Delete and Patch, it allows you to give custom headers and json data so you can add authentication cookies/tokens. The data and header is given in the format `{"example-header" : "example-header-value"}` the user agent is added automatically so no need to add one in your headers, if you do not want to have any data in that field just leave it blank reaper will automatically adjust to this and only send the headers to the target.


# Regards
I take no legal responsibility for any negative actions committed with my software. This was made for ethical purposes only <3.

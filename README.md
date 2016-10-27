Slippy
======

Slippy is a tiny client server library for exploring the async/await syntax of Python 3.5+

It has a simple websocket implementation using aiohttp so a client can subscribe to the server which sends details of async tasks on the server. A simple example of tailing a logfile is included.


## Features
- Websocket client / server for subscribing to interesting events
- Basic log tailing with support to filtering (TODO)


## Dependencies
- Python 3.5+
- aiohttp, aiofiles


#!/bin/sh

python -m aiohttp.web -H 0.0.0.0 -P 8080 slippy.server:init_func

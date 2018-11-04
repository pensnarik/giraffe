#!/usr/bin/env python3

from app import app

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=1984)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

from flaskext.script import Manager


from reel import app

manager = Manager(app)

app.test_request_context('/').push()



@manager.command
def test():
	os.system('./test_reel.py')



if __name__ == "__main__":
	manager.run()

from flask import Flask
app = Flask(__name__)

from deploy.deploy import *


print('hi')
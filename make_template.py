import get_question
import os
# TODO: 1. Make a template py file 
#       2. Put question name and boilerplate
def put_template(URL: str, problem_name: str):
    with open("../../templates/py.py", mode='r') as tf:
        bp = URL + tf.read()

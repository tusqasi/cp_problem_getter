import get_question
import os
# TODO: 1. Make a template py file 
#       2. Put question name and boilerplate
os.chdir("../questions")
def put_template(URL: str, problem_name: str):
    with open("../../templates/py.py", mode='r') as tf:
        bp = f"# URL: {URL}\n# USER: tusqasi\n{tf.read()}"
    os.chdir(problem_name)  
    with open("ques.py", mode='w') as pf:
        pf.write(bp)

put_template("httpsf", "replacement")

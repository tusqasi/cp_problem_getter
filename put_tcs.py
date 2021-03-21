import os 
import get_question

os.chdir("../questions/") # Should this be hard coded or user defined
existing_ques = os.listdir()
ques_name = get_question.get_meta()

# This handles folder name collision
if ques_name in existing_ques:
    if ques_name[-1].isdigit():
        ques_num = int(ques_name.split("_")[-1])
        ques_name = f"{ques_name[:-1]}{1+ques_num}"
    else:
        ques_name += "_01"

os.mkdir(ques_name)
os.chdir(ques_name)
# Beyond this point question_name is unique in question's directory
# save get_question.inputs() to in.txt

def write_this(file_name: str,data: list):
    with open(file_name, mode='w') as fp:
        for _ in data:
            fp.write(_)
ip, op = get_question.get_io()
write_this("in.txt", ip)
write_this("out.txt", op)

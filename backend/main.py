from admin import administration
from functions import Data
import json
from Jyp_note_book import ipynb
count = 1
while True:
    break
    question = input("Enter break to end up the loop or else Enter the question: ")
    if question != "break":
        question_number = count
        answer = input("Enter Answer : ")
        difficulty = input("Enter difficulity : ")
        Data.Question_bank(question_number,question,answer,difficulty)
        count  += 1
    else:
        break
    print("\nDone----\n")

while True:
    #break
    print("\n\n\tCommands\n\nnew\tCreate new file\ncode\tAdd code block\ntext\tAdd text block\ndelete\tDelete cell\nbreak\tto break out of loop\n")
    commands = input("Enter here : ")
    if commands == "new":
        file_name = input("Enter file name : ")
        ipynb.create_notebook(file_name)
    elif commands == "code":
        file_name = input("Enter the file name: ")
        file_name+=".ipynb"
        ipynb.add_code_cell(file_name)
    elif commands == "text":
        file_name = input("Enter file name : ")
        file_name+=".ipynb"
        text = input("Enter the text : ")
        ipynb.add_markdown_cell(file_name,text)
    elif commands == "delete":
        file_name = input("Enter file name : ")
        file_name+=".ipynb"
        cell_no = int(input("Enter the cell to be deleted : "))
        ipynb.delete_cell(file_name,cell_no)
    elif commands == "break":
        break
    else:
        print("Invalid input") 

    print("\nDone----\n")


ref = administration.reference()
temp = ref.get()

with open('/home/nakulan/VS Code/Project/data.json', 'w') as json_file:
    json.dump(temp, json_file)
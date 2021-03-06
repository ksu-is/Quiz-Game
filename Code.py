from flask import Flask, request, render_template

app=Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('index-quizgame.html')

@app.route('/quiz',methods=['GET','POST'])
def quiz():
    
character_names = open('charaters.txt','w+')
character_names.write("Homer","Marge","Bart","Lisa","Maggie","Santa’s little helper","Snowball", "Abraham","Apu", "Barney","Chief Wiggum","Itchy","Scratchy","Kent Brockman","Krusty the Clown","Lenny","Uter","Millhouse","Moe","Mr.Burns","Ned Flanders","Otto Man","Patty","Selma","Ralph Wiggum","Seymour Skinner","Waylon Smithers", "Mayor Joe Quimby","Nelson Muntz", "Groundskeeper Willie")
character_names.seek(0)
character_list = character_names.read() 

character_names = open('characters.txt','r')
characters = character_names.readline()

while characters:
    characters = character_names.readline()
    
correct = []
incorrect = []
character_list = []

def get_names():
    count = 0
    while count <= 30:
        character_input = request.form['character_input']
        if character_input.capitalize() in character_list:
            print(character_input,"already entered into list. No duplicates.")
        elif len(character_input) > 0:
            character_list.append(character_input.capitalize())
            count += 1
        elif count > 30:
            break
    return character_list

get_names()

for name in character_list:
    if name in characters:
        correct.append(name)
    else:
        incorrect.append(name)
        
correct_numbers = len(correct)


print('\n')
print("Character List:",character_list,"\n")
print("Grade:",grade,"%")
print("Correct Characters:",correct)
print("Incorrect Characters:",incorrect)

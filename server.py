#Make a simple server application using Python. Use the socket library or flask. All the server has is a dictionary which contains a toy and the quantity of that toy. The client should be able to use a GET request to the server to see how many characters it has.
from flask import *
app = Flask(__name__)
#sample server client name 
@app.route('/', methods = ['POST', 'GET'])
def data(d):
    while True:
        charlist = {'Mario': 1, 'Luigi': 2, 'Donkey Kong': 3, 'Yoshi': 4, 'Link': 5, 'Kirby': 6, 'Fox': 7, 'Pikachu': 8, 'Jigglypuff': 9, 'Samus': 10, 'Captain Falcon': 11, 'Ness': 12}
        for i in range(len(charlist)):
            charlist[i] = charlist[i].lower()
        if request.method == 'GET':
            return print("These are the characters"), charlist
        if request.method == 'POST':
            input = d.receive()
            input = input.lower()
        if input in charlist:
            input.title()
        print(input + "is in the list")
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
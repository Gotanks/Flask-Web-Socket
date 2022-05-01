#make a simple server application using Python. Use the socket library or flask. All the server has is a dictionary which contains a toy and the quantity of that toy. The client should be able to use a GET request to the server to see how many of a toy it has.
from flask import Flask
from flask import Sock

app = Flask(__name__)
sock = Sock(app)

#sample server client name 
@sock.route('/Characters')
def data(d):
    while True:
        charlist = ["Mario", "Luigi", "Donkey Kong", "Yoshi" "Link", "Kirby", "Fox", "Pikachu", "Jigglypuff", "Samus", "Captain Falcon", "Ness"]
        for i in range(len(charlist)):
            charlist[i] = charlist[i].lower()
        input = d.receive()
        input = input.lower()
        # loops through the character list for the name of character
        match = [name for name in charlist if(name in input)]
        match = [match.title() for match in match]

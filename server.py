#Make a simple server application using Python. Use the socket library or flask. All the server has is a dictionary which contains a toy and the quantity of that toy. The client should be able to use a GET request to the server to see how many characters it has.
from flask import *
app = Flask(__name__)
# charlist = {'Ganondorf': 1, 'Falco': 2, 'Bowser': 3}
charlist = {
    "Bowser": 1,
    "Ganondorf": 2,
    "Falco": 3
}

charlist = dict((k.lower(), v) for k, v in charlist.items())
#sample server client name 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    while True:
        args = request.args
        charname = args.get('name')
        charnumber = args.get('number')
        if request.method == 'POST':
            if any([True for k, v in args.items() if v == charname]):
                result = {k: v for k, v in args.items}
                return result
            else:
                return "Not in list"
        else:
            return charlist
        return "Something goes here"
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
#Make a simple server application using Python. Use the socket library or flask. All the server has is a dictionary which contains a toy and the quantity of that toy. The client should be able to use a GET request to the server to see how many characters it has.
#Make get request for client to query through ex: if user types in value in the url, the server returns key
from flask import *
app = Flask(__name__)
charlist = {
    "Bowser": "Melee",
    "Ganondorf": "Melee",
    "Falco": "Melee",
    "Lucario": "Brawl",
    "Ike": "Brawl",
    "Cloud": "Sm4sh",
    "Ridley": "Ultimate",
    "Kazuya": "Ultimate"
}

# charlist = dict((k.lower(), v) for k, v in charlist.items())
#sample server client name 
@app.route('/data', methods = ['GET'])
def data():
    args = request.args
    charname = args.get('name')
    chargame = args.get('game')
    result = charlist
    # if request.method == 'POST':
    #     return result
    if None not in (charname, chargame):
        result = {k: v for k, v in charlist.items() if k == charname and v == chargame}
            # return result
    elif charname is not None:
        result = {k: v for k, v in charlist.items() if k == charname}
         # return result.keys
    elif chargame is not None:
        result = {k: v for k, v in charlist.items() if v == chargame}
    return result
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
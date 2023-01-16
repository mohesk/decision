from flask import Flask
from newspaper import Article
from os import environ
app = Flask(__name__)

@app.route("/")
def hello_world():
    updatedIndex = words.index("(updated:")
    header = f"Recent decisions in the Dublin visa office (updated: {words[updatedIndex + 1]} {words[updatedIndex + 2]} {words[updatedIndex + 3][:5]}"
    bigger = 54364092
    smaller = 54364092
    no = 54364092
    try:
        getIndex = words.index(f"{no}")
    except:
        getIndex =0
    while True:
        try: 
            words.index(f"{no}")
            break
        except:
            no = no + 1
    bigger = no
    no = 54364092
    while True:
        try: 
            words.index(f"{no}")
            break
        except:
            no = no - 1
    smaller = no
    if getIndex:
        my_decision = f"Your decision number is 54364092 and it's { words[getIndex + 1]}"
    else:
        my_decision = "Your decision number is 54364092 and it hasn't been proccessed "
    return f'''
            <h1>{header} </h1><br>
            <h3>Previous number is {smaller} and it's { words[words.index(str(smaller)) + 1]} </h3>
            <h3> {my_decision}</h3>
            <h3>Next number is {bigger} and it's { words[words.index(str(bigger)) + 1]} </h3>
        '''


if __name__ == '__main__':
    visa = Article("https://www.irishimmigration.ie/visa-decisions/")
    visa.download()
    visa.parse()
    words = visa.text.split(" ")
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.debug =True
    app.run(HOST, PORT)

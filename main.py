from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
  <head>
    <style>
      form {
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }
        textarea {
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }
    </style>
  </head>
  <body>
    <!-- create your form here -->
      <form action="/" method="post">
      <label for="rot"> Rotate by:
        <input type="text" name="rot" value= '0' />   
      </label>
      <br>
      <label>
        <textarea name="text"></textarea>
      </label>
      <input type="submit" value='Submit Query'/>
  </body>

"""



@app.route("/", methods=['POST'])
def encrypt():
  resp = ""
  rot=int(request.form['rot'])
  text=request.form['text']

  rotated = rotate_string(text, rot)
  
  resp = "<h1>{key}</h1>".format(key=rotated)

  return resp


@app.route('/')
def index():
  return form


app.run()
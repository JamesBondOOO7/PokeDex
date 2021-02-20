from flask import Flask, render_template, redirect, request
import pokemon

app = Flask(__name__)

@app.route('/')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def pokemon_predict():

    if request.method == "POST":

        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)

        predicted_pokemon = pokemon.pokeDex(path)
        print(predicted_pokemon)

        result_dict = {
            'image' : path,
            'prediction' : predicted_pokemon
        }

    return render_template("index.html", your_result= result_dict)

@app.route('/about.html')
def about():
    images = ["./static/i2.png"]
    return render_template("about.html", img_paths=images)
    

if __name__ == '__main__':

    app.run(debug=True)
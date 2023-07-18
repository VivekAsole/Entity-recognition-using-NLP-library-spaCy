from flask import Flask, render_template, request
import spacy
import json

nlp = spacy.load("en_core_web_md") #Loading open source trained model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') #homepage


@app.route('/predict', methods=['POST']) #accessing input using POST method
def predict():
    i = 0
    dict = {}
    question = request.form['a'] #storing html input
    doc = nlp(question) #provide stored input to model

    for ent in doc.ents: # for loop to go through each token
        i = i + 1 # count entity found
        dict[i] = {'Entity': ent.text,
                   'Type': ent.label_,
                   'Value': ent.label,
                   'Position': ent.start_char}

    data_json = json.dumps(dict, indent=4) # converting python dict into json string
    return render_template("predict.html", ques=question, count=i, data=data_json) #


if __name__ == "__main__":
    app.run(debug=True)

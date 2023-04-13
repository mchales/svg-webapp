from flask import Flask, render_template, request
import model

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imageFile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    caption = model.create_new_caption(image_path)
    return render_template('index.html', prediction = caption)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
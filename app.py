from flask import Flask, render_template, request
from keras.models import load_model
import os
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("proje.html")

@app.route("/predect", methods=['POST'])
def predection():
    if ('image' not in request.files):
        return ('No file part', 400)  
    image_file = request.files["image"]
    if(image_file.filename ==""):
        return render_template("proje.html",prediction = "Please upload the image" )
    else:
        #save image to the directory
        downloads_dir = os.path.join(app.root_path, 'static/downloads')
        os.makedirs(downloads_dir, exist_ok=True)
        image_path = os.path.join(downloads_dir, image_file.filename)
        image_file.save(image_path)
    #load model
        model = load_model('./Ultrasonic_welding_IPDL.h5')
       
        img = Image.open(image_path)
        img = img.resize((224, 224))
        img_array = np.array(img)/255.0
        img_array = np.expand_dims(img_array, axis=0)
        classes= ['dent', 'good', 'overextrusion', 'scratch']
        prediction = model.predict(img_array)
        print(prediction)
        max_predect =np.argmax(prediction)
        print(max_predect)
        
        defect = classes[max_predect]
        display_image = "static/downloads/"+image_file.filename
        
        return render_template("proje.html",prediction = defect,uploaded_image=display_image)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5070)






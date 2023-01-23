from io import BytesIO
from flask import Flask, jsonify, request
import os, requests
from PIL import Image
from werkzeug.utils import secure_filename
import uuid
import json 

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "storedimages"
image_list = []

with(open('images.json','rt')) as js_file:
    image_list = json.load(js_file)
    js_file.close()



@app.route("/")
def hello():
    return ('Hola')


#Comprueba si ya hemos subido anteriormente la imagen

def check_filename(list_images, filename):
    for img in list_images:
        if img['name'] == filename:
            return True
    return False


#First endpoint /upload_image


@app.route('/upload_images', methods=["POST"])
def upload_image():
    if request.content_type == "application/json":
        data = request.get_json()
        #validate the url
        if 'url' in data:
            #save the image from the url
            url = data['url']
            l_url = url.split('/')
            filename = l_url[len(l_url)-1]
            response = requests.get(url)
            if response.status_code == 200:
                content_type = response.headers.get("content-type")
                if 'image' in content_type:
                    
                    if not check_filename(image_list,filename):
                        image=Image.open(BytesIO(response.content))
                        width, height = image.size
                        image_id = uuid.uuid4().hex
                        #creamos a partir de la imágen un thumbnail con el nombre de la imagen original, al
                        #que hemos añadido el prefijo thumb.
                        img = image.copy()
                        img.thumbnail((200, 200))                        
                        img.save(app.config["UPLOAD_FOLDER"]+'/thumbnails/'+'thumb'+filename)

                        image_list.append({"image_id": image_id, "width": width, "height": height, "name": filename})
                        with open('images.json','wt') as js_file:
                            #js_file.write(str(image_list))
                            json.dump(image_list,js_file)
                            js_file.close()

                        print(image_list)

                        #save image on the folder
                        image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))    
                    #generate a unique id for the image
                    return jsonify({"image_id": "unique_id"})

                else:
                    return jsonify({"error": "URL does not contain an image"}), 400
            else:
                return jsonify({"error": "Invalid URL"}), 400
        else:
            return jsonify({"error": "Invalid request. No url provided"}), 400
  
  #validate the image file
    elif "multipart/form-data" in request.content_type:
        file = request.files["image"]
        if file:
            filename = secure_filename(file.filename)
            ext = os.path.splitext(file.filename)[1]
            if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
                try:
                    image= Image.open(file)
                    image.verify()
                except:
                    return jsonify({"error": "Invalid image format"}), 400
             
            #save the file on the folder
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            
            #generate a unique id for the image
            return jsonify({"image_id": "unique_id"})
        else:
            return jsonify({"error": "Invalid request. No image provided"}), 400
    else:
        return jsonify({"error": "Invalid request. Please provide a json or multipart/form-data"}), 400
    

#Third endpoint /list_images
@app.route('/list_images', methods=["GET"])
def list_images():
    try:
        img_lst = []
        global image_list
        for img in image_list:
            dic_img = {}
            dic_img['name'] = img['name']
            fich = app.config["UPLOAD_FOLDER"]+'/thumbnails/'+'thumb'+img['name']
            print(fich)
            with open(fich,'rb') as file:
                str_data = ''
                data = file.readlines()
                for dato in data:
                    str_data+=dato.decode('latin-1')
                dic_img['img'] = str_data
                file.close()
            img_lst.append(dic_img)
        return jsonify(img_lst), 200
    except FileNotFoundError:
        print("File not found")
        return jsonify({"error": "No images uploaded yet"}), 404
    except PermissionError:
        print("Permision Denied")
        return jsonify({"error": "Permission denied to access the upload folder"}), 401
    except OSError:
        print("The apocalypse is coming!!!!")
        return jsonify({"error": "An issue with the server occurred"}), 500

    

#Second endpoint /analyse_image

@app.route("/analyse_images/<image_id>", methods=["GET"])
def analyse_image(image_id):
    try:
        img_lst = []
        global image_list
        for img in image_list:
            if img['image_id']== image_id:
                dic_img = {}
                dic_img['name'] = img['name']
                fich = app.config["UPLOAD_FOLDER"]+'/thumbnails/'+'thumb'+img['name']
                print(fich)
                with open(fich,'rb') as file:
                    str_data = ''
                    data = file.readlines()
                    for dato in data:
                        str_data+=dato.decode('latin-1')
                    dic_img['img'] = str_data
                    file.close()
                img_lst.append(dic_img)
            return jsonify(img_lst), 200               
    except FileNotFoundError:
        return jsonify({"error": "Image not found"}), 404
    except:
        return jsonify({"error": "Invalid image file"}), 400





if __name__=='__main__':
    app.run(debug=True)


'use strict';

function uploadImage() {
  var file = document.getElementById("image-file").files[0];
  var url = document.getElementById("image-url").value;

  //Check if the user selected a file or entered a url
  if(file){
    var formData = new FormData();
    formData.append("image", file);
    fetch("/upload", {
      method: "POST",
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error("Error:", error);
    });
  }else if(url){
    fetch("/upload", {
      method: "POST",
      body: JSON.stringify({url}),
      headers: {
        "Content-Type": "application/json"
      }
    })
    .then(response => response.json())
    .then(data => {
      alert('Image uploaded successfully. Image ID:${data.image_id}');
      console.log(data);
    })
    .catch(error => {
      console.error("Error:", error);
    });
  } else {
    alert("Please select an image file or provide an image URL.")} 
}
debugger; 


//Lists the images that have been uploaded so far

function listImages() {
    fetch("/list_images")
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                var imageData = data.decode('latin-1');
                var binaryData = atob(imageData);
                var arrayBuffer = new ArrayBuffer(binaryData.length);
                var view = new Uint8Array(arrayBuffer);
                for (var i= 0; i < binaryData.length; i++){
                  view[i] = binaryData.charCodeAt(i);
                }
                var blob = new Blob([arrayBuffer], {type:"image/jpg"});
                var image = new Image();
                image.src= URL.createObjectURL(blob);
                document.body.appendChild(image);

                let imagesList = document.getElementById("images.json");
                for (let i = 0; i < data.length; i++) {
                    let imageId = data[i].image_id;
                    let li = document.createElement("li");
                    li.innerHTML = imageId;
                    imagesList.appendChild(li);
                }
            }
        });
}


//Reads the JSON file that stores the image's height and width

function showImageInfo(imageId) {
  fetch(`/analyze_image/${imageId}`)
      .then(response => response.json())
      .then(data => {
          if (data.error) {
              alert(data.error);
          } else {
              let imageInfo = document.getElementById("image-info");
              imageInfo.innerHTML = `Image ID: ${data.image_id}<br> Width: ${data.width}<br> Height: ${data.height}`;
          }
      });
}

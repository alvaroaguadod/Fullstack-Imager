'use strict';

const printUsers = users => {
    const app = document.getElementById('app');
    const fragment = document.createDocumentFragment();
    const ul = document.createElement('ul');
    ul.classList.add("my-ul-class");
    users.forEach(user => {
        const li = document.createElement('li');
        const img = document.createElement('img');
        img.setAttribute("src", user.picture.thumbnail)
        li.append(img, ' ' + user.name.first + ' ' + user.name.last);
        ul.append(li);
    });
    fragment.append(ul);
    app.append(fragment);
}
 
const getUsers = number => {
    fetch(`https://randomuser.me/api/?results=${number}&nat=es`)
    .then(response => response.json())
    .then(data => printUsers(data.results))
    .catch(error => console.error(`There was an error ${error}`));
};
 
getUsers(10);



/*const printListaImagenes = images => {
    const app = document.getElementById('imagesList');
    const fragment = document.createDocumentFragment();
    const ul = document.createElement("ul");
    ul.classList.add("my-ul-class");
    images.forEach(image=>{
        const li = document.createElement('li');
        const img = document.createElement('img');
        img.setAttribute("src", image.picture.thumbnail)
        
        AQUÍ DARÍA USO DE LA FUNCION SHOWIMAGEINFO PARA W&H
        li.append(img, ' ' + image.name + ' ' + image.image_id + ' ' + image.width + ' ' + image.height);
        ul.append(li);
     });
     fragment.append(ul);
     app.append(fragment);
}


const getImages= number =>{
    fetch('list_images.json')
      .then(response => response.json())
      .then(data => printImages(data.results))
      .catch(error => console.error(`There was an error ${error}`));
};
 
getImages(10); /*salvo que el número serán las que hayan

*/

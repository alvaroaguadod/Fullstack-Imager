# 📷 Fullstack Imager 📷
The task consists in building a basic web page powered by a RESTful API that allows the user to upload new images (either from their computer or by providing a source url), list the images that have been uploaded so far as well as allow analyzing any of the images uploaded.<br />




![Screenshot](https://github.com/alvaroaguadod/Fullstack-Imager/blob/main/Screenshot%20Fullstack%20Imager.png)



## OH NO! BAD NEWS... already 📰😞 
Within a maximum of **96h**, I couldn't complete the task.  

**Frontend ->** In the folder named frontendpa there is 3 docker files, one JSON file and two folders. First being the static, which contains the CSS, the image, and the JS). Second one templates with the HTML. 
- The *HTML* is not yet being completed as for the error messages is just placed an space for them with red typo, and the JS functions are not being placed on it (only a JS file named app.js with the user thumbnails thing which is something I used to test the white wannabe screen).    
- The *JS* is not even tested yet therefore functions are not known to be working. 

**Backend ->** The Backend is complete and functional, if requests are made through a programme such as Insomnia. I therefore added an export from that programme. All the required endpoints are functional. 
- The */upload_images* uploads a picture from url or from a file, also creates a thumbnail from the original picture to be shown beside its picture name.  
- The */list_images* gives us a JSON with (latin-1) as the thumbnail and the key property of name.
- The */analyse_images* gives us a JSON only with the information of the <image_id> image.

**Docker ->** I need to learn more about it. Even the two images have been created, I do believe they need to be connected each other.

### Run the Code 👩‍💻

**Frontend ->** I directly opened the HTML on the Brave Browser. You can see the layout on the first screenshot. 

**Backend ->** I used Insomnia to send the requests and test it.

**Docker ->** Not yet been launched, and the connection between the two images has not been made either.

### List of Steps 👣
Desing Thinking is a skill I will start working on for my next projects.
I drew the frontend to get an idea of what it should look like and how it could be displayed.


![Screenshot](https://github.com/alvaroaguadod/Fullstack-Imager/blob/main/dibus1.png)
![Screenshot](https://github.com/alvaroaguadod/Fullstack-Imager/blob/main/dibus2.png)



As the project progressed, the questions piled up. But the politeness to say good morning (even to myself) was not lacking.

![Screenshot](https://github.com/alvaroaguadod/Fullstack-Imager/blob/main/questions%20piled%20up.png)


### ⚡️🏃🏻💨💨
This technical test required me to learn in a short period of time about **Docker**, as it was necessary to create two separate docker micro-services, one for the web page and one for the RESful API.

### 🧠 😣  💪  💡
It was a challenging task as I had not yet had the opportunity to test against the clock my Frontend skills (HTML, CSS, and JS) acquired while doing **CFGS DAW** and my Backend skills (Flask and Python) that I had acquired through self-study. The current Bootcamp on Backend with Python its being developed with a Django focused.

### 📚 🔎
I sought consultations, due to mental blocks, for functions or technologies I was not familiar with at the time of development, from the following resources:
•	StackOverFlow, ChatGPT -> for technical parts or functions I needed to learn to tackle the technical test.
•	Youtube -> for tutorials that helped me to refresh something I had learned or to reinforce my understanding of technical aspects."
https://www.youtube.com/watch?v=Esdj9wlBOaI
https://www.youtube.com/watch?v=YENw-bNHZwg
•	Brave Browser Inspect -> Perfect to see the changes that any CSS property makes in our Frontend.

### 🔮 🆕
Other functions that could have been added to the frontend include:
An specific button for the analyze function.
A Drag & Drop.
An erase button.

### Gratitud 🎁
Regardless of the outcome, it has been a continuous learning process. In which I have been able to discover with what I have struggled the most, what I need to improve, and ways to keep challenging myself to become a better programmer.


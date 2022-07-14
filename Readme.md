# Gallery-Crud-App-Django
A simple Gallery web-app made in Django with sqlite as an database. The web-app is responsive and mobile/device friendly

Deployed app link: https://gallery-crud-app-hackerearth.herokuapp.com/

----
## Tech stack

<div align="center">
<img alt="Django" src ="https://img.shields.io/badge/django-%2307405e.svg?style=for-the-badge&logo=django&logoColor=white"/>  <img src="https://img.shields.io/badge/-Python-2e3440?logoColor=white&logo=Python&style=for-the-badge&color=red" /> <img src="https://img.shields.io/badge/-HTML5-2e3440?logoColor=white&logo=html5&style=for-the-badge&color=green" /> <img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/> <img alt="SQLite" src ="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
</div>

----
## Features:
  1. <h2><b>Add new images to gallery:</b></h2> Images can be added to the Gallery by Entering Image name, Image url and Image detail.
  2. <h2><b>Edit images in Gallery:</b></h2> Images already present in the gallery can be edited to change their Image url and Image detail.
  3. <h2><b>Delete images from Gallery:</b></h2> Images can be deleted from the Gallery.
  4. <h2><b>Search images by name in Gallery:</b></h2> Images can be searched by Image name from the Navbar Search bar.
  5. <h2><b>View images in Gallery:</b></h2> Images can be viewed fully by its name, details and full resolution image.
  6. <h2><b>Pagination support for showing 9 images per page in Gallery:</b></h2> The layout is structured in such a way that it shows only 9 items per page and rest of the data on the next pages.

----
## Demo:

https://user-images.githubusercontent.com/66346161/178901009-d6c83885-1f02-4a66-942f-1ed4df9a79c0.mp4


----
## ScreenShots:
  Home page
  ![Screenshot (30)](https://user-images.githubusercontent.com/66346161/178901379-39c4b556-be4b-41eb-99a9-8d329a573d19.png)
  ![Screenshot (31)](https://user-images.githubusercontent.com/66346161/178901422-56f2b2f6-3162-46de-844a-5b1fed9140b4.png)

  Add Image
  ![Screenshot (33)](https://user-images.githubusercontent.com/66346161/178901559-89341a64-bdfb-425b-9b3d-9a053c51f772.png)

  View Image
  ![Screenshot (34)](https://user-images.githubusercontent.com/66346161/178901505-5f691458-06c3-46e1-8a28-59f3cde3f99e.png)

  Edit Image
  ![Screenshot (35)](https://user-images.githubusercontent.com/66346161/178901531-39ee4a1b-e521-491a-88e8-f07a99691608.png)

  Delete Image
  ![Screenshot (36)](https://user-images.githubusercontent.com/66346161/178901607-7fcd167c-49f0-43ca-8e35-024bf4797462.png)

  Search Image
  ![search](https://user-images.githubusercontent.com/66346161/178901683-e9e68c01-aa93-43f1-a1b5-11930c7b724e.png)
  ![Screenshot (37)](https://user-images.githubusercontent.com/66346161/178901702-469e976f-5836-4c5d-89d3-a5c15495db5b.png)
  
  ----
  ## Requirements
  - Python 3.10.2
  - Django  4.0.6
  - gunicorn  20.1.0
  - whitenoise  6.2.0
  
 ----
## Setting up
Navigate to the project directory
```terminal
cd Gallery
```
Setup a Virtual Environment and activate it
```terminal
virtualenv env
env\Scripts\activate
```
Install the dependencies from Requirements.txt file
```terminal
pip install -r requirements.txt
```
Run a Django development server
```terminal
python manage.py runserver
```

----
## Deployment
Deployments are managed via Heroku using Github. main branch is auto-deployed to https://gallery-crud-app-hackerearth.herokuapp.com/ after a git push

For Deploying the app on heroku
- Create your own git repository and push the project to it.
  ```terminal
  git init
  git add .
  git commit -m "creating repo"
  git remote add origin <your repository link>
  git branch -M main
  git push origin main

- Login to Heroku, Create an app and connect the github repo to it</br>
  ![heroku](https://user-images.githubusercontent.com/66346161/178904584-344c7ccc-7c52-4720-aa54-09e823ff42b0.png)
  
- Click on Auto Deploy and Deploy branch Main</br>
  Hurray!! The app will be deployed to the heroku url created by heroku and will be ready to use.
  

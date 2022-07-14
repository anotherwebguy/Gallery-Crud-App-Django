# Gallery-Crud-App-Django
A simple Gallery web-app made in Django with sqlite as an database. The web-app is responsive and mobile/device friendly

----
## Tech stack

<div align="center">
<img alt="Django" src ="https://img.shields.io/badge/django-%2307405e.svg?style=for-the-badge&logo=django&logoColor=white"/>  <img src="https://img.shields.io/badge/-Python-2e3440?logoColor=white&logo=Python&style=for-the-badge&color=red" /> <img src="https://img.shields.io/badge/-HTML5-2e3440?logoColor=white&logo=html5&style=for-the-badge&color=green" /> <img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/> <img alt="SQLite" src ="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
</div>

----
## Features:
  1. Add new images to gallery
  2. Edit images in Gallery
  3. Delete images from Gallery
  4. Search images by name in Gallery
  5. View images in Gallery
  6. Pagination support for showing 9 images per page in Gallery

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

  

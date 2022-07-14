Gallery-Crud-App-Django
- A simple Gallery web-app made in Django with sqlite as an database. The web-app is responsive and mobile/device friendly

Deployed app link: https://gallery-crud-app-hackerearth.herokuapp.com/

----------------------------------------------------------------------------------------------------------------------------------

Tech stack
- python
- Django
- Html
- Bootstrap
- sqlite

----------------------------------------------------------------------------------------------------------------------------------

Features
1. Add new images to gallery:
   Images can be added to the Gallery by Entering Image name, Image url and Image detail.
2. Edit images in Gallery:
   Images already present in the gallery can be edited to change their Image url and Image detail.
3. Delete images from Gallery:
   Images can be deleted from the Gallery.
4. Search images by name in Gallery:
   Images can be searched by Image name from the Navbar Search bar.
5. View images in Gallery:
   Images can be viewed fully by its name, details and full resolution image.
6. Pagination support for showing 9 images per page in Gallery:
   The layout is structured in such a way that it shows only 9 items per page and rest of the data on the next pages.

----------------------------------------------------------------------------------------------------------------------------------

Screenshots and demo video is available in the screenshots-video folder of the project

----------------------------------------------------------------------------------------------------------------------------------

Requirements: present in the Requirements.txt file 

----------------------------------------------------------------------------------------------------------------------------------

Setting up the project
 1. Navigate to the project directory
    $ cd Gallery

 2. Setup a Virtual Environment and activate it
    $ virtualenv env
    $ env\Scripts\activate

 3. Install the dependencies from Requirements.txt file
    $ pip install -r requirements.txt

 4. Run a Django development server
    $ python manage.py runserver

----------------------------------------------------------------------------------------------------------------------------------

Deployment
- Deployments are managed via Heroku using Github. main branch is auto-deployed to https://gallery-crud-app-hackerearth.herokuapp.com/ after a git push
- For Deploying the app on heroku

  1. Create your own git repository and push the project to it.
       $ git init
       $ git add .
       $ git commit -m "creating repo"
       $ git remote add origin <your repository link>
       $ git branch -M main
       $ git push origin main

  2. Login to Heroku, Create an app and connect the github repo to it

  3. Click on Auto Deploy and Deploy branch Main
       Hurray!! The app will be deployed to the heroku url created by heroku and will be ready to use.

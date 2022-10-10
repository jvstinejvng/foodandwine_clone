# Welcome to Bread & Butter!
 > Bread & Butter is a full-stack site inspired by the American magazine and website, Food & Wine. From creating to plating, share and discover recipes to a world of culinary enthusiasts and food lovers. All your recipes, all in one place.

## Live Link: [Bread & Butter!](hhttps://breadandbutter.herokuapp.com/)
###### [Inspired by Food & Wine](https://www.foodandwine.com/)
 
 
 
## **Wiki Links**
------------
### [• Database Schema](https://github.com/jvstinejvng/foodandwine_clone/wiki/Database-Schema) 
### [• Features](https://github.com/jvstinejvng/foodandwine_clone/wiki/Features) 
### [• Users Stories](https://github.com/jvstinejvng/foodandwine_clone/wiki/Users-Stories) 

## **Features**
------------
1. Sign up, log in & demo user 
2. Homepage
3. Listing detail page
4. Create and edit a listing 
5. All user's reviews
6. All user's listings
7. Create a review 

## **Technologies Used**
------------
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-100000?style=for-the-badge&logo=sql&logoColor=BA1212&labelColor=AD0000&color=A90000) 
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) 
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white) 
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) 
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) 
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)




## **Local Server Setup**
------------
1. Clone this repository:
```bash
git clone https://github.com/samanthaweglinski/Buzzer.git
```

2. Install backend dependencies:

```bash
pipenv install -r requirements.txt
```

3. Create a `.env` file based on the example with proper settings for development environment:
```
SECRET_KEY=INSERT_SECRET_KEY_HERE
DATABASE_URL=sqlite:///dev.db
```

4. Start pipenv, migrate database, seed database, and run Flask app:

```bash
pipenv shell
flask db upgrade
flask seed all
flask run
```

5. Install frontend dependencies:

```bash
cd react-app/
npm install
npm start
```

6. Navigate to [localhost:3000](http://localhost:3000)


> ### _Built by_ [_Justine Jang_](https://github.com/jvstinejvng)
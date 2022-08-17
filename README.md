
# AlexBlackeyedWeb

A Feature Rich Portfolio/Blog website made with Django and TailwindCSS in about 5 hours!


## Features

- Responsive Website Design With TailwindCSS.
- Ability to add new Projects via the Django Admin Panel.
- Ability to add new Posts on the blog via the Django Admin Panel.
- Flare System to sort not only Post on the Blog but Projects in the Projects section as well.


## Tech Stack

**Frontend:**
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

**Backend:**
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)



## Screenshots

![Main Page Screenshot](/screenshots/main.png)
![Projects Screenshot](/screenshots/projects.png)
![Blog Screenshot](/screenshots/blog.png)
![Blog Post Screenshot](/screenshots/post.png)





## Installation

Before Continuing with the Installation make sure you have both
#### Python,NodeJS
installed

```bash
  cd AlexBlackeyedWeb
  pip install -r requirements.txt
  npm i
```

    
### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`NPM_BIN_PATH`

#### Windows

ending in
    
    npm.cmd

#### Linux

ending in
    
    /npm
    
## Run Locally

Follow the previous steps and

```bash
  python manage.py runserver
```
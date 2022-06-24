# LUNAR

## What is LUNAR project?

LUNAR aims to be modern and powerful web application for [The Forgotten MMORPG Server](https://github.com/otland/forgottenserver). The most important feature is account management for the game run by this engine, however also
community things are included like: highscores, ticketing system(for the sake of quick support for the players) and more!


## TechStack
- Flask.
- SQLAlchemy ORM(the Flask extension) for the database handling.
- Flask-JWT-Extended for JWT based authentication.
- Flask-CORS for Cross-Origin Resource Sharing.
- Marshmallow for data validation.
- Pytest for unit testing and more.

[Full list of dependencies](https://github.com/damianpawlikowski/lunar/blob/main/requirements.txt)

## Authentication
Authentication is implemented within JWT. It saves HTTP-Only cookie in the client browser.
Refreshing is done implicit on the server side and everything is protected with Flask-WTF's
anty-CSRF implementation.


**NOTE**
This product is in the early stage of development and is not near ready for production.

Make sure to check out [Fronted API](https://github.com/damianpawlikowski/lunar-ui) of this project.


## SCREENSHOTS
![account](https://i.imgur.com/qhi5pR2.png)
![highscores](https://i.imgur.com/yEHDZ5T.png)
![tickets](https://i.imgur.com/LhVL5cj.png)

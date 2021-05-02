# Test assignment for Yalantis Python School
## Prerequisites
- python3.8
```
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
```
## Usage
Clone repo
```
git clone https://github.com/Voorhees2019/Yalantis-assignment.git
cd Yalantis-assignment
```
Install dependencies
```
pip install -r requirements.txt
```
For administration (http://127.0.0.1:8000/admin/) you may create a new superuser: `python manage.py createsuperuser` or use the existing one with the username 'admin' and password 'admin1234'. <br/>
Run the server
```
python manage.py runserver
```
## API
### Requirements
**Each enpoint must ends with a trailing slash except filters (http://127.0.0.1:8000/api/courses/ but http://127.0.0.1:8000/api/courses/?search=django3).** <br/>
To use POST / PUT / DELETE request methods you must have an account and must provide an authorization token.
To register an account you can make a POST request to http://127.0.0.1:8000/api/signup/ with the next body: {"username": "your_username_here", "password": "your_password_here"} and get your authorization token as a response.
If you already have an account you can get your authorization token by making a POST request to http://127.0.0.1:8000/api/login/ with the next body: {"username": "your_username_here", "password": "your_password_here"}.
### Endpoints
1. Get the course list (GET method) / create a new course (POST method): http://127.0.0.1:8000/api/courses/ <br/>
   You can filter data searching by course title or its starting or ending date (ISO 8601 format: YYYY-MM-DDTHH:MM:SS. mmmmmm) e.g. http://127.0.0.1:8000/api/courses/?search=docker <br/>
   To order response data by some field you can use ordering parameter. For example, to order courses by ending date http://127.0.0.1:8000/api/courses/?ordering=end_date <br/>
   You also may be interested in reversed orderings. You can do this by prefixing the field name with '-', like so: http://127.0.0.1:8000/api/courses/?ordering=-end_date <br/>
   To create a new course you have to specify a header name "Authorization" with a header value "Token your_token_here".
2. Get (GET method) / update (PUT method) / delete (DELETE method) a certain course by its id: http://127.0.0.1:8000/api/courses/{id}/ <br/>
   Update and delete a course can only the author of that course.
   In order to update or delete a specific course you have to provide a header name "Authorization" with a header value "Token your_token_here".

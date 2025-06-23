 Late Show API
A RESTful API for managing a Late Night TV Show system built with Flask, PostgreSQL, and JWT authentication.



Setup Instructions
1. Clone the Repo

git clone https://github.com/EDEL-WEB/late-show-api-challenge.git
cd late-show-api-challenge
2. Install Dependencies
pipenv install
3. Set Up PostgreSQL Database
Create a PostgreSQL database
psql
CREATE DATABASE late_show_db;
4. Set Environment Variables
Create a .env file in the root directory with the followin
FLASK_APP=server.app
FLASK_ENV=development
DATABASE_URI=postgresql://postgres:edel2025@localhost:5432/late_show_db
SECRET_KEY=your_jwt_secret_key

 How to Run the App
1. Activate Environment
pipenv shell
2. Run Migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
3. Seed the Database (Optional)

flask seed
4. Start the Server
bash
Copy
Edit
flask run
Authentication (Register, Login, Token)
Register

POST /auth/register
Body:
{
  "username": "testuser",
  "password": "test123"
}
 Login (Get Token)

POST /auth/login
Body:
{
  "username": "testuser",
  "password": "test123"
}
Response:
{
  "access_token": "your.jwt.token"
}
Use Token (Protected Routes)
Option A – Postman Authorization Tab:

Type: Bearer Token

Token: your.jwt.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MDY2NzA0OSwianRpIjoiMjhmYzAyOGMtZDVkOS00YTBjLWFhNzItNWEwNGIxNjE3NDRlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNzUwNjY3MDQ5LCJjc3JmIjoiZjc4NTM1MDYtNmViNS00OWY1LWEzYTgtN2M0Y2RhZmRlZjdjIiwiZXhwIjoxNzUwNjY3OTQ5fQ.2pu_lLYF9JETn6j06m2OCCm7bLNHIiOtPLVJ_7UyzLQ

Option B – Header:

makefile

Authorization: Bearer your.jwt.token
Authorization: Bearer your.jwt.token
 API Routes
Method	Endpoint	Description
GET	/shows	Get all shows
GET	/shows/<id>	Get a single show
POST	/shows	Create a show (auth)
PATCH	/shows/<id>	Update show (auth)
DELETE	/shows/<id>	Delete show (auth)
GET	/hosts	List all hosts
POST	/hosts	Create host (auth)
GET	/auth/register	Register new user
POST	/auth/login	Login and get token

Sample Request & Response
Create a Show
http
POST /shows
Headers:
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Late Night Chat",
  "host_id": 1,
  "air_time": "22:00"
}
Response:

j
{
  "id": 1,
  "title": "Late Night Chat",
  "host_id": 1,
  "air_time": "22:00"
}

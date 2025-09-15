# Polygon Area API

## 📌 Description
The Polygon Area API is a simple Flask-based API that calculates the area of regular polygons with 3 to 10 sides (triangle up to decagon).  
It accepts either query parameters (GET)  or JSON data (POST) and returns the result in JSON format.

This project was built as part of our API development requirement and demonstrates how to build and consume a custom API.

 🚀 Features
- Calculate area of regular polygons (triangle → decagon).
- Supports both **GET** and **POST** requests.
- Returns clean **JSON** responses.
- Easy to extend for more polygons or additional geometry functions.

- 
- 🛠️ INSTALLATION AND SETUP

 1. Clone the Repository
``bash
git clone https://github.com/<your-group-username>/polygon-area-api.git
cd polygon-area-api
2. Install Dependencies

Make sure you have Python 3 installed, then run:
3. Run the API

python polygon_api.py
The server will start at:
http://127.0.0.1:5000


EXAMPLE OF GET AND POST

1. GET /area

Calculate area using query parameters.

Request:

GET http://127.0.0.1:5000/area?sides=6&length=4

2. POST /area

Calculate area by sending JSON data.

Request:

POST http://127.0.0.1:5000/area
Content-Type: application/json


Body:

{
  "sides": 8,
  "length": 5
}

# Flask Product API

A simple REST API built using **Flask, SQLite, and Flask-SQLAlchemy** to perform CRUD operations on products.

## Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Postman

## Features

* Create a product
* Get all products
* Get a product by ID
* Update a product
* Delete a product
* Basic input validation
* 404 error handling

## Project Structure

```text
flask-learning/
│
├── app.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
│
└── instance/
    └── products.db
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint         | Description      |
| ------ | ---------------- | ---------------- |
| GET    | `/products`      | Get all products |
| GET    | `/products/<id>` | Get one product  |
| POST   | `/products`      | Create a product |
| PUT    | `/products/<id>` | Update a product |
| DELETE | `/products/<id>` | Delete a product |

## Example — Create Product

**POST `/products`**

```json
{
    "id": 1,
    "name": "Laptop",
    "price": 50000
}
```

## Example — Update Product

**PUT `/products/1`**

```json
{
    "name": "Gaming Laptop",
    "price": 65000
}
```

You can also update only one field:

```json
{
    "name": "Gaming Laptop"
}
```

## Database

The project uses **SQLite** as the database and **Flask-SQLAlchemy** to interact with it.

# FastAPI
# FastAPI Product API

A simple REST API built using **FastAPI** that reads product data from a JSON file and provides endpoints to retrieve and search products.

---

## 🚀 Features   

* FastAPI based REST API
* Read product data from JSON file
* Search products by name
* Clean project structure
* Interactive API documentation (Swagger UI)

---

## 📂 Project Structure

```
app/
│
├── main.py
│
├── service/
│     └── products.py
│
├── data/
│     └── products.json
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/fastapi-product-api.git
cd fastapi-product-api
```

Create virtual environment (pyenv example):

```
pyenv virtualenv 3.10.12 fastapi_env
pyenv local fastapi_env
```

Install dependencies:

```
pip install fastapi uvicorn
```

---

---

## 📖 API Documentation

FastAPI automatically generates API docs.


## 📌 API Endpoints

### Home

```
GET /
```

Response:

```
{
 "message": "Welcome to FastAPI"
}
```

---

### Get Products

```
GET /products
```

Optional Query Parameter:

```
/products?name=iphone
```

Description: Search product by name.

---

## 🧑‍💻 Tech Stack

* Python
* FastAPI
* Uvicorn
* JSON

---

## 📜 License

This project is open-source and available for learning purposes.


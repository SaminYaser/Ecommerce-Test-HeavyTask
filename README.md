# HEAVYTASK Ecommerce Test
[![Generic badge](https://img.shields.io/badge/Status-Finished-<Green>.svg)](https://shields.io/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

E-Commerce API endpoints created by Samin Yaser for HeavyTask recruitment test. 

## Requirements
* [Python](https://docs.python.org/3/)
* [Django](https://docs.djangoproject.com/en/3.1/)
* [djangorestframework](https://www.django-rest-framework.org/topics/documenting-your-api/)
* [PostgreSQL](https://www.postgresql.org/docs/13/index.html)

## Usage

### Installation Process

Installing python3
```bash
sudo apt get install python3
```
Installing Django
```bash
pip3 install Django==3.1.4
```
Installing djangorestframework
```bash
pip3 install djangorestframework
```
[Installing PostgreSQL](https://www.howtoforge.com/tutorial/how-to-install-django-with-postgresql-and-nginx-on-ubuntu-16-04/)


### Running the server

Enter the Django directory and run the following command.

```bash
python3 manage.py runserver
```

## API Reference
### Products

* **URL**:
 /products/

* **Method**:
`GET` `POST`

* **URL**:
 /products/:id

* **Method**:
`GET` `PUT` `PATCH` `DELETE`

### Customers

* **URL**:
 /customers/

* **Method**:
`GET` `POST`

* **URL**:
 /customers/:id

* **Method**:
`GET` `PUT` `PATCH` `DELETE`

### Order

* **URL**:
 /orders/

* **Method**:
`GET` `POST`

* **URL**:
 /orders/:id

* **Method**:
`GET` `PUT` `PATCH` `DELETE`


## Status Codes

API returns the following status codes:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 204 | `NO CONTENT` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

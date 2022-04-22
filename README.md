# Price Breeze

## Introduction

Price Breeze is a web application designed to make trips to the grocery store more convenient. After making an account, users can search for products on the web, sort those products according to price, location, or product name, and add items to their shopping list.

## Features
1. Account Management
   - Create account
   - Reset password
2. Search within platform
   - Web search
3. Sort products
   - Sort by factors such as price and product name
4. Construct a Shopping List
   - Add item to shopping list


## Getting Started
### Installation and Setup
1. Install Python (https://www.python.org/downloads/)
2. Libraries required:
   - django

   ```console
   pip install django
   ```

   - django crispy forms

   ```console
   pip install django-crispy-forms
   ```

   - requests_html

   ```console
   pip install requests_html
   ```

   * pandas

   ```console
   pip install pandas
   ```

   * bs4

   ```console
   pip install bs4
   ```

### Run

#### Running the Server

1. Navigate to the project's root directory in a terminal.
2. Run the following command to run the server:
```python
python manage.py runserver
```
3. Open the web page with the URL listed.

#### Admin Page
1. Run the server.
2. Navigate to the admin URL With default settings, the admin URL will be as follows:  
<http://127.0.0.1:8000/admin/>
3. Log in with the pre-existing admin credentials:
   - Username: superuser
   - Password: root  
4. Alternatively, create your own admin account with the following command:
```console
python manage.py createsuperuser
```

## Demo video

https://youtu.be/F9NhHCBetWE

## Contributors

* Elise Ducharme (ducharmee@wit.edu), account managemet
* Sarah Mahmoud (mahmouds@wit.edu), search and web scraping
* Kevin Mortimer (mortimerk1@wit.edu), database and shopping list
* Calvin Vuong (vuongc@wit.edu), results page and sorting options

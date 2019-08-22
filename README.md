# Adjust-task
This is a task done according to specifications sent by adjust.com using python3, django and psql.

- Pyhton version : 3.7.4

## To Run the application follow these steps

- First make sure you have pip installed
- Second clone the project any where to your pc

```bash
git clone https://github.com/bassemmagdy/Adjust.git
```

- Then cd to the directory

```bash
cd Adjust-task
```

- Rename .env.Example and modify it according to your database configurations

- Run the next commands to initialize and start your venv

```bash
virtualenv --python=python3 task-env
source task-env/bin/activate
```

- Next step after configuring your virtualenv and your db settings, you'll have to install requirements and migrate your database to start playing around with the API.

```bash
pip install -r requirements.txt
python manage.py migrate
```

- We are there!

```bash
python manage.py runserver
```

- first of all you will have to expose the api to fill your database via executing this Api call:

```bash
http://127.0.0.1:8000/api/get_data/
```

- After that start using the api with whatever paramas to get your data back on your side:


## The available API routes are:

- GET /api/get_data/ Returns data from csv and store it in psql database

- GET /api/performance/ This is a generic api that returns data based on your filteration methodology


## Use Cases

- For showing the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order we can use this:

```bash
http://127.0.0.1:8000/api/performance/?date=2017-06-01&grouping_by=channel, country&order_by_clicks=desc
```

- For showing the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

```bash
http://127.0.0.1:8000/api/performance/?start_date=2017-05-01&end_date=2017-05-31&grouping_by=date&order_by_date=asc
```

- For showing revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

```bash
http://127.0.0.1:8000/api/performance/?date=2017-06-01&grouping_by=os&order_by_revenue=desc
```

- For showing CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.

```bash
http://127.0.0.1:8000/api/performance/?country=ca&grouping_by=channel, cpi&order_by_cpi=desc
```

## Postman Collection

- https://www.getpostman.com/collections/81c60939078c82d5f819
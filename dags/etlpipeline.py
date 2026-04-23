from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.sdk import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import json

## Define DAG

with DAG(
    dag_id = 'nasa_apod_postgres',
    start_date = datetime(2026, 4, 21),
    schedule = '@daily',
    catchup = False

) as dag: 
    ## Step 1 : Create the table if it doesn't FileExistsError

    @task
    def create_table():
        ## Initialize the PostgresHook
        postgres_hook = PostgresHook(postgres_conn_id = "my_postgres_connection")

        ## SQL query to create the table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS apod_data(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
        );
        """
        postgres_hook.run(create_table_query)


    ## Step 2: Extract the NASA API Data (APOD) -Astronomy Picture of the Day [Extract Pipeline]
    ## https://api.nasa.gov/planetary/apod?api_key=y1j5XLsNp9JPYvka8Mgqnp6tVE0XV07qeBOkha8T
    extract_apod = HttpOperator(
        task_id = 'extract_apod',
        http_conn_id = 'nasa_api',
        endpoint = 'planetary/apod',            ## Connection ID defined in Aiflow for NASA API
        method = 'GET',                         ## NASA API endpoint for APOD
        data = {"api_key": "{{ conn.nasa_api.extra_dejson.api_key}}"},          ## Use the API key from the connection 
        response_filter = lambda response: response.json()  ## convert response to json
    )


    ## Step 3: Transform the data(Pick the information that i need to save)
    @task
    def transform_apod_data(response):
        apod_data={
            'title': response.get('title',''),
            'explanation': response.get('explanation',''),
            'url':response.get('url',''),
            'date': response.get('date',''),
            'media_type': response.get('media_type','')
        }
        return apod_data

    ## Step 4: Load the data into the Postgres SQL
    @task
    def load_data_to_postgres(apod_data):
        ## Initialize the PostgresHook
        postgres_hook = PostgresHook(postgres_conn_id = 'my_postgres_connection')

        ##Define the SQL Insert query
        insert_query = """
        INSERT INTO apod_data (title, explanation, url, date, media_type)
        VALUES(%s, %s, %s, %s, %s);
        """

        ## Execute the PostgresHook
        postgres_hook.run(insert_query, parameters = (
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type']
        ))


    ## Step 5: Verify the Data DBViewer




    ## Step 6: Define the task dependencies
    ## Extract
    create_table() >> extract_apod ## Ensure table is created before extraction
    api_response = extract_apod.output

    ## Transform
    transform_data = transform_apod_data(api_response)

    ## Load 
    load_data_to_postgres(transform_data)




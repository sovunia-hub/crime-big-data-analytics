import time
import pymysql
from pyspark.sql import SparkSession
from pyspark.sql import Row

db_config = {
  'host': 'localhost',
  'user': 'student',
  'password': 'student',
  'database': 'crimes'
}

Spark = SparkSession.builder.appName('MariaDBToSpark').getOrCreate()
def fetch_data():
  try:
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    query = """
    SELECT * FROM crimes_data
    WHERE RAND() < 0.001
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows
  
  except Exception as e:
    print(f"Error: {e}")
    return []

def save_to_csv(data):
  if data:
    rows = [Row(*row) for row in data]
    df = spark.createDataFrame(rows)
    output_path = '/home/student/spool/crime_data.csv'
    df.write.option('header', 'true').mode('append').csv('file:/home/student/spool')
    print("Data written to CSV successfully.")
  else:
    print("No data to write.")

def main() :
  while True:
    data = fetch_data()
    save_to_csv(data)
    time.sleep(10)

if __name__ == '__main__':
  main()

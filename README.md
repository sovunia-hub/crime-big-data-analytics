# Crime Analytics

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![MariaDB](https://img.shields.io/badge/MariaDB-10.5+-blue)
![Apache Hive](https://img.shields.io/badge/Apache%20Hive-3.1+-yellow)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-2.8+-orange)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.0+-red)

## Overview
Crime Analytics is a project aimed at analyzing crime data in Los Angeles from 2020 onwards. The project utilizes statistical methods and data analysis techniques to identify trends, high-risk groups, and the effectiveness of law enforcement agencies.

## Features
- **Data Pipeline Creation**: Collecting and processing crime data using MariaDB, Apache Hive, and Apache Kafka.
- **Data Analysis**: Examining crime trends, victim demographics, and crime locations.
- **Visualization**: Generating interactive charts and graphs to illustrate crime patterns.
- **Crime Prediction**: Utilizing machine learning models to predict crime hotspots.

## Technologies Used
![image](https://github.com/user-attachments/assets/54c83094-d9b0-4a4a-93cd-b6ca3a744df3)
- **Programming Language**: Python
- **Data Storage**: MariaDB, Apache Hive, HDFS
- **Data Processing**: Apache Spark, PySpark
- **Data Streaming**: Apache Kafka, Apache Flume
- **Visualization**: Plotly, Matplotlib, Seaborn

## Data Sources
The dataset consists of crime reports from the Los Angeles Police Department (LAPD), including:
- Crime type
- Date and time of occurrence
- Victim details (age, gender, descent)
- Crime location (latitude, longitude)
- Status of the case

## Workflow Steps
1. **Data Collection & Storage**:
   - Extract crime data from LAPD reports.
   - Store raw data in HDFS for processing.
   - Load data into MariaDB:
     ```sql
     MariaDB [crimes]> create table crime_data (
        DR No varchar(100),
        Date Rptd varchar(100),
        Date_Occ varchar(100),
        Time_Occ varchar(100),
        Area varchar(100),
        Area_Name varchar(100),
        Rpt_Dist No varchar(100),
        Part varchar(100),
        Crm_Cd varchar(100),
        Crm_Cd_Desc varchar(100),
        Mocodes varchar(100),
        Vict Age varchar(100),
        Vict_Sex varchar(100),
        Vict_Descent varchar(100),
        Premis_Cd varchar(100),
        Premis_Desc varchar(100),
        Weapon_Used_Cd varchar(100),
        Weapon_Desc varchar(100),
        Status varchar(100),
        Status_Desc varchar(100),
        Crm_Cd_1 varchar(100),
        Crm_Cd_2 varchar(100),
        Crm_Cd_3 varchar(100),
        Crm_Cd_4 varchar(100),
        Location varchar(100),
        Cross_Street varchar(100),
        Lat varchar(100),
        Lon varchar(100)
     );
     ```
     
2. **Data Transfer to Spool**:
   - Import data from MariaDB to Spool with [python file](https://github.com/sovunia-hub/crime-big-data-analytics/blob/main/mariadb_to_spool.py):
     ```bash
     mariadb_to_spool.py
     ```
     
3. **Data Transfer with Apache Sqoop**:
   - Import data from MariaDB to HDFS:
     ```bash
     sqoop export \
        --connect jdbc:mysql://localhost/crimes \
        --username student \
        --password student \
        --export-dir /user/student/lab_data \
        --table crime_data \
        --fields-terminated-by ';'
     ```

4. **Real-Time Data Streaming with Apache Kafka & Flume**:
   - Start a Kafka topic:
     ```bash
     kafka-topics --create \
        --bootstrap-server localhost:9092 \
        --replication-factor 1 \
        --partitions 1 \
        --topic crime_topic
     ```
   - Configure Flume agent to stream data:
     ```properties
     agent1.sources = srcl
     agent1.channels = ch1 ch2
     agent1.sinks = sink1 sink2
      
     agent1.sources.srcl.type = spooldir
     agent1.sources.srcl.spoolDir = /home/student/spool
      
     agent1.channels.ch1.type = memory
     agent1.channels.ch1.capacity = 10000
     agent1.channels.ch1.transactionCapacity = 100
      
     agent1.channels.ch2.type = memory
     agent1.channels.ch2.capacity = 10000
     agent1.channels.ch2.transactionCapacity = 100
      
     agent1.sinks.sink1.type = org.apache.flume.sink.kafka.KafkaSink
     agent1.sinks.sink1.kafka.bootstrap.servers = localhost:9092
     agent1.sinks.sinkl.kafka.topic = crime_topic
     agent1.sinks.sinkl.kafka.flumeBatchSize = 5
     agent1.sinks.sink1.channel = ch1
      
     agent1.sinks.sink2.type = logger
     agent1.sinks.sink2.channel = ch2
      
     agent1.sources.srcl.channels = ch1 ch2
     ```

5. **Data Transfer to Hive**:
   - Import data from MariaDB to Hive:
     ```bash
     sqoop import -Dorg.apache.sqoop.splitter.allow_text_splitter=true \
        --connect jdbc:mysql://localhost:3306/crimes \
        --username student \
        --password student \
        --table crimes_data \
        --hive-import \
        --hive-table hive_crimes
     ```

## Usage
- Run the data pipeline to collect and store crime data.
- Use Jupyter Notebook or scripts to analyze crime trends.
- Generate visualizations to interpret findings.

## Results
- Identification of high-crime areas in Los Angeles.
- Demographic analysis of victims.
- Evaluation of crime resolution rates by law enforcement.
- Time-based crime trends for improved law enforcement planning.

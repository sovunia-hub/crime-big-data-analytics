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

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/crime-analytics.git
   cd crime-analytics
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up databases and data pipeline using the provided SQL and configuration files.

## Usage
- Run the data pipeline to collect and store crime data.
- Use Jupyter Notebook or scripts to analyze crime trends.
- Generate visualizations to interpret findings.

## Results
- Identification of high-crime areas in Los Angeles.
- Demographic analysis of victims.
- Evaluation of crime resolution rates by law enforcement.
- Time-based crime trends for improved law enforcement planning.

## Future Work
- Implementing predictive analytics for crime forecasting.
- Expanding the dataset with additional crime records.
- Enhancing visualization with geospatial mapping.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

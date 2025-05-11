# AWS ETL IMDb Project 🎬

This project is a fully serverless ETL pipeline built with **AWS Lambda**, **S3**, **Athena**, and **Python (Pandas)**. It extracts and cleans raw IMDb movie data and makes it queryable using SQL via Amazon Athena.

---

## 🧠 Objective

Create a cloud-native ETL pipeline that:
- Cleans a raw CSV dataset from IMDb
- Removes duplicates and irrelevant rows
- Outputs a cleaned CSV file to S3
- Enables SQL querying through AWS Athena

---

## 🛠️ Tools & Technologies

- **AWS Lambda** – Python-based serverless compute
- **AWS S3** – Storage for both raw and cleaned data
- **AWS Athena** – SQL querying on S3 data using Glue catalog
- **AWS IAM** – Secure permissions between services
- **Python** – Data cleaning with Pandas
- **Boto3** – AWS SDK for Python

---

## 📊 Dataset Info

- Original: Raw IMDb movie dataset (CSV)
- Final Cleaned Output: **872 rows**
- Stored in: `s3://your-bucket-name/cleaned_imdb_data.csv`

---

## 🧪 Sample Athena Query

```sql
SELECT genre, COUNT(*) AS movie_count
FROM imdb_movies_cleaned
GROUP BY genre
ORDER BY movie_count DESC;
```



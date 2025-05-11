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

---

## 📸 Step-by-Step Deployment (with Screenshots)

This section walks through the entire deployment process from Lambda setup to Athena queries, with visual proof at each step.

### 1. Uploading Raw IMDb CSV to S3
_Screenshot: s3_raw_csv_upload.png_

Explain: The raw CSV file was uploaded to an S3 bucket named `your-bucket-name`.

### 2. Lambda Function Setup
_Screenshot: lambda_config.png_

Explain: Python function set up to clean the data, connected to S3 via IAM roles.

### 3. Lambda Test Output
_Screenshot: lambda_success.png_

Explain: A test event triggered the function, returning a `status: success` with `872 rows`.

### 4. Cleaned CSV in S3
_Screenshot: s3_cleaned_csv.png_

Explain: The cleaned CSV is saved back into the S3 bucket.

### 5. Athena Table Setup
_Screenshot: glue_catalog_table.png_

Explain: AWS Glue crawler created a table to query the cleaned CSV.

### 6. Querying in Athena
_Screenshot: athena_query_results.png_

Explain: Successfully ran a SQL query to analyze genre distribution.

### 7. (Optional) Architecture Diagram
_Screenshot: architecture_diagram.png_

Explain: Diagram showing Lambda → S3 → Athena → SQL

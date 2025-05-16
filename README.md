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

## 📸 Step-by-Step Deployment (with Screenshots)

This section walks through the entire deployment process from Lambda setup to Athena queries — including a few key troubleshooting notes from the build.

---

## ☁️ Services Used

| Service         | Purpose                                |
|------------------|----------------------------------------|
| AWS Lambda       | Python ETL logic                       |
| AWS S3           | Store raw and cleaned CSV files        |
| AWS Athena       | Query cleaned data with SQL            |
| AWS IAM          | Control access between Lambda/S3       |
| AWS Glue         | Crawl S3 to generate Athena schema     |
| AWS CloudWatch   | View Lambda logs                       |

---

<img src="https://github.com/user-attachments/assets/00b6da5c-c56c-4961-8095-3fdd4871f827" alt="aws-etl-thumbnail" width="600"/>

---

### 1. Uploading Raw IMDb CSV to S3

<img src="https://github.com/user-attachments/assets/1d94e6fb-1c9a-4cd3-a8e1-2cf81639aee5" alt="S3 Bucket Upload" height="600"/>

**Explanation:**  
The raw IMDb CSV file was uploaded to an S3 bucket created specifically for this project.

---

### 2. Lambda Function Setup

<img src="https://github.com/user-attachments/assets/79ba76c8-6a8e-482d-9989-d27a5e2ffe5e" alt="Lambda Test Output" height="600"/>

**Explanation:**  
A Python Lambda function was created to clean and transform the data using pandas. It was connected to the S3 bucket via an IAM execution role.

**🛠️ Troubleshooting:**  
The function failed on the first few tests because I didn’t include pandas in the deployment package. I zipped up a local version of the code with dependencies and re-uploaded the deployment package manually.

---

### 3. Lambda Test Output

<img src="https://github.com/user-attachments/assets/a0e335d9-18c3-4cff-b079-c7c8aca66111" alt="Lambda Config" height="600"/>

**Explanation:**  
After fixing the packaging issue, the Lambda returned a success message, indicating 872 rows had been cleaned and processed.

---

### 4. Cleaned CSV in S3

<img src="https://github.com/user-attachments/assets/34e7f613-14d8-46ec-aab6-b2a7971990bd" alt="Cleaned CSV in S3" height="600"/>

**Explanation:**  
The cleaned CSV was saved to a separate prefix in the same S3 bucket. This was used as input for the next phase of the pipeline.

---

### 5. Glue Crawler Setup

<img src="https://github.com/user-attachments/assets/a01f1d5c-b4a9-4504-9e9b-799e95233f63" alt="Glue Catalog Table" height="600"/>

**Explanation:**  
An AWS Glue crawler was set up to scan only the cleaned-data folder. It inferred the schema and registered a table in the Glue Data Catalog.

**🛠️ Troubleshooting:**  
The first crawler was pointed at the whole bucket, which picked up unwanted files. Restricting the crawler to just the cleaned-data path solved this.

---

### 6. Athena Table Setup

<img src="https://github.com/user-attachments/assets/098a9aa6-867a-4a8d-8d48-1b87989e417d" alt="Athena Query Results" height="600"/>

**Explanation:**  
The Glue-generated table was now available in Athena. I verified it by checking schema and sample results from the table preview.

---

### 7. Querying in Athena

<img src="https://github.com/user-attachments/assets/569ab66f-1209-4c5b-999a-6fdff36beb44" alt="ETL Architecture Diagram" height="600"/>

**Explanation:**  
Ran SQL queries to explore genre distribution and other fields. The Athena queries validated that the ETL process produced clean, usable data.

**🛠️ Troubleshooting:**  
At one point, I hit a few Athena query errors (like HIVE_UNKNOWN_ERROR) due to mismatched or missing headers in the cleaned CSV. I fixed the header alignment in the Lambda code and the issue went away.

---





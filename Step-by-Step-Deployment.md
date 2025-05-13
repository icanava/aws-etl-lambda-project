## 📸 Step-by-Step Deployment (with Screenshots)

This section walks through the entire deployment process from Lambda setup to Athena queries, with visual proof at each step.
## ☁️ Services Used

| Service     | Purpose                              
|-------------|---------------------------------------|
| AWS Lambda  | Python ETL logic                      |
| AWS S3      | Store raw and cleaned CSV files       | 
| AWS Athena  | Query cleaned data with SQL           | 
| AWS IAM     | Control access between Lambda/S3      | 
| AWS Glue    | Crawl S3 to generate Athena schema     | 
| AWS CloudWatch | View Lambda logs                   | 


<img src="https://github.com/user-attachments/assets/00b6da5c-c56c-4961-8095-3fdd4871f827" alt="aws-etl-thumbnail" width="600"/>


### 1. Uploading Raw IMDb CSV to S3

<img src="https://github.com/user-attachments/assets/1d94e6fb-1c9a-4cd3-a8e1-2cf81639aee5" alt="S3 Bucket Upload" height="600"/>

**Explanation:** The raw CSV file was uploaded to an S3 bucket named `my-etl-movie-bucket`.

---

### 2. Lambda Function Setup

<img src="https://github.com/user-attachments/assets/79ba76c8-6a8e-482d-9989-d27a5e2ffe5e" alt="Lambda Test Output" height="600"/>


**Explanation:** Python function set up to clean the data, connected to S3 via IAM roles.

---

### 3. Lambda Test Output
<img src="https://github.com/user-attachments/assets/a0e335d9-18c3-4cff-b079-c7c8aca66111" alt="Lambda Config" height="600"/>

**Explanation:** A test event triggered the function, returning a `status: success` with `872 rows`.

---

### 4. Cleaned CSV in S3
<img src="https://github.com/user-attachments/assets/34e7f613-14d8-46ec-aab6-b2a7971990bd" alt="Cleaned CSV in S3" height="600"/>


**Explanation:** The cleaned CSV is saved back into the S3 bucket.

---

### 6. Glue Crawler Setup
<img src="https://github.com/user-attachments/assets/a01f1d5c-b4a9-4504-9e9b-799e95233f63" alt="Glue Catalog Table" height="600"/>



**Explanation:** An AWS Glue Crawler was configured to scan the cleaned-data/ S3 path. The crawler automatically inferred schema details and created a table in the AWS Glue Data Catalog.

---

### 6. Athena Table Setup
<img src="https://github.com/user-attachments/assets/098a9aa6-867a-4a8d-8d48-1b87989e417d" alt="Athena Query Results" height="600"/>

**Explanation:** AWS Glue crawler created a table to query the cleaned CSV.

---

### 7. Querying in Athena
<img src="https://github.com/user-attachments/assets/569ab66f-1209-4c5b-999a-6fdff36beb44" alt="ETL Architecture Diagram" height="600"/>

**Explanation:** Successfully ran a SQL query to analyze genre distribution.

---



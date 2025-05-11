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

![image](https://github.com/user-attachments/assets/a265380e-a8b5-4005-b7db-44b7e6a6d79b)

### 1. Uploading Raw IMDb CSV to S3
_Screenshot: s3_raw_csv_upload.png_

**Explanation:** The raw CSV file was uploaded to an S3 bucket named `your-bucket-name`.

---

### 2. Lambda Function Setup
_Screenshot: lambda_config.png_

**Explanation:** Python function set up to clean the data, connected to S3 via IAM roles.

---

### 3. Lambda Test Output
_Screenshot: lambda_success.png_

**Explanation:** A test event triggered the function, returning a `status: success` with `872 rows`.

---

### 4. Cleaned CSV in S3
_Screenshot: s3_cleaned_csv.png_

**Explanation:** The cleaned CSV is saved back into the S3 bucket.

---

### 5. Athena Table Setup
_Screenshot: glue_catalog_table.png_

**Explanation:** AWS Glue crawler created a table to query the cleaned CSV.

---

### 6. Querying in Athena
_Screenshot: athena_query_results.png_

**Explanation:** Successfully ran a SQL query to analyze genre distribution.

---

### 7. (Optional) Architecture Diagram
_Screenshot: architecture_diagram.png_

**Explanation:** Diagram showing Lambda → S3 → Athena → SQL

import pandas as pd
import boto3

# Step 1: Extract
df = pd.read_csv("imdb_movies.csv")

# Step 2: Transform
df["Revenue (Millions)"] = df["Revenue (Millions)"].replace(["", "N/A", " ", "NA"], pd.NA)
df_cleaned = df.dropna(subset=["Revenue (Millions)"])
df_cleaned.loc[:, "Revenue (Millions)"] = df_cleaned["Revenue (Millions)"].astype(float)

# Step 3: Load (Save locally)
df_cleaned.to_csv("cleaned_imdb_movies_fixed.csv", index=False, encoding="utf-8")

# Print to verify cleaning
print(f"Original row count: {len(df)}")
print(f"Cleaned row count: {len(df_cleaned)}")
print("Top 5 rows of cleaned data:")
print(df_cleaned.head())

# Step 4: Upload to S3
s3 = boto3.client("s3")
bucket_name = "my-etl-movie-bucket"  # <-- replace with your actual bucket name
file_name = "cleaned_imdb_movies.csv"
s3_key = "cleaned_imdb_movies.csv"

s3.upload_file(file_name, bucket_name, s3_key)
print(f"✅ Uploaded {file_name} to s3://{bucket_name}/{s3_key}")

# Export as comma-delimited CSV (not tab-delimited)
df_cleaned.to_csv("final_upload_ready.csv", index=False, encoding="utf-8", sep=",")


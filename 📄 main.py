from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load_local import save_locally
from scripts.load_s3 import upload_to_s3

def run_pipeline():
    print("🚀 Starting ETL Pipeline...")

    df = extract_data()
    df = transform_data(df)

    save_locally(df)
    upload_to_s3(df)

    print("✅ Pipeline Completed Successfully")

if __name__ == "__main__":
    run_pipeline()

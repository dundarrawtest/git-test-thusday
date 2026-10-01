# Main ETL Pipeline - Core System

def extract():
    print("Extracting data from Azure Blob Storage [MAIN BRANCH]...")

if __name__ == "__main__":
    extract()

# Main ETL Pipeline

def extract():
    print("Extracting data from S3...")

def transform(data):
    print("Transforming raw data...")
    return data

if __name__ == "__main__":
    raw_data = extract()
    transform(raw_data)

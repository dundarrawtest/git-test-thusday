# Main ETL Pipeline - Core System

def extract():
    print("Extracting data from Azure Blob Storage [MAIN BRANCH]...")

def transform(data):
    print("Transforming raw data...")
    return data

def load(data):
    print("Loading transformed data to Postgres DW...")

if __name__ == "__main__":
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)

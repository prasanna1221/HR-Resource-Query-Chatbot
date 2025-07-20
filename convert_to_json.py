import os
import pandas as pd
import json
from pathlib import Path

def convert_to_json(file_path):
    ext = Path(file_path).suffix.lower()
    filename = Path(file_path).stem
    output_path = f"data/{filename}.json"

    if ext == ".csv":
        df = pd.read_csv(file_path)
    elif ext == ".xlsx":
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Only .csv or .xlsx files are supported")

    df.to_json(output_path, orient="records", indent=2)
    print(f"✅ Converted to: {output_path}")




convert_to_json("employees.csv")

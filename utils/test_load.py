import os
import pandas as pd
from utils.load import save_to_csv

def test_save_to_csv(tmp_path):
    data = [
        {'Title': 'Test', 'Price': 10000, 'Rating': 4.0, 'Colors': 2,
         'Size': 'L', 'Gender': 'Male', 'Timestamp': '2024-01-01T00:00:00'}
    ]
    file_path = tmp_path / "test_products.csv"
    save_to_csv(data, filename=str(file_path))

    assert file_path.exists()

    df = pd.read_csv(file_path)
    assert len(df) == 1
    assert df.iloc[0]['Title'] == 'Test'

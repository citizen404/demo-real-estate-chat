import pandas as pd

def load_properties(path):
    df = pd.read_csv(path)
    docs = []
    for _, row in df.iterrows():
        text = f"""
Property: {row['title']}
Location: {row['location']}
Price: {row['price']}
Bedrooms: {row['bedrooms']}
Description: {row['description']}
"""
        docs.append(text)
    return docs


def load_areas(path):
    with open(path, "r") as f:
        return f.read()
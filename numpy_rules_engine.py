#!/usr/bin/env python
# coding: utf-8

# In[6]:


csv_content = """transaction_id,price,quantity
T5001,1500,2
T5002,500,10
T5003,12000,1
T5004,1500,5
T5005,12000,3"""

with open("transactions.csv", "w", newline="") as file:
    file.write(csv_content)

import pandas as pd
import numpy as np


# In[7]:


df = pd.read_csv("transactions.csv")


# In[8]:


print("=== LOADED DATASET ===")
print(df)
print(f"\nShape: {df.shape}")


# In[9]:


print("\n=== DATA TYPES ===")
print(df.dtypes)


# In[13]:


prices = df["price"].values
quantities = df["quantity"].values

print("=== NUMPY ARRAYS ===")
print(f"Prices array: {prices}")
print(f"Quantities array: {quantities}")
print(f"Prices dtype: {prices.dtype}")
print(f"Quantities dtype: {quantities.dtype}")


# In[14]:


print(f"\nPrices is NumPy array: {isinstance(prices, np.ndarray)}")
print(f"Quantities is NumPy array: {isinstance(quantities, np.ndarray)}")


# In[15]:


revenue = prices * quantities


# In[16]:


print("=== REVENUE CALCULATION ===")
print("Revenue:", revenue)
print("No loops used! ✓")


# In[18]:


df["revenue"] = revenue
print("\n=== DATAFRAME WITH REVENUE ===")
print(df)


# In[20]:


categories = np.where(revenue > 1000, "HIGH", np.where(revenue >= 2000, "MEDIUM", "LOW"))
print("=== CLASSIFICATION ===")
print("Categories:", categories)


# In[21]:


print("\n=== CLASSIFICATION VERIFICATION ===")
for i in range(len(revenue)):
    print(f"Transaction {df.iloc[i]['transaction_id']}: "
          f"Revenue={revenue[i]:,} → Category={categories[i]}")


# In[22]:


df["category"] = categories
print("\n=== FINAL DATAFRAME ===")
print(df)


# In[23]:


output_df = df[["transaction_id", "revenue", "category"]].copy()
print("=== OUTPUT DATAFRAME ===")
print(output_df)


# In[24]:


output_df.to_csv("transaction_classification.csv", index=False)
print("\nSaved: transaction_classification.csv")


# In[25]:


print("\n=== SUMMARY STATISTICS ===")
print(f"Total transactions: {len(output_df)}")
print(f"Total revenue: {output_df['revenue'].sum():,.2f}")
print(f"Average revenue: {output_df['revenue'].mean():,.2f}")
print(f"\nCategory distribution:")
print(output_df["category"].value_counts())


# In[26]:


def business_rules_engine(input_file, output_file):

    # Load data
    df = pd.read_csv(input_file)

    # Convert to NumPy arrays
    prices = df["price"].values
    quantities = df["quantity"].values

    # Compute revenue (vectorized)
    revenue = prices * quantities

    # Apply classification rules (vectorized)
    categories = np.where(
        revenue > 10000,
        "HIGH",
        np.where(
            revenue >= 2000,
            "MEDIUM",
            "LOW"
        )
    )

    # Create output DataFrame
    output_df = pd.DataFrame({
        "transaction_id": df["transaction_id"].values,
        "revenue": revenue,
        "category": categories
    })

    # Save output
    output_df.to_csv(output_file, index=False)

    print("Business rules engine executed successfully!")
    print(f"  - Processed {len(output_df)} transactions")
    print(f"  - Total revenue: {revenue.sum():,.2f}")
    print(f"  - Output saved to: {output_file}")

    return output_df


# In[27]:


result = business_rules_engine("transactions.csv", "transaction_classification.csv")


# In[28]:


import inspect
source = inspect.getsource(business_rules_engine)
print("=== CODE INSPECTION ===")
print("Checking for loops in classification logic...")

if "for" in source and "category" in source:
    # Check if 'for' is in a comment or actual loop
    lines = source.split('\n')
    for i, line in enumerate(lines):
        if 'for' in line and 'category' in source[max(0, i-5):i+5]:
            if not line.strip().startswith('#'):
                print(f"⚠️ Potential loop found: {line.strip()}")
else:
    print("✓ No loops detected in classification logic")


# In[29]:


print("\n=== VECTORIZATION APPROACH ===")
print("✓ Revenue calculation: prices * quantities (vectorized)")
print("✓ Classification: np.where() with nested conditions (vectorized)")
print("✓ All operations use NumPy array operations")
print("✓ No Python loops for business logic")


# In[ ]:





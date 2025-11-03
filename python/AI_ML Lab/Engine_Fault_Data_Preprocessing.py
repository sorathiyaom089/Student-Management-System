
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

print("="*70)
print("Engine Fault Data Preprocessing - Scaling and Encoding")
print("="*70)

# Load the dataset
df = pd.read_csv(r"C:\Coding\EngineFaultDB_Final.csv", encoding='latin1')

print("\nOriginal Data:")
print(df.head())

# Identify numerical and categorical columns
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

print(f"\nNumerical columns: {list(numerical_cols)}")
print(f"Categorical columns: {list(categorical_cols)}")

# Scale numerical features
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# One-hot encode categorical features (if any)
if len(categorical_cols) > 0:
    df = pd.get_dummies(df, columns=categorical_cols)

print("\nFinal Dataset after Scaling and Encoding:")
print(df.head())

# Save the processed dataset
output_path = r"C:\Coding\EngineFaultDB_Final_processed.csv"
df.to_csv(output_path, index=False)

print(f"\n{'='*70}")
print(f"Processed dataset saved to: {output_path}")
print(f"Shape: {df.shape}")
print(f"{'='*70}")

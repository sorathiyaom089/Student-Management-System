
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Load the engine fault dataset
print("="*70)
print("PCA Analysis - Engine Fault Detection")
print("="*70)

df = pd.read_csv(r"C:\Coding\EngineFaultDB_Final.csv", encoding='latin1')

print(f"\nDataset loaded successfully!")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())

print(f"\nDataset info:")
print(df.info())

print(f"\nMissing values per column:")
print(df.isnull().sum())

# Select numeric features (float64 and int64)
X = df.select_dtypes(include=['float64', 'int64']).fillna(0)

print(f"\n{'='*70}")
print(f"Feature Selection")
print(f"{'='*70}")
print(f"Selected numeric columns: {list(X.columns)}")
print(f"Number of features: {X.shape[1]}")
print(f"Number of samples: {X.shape[0]}")

# Standardize the features (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"\n{'='*70}")
print(f"Feature Scaling")
print(f"{'='*70}")
print(f"Features have been standardized (mean=0, std=1)")

# Apply PCA with 2 components for visualization
n_components = 2
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_scaled)

# Display PCA results
print(f"\n{'='*70}")
print(f"PCA Results")
print(f"{'='*70}")
print(f"Original features: {X.shape[1]}")
print(f"Reduced features: {X_pca.shape[1]}")
print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
print(f"Total variance retained: {sum(pca.explained_variance_ratio_):.4f} ({sum(pca.explained_variance_ratio_)*100:.2f}%)")

# Create visualization
plt.figure(figsize=(10, 8))
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6, color='teal', edgecolors='k', linewidth=0.5)
plt.xlabel('PC1', fontsize=12, fontweight='bold')
plt.ylabel('PC2', fontsize=12, fontweight='bold')
plt.title('PCA - Engine Fault Data', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the plot
output_path = r"C:\Coding\python\AI_ML Lab\output\PCA_Engine_Fault_Visualization.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"\n{'='*70}")
print(f"Visualization saved to: {output_path}")
print(f"{'='*70}")

plt.show()

# Additional analysis: Show component loadings
print(f"\n{'='*70}")
print(f"Principal Component Loadings (Top Contributing Features)")
print(f"{'='*70}")

# Get the loadings for each principal component
loadings = pd.DataFrame(
    pca.components_.T,
    columns=[f'PC{i+1}' for i in range(n_components)],
    index=X.columns
)

print("\nPC1 - Top 10 Contributing Features:")
pc1_sorted = loadings['PC1'].abs().sort_values(ascending=False).head(10)
for feature, loading in pc1_sorted.items():
    print(f"  {feature}: {loadings.loc[feature, 'PC1']:.4f}")

print("\nPC2 - Top 10 Contributing Features:")
pc2_sorted = loadings['PC2'].abs().sort_values(ascending=False).head(10)
for feature, loading in pc2_sorted.items():
    print(f"  {feature}: {loadings.loc[feature, 'PC2']:.4f}")

# Scree plot - variance explained by each component
print(f"\n{'='*70}")
print(f"Creating Scree Plot...")
print(f"{'='*70}")

# Perform PCA with all components to show variance
pca_full = PCA()
pca_full.fit(X_scaled)

plt.figure(figsize=(10, 6))
plt.bar(range(1, len(pca_full.explained_variance_ratio_) + 1), 
        pca_full.explained_variance_ratio_, 
        alpha=0.7, color='steelblue', edgecolor='black')
plt.xlabel('Principal Component', fontsize=12, fontweight='bold')
plt.ylabel('Variance Explained Ratio', fontsize=12, fontweight='bold')
plt.title('Scree Plot - Variance Explained by Each Component', fontsize=14, fontweight='bold')
plt.xticks(range(1, len(pca_full.explained_variance_ratio_) + 1))
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()

# Save scree plot
scree_path = r"C:\Coding\python\AI_ML Lab\output\PCA_Scree_Plot.png"
plt.savefig(scree_path, dpi=300, bbox_inches='tight')
print(f"Scree plot saved to: {scree_path}")

plt.show()

# Cumulative variance explained
cumulative_variance = np.cumsum(pca_full.explained_variance_ratio_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, 
         marker='o', linestyle='--', color='darkorange', linewidth=2, markersize=6)
plt.xlabel('Number of Components', fontsize=12, fontweight='bold')
plt.ylabel('Cumulative Variance Explained', fontsize=12, fontweight='bold')
plt.title('Cumulative Variance Explained by PCA Components', fontsize=14, fontweight='bold')
plt.axhline(y=0.95, color='red', linestyle='--', label='95% Variance', alpha=0.7)
plt.axhline(y=0.90, color='green', linestyle='--', label='90% Variance', alpha=0.7)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save cumulative variance plot
cumvar_path = r"C:\Coding\python\AI_ML Lab\output\PCA_Cumulative_Variance.png"
plt.savefig(cumvar_path, dpi=300, bbox_inches='tight')
print(f"Cumulative variance plot saved to: {cumvar_path}")

plt.show()

# Find number of components for 95% variance
n_components_95 = np.argmax(cumulative_variance >= 0.95) + 1
print(f"\n{'='*70}")
print(f"Components needed for 95% variance: {n_components_95} out of {X.shape[1]}")
print(f"Dimensionality reduction: {X.shape[1]} → {n_components_95} features")
print(f"Reduction ratio: {(1 - n_components_95/X.shape[1])*100:.2f}% reduction")
print(f"{'='*70}")

print("\n✓ PCA Analysis Complete!")
print("="*70)

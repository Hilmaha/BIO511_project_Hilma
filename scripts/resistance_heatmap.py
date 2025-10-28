import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define resistance gene presence (1 = present, 0 = absent)
data = {
    "Gene": [
        "mdf(A)_1",
        "blaCTX-M-15_1",
        "blaCTX-M-9_1",
        "blaTEM-1B_1",
        "aac(6')-Ib-cr_1",
        "catA1_1",
        "catB8_1",
        "tet(D)_1",
        "sul1_5",
        "sul2_2",
        "aadA8b_2",
        "aph(3'')-Ib_2",
        "aph(6)-Id_1",
        "mph(A)_2",
        "aac(3)-IIa_1"
    ],
    "K12":      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "O25b":     [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "CCUG55970":[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index("Gene", inplace=True)

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap="YlGnBu", cbar_kws={'label': 'Presence (1) / Absence (0)'}, linewidths=0.5)
plt.title("Antibiotic Resistance Genes in E. coli Strains")
plt.ylabel("Resistance Genes")
plt.xlabel("Strains")
plt.tight_layout()

# Save
plt.savefig("resistance_genes_heatmap.png", dpi=300)


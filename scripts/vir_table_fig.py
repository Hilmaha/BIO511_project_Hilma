import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/hilma/BIO511/WGS_project/scripts/virulence_table.csv")
df = df.rename(columns={"Unnamed: 0": "gene"})

# reorder
desired_order = ["gene", "K12", "O25b", "CCUG"]
df = df[desired_order]

# --- COLOR LOGIC ---
# build matrix of colors same size as df (but ignore gene column)
colors = [["white"] * 4 for _ in range(len(df))]   # 4 columns: gene, K12, O25b, CCUG

for i, row in df.iterrows():
    in_K12  = row["K12"]  == 1
    in_O25b = row["O25b"] == 1
    in_CCUG = row["CCUG"] == 1

    # Case 1 — present in O25b + CCUG only → green (not K12)
    if in_O25b and in_CCUG and not in_K12:
        colors[i][2] = "lightgreen"  # O25b
        colors[i][3] = "lightgreen"  # CCUG

    # Case 2 — present only in CCUG → blue
    elif in_CCUG and not in_O25b and not in_K12:
        colors[i][3] = "lightblue"   # CCUG


# Create table image
fig, ax = plt.subplots(figsize=(10, len(df)*0.3 + 1))
ax.axis('off')

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.2)

# Apply colors
for i in range(len(df)):
    for j in range(1, 4):   # only color K12/O25b/CCUG columns, not gene name
        table[(i+1, j)].set_facecolor(colors[i][j])

output_path = "/home/hilma/BIO511/WGS_project/results/res_and_vir_genes/virulence_table_colored.png"
plt.savefig(output_path, bbox_inches='tight', dpi=300)




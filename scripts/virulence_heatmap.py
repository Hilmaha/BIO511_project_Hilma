import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define virulence genes for each strain
k12 = {
    "espY1","yagV/ecpE","yagW/ecpD","yagX/ecpC","yagY/ecpB","yagZ/ecpA","ykgK/ecpR",
    "entD","fepA","fes","entF","fepC","fepG","fepD","entS","fepB","entC","entE",
    "entB","entA","ompA","csgG","csgF","csgD","csgB","espR1","espL1","espR4",
    "gtrA","gtrB","gspM","gspL","gspC","aslA","espL4","espX4","espX5","fimB",
    "fimE","fimA","fimI","fimC","fimD","fimF","fimG","fimH"
}

o25b = {
    "chuV","chuU","chuY","chuX","chuW","chuT","chuA","chuS","gspL","gspM","kpsM",
    "kpsD","sat","iutA","iucD","iucC","iucB","iucA","papI","papB","papX","fyuA",
    "ybtE","ybtT","ybtU","irp1","irp2","ybtA","ybtP","ybtQ","ybtX","ybtS",
    "csgB","csgD","csgF","csgG","ompA","entA","entB","entE","entC","fepB",
    "entS","fepD","fepG","fepC","entF","fes","fepA","entD","fdeC","ykgK/ecpR",
    "yagZ/ecpA","yagY/ecpB","yagX/ecpC","yagW/ecpD","yagV/ecpE","fimH","fimG",
    "fimF","fimD","fimC","fimI","fimA","fimE","papX","papG","papF","papK",
    "papJ","papD","papC","papH","papB","papI","cnf1","hlyD","hlyB","hlyA","hlyC",
    "aslA"
}

ccug = {
    "papX","kpsD","gspM","gspL","gspK","gspJ","gspI","gspH","gspG","gspF",
    "gspE","gspD","gspC","chuS","shuA","shuT","chuW","shuX","chuY","chuU","chuV",
    "draP","afaD","afaC-I","afaB-I","afaA","daaF","espY4","aslA","espL4",
    "espX4","espX5","fimB","fimE","fimA","fimI","fimC","fimD","fimF","fimG",
    "fimH","espX1","espY1","espY2","yagV/ecpE","yagW/ecpD","yagX/ecpC",
    "yagY/ecpB","yagZ/ecpA","ykgK/ecpR","fdeC","espY3","entD","fepA","fes",
    "entF","fepC","fepG","fepD","entS","fepB","entC","entE","entB","entA","ompA",
    "csgG","csgF","csgD","csgB","espR1","espL1","espR4","ybtS","ybtX","ybtQ",
    "ybtP","ybtA","irp2","irp1","ybtU","ybtT","ybtE","fyuA","iucA","iucB","iucC",
    "iucD","iutA"
}

# Combine all unique genes
all_genes = sorted(k12 | o25b | ccug)

# Build dataframe
data = {
    "Gene": all_genes,
    "K12": [1 if g in k12 else 0 for g in all_genes],
    "O25b": [1 if g in o25b else 0 for g in all_genes],
    "CCUG55970": [1 if g in ccug else 0 for g in all_genes]
}

df = pd.DataFrame(data).set_index("Gene")

# Plot
plt.figure(figsize=(12, 18))
sns.heatmap(df, cmap="YlOrBr", linewidths=0.5, linecolor='gray', cbar_kws={'label': 'Presence (1) / Absence (0)'})
plt.title("Virulence Gene Presence/Absence Across E. coli Strains")
plt.ylabel("Virulence Genes")
plt.xlabel("Strains")
plt.tight_layout()
plt.savefig("virulence_heatmap.png", dpi=300)


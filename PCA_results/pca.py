import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

# loading the covariance matrix
cov_matrix = np.loadtxt('out_covmat.cov')

# list of genomes
genomes = [
    'DOG_1', 'DOG_2', 'DOG_3', 'DOG_4', 'DOG_5', 'DOG_6', 'DOG_7', 'DOG_8', 'HYBRID_F1_1', 'HYBRID_F1_2', 'HYBRID_F1_3', 'HYBRID_F1_4', 'HYBRID_F1_5', 'HYBRID_F1_6', 'HYBRID_F1_7', 'HYBRID_F1_8', 'HYBRID_F2_1', 'HYBRID_F2_2', 'WOLF_CZ_1', 'WOLF_CZ_2', 'WOLF_CZ_3', 'WOLF_DE_1', 'WOLF_DE_2', 'WOLF_DE_3', 'WOLF_DE_4', 'WOLF_DE_5', 'WOLF_DE_6', 'WOLF_DE_7', 'WOLF_DE_8', 'WOLF_DE_9', 'WOLF_DE_10', 'WOLF_DE_12', 'WOLF_DE_13', 'WOLF_DE_15', 'WOLF_DE_16', 'WOLF_DE_17', 'WOLF_DE_18', 'WOLF_DE_19', 'WOLF_DE_20', 'WOLF_DE_21', 'WOLF_DE_22', 'WOLF_DE_25', 'WOLF_DE_26', 'WOLF_DE_27', 'WOLF_PL_8', 'WOLF_PL_10', 'WOLF_PL_14', 'WOLF_PL_16', 'WOLF_PL_22', 'WOLF_PL_27', 'WOLF_PL_28', 'WOLF_PL_32', 'WOLF_PL_34', 'WOLF_PL_35', 'WOLF_PL_37', 'WOLF_PL_38', 'WOLF_SK_5', 'WOLF_SK_6', 'WOLF_SK_7', 'WOLF_SK_9', 'WOLF_SK_10', 'WOLF_SK_11', 'WOLF_SK_12', 'WOLF_SK_13', 'WOLF_SK_14', 'WOLF_SK_17', 'WOLF_SK_18', 'WOLF_SK_21', 'WOLF_SK_22', 'WOLF_SK_24', 'WOLF_SK_27', 'WOLF_SK_28', 'WOLF_SK_30', 'WOLF_SK_31', 'WOLF_SK_32', 'WOLF_SK_33', 'WOLF_SK_35', 'WOLF_SK_36', 'WOLF_SK_38', 'WOLF_SK_39', 'WOLF_SK_42', 'WOLF_SK_43', 'WOLF_SK_44', 'WOLF_SK_45', 'WOLF_SK_46', 'WOLF_SK_47', 'WOLF_SK_48', 'WOLF_SK_49', 'WOLF_SK_50', 'WOLF_SK_51', 'WOLF_SK_52', 'WOLF_SK_53', 'WOLF_SK_54', 'WOLF_UA_1', 'WOLF_UA_2', 'WOLF_UA_3', 'WOLF_UA_5', 'WOLF_UA_6', 'WOLF_UA_7', 'WOLF_UA_8', 'WOLF_UA_9', 'WOLF_UA_10', 'WOLF_UA_11', 'WOLF_IT_5', 'WOLF_IT_7', 'WOLF_IT_8', 'WOLF_IT_9', 'WOLF_IT_10', 'WOLF_IT_13', 'WOLF_AT_1'
]

# creating a PCA model
pca = PCA(n_components=2)
pca_result = pca.fit_transform(cov_matrix)

# explained variation
explained_variance = pca.explained_variance_ratio_

# transformation of PCA results to DataFrame
pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
pca_df['Genome'] = genomes

# defining colours for individual groups
colors = {
    'DOG': 'blue',
    'HYBRID_F1': 'green',
    'HYBRID_F2': 'red',
    'WOLF_CZ': 'purple',
    'WOLF_DE': 'orange',
    'WOLF_PL': 'brown',
    'WOLF_SK': 'pink',
    'WOLF_UA': 'gray',
    'WOLF_IT': 'cyan',
    'WOLF_AT': 'yellow'
}

# adding colors to DataFrame
pca_df['Color'] = pca_df['Genome'].apply(lambda x: colors[x.rsplit('_', 1)[0]])

# graph plotting
plt.figure(figsize=(10, 8))
for group, color in colors.items():
    indices = pca_df['Genome'].str.startswith(group)
    plt.scatter(pca_df.loc[indices, 'PC1'], pca_df.loc[indices, 'PC2'], c=color, label=group)

plt.xlabel(f'PC1 ({explained_variance[0]*100:.2f}%)')
plt.ylabel(f'PC2 ({explained_variance[1]*100:.2f}%)')
#plt.title('PCA of Genomic Data')
plt.legend()
plt.show()

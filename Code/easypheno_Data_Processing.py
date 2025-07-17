import pandas as pd

# 1. 加载基因型数据并转置
geno = pd.read_csv("../Data/BYxRM_GenoData.txt", sep="\t", index_col=0)  # marker 是行索引
geno = geno.T  # 转置，使 sample 成为行
geno.index.name = 'sample_id'  # 设置行索引名为 sample_id
geno.reset_index(inplace=True)  # 将 sample_id 提到第一列
geno.to_csv("../Data/x_matrix.csv", index=False)

# 2. 加载表型数据
pheno = pd.read_csv('../Data/BYxRM_PhenoData.txt', sep='\t')
pheno.rename(columns={pheno.columns[0]: 'sample_id'}, inplace=True)
pheno.to_csv('../Data/y_matrix.csv', index=False)
print(pheno.isnull().sum())
# 以均值填充缺失值
# 读取数据
pheno = pd.read_csv('../Data/y_matrix.csv')

# 将所有非 sample_id 的列转换为 float（强制转换）
for col in pheno.columns:
    if col != 'sample_id':
        pheno[col] = pd.to_numeric(pheno[col], errors='coerce')

# 用列的均值填充缺失值
pheno.fillna(pheno.mean(numeric_only=True), inplace=True)

# 再次检查是否还有缺失值
missing = pheno.columns[pheno.isnull().any()].tolist()
if missing:
    print("❗ 仍有缺失值的列：", missing)
else:
    print("✅ 所有缺失值已处理完毕")

# 保存
pheno.to_csv('../Data/y_matrix.csv', index=False)
#print(pheno.isnull().sum())




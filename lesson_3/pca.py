from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""准备数据集"""
iris = load_iris()
# X：得到input输入 Y则是对于output，label，target，通常Y有一个属性，X有很多属性
X = iris.data
# feature_names 会返回一个list，存放所有的features，即是特征
print(iris.feature_names)
# nparray的数据类型
print(type(X))
# 150行，4列
print(X.shape)
# Y 的shape会是只有一列，行数不变，因为只预测一个属性
"""
通过eigenvalues 和 eigenvectors 来求PC和explained variance
"""
# covariance_matrix
# 默认列为属性，行为数据
# 此处会计算出协方差矩阵
covariance_matrix = np.cov(X, rowvar=False)
print(f"covariance matrix: \n\n{covariance_matrix}")
# eigenvalue and eigenvectors
# 输入一个矩阵，返回特征值和特征向量
# 此处向量仍旧是竖着的
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

print("eigenvalue:", eigenvalues)
print("eigenvectors:\n", eigenvectors)
# 通过eigenvalues获取 explained variance
# eigenalues 是一个nparray
explained_variance_ratio_list = eigenvalues/sum(eigenvalues)

"""
通过pca()获取 explained variance
"""
#如果没有指定n——components
# 会默认为最大，用于观察最后需要减少到多少个features
pca = PCA()
# 相当于训练
X_pca = pca.fit_transform(X)

# 获取explained variance
explained_variance_ratio = pca.explained_variance_ratio_

# 计算 cumulative explained variance
cumulative_explained_variance = np.cumsum(eigenvalues/sum(eigenvalues))

# 打印累积解释方差
for i, variance in enumerate(cumulative_explained_variance):
    print(f"The total explained variance of PC {i + 1} is: {variance}")
#此处就可以知道了

"""
指定两个PC,转化原有的数据
"""
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# 将降维后的数据转换为Pandas DataFrame
columns = ['PC1', 'PC2']
df = pd.DataFrame(X_reduced, columns=columns)
df["target"] = iris.target
#figure 表示要开始画图了
plt.figure()
plt.scatter(df['PC1'], df['PC2'], c=df['target'])
plt.show()
plt.close()
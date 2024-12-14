from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""准备数据集"""
iris = load_iris()
X = iris.data

print(iris.feature_names)
print(type(X))
print(X.shape)

"""
通过eigenvalues 和 eigenvectors 来求PC和explained variance
"""
# covariance_matrix
covariance_matrix = np.cov(X, rowvar=False)
print(f"covariance matrix: \n\n{covariance_matrix}")
# eigenvalue and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

print("eigenvalue:", eigenvalues)
print("eigenvectors:\n", eigenvectors)
# 通过eigenvalues获取 explained variance

"""
通过pca()获取 explained variance
"""
pca = PCA()
X_pca = pca.fit_transform(X)

# 获取explained variance
explained_variance_ratio = pca.explained_variance_ratio_

# 计算 cumulative explained variance
cumulative_explained_variance = np.cumsum(eigenvalues/sum(eigenvalues))

# 打印累积解释方差
for i, variance in enumerate(cumulative_explained_variance):
    print(f"The total explained variance of PC {i + 1} is: {variance}")

"""
指定两个PC,转化原有的数据
"""
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# 将降维后的数据转换为Pandas DataFrame
columns = ['PC1', 'PC2']
df = pd.DataFrame(X_reduced, columns=columns)
df["target"] = iris.target
plt.figure()
plt.scatter(df['PC1'], df['PC2'], c=df['target'])
plt.show()
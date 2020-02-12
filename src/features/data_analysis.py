import numpy as np
from sklearn.decomposition import PCA
from src.visualization.visualize import plot,barPlot

def removeCorrelatedFeatures(df,threshold):
    """Remove correlated features according to pearson method
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame object.
        threshold : float
            Threshold to be included in the function.
        Returns
        selected_columns: list
            Columns to be removed.
    """
    corr = df.corr(method = 'pearson')
    columns = {}
    selected_columns = []
    for column in corr.columns.values:
        if column not in columns:
            columns[column] = True
    for i in range(corr.shape[0]):
        if columns[list(corr.columns.values)[i]]:
            for j in range(i+1, corr.shape[0]):
                if (corr.iloc[i,j] >= 0.70 and str(list(corr.columns.values)[j]) != str(list(corr.columns.values)[i])):
                    if columns[list(corr.columns.values)[j]]:
                        columns[list(corr.columns.values)[j]] = False
    for column in columns.keys():
        if columns[column]:
            selected_columns.append(column)
    return selected_columns

def pcaAnalysis(data_points,pcaComponents,reportDir):
    """PCA Analysis, that can be used to determine the optimal number of PCA components to be used
        Parameters
        ----------
        data_points : numpy.ndarray
            Array of type numpy.ndarray.
        pcaComponents : int
            Number of components to be used in PCA analysis.
        Returns
        None
    """
    pca = PCA()
    pca.fit(data_points)
    plot(range(0,8), pca.explained_variance_, 'bx-','pca component','explained variances','Elbow Method For Optimal Number of PCA Component',
    reportDir)
def applyPCA(data_points,pcaComponents):
    """Apply PCA to a list of values
        Parameters
        ----------
        data_points : numpy.ndarray
            Array of type numpy.ndarray.
        pcaComponents : int
            Number of components to be used in PCA analysis.
        Returns
            Array of type numpy.ndarray.
    """
    pca = PCA(n_components=pcaComponents)
    return pca.fit_transform(data_points)

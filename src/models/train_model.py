from sklearn.cluster import KMeans
from sklearn import metrics
from src.visualization.visualize import plot

def kMeansAnalysis(data_points=None,kMeansRange=range(2,6),reportDir=None):
    Sum_of_squared_distances = []
    K = kMeansRange
    for k in K:
        km = KMeans(n_clusters=k,random_state=5)
        km = km.fit(data_points)
        Sum_of_squared_distances.append(km.inertia_)

    plot(K,Sum_of_squared_distances,'bx-','k','Sum_of_squared_distances','Elbow Method For Optimal k',reportDir)

def applyKmeans(data_points=None,k=None):
    return KMeans(n_clusters=k,random_state=5).fit_predict(data_points)

import pandas as pd 
from src.features.data_analysis import pcaAnalysis,applyPCA
import sys
import logging 
from src.models.train_model import kMeansAnalysis,applyKmeans

def main():
    try:
        log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=logging.INFO, format=log_fmt)
        logger = logging.getLogger(__name__)
        logger.info('analyze and apply PCA to reduce dimension')
        df = pd.read_csv("data/processed/us-accidents.csv")
        df.drop(['Unnamed: 0'],inplace=True,axis=1)
        data_points = df.values
        pcaAnalysis(data_points,3,'reports/figures/elbow_method_optimal_number_pca.png')
        data_points = applyPCA(data_points,3)

        logger.info('analyze and apply Kmeans algorithm')
        kMeansAnalysis(data_points,range(2,6),'reports/figures/kmeans_elbow_method.png')
        applyKmeans(data_points,3)
    except:
        print("no such file, check makeFile once again for the right pipeline execution")


if __name__ == '__main__':
    main()
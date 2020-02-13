# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import sys
import pandas as pd
import numpy as np
from src.features.preprocess_features import variance_threshold_selector, handleMissingData
from src.features.data_analysis import removeCorrelatedFeatures

@click.command()
@click.argument('input_filename', type=click.Path(exists=True))
@click.argument('output_filename', type=click.Path(exists=True))
def main(input_filename,output_filename):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    logger.info('first import data')
    df = pd.read_csv(input_filename)
    

    logger.info("next drop columns that are not variant enough")
    variance_threshold_selector(df.dropna(),0.8,logger)

    logger.info("Drop columns unnecessary, change type of columns and handle null values")
    df.drop(['End_Lat','End_Lng','Number','Wind_Chill(F)','Precipitation(in)'],inplace = True, axis = 1)
    for column in df.columns.values:
        if df[column].dtype == bool:
            df[column] = df[column].astype(int)
    df = df.select_dtypes(include=[np.float64,np.int64,np.int32])
    handleMissingData(df)
    
    logger.info("Remove correlated features")
    selectedColumns = removeCorrelatedFeatures(df,0.70)
    df = df[selectedColumns]

    logger.info("Remove features not related road and save the data to data/interim")
    df = df[['Amenity','Crossing','Junction','No_Exit','Railway','Station','Stop',
             'Traffic_Signal']]
    df.to_csv(output_filename)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()

import pandas as pd 

def variance_threshold_selector(data,threshold,logger):
    """Keep object type columns that are variant enough 
        Parameters
        ----------
        data : pd.DataFrame
            DataFrame object.
        threshold: float
            Threshold value to be included in the function
        logger: logging.logger
            Print logs
        Returns
        -------
        None
    """
    to_be_deleted = []
    for column in data.columns.values:
        if data[column].dtype == 'object' or data[column].dtype == 'str' or data[column].dtype == bool:
            try:
                if max(data[column].value_counts()) > sum(data[column].value_counts())*threshold:
                    to_be_deleted.append(column)
            except:
                pass
    logger.info("dropping object type columns that are not variant enough. Dropped columns: "+
    str(to_be_deleted)+", threshold: "+str(threshold))
    data.drop(to_be_deleted,axis=1,inplace=True)


def handleMissingData(data):
    """Handle missing data
        Parameters
        ----------
        data : pd.DataFrame
            DataFrame object.
        Returns
        -------
        None
    """
    for column in data.columns.values:
        if data[column].isna().sum() and (data[column].dtype == int or data[column].dtype == float):
            data[column].fillna(data[column].mean(),inplace=True)
        else:
            data[column].fillna(data[column].mode()[0],inplace=True)



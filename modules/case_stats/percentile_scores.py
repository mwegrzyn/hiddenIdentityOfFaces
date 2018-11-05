"""Functions for computing percentile scores"""

# import required modules
import pandas as pd
import numpy as np
from scipy import stats
from sklearn import preprocessing


# get z scores and transform to percentiles
def get_percentiles(con_data,pat_data):
    """Transform the patient's raw score into a percentile score

    This function uses the z-distribution and then transforms
    the z-values into percentile scores

    Parameters
    ----------
    con_data : (n,1) shaped numpy array
        Can be a list, array or pandas-series of values
        All the data of the controls
    pat_data : (1,1) shaped numpy array
        data of the patient

    Returns
    -------
    
    the percentile score of the patient

    """
    # get transformation parameters from controls
    my_scaler = preprocessing.StandardScaler()
    my_scaler.fit(con_data)
    # apply to patient to get the z-score
    z = my_scaler.transform(pat_data)[-1]
    # transform z-scores to cumulative distribution
    cdf = stats.norm.cdf(z)[-1]
    # scale from 0 to 100 instead of 0 to 1
    percentile = cdf*100
    # get z out of array
    z = z[-1]
    return z, percentile


# apply to each column of a df
def make_percentile_df(df,pat_idx):
    """compare percentiles for all columns of a df
    
    Applies the get_percentiles function to all columns of a dataframe    

    Parameters
    ----------
    df : pandas dataframe
        table with values

    Returns
    -------
    pc_df : pandas dataframe
        table with percentiles of patient
    """

    # make a new dataframe
    pc_df = pd.DataFrame()
    # for each column of the input dataframe
    for c in df.columns:
        # this will only work for columns with all values being numbers

        # transform values to percentile scores
        this_df = df.loc[:,c]
        con_data = this_df.drop(pat_idx).values
        pat_data = this_df.loc[pat_idx]
        
        con_data = con_data.reshape(-1,1)
        pat_data = np.array([pat_data]).reshape(-1,1)

        con_data.shape,pat_data.shape
        z, pc = get_percentiles(con_data, pat_data)
        
        d = {c:{'z':z,'percentile':pc}}
        # transform values to dataframe
        this_pc = pd.DataFrame(d).T
        # add to big dataframe
        pc_df = pd.concat([pc_df,this_pc],axis=0)


    return pc_df

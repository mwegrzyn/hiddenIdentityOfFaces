"""Function to make output dataframe"""

# import required modules
import numpy as np
from scipy import stats
from .percentile_scores import *
from .ttest_single import *


def make_percentiles(group_mean, group_std, pat_mean):

    group_array = np.random.normal(loc = group_mean, scale = group_std, size = 1000000)
    group_array = group_array.reshape(-1,1)
    pat_array = np.array([pat_mean]).reshape(-1,1)
    percentile_score = get_percentiles(group_array,pat_array)

    return percentile_score


def make_tstats_df(df,pat_idx):
    
    # get summary statistics of control group
    group_df = df.drop(pat_idx).apply(['mean','std','count'])
    # get raw data of patient
    pat_df = df.loc[[pat_idx]]
    # hard-code the patient name to be (upper-case) 'JB'
    pat_df.index = ['JB']
    # combine
    stats_df = pd.concat([group_df,pat_df])

    # initialize dictionary to write results to
    d = {}
    # for each task/feature
    for c in stats_df.columns:
        # get the data necessary to compute a ttest
        pat_mean = stats_df.loc['JB',c]
        group_mean = stats_df.loc['mean',c]
        group_std = stats_df.loc['std',c]
        group_n = stats_df.loc['count',c]
        # compute the ttest
        t,df,p = ttest_single(pat_mean,group_mean,group_std,group_n)
        # add to dictionary
        d[c] = {'t':'%.2f'%t,'df':int(df),'p':'%.3f'%p}
    
    # turn dict into df
    ttest_df = pd.DataFrame(d).T
    # custom order
    ttest_df = ttest_df.loc[:,['t','df','p']]
    
    return ttest_df

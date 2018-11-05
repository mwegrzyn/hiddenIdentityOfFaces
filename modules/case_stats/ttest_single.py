"""Functions for computing t-tests"""

# import required modules
import numpy as np
from scipy import stats

# main function
def ttest_single(x_pat,x_group,s_group,n):

    """Compare one person with a sample of multiple persons

    The formula to compute the t-value is as follows::
    
        (x_pat - x_group) / (s_group * sqrt( ( n+1 )/n ) ) 

    If the t-value obtained is negative and its magnitude exceeds the one-tailed
    5% critical value for t on n-1 degrees of freedom,
    then it can be concluded that the patient's score is sufficiently
    low to enable rejection of the null hypothesis that it is an observation
    from the scores of the control population
    (the patient is therefore considered to exhibit an impairment on the task in question)

    Parameters
    ----------
    x_pat : float or int
        Patient's score
    x_group : float or int
        Mean of the scores in the control sample
    s_group : float or int
        Standard deviation of scores in the control sample
    n : int
        The size of the control sample

    Returns
    -------
    t : float
        t-value for the comparison of patient with controls
    df : int
        Degrees of freedom, computed as n-1
    p : float
        two-tailed p-value for t 

    Notes
    -----
    This function applies the formula described in 
    
        Crawford, J. R., Garthwaite, P. H., & Howell, D. C. (2009). 
        On comparing a single case with a control sample: An alternative perspective.
        Neuropsychologia, 47(13), 2690-2695.

    Examples
    --------
    Say that the patient and the group have equal means
    and the samle size is 100. Then the following results
    should be produced:
        t-value is zero (no difference at all)
        df's are 99 (sample size of 100 minus 1)
        p-value is one (not significant at all)

    >>> 't=%.10f, df=%.1f, p=%.10f'%ttest_single(10,10,1,100)
    't=0.0000000000, df=99.0, p=1.0000000000'
    
    Say that the patient is two standard deviations below
    the controls. Then, - given a large enough sample - 
    the result should be significant:
    
    >>> 't=%.10f, df=%.1f, p=%.10f'%ttest_single(8,10,1,100)
    't=-1.9900743804, df=99.0, p=0.0493404337'
    
    In too small a sample, the difference will not be significant
    
    >>> 't=%.10f, df=%.1f, p=%.10f'%ttest_single(8,10,1,10)
    't=-1.9069251785, df=9.0, p=0.0888979325'
    
    Nor will a smaller difference be significant in a large sample
    
    >>> 't=%.10f, df=%.1f, p=%.10f'%ttest_single(8.1,10,1,100)
    't=-1.8905706614, df=99.0, p=0.0616060466'
    """

    # numerator of the formula 
    num = ( float(x_pat) - x_group )
    # denominator of the formula
    delim = (s_group*np.sqrt( (n+1.0)/n) )
    
    # t-value
    t = num/delim
    
    # degrees of freedom
    df = n-1
    
    # two-sided p-value (more conservative than the one-sided p suggested in the cited article)
    p = stats.t.sf(np.abs(t), df)*2
    
    return t,df,p

# run doctests
import doctest
doctest.run_docstring_examples(ttest_single,globals(),verbose=False,name='ttest_single')

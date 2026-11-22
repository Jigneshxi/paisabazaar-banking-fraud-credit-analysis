import os
import pytest
import pandas as pd
import numpy as np
from scipy import stats

p_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
clean_csv = os.path.join(p_dir, "paisabazaar_credit_score_clean.csv")

@pytest.fixture(scope="module")
def df():
    if not os.path.exists(clean_csv):
        raw_csv = os.path.join(p_dir, "dataset.csv")
        df_raw = pd.read_csv(raw_csv)
        return df_raw
    return pd.read_csv(clean_csv)

def test_clean_dataset_integrity(df):
    """Verify that dataset contains full 100,000 records and zero missing values."""
    assert len(df) == 100000
    assert df.isnull().sum().sum() == 0
    assert 'Credit_Score' in df.columns

def test_credit_score_categories(df):
    """Verify all 3 credit score categories are present in valid proportions."""
    scores = set(df['Credit_Score'].unique())
    assert scores == {'Good', 'Standard', 'Poor'}
    counts = df['Credit_Score'].value_counts()
    assert counts['Standard'] > counts['Poor'] > counts['Good']

def test_hypothesis_1_income_anova(df):
    """Verify Hypothesis 1: One-way ANOVA confirms significant income difference across credit scores."""
    good_inc = df[df['Credit_Score'] == 'Good']['Annual_Income']
    std_inc = df[df['Credit_Score'] == 'Standard']['Annual_Income']
    poor_inc = df[df['Credit_Score'] == 'Poor']['Annual_Income']
    
    f_stat, p_val = stats.f_oneway(good_inc, std_inc, poor_inc)
    assert f_stat > 1000
    assert p_val < 0.001
    assert good_inc.mean() > std_inc.mean() > poor_inc.mean()

def test_hypothesis_4_delayed_payments(df):
    """Verify Hypothesis 4: Delayed payments severely penalize credit score."""
    poor_delay = df[df['Credit_Score'] == 'Poor']['Num_of_Delayed_Payment']
    good_delay = df[df['Credit_Score'] == 'Good']['Num_of_Delayed_Payment']
    
    t_stat, p_val = stats.ttest_ind(poor_delay, good_delay, equal_var=False)
    assert t_stat > 50
    assert p_val < 0.001
    assert poor_delay.mean() > good_delay.mean()

def test_feature_engineering_ratios(df):
    """Verify derived financial health ratios are positive and bounded."""
    if 'Debt_to_Income' in df.columns:
        assert (df['Debt_to_Income'] >= 0).all()
    if 'Credit_Utilization_Ratio' in df.columns:
        assert (df['Credit_Utilization_Ratio'] >= 0).all()
        assert (df['Credit_Utilization_Ratio'] <= 100).all()

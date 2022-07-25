# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/08_gbe.rtt.data_provider.ipynb (unless otherwise specified).

__all__ = ['RTTDataProvider']

# Cell
from fastcore.foundation import patch
from ..data_provider import GBEProvider
from ...data_provider import get_efficiently
import numpy as np

# Cell
class RTTDataProvider(GBEProvider):
    '''This class builds upon GBEProvider to get the working memory task data.'''
    def __init__(self, data_folder_path):
        GBEProvider.__init__(self, data_folder_path)

# Cell
@patch
def decode_rtt_strings(self:RTTDataProvider, gbe_data):
    df = self.decode_gbe_strings(gbe_data, "RewardAndHappinessGame")
    # Calculating outcome variables
    df['trial_type'] = np.nan
    df.loc[(df.choiceamount.astype(float) < 0),'trial_type'] = 'loss'
    df.loc[(df.choiceamount.astype(float) > 0),'trial_type'] = 'win'
    df.loc[(df.choiceamount.astype(float) == 0),'trial_type'] = 'mixed'
    df['result'] = df.trialresult.replace({'1':'gain', '2': 'loss', '3':'certain'})
    df['gambled'] = df.result!='certain'
    # Filtering variables of interest
    df = df[["gbe_index","trial_number","timestarted", "timesubmitted", "choiceamount", "decisiontime", "happiness", "happinessstart", "happinesstime" ,"spinnerangle", "spinnerloseamount", "spinnerwinamount", "spintime", "trial_type","trialresult","gambled"]]
    return df

# Cell
@patch
@get_efficiently
def get_rtt_data(self:RTTDataProvider):
    gbe_data = self.get_gbe_data()
    df = self.decode_rtt_strings(gbe_data)
    return df
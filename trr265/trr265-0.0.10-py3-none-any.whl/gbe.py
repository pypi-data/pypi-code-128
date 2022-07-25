# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/02_gbe.ipynb (unless otherwise specified).

__all__ = ['GBEProvider']

# Cell
import numpy as np
from .data_provider import DataProvider, get_efficiently
from fastcore.foundation import patch
import pandas as pd
from matplotlib import pyplot as plt
import re

# Cell
class GBEProvider(DataProvider):
    '''This class builds upon DataProvider and focusses on GBE data.'''
    def __init__(self, data_folder_path):
        DataProvider.__init__(self, data_folder_path)
        self.GBE_COLUMNS = ['FruitTapGame','WorkingMemoryGame','CardGame','RewardAndHappinessGame']

# Cell
@patch
def get_gbe_from_movisense(self:GBEProvider):
    """
    This function pulls GBE data from movisense and sets cancelled sessions to None.  Here, we only include rows that have at least one non-cancelled GBE game.
    """
    # Getting GBE data
    df = self.get_mov_data().query("Form == 'GreatBrainExperiment'")
    # Setting cancelled sessions to missing
    df[self.GBE_COLUMNS] = df[self.GBE_COLUMNS].replace({'{canceled": true}"':None})
    # Only included rows with at least one non-cancelled GBE game
    df = df[~df[self.GBE_COLUMNS].isna().all(axis=1)]
    df = df.sort_values(['participant','trigger_date'])
    shifted = df.groupby('participant').sampling_day.shift(1)
    df['time_since_last_gbe'] = df['sampling_day'] - shifted
    df['time_since_last_gbe'].fillna(0, inplace = True)
    df['session_number'] = df.groupby('participant').cumcount() + 1
    # Creating the trigger type variable
    replace_dict = {
    'Button Pressed Spiele starten und Initialfragen (~40min)':'initial',
    'Participant Defined Time Trigger':'ema',
    'Button Pressed Bedarfstart GBE (Ausnahme)':'optional',
    'Button Pressed Bedarfsstart GBE':'optional'}
    df['trigger_type'] = df.Trigger.apply(lambda x: x.replace('Pressed:','Pressed').split(':')[0]).replace(replace_dict)
    df['gbe_index'] = df.participant + '_' + df.session_number.apply(lambda x: '%03d'%int(x))
    df = df.set_index('gbe_index')
    return df

# Cell
@patch
def define_initial_dataset(self:GBEProvider, df):
    initial_pps = df.sort_values(['starting_date','trigger_date']).groupby('participant').first().iloc[:300].index
    df['is_initial'] = df.participant.isin(initial_pps)
    df = df.sort_index()
    return df

# Cell
@patch
def define_baseline_sessions(self:GBEProvider, df):
    first_two_sessions = df.session_number <= 2
    same_day = df.time_since_last_gbe == 0
    initial_or_optional = df.trigger_type != 'ema'
    df['is_baseline'] = first_two_sessions & same_day & initial_or_optional
    return df

# Cell
@patch
def find_gbe_game_starting_time(self:GBEProvider, s):
    '''As baseline GBEs have the same trigger date, we first have to parse the time from the GBE data.'''
    nan_time = pd.to_datetime(np.nan)
    try:
        gbe_columns = s.split(',')

    except:
        return nan_time
    if 'timestarted' not in gbe_columns:
        return nan_time
    time_started_index = gbe_columns.index('timestarted')
    time_started = pd.to_datetime(s.split('\n')[1].split(',')[time_started_index][2:-2])
    return time_started



@patch
def check_time_between_sessions(self:GBEProvider, df):
    time_1 = pd.to_datetime(np.nan)
    time_2 = pd.to_datetime(np.nan)
    if len(df)==2:
        time_1 = self.find_gbe_game_starting_time(df.iloc[0])
        time_2 = self.find_gbe_game_starting_time(df.iloc[1])
    try:
        return (time_2 - time_1).seconds/60
    except:
        return np.nan

# Cell
@patch
def get_gbe_data(self:GBEProvider):
    df = self.get_gbe_from_movisense()
    df = self.define_initial_dataset(df)
    df = self.define_baseline_sessions(df)
    return df

@patch
def get_initial_baseline(self:GBEProvider):
    df = self.get_gbe_data()
    return df.query("is_initial and is_baseline")

@patch
def get_replication_baseline(self:GBEProvider):
    df = self.get_gbe_data()
    return df.query("(is_baseline and (not initial)")

# Cell
@patch
def decode_gbe_string(self:GBEProvider, s):
    """This function function turns one gbe output string into a dataframe"""
    def replace(g):
        return g.group(0).replace(',', '|')
    s = re.sub(r'\[.*?\]', replace, s) # The comma separated string can contain comma separated list items
    columns, df = s.replace('","',';').replace('"','').split('\n')
    df = pd.DataFrame([column.split(',') for column in df.split(';')][:-1]).transpose().ffill().iloc[:-1]
    df.columns = [c.replace('tr_','') for c in columns.split(',')[:-1]]
    def to_datetime(x):
        return pd.to_datetime(x[1:-1])
    if 'timestarted' in df.columns:
        df['timestarted'] = df.timestarted.apply(to_datetime)
        df['timesubmitted'] = df.timesubmitted.apply(to_datetime)
        df.drop(columns = 'appversion', inplace = True)
    else:
        df['timestarted'] = pd.to_datetime(np.nan)
        df['timesubmitted'] = pd.to_datetime(np.nan)
    return df

# Cell
@patch
def decode_gbe_strings(self:GBEProvider, df, column):
    '''This function turns all gbe output strings in a column into dataframes and concatenates them.'''
    df = df[~df[column].isna()] # Selecting non nan data
    #gbe_data = pd.concat(df.set_index(['participant','session_number'])[column].apply(self.decode_gbe_string).values, keys = df.index)
    #gbe_data = pd.concat(df[column].apply(self.decode_gbe_string).values)
    df = pd.concat(df[column].apply(self.decode_gbe_string).values, keys = df.index)
    df.index.rename('trial_number',level = 1, inplace = True)
    df = df.reset_index()
    df['trial_number'] = df.trial_number + 1
    return df
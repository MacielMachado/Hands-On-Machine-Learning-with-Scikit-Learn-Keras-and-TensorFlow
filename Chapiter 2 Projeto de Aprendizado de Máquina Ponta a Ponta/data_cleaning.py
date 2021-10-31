
from sklearn.preprocessing import OrdinalEncoder

class data_cleaner_and_manipulator():
    def __init__(self):
        pass

    def treat_NaN(self, df, type, cols = None):
        '''
        Most machine learning algorithms doesn't work with NaN values, 
        therefore this method is built to treat them.
        '''
        # Drop all the instances with NaN
        if type == 'dropna_row':
            df.dropna(subset = cols, axis = 0)
        # Drop all the feature that contains any NaN instance
        elif type == 'drop_col':
            df.dropna(subset = cols, axis = 1)
        # Fill all the NaN values with its feature median value
        elif type == 'fillna_median':
            if cols == None: df.fillna(df.median())
            else: df[cols] = df[cols].fillna(df.median())
            return df, df.median()
        # Fill all the NaN values with its feature mean value
        elif type == 'fillna_mean':
            if cols == None: df.fillna(df.median())
            else: df[cols] = df[cols].fillna(df.mean())
            return df, df.mean()
        return df

    def get_columns_of_specific_dtype(self, df, dtype):
        return list(df.select_dtypes(include=[dtype]).columns)

    def textEncoder(self, df):
        ordinal_encoder = OrdinalEncoder()
        ordinal_encoder.fit_transform(df)
        return df

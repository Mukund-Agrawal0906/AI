import pandas as pd

data = {'TimeStamp': ['2022-01-01 08:30:00', '2022-01-01 15:45:00', '2022-01-02 12:00:00']}
time_df = pd.DataFrame(data)

time_df['TimeStamp'] = pd.to_datetime(time_df['TimeStamp'])

time_df['Hour'] = time_df['TimeStamp'].dt.hour

print("DataFrame with Hour component:")
print(time_df)

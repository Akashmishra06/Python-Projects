from backtestTools.histData import getEquityBacktestData
from datetime import datetime
import pandas as pd
import numpy as np
import talib
import csv


startDate = datetime(2022, 5, 1, 9, 15)
endDate = datetime(2024, 4, 21, 15, 30)

startTimeEpoch = startDate.timestamp()
endTimeEpoch = endDate.timestamp()

stockName = "ABB"

df = getEquityBacktestData(stockName, startTimeEpoch - 864000, endTimeEpoch, "D")
print(df)

df["rsi"] = talib.RSI(df["c"], timeperiod=14)
df.dropna(inplace=True)
print(df)


filtered_df = df[((df['rsi'] < 60) & (df['rsi'] > 40)) | ((df['rsi'].shift(1) < 60) & (df['rsi'].shift(1) > 40))]


filtered_df['price_change'] = filtered_df['c'] - filtered_df['o']

filtered_df['color'] = filtered_df['price_change'].apply(lambda x: 'green' if x > 0 else 'red')

filtered_df.to_csv("color.csv", index=False)

print(filtered_df)


with open('color.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rsi = float(row['rsi'])  # Convert RSI value to float
        print("RSI:", rsi)

        if rsi > 60:
            print("\n")
        elif rsi < 40:
            print("\n")


with open('color.csv', newline='') as csvfile:
    with open('output.csv', 'w', newline='') as outputfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(outputfile, fieldnames=reader.fieldnames)
        
        writer.writeheader()  
        
        for row in reader:
            rsi = float(row['rsi'])  
            print("RSI:", rsi)

            writer.writerow(row)

            if rsi > 60:
                outputfile.write('\n'+('*'*100)+'\n')
            elif rsi < 40:
                outputfile.write('\n'+('*'*100)+'\n')


with open('output.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Open the output CSV file for writing
    with open('output_with_outcomes.csv', 'w', newline='') as outfile:
        fieldnames = reader.fieldnames + ['outcome']  
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        prev_color = None
        
        # Iterate over each row
        for row in reader:
            color = row['color']
            if prev_color is not None and color == prev_color:
                outcome = 'loss'
                print('loss')
            else:
                outcome = 'win'
                print('win')
            prev_color = color
            
            # Add the 'outcome' to the row
            row['outcome'] = outcome
            
            # Write the row with the added outcome to the output CSV file
            writer.writerow(row)
            
            # Check if a new line is encountered
            if '****************************************************************************************************' in row:
                prev_color = None
                print('\n')
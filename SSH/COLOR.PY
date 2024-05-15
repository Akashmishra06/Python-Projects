# from backtestTools.histData import getEquityBacktestData
# from datetime import datetime
# import pandas as pd
# import numpy as np
# import talib
# import csv


# startDate = datetime(2022, 5, 1, 9, 15)
# endDate = datetime(2024, 4, 21, 15, 30)

# startTimeEpoch = startDate.timestamp()
# endTimeEpoch = endDate.timestamp()

# stockName = "ABB"

# df = getEquityBacktestData(stockName, startTimeEpoch - 864000, endTimeEpoch, "D")
# print(df)

# df["rsi"] = talib.RSI(df["c"], timeperiod=14)
# df.dropna(inplace=True)
# print(df)


# filtered_df = df[((df['rsi'] < 60) & (df['rsi'] > 40)) | ((df['rsi'].shift(1) < 60) & (df['rsi'].shift(1) > 40))]


# filtered_df['price_change'] = filtered_df['c'] - filtered_df['o']

# filtered_df['color'] = filtered_df['price_change'].apply(lambda x: 'green' if x > 0 else 'red')

# filtered_df.to_csv("color.csv", index=False)

# print(filtered_df)


# with open('color.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         rsi = float(row['rsi'])  # Convert RSI value to float
#         print("RSI:", rsi)

#         if rsi > 60:
#             print("\n")
#         elif rsi < 40:
#             print("\n")


# with open('color.csv', newline='') as csvfile:
#     with open('output.csv', 'w', newline='') as outputfile:
#         reader = csv.DictReader(csvfile)
#         writer = csv.DictWriter(outputfile, fieldnames=reader.fieldnames)
        
#         writer.writeheader()  
        
#         for row in reader:
#             rsi = float(row['rsi'])  
#             print("RSI:", rsi)

#             writer.writerow(row)

#             if rsi > 60:
#                 outputfile.write('\n'+('*'*100)+'\n')
#             elif rsi < 40:
#                 outputfile.write('\n'+('*'*100)+'\n')


# with open('output.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
    
#     # Open the output CSV file for writing
#     with open('output_with_outcomes.csv', 'w', newline='') as outfile:
#         fieldnames = reader.fieldnames + ['outcome']  
#         writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#         writer.writeheader()
        
#         prev_color = None
        
#         # Iterate over each row
#         for row in reader:
#             color = row['color']
#             if prev_color is not None and color == prev_color:
#                 outcome = 'loss'
#                 print('loss')
#             else:
#                 outcome = 'win'
#                 print('win')
#             prev_color = color
            
#             # Add the 'outcome' to the row
#             row['outcome'] = outcome
            
#             # Write the row with the added outcome to the output CSV file
#             writer.writerow(row)
            
#             # Check if a new line is encountered
#             if '****************************************************************************************************' in row:
#                 prev_color = None
#                 print('\n')


















from backtestTools.histData import getEquityBacktestData
from datetime import datetime
import pandas as pd
import numpy as np
import talib
import csv



startDate = datetime(2018, 5, 1, 9, 15)
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
        # print("RSI:", rsi)

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
            # print("RSI:", rsi)

            writer.writerow(row)

            if rsi > 60:
                outputfile.write('\n'+('*'*200)+'\n')
            elif rsi < 40:
                outputfile.write('\n'+('*'*200)+'\n')




with open('output.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Open the output CSV file for writing
    with open('Alternative.csv', 'w', newline='') as outfile:
        fieldnames = reader.fieldnames + ['Alternative']  
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        prev_color = None
        
        # Iterate over each row
        for row in reader:
            color = row['color']
            if prev_color is not None and color == prev_color:
                Alternative = 'loss'
            elif prev_color is not None and color != prev_color:
                Alternative = 'win'
            else:
                # For the first row, there's no previous color to compare
                Alternative = 'None'
            prev_color = color
            
            # Create a new dictionary with the updated row information
            updated_row = {**row, 'Alternative': Alternative}
            
            # Write the updated row to the output CSV file
            writer.writerow(updated_row)




with open('Alternative.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Open the output CSV file for writing
    with open('outcomes.csv', 'w', newline='') as outfile:
        fieldnames = reader.fieldnames + ['YES_NO']  # Change column name to 'YES_NO'
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Initialize previous color and result
        prev_Alternative = None
        result = None
        
        # Iterate over each row
        for row in reader:
            Alternative = row['Alternative']
            
            if prev_Alternative == 'loss' and Alternative == 'loss':
                result = 'No'
                print('No')
            elif prev_Alternative == 'loss' and Alternative == 'win':
                result = 'Yes'
                print('Yes')
            else:
                result = 'None'
                print("None")
            
            # Update prev_Alternative
            prev_Alternative = Alternative
            
            # Write the row with the added outcome to the output CSV file
            writer.writerow({**row, 'YES_NO': result})  # Change column name to 'YES_NO' and write it directly to the row






# Open the input CSV file for reading
with open('outcomes.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Open the output CSV file for writing
    with open('Final.csv', 'w', newline='') as outfile:
        fieldnames = reader.fieldnames + ['outcomes']  # Add 'outcomes' field
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Initialize previous outcome and result
        prev_outcome = None
        result = None
        
        # Iterate over each row
        for row in reader:
            outcome = row['YES_NO']
            
            if prev_outcome == 'No' and outcome == 'No':
                result = 'B'
                print('B')
            elif prev_outcome == 'No' and outcome == 'Yes':
                result = 'A'
                print('A')
            else:
                result = 'None'
                print('None')
            
            # Update prev_outcome
            prev_outcome = outcome
            
            # Add the 'outcomes' to the row
            row['outcomes'] = result
            
            # Write the row with the added outcome to the output CSV file
            writer.writerow(row)















# Define function to count outcomes
def count_outcomes(csv_file):
    A_count = 0
    B_count = 0

    # Open and read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            outcomes_Count = row.get('outcomes'.strip())

            if outcomes_Count == 'A':
                A_count += 1
            elif outcomes_Count == 'B':
                B_count += 1

    return A_count, B_count

# Define function to count Yes and No
def count_YesNO(csv_file):
    Yes_count = 0
    No_count = 0

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            YesNO_Count = row.get('YES_NO'.strip())

            if YesNO_Count == 'Yes':
                Yes_count += 1
            elif YesNO_Count == 'No':
                No_count += 1

    return Yes_count, No_count

# Define function to count alternatives
def count_alternatives(csv_file):
    win_count = 0
    loss_count = 0

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Alternative_Count = row.get('Alternative'.strip())

            if Alternative_Count == 'win':
                win_count += 1
            elif Alternative_Count == 'loss':
                loss_count += 1

    return win_count, loss_count

# Define function to count colors
def count_color(csv_file):
    red_count = 0
    green_count = 0

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            color_Count = row.get('color'.strip())

            if color_Count == 'red':
                red_count += 1
            elif color_Count == 'green':
                green_count += 1

    return red_count, green_count

# Path to the CSV file
csv_file_path = 'Final.csv'

# Call functions to count outcomes, Yes/No, alternatives, and colors
A_count, B_count = count_outcomes(csv_file_path)
Yes_count, No_count = count_YesNO(csv_file_path)
win_count, loss_count = count_alternatives(csv_file_path)
red_count, green_count = count_color(csv_file_path)

# Calculate probabilities
total_outcomes = A_count + B_count
total_YesNO = Yes_count + No_count
total_alternatives = win_count + loss_count
total_colors = red_count + green_count

# Prepare output string
output = f"Outcomes:\nA count: {A_count}\nB count: {B_count}\n\n" \
         f"Yes/No:\nYes count: {Yes_count}\nNo count: {No_count}\n\n" \
         f"Alternatives:\nwin count: {win_count}\nloss count: {loss_count}\n\n" \
         f"Colors:\nred count: {red_count}\ngreen count: {green_count}\n\n" \
         f"Probabilities:\nProbability of A: {A_count / total_outcomes}\nProbability of B: {B_count / total_outcomes}\n\n" \
         f"Probability of Yes: {Yes_count / total_YesNO}\nProbability of No: {No_count / total_YesNO}\n\n" \
         f"Probability of win: {win_count / total_alternatives}\nProbability of loss: {loss_count / total_alternatives}\n\n" \
         f"Probability of red: {red_count / total_colors}\nProbability of green: {green_count / total_colors}\n"

# Print the results
print(output)

# Save details to a text file
with open('results.txt', 'w') as file:
    file.write(output)



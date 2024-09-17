import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('data.json')

# #df.dropna(inplace = True)
# print(df)
# print("\nFillna empty cells\n")
# #x = 1247
# x = df["Calories"].mode()[0] #there may be multiple values with the most frequent appearance
# df.fillna({"Calories" : x}, inplace = True)
# # #df["Calories"] = df["Calories"].fillna(1247)
# print(df)

# print("\nFixing wrong format\n") #or just dropping the wrong line
# df.dropna(subset = "Steps", inplace = True)
# print(df)

# print("getting row 3")
# #print(df.loc[2])
# print(df.shape[0])

# print("correcting data") #creating rules
# for x in df.index:
#     if df.loc[x, "Age"] > 45:
#         df.loc[x, "Age"] = 45
#         #df.drop(x, inplace = True)

# # #print(df.duplicated()) #returns bool
# # df.drop_duplicates(inplace = True)
# print(df)

# print("Correlation")
# print(df[['Calories', 'Steps']].corr())


print("Plotting")
#df.plot()
#df.plot(kind = 'scatter', x = 'Calories', y = 'Steps')
#df.plot(kind = 'scatter', x = 'Age', y = 'Steps')
df["Calories"].plot(kind = 'hist')
plt.savefig("plot.pdf", format = "pdf")
plt.show()


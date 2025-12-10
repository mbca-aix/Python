# print(10)
# print('Hello world')

# 100

#   * 언패킹 연산자
aa= [10,20,30]

for v in aa:
    print(v)

for idx,v in enumerate(aa): #a는 튜플(인덱스,값)
    print(idx, v)
   


# import matplotlib.pyplot as plt
# import pandas as pd

# df= pd.read_excel('./files/team_score.xlsx')
# print(df.head())
# print(df['Unnamed: 0'])
# print(df['삼성'])

# plt.scatter(df['Unnamed: 0'], df['삼성'])
# #plt.boxplot([df['LG'], df['삼성']])
# plt.show()

# print(df.info())
# Q1= df['삼성'].quantile(0.25)
# Q3= df['삼성'].quantile(0.75)
# IRQ= Q3-Q1

# print(Q1)
# print(Q3)
# print(IRQ)

# aa= df[df['삼성'] > Q3+IRQ*1.5]
# print(aa)

# aa= df['삼성'] > Q3+IRQ*1.5
# print(aa)


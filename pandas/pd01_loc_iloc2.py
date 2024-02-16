import pandas as pd

data = [
    ["삼성", "1000", "2000"]
    , ["현대", "1100", "3000"]
    , ["LG", "2000", "500"]
    , ["아모레", "3500", "6000"]
    , ["네이버", "100", "1500"]
 
]

index = ["031", "059", "033", "045", "023"] # 인덱스는 스트링, 연산할 때 쓰는 데이터가 아니다.
columns = ["종목명", "시가", "종가"]

df = pd.DataFrame(data=data, index=index, columns=columns)

print(df)
#      종목명    시가    종가
# 031   삼성  1000  2000
# 059   현대  1100  3000
# 033   LG  2000   500
# 045  아모레  3500  6000
# 023  네이버   100  1500

df['시가'] = df['시가'].astype(int)
df['종가'] = df['종가'].astype(int)

print("================ 시가가 1100원 이상인 행을 모두 출력 ===================")
result = df.loc[df['시가'] >= 1100]
print(result)
print("================ 시가가 1100원 이상인 종가만 출력 ===================")
result = df.loc[df['시가'] >= 1100, '종가']
print(result)
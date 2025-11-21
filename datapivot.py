import pandas as pd
import numpy as np


import pandas as pd


file_path = './data/bangtantour_list.csv'

try:
    df = pd.read_csv(file_path)
    print("✅ 원본 데이터프레임 (상위 5개 행):")
    print(df.head())
    print("-" * 30)

    # 3. pivot_table() 함수를 사용하여 데이터 피벗

    pivot_df = pd.pivot_table(
        df,
        values='SalesAmount', # 테이블에 채워질 값으로 사용할 컬럼
        index='Region',        # 새로운 테이블의 인덱스(행)로 사용할 컬럼
        columns='Product',     # 새로운 테이블의 컬럼(열)로 사용할 컬럼
        aggfunc='sum',         # 값(values)에 적용할 집계 함수 (평균: 'mean', 합계: 'sum', 개수: 'count' 등)
        fill_value=0           # 결측값(NaN)을 대체할 값 설정 (여기서는 0으로)
    )

    print(pivot_df)

except FileNotFoundError:
    print(f"❌ 오류: 지정된 파일 경로 '{file_path}'에 파일이 없습니다. 파일 경로를 확인해 주세요.")
except Exception as e:
    print(f"❌ 오류 발생: {e}")


pivot_df.to_csv('pivot_table_results.csv', 
                encoding='utf-8', # 한글 등이 포함될 경우 인코딩 지정
                index=True)       # 행 레이블(인덱스)도 파일에 저장

print("✅ 'pivot_table_results.csv' 파일로 저장이 완료되었습니다.")
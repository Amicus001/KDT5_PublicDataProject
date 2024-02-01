import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

#데이터 로드
data = pd.read_excel('./data/전체재해현황및분석업종별.xlsx', index_col=(0,1), header = 1)
yearsdata = pd.read_excel('./data/입사근속기간별.xlsx', index_col=(0,1), header = (0,1))

#필요한 데이터만 뽑아보기
data = data['요양재해자수 (명)']

#print(type(data.loc[('운수·창고 및 통신업','통신업')]))

tongshinjobs = data.loc[('운수·창고 및 통신업','통신업')]
managementjobs = data.loc[('기타의 사업','시설관리및사업지원서비스업')]
tongshinyears = yearsdata.loc[('운수·창고 및 통신업','통신업')]
managementyears = yearsdata.loc[('기타의 사업','시설관리및사업지원서비스업')]

#print(type(tongshinjobs))
#업종별 전체재해자수를 근속기간별로 나눠서-> 근속기간별 요양재해자 비율 구하기.
tongshin_ratio = (tongshinyears/tongshinjobs)
management_ratio = (managementyears/managementjobs)

#시각화
# colorlist = ['#3395E5','#518EDB','#7088D2','#8F82C9','#AE7BC0','#CD75B7','#EC6FAE']
# colorlist2 = ['#0357C4','#276FCC','#4B87D4','#6F9FDD','#93B7E5','#B7CFEE','#DBE7F6']
title = ['통신업','시설관리및사업지원서비스업']
plt.figure(figsize=(10,10))
plt.bar(x = tongshin_ratio.index.get_level_values(1)[1:-1], height= tongshin_ratio.values[1:-1])
plt.title('통신업')
plt.tight_layout()
plt.show()
plt.figure(figsize=(10,10))
plt.bar(x = management_ratio.index.get_level_values(1)[1:-1], height= management_ratio.values[1:-1])
plt.title(['시설관리 및 사업지원 서비스업'])
plt.tight_layout()
plt.show()
plt.savefig('graphs/'+title+'.png', dpi=100)

# print(managementjobs.head(3))
# # print(tongshinjobs.head(3))
# print(tongshinjobs)
# print(managementjobs)













# #print(data.head())
# #0print(yearsdata.head())
# data_merged = pd.merge(data, yearsdata, how='inner', left_index=True, right_index=True)
# #print(data_merged.columns)
# #print(data_merged.loc['광업'])
# mining_drop= data_merged.loc['광업'].drop(labels = '소계')
# mining_drop = data_merged.loc['광업'].drop(labels = '분류불능')
#
# mining_drop.plot(kind = 'bar', rot=90, figsize=(20,6))
#
# print(mining_drop.head())
# plt.show()
#

#print(data_merged.head())
#data_merged.plot(kind='bar', rot=90, figsize=(20,6))


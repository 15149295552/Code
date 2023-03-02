'''
基于用户的协同过滤UCF
'''
import pandas as pd
import numpy as np

data = pd.read_json('../data_test/ratings.json')

login_user = 'Michael Henry'
sim_mat = data.corr()
#拿到登录用户和每个用户的相似度
sim_scores = sim_mat[login_user]
#删除自己和自己的相似度
sim_scores = sim_scores.drop(login_user)
#只拿到强相关的相似用户 0.6
sim_scores = sim_scores[sim_scores>0.6]
#声明一个字典，存储推荐列表数据
# {'电影1':[[打分1,.....],[相似度1,......]],
#  '电影2':[[打分1,.....],[相似度1,......],......}
rec_movies = {}

for sim_user,sim_score in sim_scores.items():
    #拿到每个相似用户看过的电影
    sim_moives = data[sim_user].dropna()
    for m,s in sim_moives.items():
        #判断当前电影登录用户是否看过
        if np.isnan(data[login_user][m]):
            if m not in rec_movies.keys():
                rec_movies[m] = [[],[]]
            rec_movies[m][0].append(s)
            rec_movies[m][1].append(sim_score)

rect_list = []
for i in rec_movies.items():
    scores = np.array(i[1])
    score = np.sum(scores[0] * scores[1])
    rect_list.append((i[0],score))
#对rect_list进行排序
res = sorted(rect_list,key=lambda x:x[1],reverse=True)
for i in res:
    print('推荐电影:{},推荐值:{}'.format(i[0],i[1]))
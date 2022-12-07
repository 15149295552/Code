'''
简单的基于ＵＣＦ的协同过滤
'''
import pandas as pd
import numpy as np

ratings = pd.read_json('../data_test/ratings.json')

#获取当前登录用户
login_user = 'Michael Henry'
#相似度矩阵(皮尔逊相关系数)
sim_mat = ratings.corr()
sim_score = sim_mat[login_user]
#删除自己
sim_score = sim_score.drop(login_user)
#过滤相似度
sim_score = sim_score[sim_score > 0.6]

#拿到相似用户都看过那些电影，以及对电影的打分
# {'电影A':[[打分1,打分2],[相似度1,相似度2]],......}
rec_movies = {}
for sim_user,score in sim_score.items():
    sim_movies = ratings[sim_user].dropna() #相似用户看过的全部电影
    for m,s in sim_movies.items():
        if np.isnan(ratings[login_user][m]):
            #没看过这部电影
            if m not in rec_movies:
                rec_movies[m] = [[],[]]
            #从理论上说,可以判断评分大于多少分的,在进行推荐
            rec_movies[m][0].append(s)
            rec_movies[m][1].append(score)

print(sorted(rec_movies.items(),
       key=lambda x:np.average(x[1][0],weights=x[1][1]),
       reverse=True))#降序排序







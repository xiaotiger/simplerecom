超级简单的基于kNN的协同过滤推荐
试验一下kNN推荐的基本思路，在数量很小的情况下，可以载入内存计算。
kNN的协同推荐分为基于用户相似的推荐和基于物品的推荐。
基于用户的推荐，基本思路是找到和你相似的用户，把他们购买的物品推荐给你。
基于物品的推荐，基本思路是找你你曾经购买的物品，把这些物品相似的物品推荐给你。
只是说明一下相应的流程和步骤。
基于kNN的系统过滤推荐分为三步：
（1） 构建数据模块。读取用户－物品评分矩阵。
（2） 计算相似矩阵。采用合适的相似度计算函数计算用户的相似度和物品的相似度。
（3） 计算推荐结果。通过相似度矩阵，计算可以推荐的候选，rank，取topN。

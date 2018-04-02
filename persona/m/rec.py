#encoding:utf8
import codecs
import numpy as np
import os

def get_id_to_name(fn):
    dic = {}
    with codecs.open(fn, 'r', encoding='utf8') as f:
        for line in f:
            items = line.strip().split('\t')
            dic[int(items[0])] = items[1]
    return dic

def get_name_to_id(fn):
    dic = {}
    with codecs.open(fn, 'r', encoding='utf8') as f:
        for line in f:
            items = line.strip().split('\t')
            dic[items[1]] = int(items[0])
    return dic

def get_topk_scores(k, scores):
    scores = [(i, scores[i]) for i in range(len(scores))]
    scores.sort(lambda x,y:-cmp(x[1], y[1]))
    return scores[:k]

def get_cos(x, y):
    return np.dot(x, y) / (np.linalg.norm(x)*np.linalg.norm(y))

def get_topk_match(k, id, data_mat):
    sim = [(i, get_cos(data_mat[i,:], data_mat[id,:])) for i in range(data_mat.shape[0]) if i != id]
    sim.sort(lambda x,y:-cmp(x[1], y[1]))
    return sim[:k]

def run():
    # read data
    user_to_id = get_name_to_id(os.path.dirname(os.path.realpath(__file__)) + '/user_id.txt')
    id_to_user = get_id_to_name(os.path.dirname(os.path.realpath(__file__)) + '/user_id.txt')

    attraction_to_id = get_name_to_id(os.path.dirname(os.path.realpath(__file__)) + '/attraction_id.txt')
    id_to_attraction = get_name_to_id(os.path.dirname(os.path.realpath(__file__)) + '/attraction_id.txt')

    M = len(user_to_id)
    N = len(attraction_to_id)

    data = np.zeros([M,N])

    with codecs.open(os.path.dirname(os.path.realpath(__file__)) + '/all_data.txt', 'r', encoding='utf8') as f:
        for line in f:
            items = line.strip().split('\t')
            if items[0] in user_to_id and items[1] in attraction_to_id:
                data[user_to_id[items[0]],attraction_to_id[items[1]]] = np.float(items[2])


    U,S,V = np.linalg.svd(data)

    total_S = np.sum(S)
    sum = 0
    for i in range(len(S)):
        sum += S[i]
        if sum >= total_S * 0.9:
            break

    S = S[:i]
    U = U[:, :i]
    V = V[:i, :]

    pred_mat = np.dot(np.dot(U, np.diag(S)), V)

    # recommend to user

    k = 10             # top k attractions
    user_id = 500      # for user_id

    scores = get_topk_match(k, user_id, pred_mat)

    pred_mat = pred_mat

    s = np.zeros(pred_mat.shape[1])

    for i in range(len(scores)):
        s = s + pred_mat[scores[i][0]]
    s = s / len(scores)

    rank = get_topk_scores(k, s)
    rank.sort(lambda x,y:cmp(x[0], y[0]))

    # rank_data is groundtruth of user_id
    rank_data = get_topk_scores(k, data[user_id,:])
    rank_data.sort(lambda x,y:cmp(x[0], y[0]))

    print "recommend attractions for ",user_id
    print rank
    return rank

'''
if __name__=="__main__":
    print("main")
    run()
'''


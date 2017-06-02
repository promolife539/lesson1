big_school_list=[{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [4,4,4,4,5]},
                     {'school_class': '5a', 'scores': [4,3,4,3,3]},{'school_class': '5a', 'scores': [3,3,3,3,3]}]
sum_shool_list=[]
for avg_scores in big_school_list:
    avg_class=avg_scores.get('scores')
    print(sum(avg_class)/len(avg_class))
    sum_shool_list.append(sum(avg_class)/len(avg_class))
print(sum(sum_shool_list)/len(sum_shool_list))
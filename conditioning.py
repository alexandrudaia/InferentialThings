class conditional_probs(object):
    def __init__(self,data):
        self.data=np.array(data)
        self.cats=[{} for  col  in  range(self.data.shape[1]-1)]
    def categories_dict(self):
        #makes a list of dictionaris  where  in  each dict  in added  categories  for  a particular columns
        for column in  range(self.data.shape[1]-1):
            self.cats[column]={elem:0 for elem in np.unique(self.data[:,column])}
    def conditioning(self):
        #reducing- get  reduces distribution
        for  i  in  range(len(self.cats)):
            for elem in self.cats[i]:
                reduced=self.data[self.data[:,i]==elem,self.data.shape[1]-1]
                self.cats[i][elem]=reduced/sum(reduced)
        #normalization to make it  prob
    def margins(self,I,D):
        #P(i,d)=d
        #
        ok=True
        
data=pd.read_csv(" /toytable.csv")
#data=data.drop(['Prob'],axis=1)
data=np.array(data)
c=conditional_probs(data)
 
c.categories_dict()
#c.cats brings [{'i0': 0, 'i1': 0}, {'d0': 0, 'd1': 0}, {'g1': 0, 'g2': 0, 'g3': 0}]
c.conditioning()
c.cats
#[{'i0': array([0.20999999999999996, 0.27999999999999997, 0.20999999999999996,
#         0.015, 0.07499999999999998, 0.20999999999999996], dtype=object),
#  'i1': array([0.626865671641791, 0.06069651741293532, 0.013930348258706466,
#         0.14925373134328357, 0.08955223880597016, 0.05970149253731343], dtype=object)},
# {'d0': array([0.17948717948717946, 0.2393162393162393, 0.17948717948717946,
#         0.3589743589743589, 0.034757834757834755, 0.007977207977207976], dtype=object),
#  'd1': array([0.03, 0.14999999999999997, 0.41999999999999993, 0.19999999999999996,
#         0.12, 0.07999999999999999], dtype=object)},
# {'g1': array([0.28187919463087246, 0.020134228187919465, 0.5637583892617449,
#         0.1342281879194631], dtype=object),
#  'g2': array([0.614484272128749, 0.16459400146305778, 0.08924652523774688,
#         0.13167520117044623], dtype=object),
#  'g3': array([0.44744318181818177, 0.44744318181818177, 0.019886363636363636,
#         0.08522727272727272], dtype=object)}]
#  

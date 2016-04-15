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
        
        

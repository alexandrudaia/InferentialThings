class joint(object):
    
    def __init__(self,train_df,discretize):
        self.train_df=train_df#sets  ds
 
        self.n_col=train_df.shape[1]+1
        self.n_rows=train_df.shape[0]
        self.discretize=discretize#boolean
        self.categories=[[] for  cat in  range(train_df.shape[1])]#list of  lists where in each list are feature cat
    def discretize(self):
        if self.discretize==True:
            print("Discretizing...")
            #self.train_df=discretized train 
            #TO DO 
        else:
            print("Features are discretized")
            
    def set_categories(self):
        if self.discretize==False:
            print("getting  categories")
            self.categories=[[np.unique(self.train_df[:,col])] for col in range(self.train_df.shape[1])]
         
        else:
            self.discretize()
            print("getting  categories ")
            #TO DO 
        #set  nrows 
        total_cat=0
        for cat in self.categories :
            total_cat=total_cat*len(cat)
        self.n_rows=total_cat
    def make_joint_function(self):
        if self.n_rows>4:
            print("creating df")
            #TO DO - return  some data structure
            """ignore   for now   creation   from  real   file, must add  computing things"""""
 
        
            
data=pd.read_csv("....toytable.csv")
data=data.drop(['Prob'],axis=1)
data=np.array(data)
j=joint(data,False)
j.set_categories()
j.categories

            
            
            
 

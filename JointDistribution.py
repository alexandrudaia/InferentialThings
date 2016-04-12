class joint(object):
    
    def __init__(self,train_df,discretize,num_bins):
        self.train_df=train_df#sets  ds
        self.num_bins=num_bins#number  of  categories for  discretization
        self.n_col=train_df.shape([1])+1
        self.n_rows=0
        self.discretize=discretize#boolean
        self.categories=[[] for  cat in  range(train_df.shapee[1])]#list of  lists where in each list are feature cat
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
            #FILL   IN   CATEGORIES  - TO DO 
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
class create_joint_probs(object):
    def __init__(self,train_df,structure_from_joint):
        print("making  joint probs")
        """for every  element   in big  ,,matrix'' like structure   must  make  it  the prob with some kind  of pattern
        matching"""
        
            
            
            
            
            
 

class createJoint(object):
    def __init__(self,train_data):
        self.data=np.array(train_data)#makes the data as array
    def  getJoint(self):
        """ must   bring  the  joint  distribution  like  in Distribution  video .
        This means that   if we  feed it  with  sme data set , will  give use  th   unique rows and  their  frequency
        , in order to  work   if  we  have  some other  data set  besided   toy example
        """ 
        #NOT  THIS  IS NOT    OWN  IMPLEMENTATION I FOUND  IT ON  SOME  FORUM BUT IS  VERY EFFICIENT 
        import collections
        d = collections.OrderedDict()
        a=self.data
        for a in A:
            t = tuple(a)
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
        result = []
        for (key, value) in d.items():
            result.append(list(key) + [value])
        B = np.asarray(result)
        # AT  LAST COLUMN  IN B ARE stored  the  occurences  bust divided them by  total cases
        prob= B[:,B.shape[1]-1]/self.data.shape[0]
        prob=prob.reshape(prob.shape[0],1)
 
        return np.hstack((B[:,:-1],prob))
                
                
                
        
        

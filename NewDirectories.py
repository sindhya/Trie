_end = '_end_'
def make_trie(words):
     root = dict()
     current_dict = root
     for word in words:         
         current_dict = current_dict.setdefault(word, {})
     current_dict = current_dict.setdefault(_end, _end)    
     return root
 
def in_trie(trie, words):
     current_dict = trie
     for word in words:
         if word in current_dict:             
             current_dict = current_dict[word]
         else:
             return False
     else:
         if _end in current_dict:
             return True
         else:
             return False
def insert_trie(trie,words):
    current_dict = trie
    parent = {}
    no_of_insert = 0
    for word in words:
        if word in current_dict:
            current_dict=current_dict[word]            
        else:
            current_dict = current_dict.setdefault(word,{})
            no_of_insert = no_of_insert + 1
    current_dict = current_dict.setdefault(_end, _end) 
    return trie,no_of_insert

words=[]
testcases=[]
with open ("input.txt") as fin , open("output.txt","w") as fout:
    TT = int(fin.readline().strip())
    for x in range(TT):
        words=[]
        testcases=[]
        root = make_trie('')
        
        (N,M)= fin.readline().strip().split(' ',1)
        N = int(N)
        M = int(M)
        

        for y in range(N):
            words.append(fin.readline().strip().split('/'))
        for z in range(M):
            testcases.append(fin.readline().strip().split('/'))
        
        for each_word in words:
            del each_word[0]
            root,no_of_insert=insert_trie(root,each_word)

        total_insert = 0 
        for current_test in testcases:
            del current_test[0]
            root,no_of_insert=insert_trie(root,current_test)
            total_insert+=no_of_insert
            
        fout.write("Case #" + str(x+1) +": "+str(total_insert)+'\n')
        
        
            
        
        


class TrieNode:

    def __init__(self, string):
        self.key = string
        self.end = False
        self.children = {}
        

class TrieDS:
    
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, string):
        node = self.root
        
        for lt in string:
            if lt in node.children:
                node = node.children[lt]
            else:
                new_node = TrieNode(lt)
                node.children[lt] = new_node
                node = new_node
    
        node.end = True
    
    def search(self, node, string):
        
        for lt in string:
            if lt in node.children:
                node = node.children[lt]
            else:
                return False
        
        return node
        
    def prefix_query(self, string):
        
        node = self.root
        
        split_strings = string.split() 
        
        first_word = ' '.join(split_strings[:-1])
        last_word = split_strings[-1]
        
        check_word = self.search(node, last_word)
        
        completed = []
        
        if check_word:
            t = self.prefix_complete(check_word, last_word)
            
            for suggestion in t:
                if first_word:
                    completed.append(first_word + ' ' + suggestion)
                else:
                    completed.append(first_word + '' + suggestion)
                
        else:
            return string
        
        return completed
        
    
    def prefix_complete(self, node, string):
        if node.end:
            yield string 
        
        for child in node.children:
            yield from self.prefix_complete(node.children[child], string + child)
            
        
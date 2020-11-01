from flask import Flask, make_response, jsonify
from flask_restful import Resource, Api, reqparse
from ds import TrieDS
import time

app = Flask(__name__)
api = Api(app)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


with open('7776palavras.txt', encoding='utf-8', errors='ignore')  as f:
    ptwords = f.readlines()

with open('master.txt', encoding='utf-8', errors='ignore')  as f:
    enwords = f.readlines()


portugueseTrie = TrieDS()
englishTrie = TrieDS()

for word in ptwords:
    portugueseTrie.insert(word.rstrip('\n'))

for word in enwords:
    englishTrie.insert(word.rstrip('\n').lower())
    

del ptwords
del enwords
      
class PrefixQuery(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('string', type=str, required=True)
        parser.add_argument('limit', type=int, default=15)
        parser.add_argument('lang', type=str, default='en')
        args = parser.parse_args()
        
        start_time = time.process_time()
        
        lang = args['lang']
        string = args['string']
        
        lang_dict = {
            "en": englishTrie, 
            "pt": portugueseTrie
        }

        trie = lang_dict[lang]
        
        suggestions = trie.prefix_query(string)

        limit = args['limit']
        
        elapsed_time = (time.process_time() - start_time)
        
        return jsonify({
            'candidates': suggestions[:limit],
            'elapsed_time': elapsed_time,
            'total_candidates': len(suggestions)
            })

api.add_resource(PrefixQuery, '/')


#if __name__ == '__main__':
#    app.run(debug=True)

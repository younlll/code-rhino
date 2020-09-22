def solution(words, queries):
    result = []
    trie_by_length = [Trie() for i in range(10001)]
    r_trie_by_length = [Trie() for i in range(10001)]
    for word in words:
        trie_by_length[len(word)].add(word)
        r_trie_by_length[len(word)].add(word[::-1])
    for query in queries:
        if query[0] != "?":
            result.append(trie_by_length[len(query)].search(query))
        else:
            query = query[::-1]
            result.append(r_trie_by_length[len(query)].search(query))
    return result


class Trie():
    head = dict()
    def add(self, word):
        curr = self.head
        for ch in word:
            curr.setdefault(ch,[0,{}])
            curr[ch][0] +=1
            curr = curr[ch][1]
    
    def search(self, word):
        curr = self.head
        for i in range(len(word)):
            if word[i] in curr.keys():
                if word[i+1] == '?':
                    return curr[word[i]][0]
                curr = curr[word[i]][1]
            else:
                return 0

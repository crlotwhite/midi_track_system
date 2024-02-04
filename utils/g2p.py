class G2P:
    def __init__(self):
        self.onsets = ['k0', 'kk', 'nn', 't0', 'tt', 'rr', 
                    'mm', 'p0', 'pp', 's0', 'ss', '', 
                    'c0', 'cc', 'ch', 'kh', 'th', 'ph', 'h0']
        self.vowels = ['aa', 'qq', 'ya', 'yq', 'vv', 'ee', 'yv', 
                    'ye', 'oo', 'wa', 'wq', 'wo', 'yo', 'uu', 
                    'wv', 'we', 'wi', 'yu', 'xx', 'xi', 'ii']
        self.codas = ['', 'kf', 'kk', 'ks', 'nf', 'nc', 'nh', 
                    'tf', 'll', 'lk', 'lm', 'lb', 'ls', 'lt', 
                    'lp', 'lh', 'mf', 'pf', 'ps', 's0', 'ss', 
                    'ng', 'c0', 'ch', 'kh', 'th', 'ph', 'h0']
    
    def rule1(self, words):
        return [self.jamo(word) for word in words]

    def rule2(self, words):
        for i in range(len(words)):
            o, v, c = words[i]
            if c.startswith('k'):
                c = 'kf'
            elif c.startswith('t') or c.startswith('c') or c.startswith('s'):
                c = 'tf'
            elif c.startswith('p'):
                c = 'pf'
            words[i] = (o, v, c)
        
        return words
    
    def rule3(self, words):
        pair = {
            'll': 'rr',
            'nf': 'nn',
            'mf': 'mm',
            'pf': 'p0',
            'kf': 'k0',
            'tf': 't0',
        }
        for i in range(len(words)-1):
            o, v, c = words[i]
            no, nv, nc = words[i+1]
            if no == '' and c in pair:
                no = pair[c]
                c = ''
                words[i] = (o, v, c)
                words[i+1] = (no, nv, nc)
                
        return words
    
    def jamo(self, char):
        if '가' <= char <= '힣':
            base = ord('가')
            offset = ord(char) - base
            oi = offset // 588
            vi = (offset - oi * 588) // 28
            ci = offset % 28
            
            onset = self.onsets[oi]
            vowel = self.vowels[vi]
            coda = self.codas[ci]
            
            return onset, vowel, coda
        else:
            raise ValueError
        
    def get_rules(self):
        rules = []
        for attr in dir(self):
            if attr.startswith('rule'):
                rules.append(getattr(self, attr))
        
        return rules
    
    def gen(self, words):
        rules = self.get_rules()
        if len(words) > 1:
            for rule in rules:
                words = rule(words)
        else:
            for rule in rules[:-1]:
                words = rule(words)
                
        return [','.join([w for w in word if w != '']) for word in words]
        

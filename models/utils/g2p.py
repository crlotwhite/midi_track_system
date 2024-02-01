class G2P:
    def role1(self, words):
        return [self.jamo(word) for word in words]

    def role2(self, words):
        for word in words:
            _, _, c = word
            if c != '':
                c = c # 가느다란물방울로 교체
            
        return words
    
    def role3(self, words):
        return words
    
    def jamo(char):
        if '가' <= char <= '힣':
            base = ord('가')
            onsets = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
            vowels = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
            codas = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
            
            offset = ord(char) - base
            oi = offset // 588
            vi = (offset - oi * 588) // 28
            ci = offset % 28
            
            onset = onsets[oi]
            vowel = vowels[vi]
            coda = codas[ci]
            
            return onset, vowel, coda
        else:
            return char
        
    def get_rules(self):
        rules = []
        for attr in dir(self):
            if attr.startswith('rule'):
                rules.append(getattr(self, attr))
        
        return rules
    
    def gen(self, words):
        rules = self.get_rules()
        for rule in rules:
            words = rule(words)
            
        return words

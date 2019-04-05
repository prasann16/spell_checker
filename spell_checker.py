class spell_checker:

    def __init__(self,filename):
        file = open(filename,'r')
        self.city_names = file.read().split('\n')
        self.city_names = self.city_names[:-1] # Removing last empty value in the list
        file.close()
        self.city_names_lower = [city.lower() for city in self.city_names]
        self.WORDS = self.city_names_lower

    def edits1(self,word):
        "All edits that are one edit away from `word`."
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]

        return set(deletes + transposes + replaces + inserts)

    def edits2(self,word):
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def candidates(self,word):
        "Generate possible spelling corrections for word."
        return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or self.known(self.edits3(word)) or ["No match found"])

    def known(self,words):
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in self.WORDS)

    def result(self,word):
        output_list = []
        for w in self.candidates(word.lower()):
            output_list.append(self.city_names[self.city_names_lower.index(w)])
        return output_list

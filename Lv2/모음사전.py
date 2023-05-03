def solution(word):
    moeum = "AEIOU"
    words = []
    
    def setWords(i, w):
        if i > 4 or w==word:
            return
        
        for j in range(len(moeum)):
            words.append(w + moeum[j])
            setWords(i+1, w + moeum[j])
    
    setWords(0, "")
    
    # return words.index(word) + 1
    return len(words)
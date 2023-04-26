def solution(phone_book):
    phoneBookDict = {pb:1 for pb in phone_book}
    
    for pb in phone_book:
        temp = ''
        
        for p in pb:
            temp += p
            
            if temp in phoneBookDict and temp!=pb:
                return False
    
    return True
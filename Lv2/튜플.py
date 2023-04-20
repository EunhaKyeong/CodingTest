def solution(s):
    s = s.replace('{', '').replace('}', '').split(',')
    s = {int(i): s.count(i) for i in set(s)}
    s = dict(sorted(s.items(), key=lambda x:x[1], reverse=True))
    
    return list(s.keys())
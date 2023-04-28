import re

def solution(skill, skill_trees):
    
    skill_trees = [re.sub('[^' + skill + ']', '', tree) for tree in skill_trees]
    skill_trees = [tree for tree in skill_trees if skill[0:len(tree)]==tree]    
             
    return len(skill_trees)
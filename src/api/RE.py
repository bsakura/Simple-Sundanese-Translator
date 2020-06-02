import re
def reg(text, pattern) :
    pattern_lower = pattern.lower()
    text_lower = text.lower()
    regex_pattern = r"(" + pattern_lower +")"
    result = re.findall(regex_pattern, text_lower)
    if len(result) > 0 :
        return text_lower.find(result[0])
    else : 
        return -1

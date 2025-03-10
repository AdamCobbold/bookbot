def word_count(text):
    seperated = text.split()
    return len(seperated)

def char_count(text):
    character_count = {}
    alt_text = text.lower()
    for chara in alt_text:
        if chara in character_count:
            character_count[chara] += 1
        else:
            character_count[chara] = 1
    return character_count

def sort_count(dic):
    return sorted(dic.items(), key=lambda x:x[1], reverse=True)
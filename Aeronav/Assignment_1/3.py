def find_req(string):
    word = ""
    all_words = []
    string = string + " "
    for i in range(0, len(string)):
        if(string[i] != ' '):
            word = word + string[i];  
        else:
            all_words.append(word);  
            word = "";  
          
    small = large = all_words[0];  
   
    for k in range(0, len(all_words)):
        if(len(small) > len(all_words[k])):
            small = all_words[k]
        if(len(large) < len(all_words[k])):
            large = all_words[k]
    return small,large
import nltk
import random
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def paraphrase(tree: str, limit: int):
    tokens = nltk.word_tokenize(tree)
    tagged = nltk.pos_tag(tokens)
    check_list = ['NNP', ',', 'CC']
    damp_dict = {}
    result_dict = {}
    damp_list = []
    shuffled_list = []
    list_of_index = []
    saved_list_of_index = []
    index_value = 0
    counter = 0
    z = 0
    
    
    #filters NNP and ads it to dict where key: index of item in original sentence, item: item AND create list where add indexes of filtered items
    for item in tagged:
        in_memory = tagged.index(item)
        if item[1] == check_list[0] and tagged[in_memory + 1][1] in check_list:
            counter += 1
            if counter < 2:
                damp_dict.update({in_memory: item})
                index_value += 1
                damp_list.append([in_memory])
            elif counter == 2:
                damp_dict.update({in_memory - 1: tagged[in_memory - 1], in_memory: item})
                damp_list[index_value - 1].append(in_memory)
                counter = 0
    
    while limit > 0:
        #randomized shuffling to create unique combinations of indexes and ading in specified list
        static_list = damp_list.copy()
        random.shuffle(static_list)
        if static_list != damp_list:
            if static_list not in shuffled_list:
                shuffled_list.append(static_list)

        copy_of_damp_dict = damp_dict.copy()
        
        #filtering unique combinations from list and push it in copy of original dict to change items you get with the same key
        for i in shuffled_list:
            x = 0
            if i not in saved_list_of_index:
                saved_list_of_index.append(i)
                for j in i:
                    for k in j:
                        if k not in list_of_index:
                            list_of_index.append(k)
                for key in copy_of_damp_dict:
                    copy_of_damp_dict.update({key: damp_dict[list_of_index[x]]})
                    x += 1

        list_of_index.clear()

        copy_of_tagged = tagged.copy()
        
        #creates new unique variant of original sentence
        for i in tagged:
            y = tagged.index(i)
            if y in copy_of_damp_dict:
                copy_of_tagged[y] = copy_of_damp_dict[y]
        if copy_of_tagged not in result_dict.values() and copy_of_tagged != tagged:
            result_dict.setdefault(z, copy_of_tagged)
            z += 1
        limit -= 1

    return result_dict

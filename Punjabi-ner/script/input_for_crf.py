import pandas as pd
import nltk
import jsonlines


def unigram_for_crf(lst):
    # unigram
    word_list = []
    tag_list = []
    sentence_no_list = []
    for list_ in range(0, len(lst)):
        nested_list = []
        nested_tag = []
        nested_word_list = lst[list_]['data'].split(' ')
        for itr in range(0, len(lst[list_]['label'])):
            word_indices = lst[list_]['label'][itr][:-1]
            # print(lst[list_]['label'][itr][:-1])
            # print(lst[list_]['data'][word_indices[0]:word_indices[1]])
            nested_list.append(lst[list_]['data'][word_indices[0]:word_indices[1]])
            # print('sentence no - ',list_)

            # print(lst[list_]['label'][itr][-1:])
            nested_tag.append(lst[list_]['label'][itr][-1:][0])
        # print(len(nested_list), len(nested_tag), nested_tag)
        print(nested_word_list)
        print(nested_list)
        for split_token in (nested_word_list):
            for tagged_token_itr in range(0, len(nested_list)):
                if split_token == nested_list[tagged_token_itr]:
                    print(split_token)
                    word_list.append(nested_list[tagged_token_itr])
                    sentence_no_list.append(list_)
                    tag_list.append(lst[list_]['label'][tagged_token_itr][-1:][0])
                # else:
                #   word_list.append(split_token)
                #   sentence_no_list.append(list_)
                #   tag_list.append('UNKNOWN')
    df = pd.DataFrame(
        {'Words': word_list,
         'Ner_tags': tag_list,
         'Sentence_no': sentence_no_list
         })
    df.to_csv('/home/bavalpreet/PycharmProjects/Punjabi-ner/data/input_to_crf/unigrams.csv')
    return print(len(word_list), len(tag_list), len(sentence_no_list))


def generate_bigram(sent):
    sentence = sent
    words = sentence.split()
    list_of_bigram = []
    for tup in list(nltk.bigrams(words)):
        uni_0 = str(tup[0])
        uni_1 = str(tup[1])
        # print(uni_0, uni_0)
        list_of_bigram.append(str(uni_0 + ' ' + uni_1))
    return list_of_bigram


def bigrams_for_crf(lst):
    # bigram
    word_list = []
    tag_list = []
    sentence_no_list = []
    for list_ in range(0, len(lst)):
        nested_list = []
        nested_tag = []
        nested_word_list = generate_bigram(lst[list_]['data'])
        for itr in range(0, len(lst[list_]['label'])):
            word_indices = lst[list_]['label'][itr][:-1]
            # print(lst[list_]['label'][itr][:-1])
            # print(lst[list_]['data'][word_indices[0]:word_indices[1]])
            nested_list.append(lst[list_]['data'][word_indices[0]:word_indices[1]])
            # print('sentence no - ',list_)

            # print(lst[list_]['label'][itr][-1:])
            nested_tag.append(lst[list_]['label'][itr][-1:][0])
        # print(len(nested_list), len(nested_tag), nested_tag)
        print(nested_word_list)
        print(nested_list)
        for split_token in (nested_word_list):
            for tagged_token_itr in range(0, len(nested_list)):
                if split_token == nested_list[tagged_token_itr]:
                    print(split_token)
                    word_list.append(nested_list[tagged_token_itr])
                    sentence_no_list.append(list_)
                    tag_list.append(lst[list_]['label'][tagged_token_itr][-1:][0])
                # else:
                #   word_list.append(split_token)
                #   sentence_no_list.append(list_)
                #   tag_list.append('UNKNOWN')
    df = pd.DataFrame(
        {'Words': word_list,
         'Ner_tags': tag_list,
         'Sentence_no': sentence_no_list
         })
    df.to_csv('/home/bavalpreet/PycharmProjects/Punjabi-ner/data/input_to_crf/bigrams.csv')
    return print(len(word_list), len(tag_list), len(sentence_no_list))


if __name__ == "__main__":
    with jsonlines.open(
            '/home/bavalpreet/PycharmProjects/Punjabi-ner/data/anmol/batch1/annotations/0_200_admin.jsonl',
            'r') as jsonl_f:
        lst = [obj for obj in jsonl_f]
    unigram_for_crf(lst)
    bigrams_for_crf(lst)
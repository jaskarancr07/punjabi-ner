import json
import pickle
import random
import json

final = []


def input_data_for_spacy(input_file_path, output_file_path,entity_types):
    with open(str(input_file_path), encoding='utf-8-sig') as f:
        b = [line.split('\n', 1) for line in f]
        for i in range(len(b)):
            temp = json.loads(b[i][0])
            # print(temp['text'])
            if temp['label']:
                ent_res = [tuple(x) for x in temp['label'] if x[2] in entity_types]
            else:
                ent_res = []
            dictionary_f_tup = {'entities': ent_res}
            temp_tuple = (temp['data'], dictionary_f_tup)
            # print(temp_tuple)
            final.append(temp_tuple)
    with open(str(output_file_path), "wb") as fp:
        pickle.dump(final, fp)
    return print('data is ready for ingestion to spacy model')


if __name__ == "__main__":
    input_data_for_spacy(
        '/home/jaskaran/PycharmProjects/Punjabi-ner/data/2_merged_file_new.jsonl',
        '/home/jaskaran/PycharmProjects/Punjabi-ner/data/spacy_input/batch2_merged_file.pkl',
        ['DATE','LANGUAGE','LOCATION','ORG','PERSON','QUANTITY'])

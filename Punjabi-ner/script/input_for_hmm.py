import json
import pickle
from tqdm import tqdm
final = []
def input_data_for_hmm(input_file_path, output_file_path):
    with open(str(input_file_path), encoding='utf-8-sig') as f:
        b = [line.split('\n', 1) for line in f]
        for i in tqdm(range(len(b))):
            temp = json.loads(b[i][0])
            ls = []
            if temp['label']:
                start = 0
                for label in temp['label']:
                    end = label[0]
                    for ele in temp['data'][start:end].split(' '):
                        if ele:
                            ls.append((ele, None))
                    ls.append((temp['data'][label[0]:label[1]], label[2]))
                    start = label[1]
                if temp['label'][-1][1]<len(temp['data']):
                    for ele in temp['data'][temp['label'][-1][1]:].split(' '):
                        if ele:
                            ls.append((ele,None))
            else:
                for ele in temp['data'].split(' '):
                    if ele:
                        ls.append((ele, None))
            final.append(ls)
    with open(str(output_file_path), "wb") as fp:
        pickle.dump(final, fp)
    return print('data is ready for ingestion to hmm model')


if __name__ == '__main__':
    input_data_for_hmm('/home/jaskaran/PycharmProjects/Punjabi-ner/data/1_merged_file_clean.jsonl',
        '/home/jaskaran/PycharmProjects/Punjabi-ner/data/hmm_input/1_merged_file.pkl')
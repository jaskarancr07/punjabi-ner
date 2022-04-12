import pickle
import json


def count_back_space(str1):
    no_end_spaces = 0
    for i in range(len(str1) - 1, -1, -1):
        if str1[i] == ' ':
            no_end_spaces += 1
        else:
            break
    return no_end_spaces

def count_start_space(str1):
    no_start_spaces = 0
    for i in range(0,len(str1),1):
        if str1[i] == ' ':
            no_start_spaces += 1
        else:
            break
    return no_start_spaces


def clean_merge_data(input_file_path, output_file_path):
    result = []
    with open(str(input_file_path), encoding='utf-8-sig') as f:
        b = [line.split('\n', 1) for line in f]
        for i in range(len(b)):
            temp = json.loads(b[i][0])
            if temp['label']:
                new_label_ls = []
                for label_ls in temp['label']:
                    label_txt = temp['data'][label_ls[0]:label_ls[1]]
                    end_space_count = count_back_space(label_txt)
                    start_space_count = count_start_space(label_txt)
                    new_label_ls.append([label_ls[0]+start_space_count,label_ls[1]-end_space_count,label_ls[2]])
                temp['label'] = new_label_ls
            result.append(temp)



    with open(output_file_path,'w', encoding='utf-8-sig') as outfile:
        # json.dump(result, outfile)
        # write each line as a json
        outfile.write("\n".join(map(json.dumps, result)))
        return print('success')





if __name__ == "__main__":
    clean_merge_data(
        '/home/jaskaran/PycharmProjects/Punjabi-ner/data/1_merged_file.jsonl',
        '/home/jaskaran/PycharmProjects/Punjabi-ner/data/1_merged_file_clean.jsonl')
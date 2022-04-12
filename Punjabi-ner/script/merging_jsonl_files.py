# combining the batch files into one file for individual annonator
import json
import glob


def combine_batchfile_annonatorwise(name, batch_no):
    annonator_name = str(name)
    batch = str(batch_no)
    result = []
    for f in glob.glob(
            "/content/drive/MyDrive/punjabi-text/punjabi_ner_data/" + annonator_name + "/batch1/annotations/*.jsonl"):
        with open(f, 'r', encoding='utf-8-sig') as infile:
            for line in infile.readlines():
                try:
                    result.append(json.loads(line))  # read each line of the file
                except ValueError:
                    print(f)

    # This would output jsonl
    with open(
            '/home/bavalpreet/PycharmProjects/Punjabi-ner/data/annonator_wise_combined_data/' + annonator_name + '_' + batch + '_merged_file.jsonl',
            'w', encoding='utf-8-sig') as outfile:
        # json.dump(result, outfile)
        # write each line as a json
        outfile.write("\n".join(map(json.dumps, result)))
    return print('success')


def consolidate_batch_wise(batch_no):
    batch = str(batch_no)
    result = []
    for f in glob.glob("/home/bavalpreet/PycharmProjects/Punjabi-ner/data/annonator_wise_combined_data/*.jsonl"):
        with open(f, 'r', encoding='utf-8-sig') as infile:
            for line in infile.readlines():
                try:
                    result.append(json.loads(line))  # read each line of the file
                except ValueError:
                    print(f)

    # This would output jsonl
    with open(
            '/home/bavalpreet/PycharmProjects/Punjabi-ner/data/consolidated_data/batch1/' + batch + '_merged_file.jsonl',
            'w', encoding='utf-8-sig') as outfile:
        # json.dump(result, outfile)
        # write each line as a json
        outfile.write("\n".join(map(json.dumps, result)))
        return print('success')


if __name__ == "__main__":
    for name in ['anmol', 'harjot', 'jasleen', 'navjot', 'rahul']:
        combine_batchfile_annonatorwise(name, '1')
    consolidate_batch_wise('1')

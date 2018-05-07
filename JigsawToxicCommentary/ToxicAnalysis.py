import csv;
import os;
import io;
import sys;

import nltk;
import shlex;

from pprint import pprint;

obscenities_full_path = 'Data/Obscenities.txt';
comments_full_path = '~/Documents/Kaggle/JigsawToxicCommentClassification/train_obscene.csv'

obscenities = {};

# nltk.download(); // invoke this one time to download all needed natural-language tool kit packages

def uprint(*objects, sep=' ', end='\n', file = sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# load look-up dictionaries
        
with io.open(obscenities_full_path, mode='r', encoding='utf-8-sig') as csv_in_file:
    # instantiate a CSV reader
    csv_reader = csv.reader(csv_in_file, delimiter=',', quotechar='"');

    rows = 0;
    # row-by-row
    for row in csv_reader:
        rows += 1;
        obscenities[row[0]] = row[0];

pprint(f'Obscenities: {obscenities.keys()}', depth=9);

if comments_full_path.startswith('~'):
    comments_full_path = os.path.normpath(os.path.expanduser(comments_full_path));

with io.open(comments_full_path, mode='r', encoding='utf-8-sig') as csv_in_file:
    # instantiate a CSV reader
    csv_dict_reader = csv.DictReader(csv_in_file, delimiter=',', quotechar='"');

    rows = 0;
    # row-by-row
    for row in csv_dict_reader:
        
        rows += 1;
        
        comment_text = row['comment_text'];
        comment_text_lc = comment_text.lower();
        comment_text_lc = comment_text_lc.replace('\\', '\\\\');
        comment_text_lc = comment_text_lc.replace("'", "\\'");
        comment_text_lc = comment_text_lc.replace('"', '\\"');
        uprint(f'row {rows}, comment_text_lc: {comment_text_lc}');
        
        split_matches = [];
        split_words = comment_text_lc.split();
        for word in split_words:
            if word in obscenities.keys():
                split_matches.append(word);
        uprint(f'row {rows}, split_matches: {split_matches}, split_words: {split_words}');
        
        shlex_matches = [];
        shlex_words = shlex.split(comment_text_lc);
        for word in shlex_words:
            if word in obscenities.keys():
                shlex_matches.append(word);
        uprint(f'row {rows}, split_matches: {split_matches}, shlex_words: {shlex_words}');
        
        # nltk_matches = [];
        # nltk_words = nltk.word_tokenize(comment_text_lc);
        # for word in nltk_words:
        #     if word in obscenities.keys():
        #         nltk_matches.append(word);
        # uprint(f'row {rows},  nltk_matches: {ntlk_matches},  nltk_words: {nltk_words}');
        
print('Processing completed!')

#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv;
import os;
import io;
import re;
import sys;

import operator;
import nltk;
import shlex;

from pprint import pprint;

obscenities_full_path = 'Data/Obscenities.txt';
non_obscene_full_path = '~/Documents/SCOWL/final/english-words.95';
cleansed_words_full_path = 'Data/CleansedWords.txt';
comments_full_path = '~/Documents/Kaggle/JigsawToxicCommentClassification/train_obscene.csv'
build_obscenities = True;
output_cleansed_words = True;

obscenities = {};
non_obscenities = {};
cleansed_words = {};

# nltk.download(); // invoke this one time to download all needed natural-language tool kit packages

def uprint(*objects, sep=' ', end='\n', file = sys.stdout):
    enc = file.encoding;
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file);
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc);
        print(*map(f, objects), sep=sep, end=end, file=file);

def unpunctuate(value):
    
    value = value.replace('"','') \
                 .replace('!','') \
                 .replace('#','') \
                 .replace('$','') \
                 .replace('^','') \
                 .replace('&','') \
                 .replace('%','') \
                 .replace("'","") \
                 .replace('(','') \
                 .replace(')','') \
                 .replace('*','') \
                 .replace('+','') \
                 .replace('=','') \
                 .replace('-','') \
                 .replace(',','') \
                 .replace('.','') \
                 .replace('_','') \
                 .replace('/','') \
                 .replace(':','') \
                 .replace(';','') \
                 .replace('<','') \
                 .replace('>','') \
                 .replace('[','') \
                 .replace(']','') \
                 .replace('{','') \
                 .replace('}','') \
                 .replace('|','') \
                 .replace('?','') \
                 .replace('@','') \
                 .replace('\\','') \
                 .replace('`','') \
                 .replace(',','') \
                 .replace('"','') \
                 .replace('~','') \
                 .replace('¯','') \
                 .replace('—','') \
                 .replace('£','') \
                 .replace('§','') \
                 .replace('¨','') \
                 .replace('©','') \
                 .replace('™','') \
                 .replace('´','') \
                 .replace('·','') \
                 .replace('¸','') \
                 .replace('–','') \
                 .replace('‘','') \
                 .replace('“','') \
                 .replace('⟲','') \
                 .replace('☺','') \
                 .replace('☻','') \
                 .replace('”','');
    value = re.sub('\d','', value);
    value = value.strip();
    return value;

# load look-up dictionaries

if not build_obscenities:        
    with io.open(obscenities_full_path, mode='r', encoding='ISO-8859-1') as csv_in_file:
        # instantiate a CSV reader
        csv_reader = csv.reader(csv_in_file, delimiter=',', quotechar='"');
    
        rows = 0;
        # row-by-row
        for row in csv_reader:
            rows += 1;
            obscenities[row[0]] = row[0];
    
    pprint(f'Obscenities: {obscenities.keys()}', depth=9);


if non_obscene_full_path.startswith('~'):
    non_obscene_full_path = os.path.normpath(os.path.expanduser(non_obscene_full_path));

with io.open(non_obscene_full_path, mode='r', encoding='ISO-8859-1') as csv_in_file:
    # instantiate a CSV reader
    csv_reader = csv.reader(csv_in_file, delimiter=',', quotechar='"');

    rows = 0;
    # row-by-row
    for row in csv_reader:
        rows += 1;
        non_obscenities[row[0]] = row[0];
        cleansed_words[row[0]] = row[0];

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
        # uprint(f'row {rows}, comment_text_lc: {comment_text_lc}');
        
        # split_words = comment_text_lc.split();
        
        shlex_words = shlex.split(comment_text_lc);
        for word in shlex_words:
            word = unpunctuate(word);
            if word != '':
                if not non_obscenities.get(word):
                    try:
                        obscenities[word] += 1;
                    except KeyError:
                        obscenities[word] = 1;
                if not cleansed_words.get(word):
                    cleansed_words[word] = word;
        
        #=======================================================================
        # nltk_words = nltk.word_tokenize(comment_text_lc);
        # for word in nltk_words:
        #     if not non_obscenities.get(word):
        #         try:
        #             obscenities[word] += 1;
        #         except KeyError:
        #             obscenities[word] = 1;
        #=======================================================================
        
    for key, value in sorted(obscenities.items(), key=operator.itemgetter(1), reverse=True):
        if value > 100:
            uprint(f'key: {key}, value: {value}');
            
    print(f'    Total obscenities: {len(obscenities)}');
    print(f'Total non-obscenities: {len(non_obscenities)}');

    if output_cleansed_words:

        if cleansed_words_full_path.startswith('~'):
            cleansed_words_full_path = os.path.normpath(os.path.expanduser(cleansed_words_full_path));
        
        with io.open(cleansed_words_full_path, mode='w', encoding='utf-8-sig') as csv_out_file:
            for key in sorted(cleansed_words.keys()):
                    csv_out_file.write(key + '\n');
            
print('Processing completed!')

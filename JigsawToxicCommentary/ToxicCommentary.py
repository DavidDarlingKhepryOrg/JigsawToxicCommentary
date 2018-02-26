import csv;
import io;
import os;

source_folder_path = '~/Documents/Kaggle/JigsawToxicCommentClassification';
target_folder_path = '~/Documents/Kaggle/JigsawToxicCommentClassification';

if source_folder_path.startswith('~/'):
    source_folder_path = 

# meanings and
# their column numbers
toxic = 2;
toxic_severe = 3;
obscene = 4;
threat = 5;
insult = 6;
identity_hate = 7;

# zero(0) means read an
# unlimited number of rows
max_rows = 0;

# create the requisite files and their corresponding writes
cleansed_file = io.open(target_folder_path + '/train_cleansed.csv', mode='w', encoding='utf-8');
cleansed_writer = csv.writer(cleansed_file, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL);

any_ones_file = io.open(target_folder_path + '/train_any_ones.csv', mode='w', encoding='utf-8');
any_ones_writer = csv.writer(any_ones_file, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL);

toxic_file = io.open(target_folder_path + '/train_toxic.csv', mode='w', encoding='utf-8');
toxic_writer = csv.writer(toxic_file, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL);

toxic_severe_file = io.open(target_folder_path + '/train_toxic_severe.csv', mode='w', encoding='utf-8');
toxic_severe_writer = csv.writer(toxic_severe_file, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL);

obscene_file = io.open(target_folder_path + '/train_obscene.csv', mode='w', encoding='utf-8');
obscene_writer = csv.writer(obscene_file, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL);

threat_file = io.open(target_folder_path + '/train_threat.csv', mode='w', encoding='utf-8');
threat_writer = csv.writer(threat_file, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL);

insult_file = io.open(target_folder_path + '/train_insult.csv', mode='w', encoding='utf-8');
insult_writer = csv.writer(insult_file, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL);

identity_hate_file = io.open(target_folder_path + '/train_identity_hate.csv', mode='w', encoding='utf-8');
identity_hate_writer = csv.writer(identity_hate_file, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL);


# open the train.csv file for reading with UTF-8 encoding
with open(source_folder_path + '/train.csv', mode='r', encoding='utf-8') as csv_in_file:
    # instantiate the CSV reader
    csv_reader = csv.reader(csv_in_file, delimiter=',', quotechar='"');
    rows = 0;
    # row-by-row
    for row in csv_reader:
        rows += 1;
        # if header row
        if rows == 1:
            cleansed_writer.writerow(row);
            any_ones_writer.writerow(row);
            toxic_writer.writerow(row);
            toxic_severe_writer.writerow(row);
            obscene_writer.writerow(row);
            threat_writer.writerow(row);
            insult_writer.writerow(row);
            identity_hate_writer.writerow(row);
        # otherwise
        else:
            # cleanse each column
            # of the row in question
            for i in range(len(row)):
                row[i] = row[i].replace('\n',' ').strip();
            # output to the cleansed file
            cleansed_writer.writerow(row);
            # column-by-column
            # starting at column 2 
            for i, text in enumerate(row):
                # if second column or greater
                # and the column value is not zero
                if i >= 2 and row[i] != '0':
                    # output to the any_ones file
                    any_ones_writer.writerow(row);
                    # don't read another column
                    break;
            if row[toxic] != '0':
                toxic_writer.writerow(row);
            if row[toxic_severe] != '0':
                toxic_severe_writer.writerow(row);
            if row[obscene] != '0':
                obscene_writer.writerow(row);
            if row[threat] != '0':
                threat_writer.writerow(row);
            if row[insult] != '0':
                insult_writer.writerow(row);
            if row[identity_hate] != '0':
                identity_hate_writer.writerow(row);
        if max_rows != 0 and rows >= max_rows:
            break;

# close the requisite files
cleansed_file.close();
any_ones_file.close();
toxic_file.close();
toxic_severe_file.close();
obscene_file.close();
threat_file.close();
insult_file.close();
identity_hate_file.close();
        
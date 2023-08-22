import os
from tkinter.filedialog import askdirectory
import shutil


def split_rows(main_path):
    rows = []
    files = os.listdir(main_path)
    for f in files:
        if f.endswith('.tiff'):
            row = f[0:3]
            row_folder = main_path + '/' + row
            if row not in rows:
                os.mkdir(row_folder)
                rows.append(row)
            shutil.move(main_path + '/' + f, row_folder + '/'+ f)


def split_columns(main_path):
    rows = os.listdir(main_path)
    for row in rows:
        row_folder = main_path + '/' + row
        files = os.listdir(row_folder)
        columns = []
        for file in files:
            column = file[3:6]
            column_folder = row_folder + '/' + column
            if column not in columns:
                os.mkdir(column_folder)
                columns.append(column)
            shutil.move(row_folder + '/' + file, column_folder + '/' + file)


def split_channels(main_path):
    rows = os.listdir(main_path)
    for row in rows:
        folders = dict()  # dictionary of columns to channel
        row_folder = main_path + '/' + row
        for subdir, dirs, files in os.walk(row_folder):
            for file in files:
                column = file[3:6]
                if column not in folders.keys():
                    folders[column] = []
                channel = file[13:16]
                channel_folder = subdir + '/' + channel
                if channel not in folders[column]:
                    folders[column].append(channel)
                    os.mkdir(channel_folder)
                #print(file, ' ', subdir, ' ', row, ' ', column)
                shutil.move(subdir + '/' + file, channel_folder + '/' + file)

if __name__ == '__main__':
    main_path = askdirectory(title='Select the folder where the files are')
    split_rows(main_path)
    split_columns(main_path)
    split_channels(main_path)

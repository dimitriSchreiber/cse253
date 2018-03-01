import numpy as np
import os


def dataloader(inputstring, train_percent):
    
    file = open(inputstring)
    text = file.readlines()
    file.close()

    text_array = np.asarray(text)

    #Creates list of each song
    indicies = np.where(text_array == '<start>\n') #Location of where each abc file starts
    data = []
    for i in range(len(indicies[0])):
        if i+1 == len(indicies[0]):
            #For the last abc file
            abc = text_array[indicies[0][i]:]
        else:
            abc = text_array[indicies[0][i]:indicies[0][i+1]]
        data.append(''.join(abc))

    #print(data[0])
    #print(data[1123])


        
    train_len = int(np.floor(len(data)*train_percent))
    validation_len = len(data) - train_len

    print(train_len)
    print(validation_len)

    np.random.seed(0)
    #Each index references to a single song
    indxs = np.asarray(range(len(data)))
    print(indxs)
    np.random.shuffle(indxs)
    print(indxs)

    temp = np.asarray(data)
    train_data = temp[indxs[0:train_len]]
    validation_data = temp[indxs[train_len:]]
    print(len(train_data))
    print(len(validation_data))
    
    train_ascii_vals = []
    validation_ascii_vals = []

    for songs in train_data:
        for chars in songs:
            train_ascii_vals.append(ord(chars))

    for songs in validation_data:
        for chars in songs:
            validation_ascii_vals.append(ord(chars))

    #Each character is a row in this notation
    onehot_train = np.eye(128)[train_ascii_vals]
    onehot_validation = np.eye(128)[validation_ascii_vals]


    
    return data, train_data, validation_data, onehot_train, onehot_validation
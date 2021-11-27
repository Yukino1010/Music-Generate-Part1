# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:45:39 2021

@author: s1253
"""

from music21 import converter, chord, note,environment
environment.set('musescoreDirectPNGPath', r'C:\Program Files\MuseScore 3\bin\MuseScore3.exe')

import os
import pickle
import numpy as np
from tensorflow.keras.utils import to_categorical

path = "./data/"
file_list = os.listdir(path)


dataset_name = 'data'
seq_len = 32
notes = []
durations = []
    
for file in file_list:
    file = "./{}/{}".format(dataset_name, file)
    
    original_score = converter.parse(file).chordify()
    
    score = original_score.transpose(0)
    
    
    notes.extend(['START'] * seq_len)
    
    durations.extend([0] * seq_len)
    
    
    for element in original_score.flat:
        
        if isinstance(element, chord.Chord):
            notes.append('.'.join(n.nameWithOctave for n in element.pitches))
            durations.append(element.duration.quarterLength)
    
        if isinstance(element, note.Note):
            if element.isRest:
                notes.append(str(element.name))
                durations.append(element.duration.quarterLength)
            else:
                notes.append(str(element.nameWithOctave))
                durations.append(element.duration.quarterLength)

#%%                

# save notes and durations
with open(r"preprocess/notes_org", 'wb') as f:
    pickle.dump(notes, f) 
with open(r"preprocess/durations_org", 'wb') as f:
    pickle.dump(durations, f)            

#print(len(notes))
            
sort_notes = sorted(set(notes))    
num_note = len(sort_notes)     
sort_duration = sorted(set(durations)) 
num_duration = len(sort_duration)


def create_lookups(element_names):
    # create dictionary to map notes and durations to integers
    element_to_int = dict((element, number) for number, element in enumerate(element_names))
    int_to_element = dict((number, element) for number, element in enumerate(element_names))

    return (element_to_int, int_to_element)


note_to_int, int_to_note = create_lookups(sort_notes)     
duration_to_int, int_to_duration = create_lookups(sort_duration)

lookups = [note_to_int, int_to_note, duration_to_int, int_to_duration]
 
with open(r"preprocess/lookup",'wb') as f:
    pickle.dump(lookups, f)
        
note_input = []
note_output = []
duration_input = []
duration_output = []   
 
for i in range(len(notes) - seq_len):
    note_in = notes[i:i+seq_len]
    note_out = notes[i+seq_len]
    note_input.append([note_to_int[char] for char in note_in])
    note_output.append(note_to_int[note_out])
    
    duration_in = durations[i:i+seq_len]
    duration_out = durations[i+seq_len-1]
    duration_input.append([duration_to_int[char] for char in duration_in])
    duration_output.append(duration_to_int[duration_out])
    
le = len(note_input)    
note_input = np.reshape(note_input, (le, seq_len))
duration_input = np.reshape(duration_input, (le, seq_len))

net_input = [note_input, duration_input]

note_out_cat = to_categorical(note_output, num_classes=num_note)
duration_out_cat = to_categorical(duration_output, num_classes=num_duration)
        
net_out = [note_out_cat, duration_out_cat]


with open(r"preprocess/input",'wb') as f:
    pickle.dump(net_input, f)
    

with open(r"preprocess/output",'wb') as f:
    pickle.dump(net_out, f)
            
            
            
            
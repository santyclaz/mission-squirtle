import librosa
import numpy as np

def compare_mfcc(file1, file2):
    print(f"Comparing {file1} and {file2}")

    mfcc1 = get_mfcc(file1)
    mfcc2 = get_mfcc(file2)

    # Calculate the difference between the two MFCC feature sets
    difference = np.linalg.norm(mfcc1 - mfcc2)

    print(f"MFCC difference: {difference}")
    if difference < 51:  # Adjust this threshold based on your needs
        msg = "MARINE MAMMAL SOUND... BEEP BEEP, ME REPEAT, MARINE MAMMAL SOUND... BEEP BEEP"
    else:
        msg = "NO MARINE MAMMAL SOUND... BEEP BEEP, I REPEAT, NO MARINE MAMMAL SOUND... BEEP BEEP"

    return msg

def get_mfcc(file_path):
    # Load audio file
    audio_data,sample_rate = librosa.load(file_path)

    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)

    # Return the mean of the MFCCs for comparison
    return np.mean(mfccs.T, axis=0)
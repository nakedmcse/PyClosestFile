# Closest File - find file with most matching words in the name for a given input filename
import re,os
delimiters = re.compile(r"[,;-_. ]")

# Get dictionary of words/occurances in string
def get_words(filename):
    retval = {}
    for word in delimiters.split(filename):
        word = word.lower()
        if word in retval.keys():
            retval[word] += 1
        else:
            retval[word] = 1
    return retval

# Get matching counts
def matching_count(orig_words,compare_words):
    matches = 0
    for word in orig_words.keys():
        if word in compare_words.keys() and orig_words[word] == compare_words[word]:
            matches += 1
    return matches

# Find closest matching file
received_filename = "[Judas][Dual Audio][FLAC][x264]Oda_Nobuna_no_Yabou_-_04.mkv"
media_directory = "/Users/walker/Movies/Anime/Oda Nobuna no Yabou [1080]"
closest_filename = ""
matches, max_matches = 0,0

received_words = get_words(received_filename)

for file in os.listdir(media_directory):
    matches = matching_count(received_words,get_words(file))
    if matches > max_matches:
        max_matches = matches
        closest_filename = file

print(f"{received_filename} --> {closest_filename}")
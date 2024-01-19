# Closest File - find file with most matching words in the name for a given input filename
import re,os
delimiters = re.compile(r"[,;-_. ]")

# Get dictionary of words/occurances in string
def get_words(filename):
    retval = {}
    for word in map(str.lower,delimiters.split(filename)):
        retval[word] = retval[word] + 1 if (word in retval) else 1         
    return retval

# Get matching counts
def matching_count(orig_words,compare_words):
    matches = 0
    for word in orig_words.keys():
        if word in compare_words and orig_words[word] == compare_words[word]:
            matches += 1
    return matches

# Find closest matching file
def closest_file(received,media_dir):
    closest_filename = ""
    matches, max_matches = 0,0

    received_words = get_words(received)

    for file in os.listdir(media_dir):
        matches = matching_count(received_words,get_words(file))
        if matches > max_matches:
            max_matches = matches
            closest_filename = file
    
    return closest_filename

# Main
received_filename = "[Judas][Dual Audio][FLAC][x264]Oda_Nobuna_no_Yabou_-_04.mkv"
media_directory = "/Users/walker/Movies/Anime/Oda Nobuna no Yabou [1080]"

print()
print(f"{received_filename} --> {closest_file(received_filename,media_directory)}")
print()
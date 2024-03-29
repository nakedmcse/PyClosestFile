# Closest File - find file with most matching words in the name for a given input filename
import re,os,Levenshtein
delimiters = re.compile(r"[-,;_. ]")

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

# Find closest matching file via Levenshtein
def closest_file_lev(received,media_dir):
    closest_filename = ""
    diffs, min_diffs = 0,99999

    for file in os.listdir(media_dir):
        diffs = Levenshtein.distance(received,file)
        if diffs < min_diffs:
            min_diffs = diffs
            closest_filename = file
    
    return closest_filename

# Main
received_filename1 = "[Judas][Dual Audio][FLAC][x264]Oda_Nobuna_no_Yabou_-_04.mkv"
received_filename2 = "[Judas][Dual Audio]Oda_Nobuna_no_Yabou_01_[FLAC][x264].mkv"
received_filename3 = "[Judas]Oda Nobuna no Yabou-10 [Dual Audio][FLAC][x264].mkv"
media_directory = "/Users/walker/Movies/Anime/Oda Nobuna no Yabou [1080]"

print()
print("Word Comparison")
print(f"{received_filename1} --> {closest_file(received_filename1,media_directory)}")
print(f"{received_filename2} --> {closest_file(received_filename2,media_directory)}")
print(f"{received_filename3} --> {closest_file(received_filename3,media_directory)}")
print()
print("Levenshtein Comparison")
print(f"{received_filename1} --> {closest_file_lev(received_filename1,media_directory)}")
print(f"{received_filename2} --> {closest_file_lev(received_filename2,media_directory)}")
print(f"{received_filename3} --> {closest_file_lev(received_filename3,media_directory)}")
print()
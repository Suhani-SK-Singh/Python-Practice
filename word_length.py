#Student name : Suhani
#Student number: 119220491

#Programs to:
#1. Find average word length in a file.
#2. Display lines (along with line numbers), in a file which differs
#   from the previous line.
#3. To copy the content of list of files into an output file.

def word_length(fname) :
    # Function finds the average word length of the file. Punctuation is ignored
    # while calculating the word length.

    # Argument :fname, the filename
    # Return value : avg_word_length, Average word length of the file

    file = open(fname, 'r')
    file_text = file.read()

    num_words = 0
    total_word_len = 0

    punctuation_mark = '?.:;"",!-\\\'<>@#$%^&*~`_(){}[]'
    words = file_text.split()

    for word in words :
        word = word.strip(punctuation_mark)
        num_words += 1
        total_word_len += len(word)

    avg_word_length = total_word_len / num_words
    file.close()
    return avg_word_length

def squeeze(filename) :
    # Prints each line of the file which differs from the previous line,
    # prefixed with its line number in the input file.

    # Argument : filename, the path of input file

    file = open(filename, 'r')

    previous_line = ''
    current_line = ''
    line_num = 0

    for current_line in file :
        line_num += 1
        if current_line != previous_line :
            print('[', line_num, ']', current_line)
        previous_line = current_line

    file.close()

def join_files(inputfilenames, outputfilename) :
    # Copy the contents of all files in the list inputfilenames
    # to the file outputfilename.

    # Arguments:
    # 1. inputfilenames : A list containing paths of files to merge
    # 2. outputfilename : Path of the merged output file
    output_file = open(outputfilename, 'w')

    for filename in inputfilenames :
        input_file = open(filename, 'r')
        file_text = input_file.read() + '\n'

        output_file.write(file_text)
        input_file.close()
    output_file.close()

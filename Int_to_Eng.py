
# Student name : Suhani
# Student number: 119220491
# date: 14th nov 2019

#Functon to_english :converts positive integer value 'n' into english words.
#Argument- Positive integer value 'n' less than 1000
#Return- English word for n value
num_to_word_1 = {
   1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', 6 : 'Six',
    7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten', 11 : 'Eleven',
    12 : 'Tweleve', 13 : 'Thirteen', 14 : 'Fourteen', 15 : 'Fifteen',
    16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen', 19 : 'Nineteen',
}

num_to_word_2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def str_small_num(number) :
    tens, ones = divmod(number, 10)
    ret_str = num_to_word_2[tens - 2]

    if ones == 0 :
        return ret_str
    return ret_str + ' ' + num_to_word_1.get(ones)

def to_english(n) :
    if n >= 1000 :
        return ('Please enter a positive number less than 1000')
    if n == 0 :
        return 'Zero'
    if n < 20 :
        return num_to_word_1.get(n)

    elif n >= 20 and n < 100 :
        return str_small_num(n)

    elif n >= 100 and n < 1000 :
        hundreds, ones = divmod(n, 100)
        retString = num_to_word_1.get(hundreds) + ' Hundred'

        if ones == 0 :
           return retString

        elif ones < 20 :
           return retString + ' and ' + num_to_word_1.get(ones)

        else :
            return retString + ' and ' + str_small_num(ones)



##Function determines if the given two strings are anagrams or not.
##Argument:two strings
##return : True if strings are anagram and False if they are not Anagrams.
def anagrams(s1, s2) :
    s1 = ''.join(i for i in s1 if i.isalnum()).lower()
    s2 = ''.join(i for i in s2 if i.isalnum()).lower()

    if len(s1) != len(s2) :
        return False

    count = {}
    for letter in s1 :
        if letter in count :
            count[letter] += 1

        else :
            count[letter] = 1

    for letter in s2 :
        if letter in count :
            count[letter] -= 1

        else :
            count[letter] = 1

    for k in count :
        if count[k] != 0 :
            return False

    return True


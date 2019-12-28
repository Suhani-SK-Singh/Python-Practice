# This program is calculating next value of syracuse seq by function (syracuse_fn) to finally generate the syracuse seq
# and return length and largest number of syracuse seq .It checks for longest sequence in range of number which it takes as input ,untill 1 and returns
# starting point and length of longest seq.

# Student name : Suhani
# Student number: 119220491
# date: 14th oct 2019

def syracuse_fn(n):
    """
    This Function takes input as Number and provides output as an integer next value of syracuse seq.

    Arguments:
    1. n :any number for which we have to find syracuse next value

    Return:
    2.Returns next value of syracuse sequence

    """

    if n % 2 == 0:
        n = n / 2
    else:
        n = (n * 3) + 1
    return (int(n))


def syracuse_seq(n):
    """
    This function takes input from the syracuse_fn and generates the syracuse sequence to return length and largest value of sequence

    Arguments:
    1. n : any number for which we have to find syracuse seq

    Return:
    2.Returns length and largest value of sequence.

    """
    syracuse_series = [n]

    while n != 1:
        n = syracuse_fn(n)
        syracuse_series.append(int(n))

    length = len(syracuse_series)
    syracuse_series.sort(reverse=True)
    largest = syracuse_series[0]
    return length, largest


def longest_seq(n):
    """
    This function takes input from syracuse_sequence and returns the starting point , sequence length of syracuse series having longest sequence by checking value in range 1 to n+1.

    Arguments:
    1. n :range of seracuse seq calculated.
    Return:
    2.Returns start point and seq length of sequence.

    """

    longest_value = {}
    for n in range(1, n + 1):
        output = syracuse_seq(n)
        longest_value[n] = output[0]
    start_point = max(longest_value, key=longest_value.get)
    sequence_length = longest_value.get(start_point)
    return start_point, sequence_length


















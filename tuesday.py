alist = ['this' , 'is', 'a', 'sentence', '.']

rev = [i[::-1] for i in alist]

print(alist[::-1]) 
print(str(rev))

# I couldn't figure out how to get it into one print statement. :(

def string_freq(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( string_freq('In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map'))

# i can't interact with the jupyter notebook so I was only
# able to get part of the sentence :(


def linear_search(nums_, x):

    for i in nums_:

        if nums_[i] == x:
            return i
        else:
            return -1

nums_ = [10,23,45,70,11,15]
x = 70

print(str(linear_search(nums_,x)))

# time complexity O/n
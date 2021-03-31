# "binary search"
# edited version of code by Petar Ivanov
# changes: 
#    rationalized variable names
#    part in seq rather than seq.find(part)==-1     <--- good
#    merged substr_in_all() into common_substr()    <--- good
#    extract seq_0 from seqs                <--- very good

# return first substring of given length that is found in all sequences?
def common_substr(seq_0, seqs, length):
    # look at all possible substrings of a given 'length' 
    for start in range(len(seq_0) - length + 1):
        part = seq_0[start:start+length]

        # as soon as you find a sequence that doesn't contain this substring move on to the next substring
        # otherwise return this substring
        # note: indicates that there is at least one common substring of this length
        for seq in seqs:
            if part not in seq:
                break
        else:
            return part
    return ""

def longest_common_substr(seqs):
    # pop seq_0 to reduce number of sequences to search and eliminate need to re-extract each time 
    seq_0 = seqs.pop(0)

    ## starting points for the bounds on the longest common substring used in the binary search ##
    left = 0
    # +1 added to allow entire sequence to be the longest common substring 
    right = len(seq_0) + 1

    # repeat until left and right are adjacent              
    #     use left + 1, because you've already eliminated the right most and you get an endless loop otherwise ...
    while left + 1 < right:
        # pick midpoint in lengths -- nb:  assumes integer math
        mid = (left + right) / 2

        # if any substring of length mid is common to all sequences 
        #    look for substrings of this length or longer
        # otherwise look for substrings of this length or less
        if common_substr(seq_0, seqs, mid) != "":
            left = mid
        else:
            right = mid

    return common_substr(seq_0, seqs, left)
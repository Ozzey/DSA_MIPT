# def prefix(sub,max_sub):
#     #Search for prefix-suffix
#     max_sub[0]
#     i = 1
#     while i < len(sub):
#         if sub[i] == sub[l]:
#             l += 1
#             max_sub[i] = l
#             i += 1
#         else:
#             if l != 0:
#                 l = max_sub[l - 1]
#             else:
#                 max_sub[i] = 0
#                 i += 1
#


def Search(sub, txt):

    max_sub = [0] * len(sub)
    #search for substring
    i = 0
    j = 0
    # prefix(sub,max_sub)
    while i < len(txt):
        if sub[j] == txt[i]:
            i += 1
            j += 1
        if j == len(sub):
            print("Index:", str(i - j))
            j = max_sub[j - 1]

        elif i < len(txt) and sub[j] != txt[i]:

            if j != 0:
                j = max_sub[j - 1]
            else:
                i += 1


txt = "bbaabb"
sub = "b"
Search(sub, txt)


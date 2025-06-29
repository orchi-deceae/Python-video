
##! Fill between
# def use1(t1, t2, t3, txt2, n):
#     t = t3 + t2 + t1
#     if t1 == 'n': 
#         n -= 1
#     if n: txt2 += 'hi'
#     if t == 'fgh': 
#         n += 1
#     txt2 += t1
#     return txt2, n

##! Worse (maybe)
# def use1(t1, t2, t3, txt2):
#     t = t3 + t2 + t1
#     n = 0
#     if t == 'fgh': n += 1
#     txt2 += t1
#     if n: txt2 += '<span>'
#     return txt2

# #! After (only)
# def use1(t1, t2, t3, txt_):
#     t = t3 + t2 + t1
#     txt_ += t1
#     if t == 'fgh': txt_ += '\n<span>'
#     if t == 'opq': txt_ += '</span>\n<span>'
#     if t == 'wxy': txt_ += '</span>\n<span>'
#     return txt_

#! Before (included)
def use1(t1, t2, t3, txt_):
    t = t3 + t2 + t1
    if t == 'fgh': txt_ += '\n<span>'
    if t == 'opq': txt_ += '</span>\n<span>'
    if t == 'wxy': txt_ += '</span>\n<span>'
    txt_ += t3
    return txt_


txt = 'abcdefghijklmnopqrstuvwxyz'
t1, t2, t3, txt_ = '', '', '', ''
for t in txt:
    t3 = t2
    t2 = t1 
    t1 = t
    txt_ = use1(t1, t2, t3, txt_)
txt = txt_
txt += t2 + t1 + '</span>'
print(txt)              
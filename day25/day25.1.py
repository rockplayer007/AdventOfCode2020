pub_key_c = 11349501
pub_key_d = 5107328

def find_loop(key):
    loop_size = 0
    subj_num = 7
    value = 1
    while value != key:
        loop_size += 1
        value *= subj_num
        value = value % 20201227
    return loop_size, value

def transform_subj(loop_size, subj_num):

    #subj_num = 7
    value = 1
    for i in range(loop_size):
        loop_size += 1
        value *= subj_num
        value = value % 20201227
    return value

loop_d, subj_d = find_loop(pub_key_d)
loop_c, subj_c = find_loop(pub_key_c)

print(transform_subj(loop_d, pub_key_c))
print(transform_subj(loop_c, pub_key_d))
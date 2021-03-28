#!/usr/bin/python3

def d2b(dec_num):
    return bin(dec_num)[2:]

def b2d(bin_num): # Takes a binary number as a string and returns a decimal int
    num = 0
    size = len(bin_num)
    for i in range(size):
        num += pow(2,size-1-i)*int(bin_num[i])
    return num

def even_square(num, size):
    return (num % size) + 1 

def odd_square(num, size):
    return size - (num % size)

def find_target_square(bin_num):
    size = len(bin_num)
    num = b2d(bin_num)
    if(num//size % 2 == 0):
        return even_square(num, size)
    else:   
        return odd_square(num, size)


def build_test_list(size): # Takes a factor of 2 as an argument, breaks otherwise
    test_list = []
    for i in range(2**size):
        test_list.join(d2b(i).zfill(size.bit_length()+1))
    return test_list

def test_square_find(size): # Takes a factor of 2 as an argument, breaks otherwise
    test_list = build_test_list(size)
    for i in test_list: 
        print(find_target_square(i))
 
def find_possible_moves(bin_num):
    print("Current square: %d" % find_target_square(bin_num))
    for i in range(len(bin_num)):
        new_num = flip_bit(bin_num,i)
        print("%s gives square: %d" %(new_num,find_target_square(new_num)))
    


def flip_bit(bin_num, position):
    new_num = ""
    for i in range(len(bin_num)):
        if(i == position):
            if(bin_num[i] == '1'):
                new_num += "0"
            elif(bin_num[i] == '0'):
                new_num += "1"
            else:
                print("Something went wrong: flip_bit")
        else:
            new_num += bin_num[i]

    return new_num



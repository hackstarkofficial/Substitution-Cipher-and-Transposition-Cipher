#!/usr/bin/python
# Python program to demonstrate Substitution Cipher & Transposition Cipher By M. Ahmed Talha

import math
import string

cipher_tc = []


def encryptFunction():
    all_letters = string.ascii_letters
    dict1 = {}
    plain_txt_tc = input("Write A Message To Encrypt : ")
    key = input(
        "Enter A Key in Decimal Value For Substitution Cipher To Encrypt Message: "
    )
    key = int(key)
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i + key) % len(all_letters)]
    cipher_txt = []
    for char in plain_txt_tc:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp = char
            cipher_txt.append(temp)
    cipher_txt = "".join(cipher_txt)
    dict2 = {}
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i - key) % (len(all_letters))]
    key = input(
        "Enter Key For Transposition Cipher in Alphabets Value To Encrypt Message: "
    )
    cipher = ""
    k_indx = 0
    plain_txt_tc_len = float(len(plain_txt_tc))
    plain_txt_tc_lst = list(plain_txt_tc)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(plain_txt_tc_len / col))
    fill_null = int((row * col) - plain_txt_tc_len)
    plain_txt_tc_lst.extend("_" * fill_null)
    matrix = [
        plain_txt_tc_lst[i : i + col] for i in range(0, len(plain_txt_tc_lst), col)
    ]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += "".join([row[curr_idx] for row in matrix])
        k_indx += 1
    print("Cipher Text in Transposition Cipher is :", end=" ")
    print(cipher)
    global cipher_tc
    cipher_tc = cipher
    encryptFunction.bye = cipher
    print("Cipher Text in Substitution Cipher is :", end=" ")
    return cipher_txt


def decryptFunction(cipher_txt_sc):
    decrypt_txt = []
    key_sc = input(
        "Enter Key For Substitution Cipher in Decimal Value To Decrypt Message: "
    )
    key_sc = int(key_sc)
    all_letters = []
    all_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict2 = {}
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i - key_sc) % (len(all_letters))]
    for char in cipher_txt_sc:
        if char in all_letters:
            temp = dict2[char]
            decrypt_txt.append(temp)
        else:
            temp = char
            decrypt_txt.append(temp)
    decrypt_txt = "".join(decrypt_txt)
    print("Decryped Message of Substitution Cipher is :", decrypt_txt)

    key = input(
        "Enter Key For Transposition Cipher in Alphabets Value To Decrypt Message: "
    )
    cipher = cipher_tc
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = "".join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot", "handle repeating words.")
    print("Decryped Message of Transposition Cipher is : {}".format(msg))


#  Main Program -->


cipher_txt_sc = []
cipher_txt_sc = encryptFunction()
print(cipher_txt_sc)
decryptFunction(cipher_txt_sc)

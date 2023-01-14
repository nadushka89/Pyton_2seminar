# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def rle_encode(data_input):
    encoding = ''
    count = 1
    if not data_input:
        return ''
    for ind in range(1, len(data_input)):
        if data_input[ind] == data_input[ind - 1]:
            count += 1
        else :
            if count == 1:
                encoding += data_input[ind - 1]
            else:
                encoding += str(count) + data_input[ind - 1]
                count = 1
    else:
        if count == 1:
            encoding += data_input[ind]
        else:
            encoding += str(count) + data_input[ind]
    return encoding

def rle_decode(data_output):
    decoding = ''
    count = ''
    for char in data_output:
        if char.isdigit():
            count += char
        else :
            if not count:
                decoding += char
            else: 
                decoding += int(count) * char
                count = ''
    return decoding
d = open ('start_file.txt','r')
encoded_result = rle_encode(d.readline()) 
print(encoded_result)
d.close()
data = open('encoded_res.txt', 'w')
data.writelines(encoded_result)
data.close()

text_rle=rle_decode(encoded_result)
print(text_rle)

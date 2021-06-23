

path_Enc_list = ['./result_22/Enc_record_22.txt', './result_27/Enc_record_27.txt',
                 './result_32/Enc_record_32.txt', './result_37/Enc_record_37.txt']
path_Dec_list = ['./result_22/Dec_record_22.txt', './result_27/Dec_record_27.txt',
                './result_32/Dec_record_32.txt', './result_37/Dec_record_37.txt']

with open('table.txt', 'w') as f:
    pass ##清空文件


for path_Enc, path_Dec in zip(path_Enc_list, path_Dec_list):
    with open(path_Enc) as f1:
        lines = f1.readlines()
    reverse_lines = reversed(lines)

    with open(path_Dec) as f2:
        reverse_lines_dec = reversed(f2.readlines())
        last_line = next(reverse_lines_dec)
        last_line = last_line.strip()
        last_line = last_line.split()
        dec_time = last_line[2]

    line_count = 1
    for line in reverse_lines:
        if line_count == 1:
            line1 = line.strip()
        if line_count == 4:
            line4 = line.strip()
        line_count += 1

    ##print(line1.split())
    ##print(line4.split())
    line1 = line1.split()
    line4 = line4.split()

                        
    with open('table.txt', 'a') as f3:
        for i in range(2, 6):
            f3.write(line4[i])
            f3.write('\t')
        f3.write(line1[2])
        f3.write('\t')
        f3.write(dec_time)
        f3.write('\n')

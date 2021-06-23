
file1 = 'result_22/Dec_record_22.txt'
file2 = 'result_27/Dec_record_27.txt'
file3 = 'result_32/Dec_record_32.txt'
file4 = 'result_37/Dec_record_37.txt'

files = [file1, file2, file3, file4]
CCLM_count = 0
PDLM_count = 0
MDLM_L_count = 0
MDLM_T_count = 0

for file in files:

    with open(file) as f1:
        lines = f1.readlines()

    for line in lines:
        #print(line)
        if line == 'CCLM_IDX\n':
            CCLM_count += 1
        elif line == 'MDLM_L_IDX\n':
            MDLM_L_count += 1
        elif line == 'MDLM_T_IDX\n':
            MDLM_T_count += 1
        elif line == 'PDLM\n':
            PDLM_count += 1
        
print('CCLM_IDX : ', CCLM_count)
print('PDLM : ', PDLM_count)
print('MDLM_L_IDX : ', MDLM_L_count)
print('MDLM_T_IDX : ', MDLM_T_count)

import tqdm 
import re 
import glob 
import json 

file_name = "sample_outputs/DB_2.text"

# text_file = open(file_name,'r')
# file_text = text_file.read()
# text_file.close()
# file_text = file_text.split('*BEGIN_TABLE_EXTRACTION')[0].split('\n')

file_1 = open('asdfasdf2.text', 'w')
header_arr = []
comment_update_action_arr = []
line_count = 0
with open(file_name,'r') as f:
    # file_1.write('hello')
    done = False
    i=0
    file_text = f.readlines()
    print(len(file_text[30]))
    for line in file_text: 
        # print(len(line))
        # line.split('\n')
        # file_text[i].split('\n')
        if i+1 < len(file_text):
            i+=1 
            if file_text[i].strip('\n') == 'Update':
                done = True 
                header = line 
                file_1.write('*HEADER*: ')
                file_1.write(header)
                file_1.write('\n')
                # file_text[i] = comment_update_action 
                comment_update_action_arr.append(file_text[i])
                file_1.write(file_text[i])
                file_1.write('\n')
            elif file_text[i].strip('\n') =='Comment' or file_text[i].strip('\n') == 'Action':
                comment_update_action_arr.append(file_text[i])
                file_1.write(line)
                # print(line, 'yes')
                file_1.write('\n')
                file_1.write('\n')
                file_1.write(file_text[i])
                file_1.write('\n')

            elif done == True: 
                if ':' in line and len(line.split(" ")) > 8 and (file_text[i-1].strip('\n') == 'Comment' or file_text[i-1].strip('\n') == 'Update' or file_text[i-1].strip('\n') == 'Action'): 
                    subheader = line.split(":")[0]
                    # print(line)
                    print(subheader)
                    # first_line = line.split(":")[1]
                if len(line.split(" ")) > 5: 
                    file_1.write(line)
                    # print(line,'no')
                    # line_count+=1 
                if 'Action\n' in comment_update_action_arr and len(line) < 7: 
                    # file_1.write(line)
                    file_1.write('\n *DONE*')
                    break 
# print(line_count)
file_1.close()


# file_= open('main_text.text','w')

# header_arr = []
# comment_update_action_arr = []
# i=0 
# done = False
# print(len(file_text))


# for line in file_text: 
#     i+=1 
#     if file_text[i] == 'Update':
#         done = True 
#         header = line 
#         file_.write('*HEADER*: ')
#         file_.write(header)
#         file_.write('\n')
#         # file_text[i] = comment_update_action 
#         comment_update_action_arr.append(file_text[i])
#         file_.write(file_text[i])
#         file_.write('\n')
#     elif file_text[i] =='Comment' or file_text[i] == 'Action':
#         comment_update_action_arr.append(file_text[i])
#         file_.write(file_text[i])
#         file_.write('\n')
#     if done == True: 
#         if ':' in line and len(line.split(" ")) > 8 and file_text[i-1] == 'Comment' or file_text[i-1] == 'Update' or file_text[i-1] == 'ACtion': 
#             subheader = line.split(":")[0]
#             print(line)
#             print(subheader)
#             # first_line = line.split(":")[1]
#         if len(line.split(" ")) > 8: 
#             file_.write(line)
#         if 'Action' in comment_update_action_arr and len(file_text[i].split(" ")) < 3: 
#             file_.write(line)
#             file_.write('\n *DONE*')
#             break


# reference 

# with open (file_name, 'r') as fh: 
    # total_text = file_name.split('*BEGIN_TABLE_EXTRACTION')

    # total_txt = list(fh) 
    # total_txt = [x.strip('\n') for x in total_txt]
    # tmp = []
    # for line in total_txt: 
    #     dict1 = {}
    #     for idx, val in enumerate(line): 
    #         dict1[total_txt[0][idx]] = line[idx]
    #     tmp.append(dict1)
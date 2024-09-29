'''
Module for utility functions
'''
import os

def get_script_insights(filename):
    code_file = open(filename, 'r')
    
    #grabbing all lines of code for analysis
    all_lines = []
    file_data = {}
    with code_file as f:
       all_lines = f.readlines()
    code_file.close()  

    #look for initial introduction comment
    comment_string = ""
    if all_lines[0] == "'''\n":
        for x in range(1, len(all_lines)):
            if all_lines[x] == "'''\n":
                break
            else:
                comment_string += f"{all_lines[x]}"
    
    file_data['description'] = comment_string

    all_tags = []
    #looking for tags, noting that tags can only be used once    
    for x in range(0, len(all_lines)):
        if all_lines[x].startswith('#tags\n') or all_lines[x].startswith('# tags\n'):
            tag_line = all_lines[x+1]
            all_tags = tag_line[1:len(tag_line)].strip().split(',')
            break
    
    all_context = [all_lines[y+1][1:len(all_lines[y+1])] for y in range(0, len(all_lines)) if all_lines[y].startswith('#context\n') or all_lines[y].startswith('# context\n')]
    print(all_context)
    
    file_data['tags'] = all_tags
    file_data['context'] = all_context

    return file_data




def show_all_script_files():
    file_data = []
    for each_item in os.listdir('./scripts'):
        if each_item.endswith('.py'):
            file_path = os.path.join('./scripts', each_item)
            file_insights = get_script_insights(file_path)
            data = {
                'filename': each_item,
                'description': file_insights['description'],
                'tags': file_insights['tags'],
                'context': file_insights['context']
            }
            file_data.append(data)
    return file_data

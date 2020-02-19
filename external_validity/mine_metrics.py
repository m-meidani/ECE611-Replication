import sqlite3
import re
import pickle


def rplFunc(matchedItems):
    return ''


def remove_comment(code):
    regex = r"#(.+)"
    CmtRemoved = re.sub(regex,
                        rplFunc,
                        code)
    matched = re.finditer(regex, code, re.MULTILINE)
    numOfCmts = sum(1 for _ in matched)
    return CmtRemoved, numOfCmts


def countStrings(code):
    # code = code.replace(r'n', "") #cause \n cause error to regex
    # print(code);
    # return ""

    SQRegex = r"\'(.+?)\'"
    DQRegex = r"\"(.+?)\""
    matched = re.finditer(SQRegex, code, re.MULTILINE)
    DQinSQ = 0
    SQNo = 0
    for Str in matched:
        SQNo += 1
        # print(SQNo,':',Str.group())
        DQinSQ += sum(1 for _ in re.finditer(DQRegex,
                                             Str.group(), re.MULTILINE))
    matched = re.finditer(DQRegex, code, re.MULTILINE)
    SQinDQ = 0
    DQNo = 0
    for Str in matched:
        DQNo += 1
        # print(DQNo,':',Str.group())
        SQinDQ += sum(1 for _ in re.finditer(SQRegex,
                                             Str.group(), re.MULTILINE))
    return SQNo+DQNo-(DQinSQ+SQinDQ)


# table_name = 'old_new_puppet'
table_name = 'no_defect_puppets'

con = sqlite3.Connection('newdb.sqlite')
cur = con.cursor()
# cur.execute("SELECT * FROM {} WHERE TRIM(old_content)<>'' ".format(table_name))
cur.execute("SELECT * FROM {} WHERE TRIM(content)<>'' LIMIT 1719".format(table_name))

rows = cur.fetchall()
rowNumber = 0
print(rowNumber)
analytics = []

AllSums = {
    'Attribute': 0,
    'Command': 0,
    'Comment': 0,
    'Ensure': 0,
    'File': 0,
    'File_mode': 0,
    'Hard_coded_string': 0,
    'Include': 0,
    'Lines_of_code': 0,
    'Require': 0,
    'SSH_KEY': 0,
    'URL': 0,
    'defect_status':0
}
allMetrics = []
for row in rows:
    rowNumber += 1
    metrics = {}
    # fileContent = row[3]
    fileContent = row[2]
    metrics['ID'] = row[0]
    metrics['Attribute'] = fileContent.count('=>')
    metrics['Command'] = fileContent.count('cmd')
    _, metrics['Comment'] = remove_comment(fileContent)
    metrics['Ensure'] = fileContent.count('ensure')
    metrics['File'] = fileContent.count('file')
    metrics['File_mode'] = fileContent.count('mode')
    metrics['Hard_coded_string'] = countStrings(fileContent)
    metrics['Include'] = fileContent.count('include')
    metrics['Lines_of_code'] = fileContent.count("\n")
    metrics['Require'] = fileContent.count('require')
    metrics['SSH_KEY'] = fileContent.count('ssh_authorized_key')
    metrics['URL'] = fileContent.count('http://')+fileContent.count('https://')
    metrics['defect_status'] = 0
    for key in AllSums.keys():
        AllSums[key] += metrics[key]
    allMetrics.append(metrics)

f = open('./Dataset/ValidMinedData.pckl', 'wb')
pickle.dump(allMetrics, f)
f.close()    
print(AllSums)
print("metrics saved!")
# print(allMetrics)

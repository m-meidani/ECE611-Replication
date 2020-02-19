import re

def rplFunc(matchedItems):
    return '';
def remove_comment(code):
    regex = r"#(.+)"
    CmtRemoved = re.sub(regex,
        rplFunc,
        code);
    # print(matches);
    matched = re.finditer(regex, code, re.MULTILINE)
    numOfCmts = sum(1 for _ in matched)
    return CmtRemoved,numOfCmts

def countStrings(code):
    # code = code.replace(r'n', "") #cause \n cause error to regex
    # print(code);
    # return ""
    
    SQRegex = r"\'(.+?)\'"
    DQRegex=r"\"(.+?)\""
    matched = re.finditer(SQRegex, code, re.MULTILINE)
    DQinSQ=0;
    SQNo=0;
    for Str in matched:
        SQNo+=1
        # print(SQNo,':',Str.group())
        DQinSQ += sum(1 for _ in re.finditer(DQRegex, Str.group(), re.MULTILINE))
    matched = re.finditer(DQRegex, code, re.MULTILINE)
    SQinDQ=0;
    DQNo=0;
    for Str in matched:
        DQNo+=1
        print(DQNo,':',Str.group())
        SQinDQ += sum(1 for _ in re.finditer(SQRegex, Str.group(), re.MULTILINE))
    return SQNo+DQNo-(DQinSQ+SQinDQ)

def countLOC(code):
    return code.count("\n");
    
import sqlite3

table_name='old_new_puppet'

con = sqlite3.Connection('newdb.sqlite')
cur = con.cursor()
cur.execute("SELECT * FROM {} WHERE id='{}' ".format(table_name,'5bbce1f36d10f6a246167fd9391032b00bdf5a36'))

rows = cur.fetchall()
code = rows[0][3];
print(countLOC(code));
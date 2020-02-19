import csv
import sqlite3
import os
import sys
import time

table_name='no_defect_puppets'
clmns={
    'id':'varchar(50)',
    'size':'varchar(20)',
    'binary':'varchar(10)',
    'copies':'varchar(10)',
}

con = sqlite3.Connection('newdb.sqlite')
cur = con.cursor()


maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)


with open('./external_validity/valid-puppets.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    columns=spamreader.__next__()
    index=0;
    thrsh=100;

    query='CREATE TABLE if not exists "{}" ('.format(table_name);
    for clmn in columns:
        if clmn in clmns.keys():
            query = query+'"{}" {},'.format(clmn,clmns[clmn])
        else:
            query = query+ '"{}" TEXT,'.format(clmn)
    query=query.strip(',')+')'
    cur.execute(query);
    for row in spamreader:
        index=index+1
        insertValues='';
        for data in row:
            insertValues=insertValues+"','"+data.replace("'","''").strip();
        insertValues=insertValues
        query='INSERT INTO {} ({}) VALUES({});'.format(table_name,','.join(columns),"'"+insertValues.strip("','")+"'");
        # print(query);
        try:
            cur.execute(query);
        except:
            print(query);
            sys.exit();
        con.commit()
        # time.sleep(0.1);
print('{} record added successfully!'.format(index));
cur.close()
con.close()

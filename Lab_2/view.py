import sys, os
from psycopg2 import sql

class View(object):

    @staticmethod
    def show_tables(cursor):
            print('#'*20)
            for tab in cursor:
                for t in tab:
                    print(t,end='')
                print()
            print('#'*20)

    @staticmethod
    def show_table_columns(cursor,table):
        cur=cursor.fetchone()
        if cur!=None:
            os.system('cls')
            print("Columns of '{}' table:\n".format(table))
            print('#'*20)
            for c in cur:
                 print(c,end='')
            print()
            for tab in cursor:
                for t in tab:
                    print(t,end='')
                print()
            print('#'*20)
        else:
            os.system('cls')
            print("Can\'t write columns of '{}' table".format(table))
            
    @staticmethod
    def show_insert(table,columns,values,flag):
        if flag:
            print("Insert in '{}' table in '{}' columns this {} values".format(table,columns,values))
        else:
            print("Can\'t insert in '{}' table in {} columns this {} values".format(table,columns,values))

    @staticmethod
    def show_update(table,set,cond,flag):
        if flag:
            print("Update in '{}' table and set {} by {} condition".format(table,set,cond))
        else:
            print("Can\'t update in '{}' table and set {} by {} condition".format(table,set,cond))
    
    @staticmethod
    def display_delete(table, condition,flag):
        if flag:
            print("Delete in item(s) '{}' table by {} condition".format(table,condition))
        else:
            print("Can\'t delete in item(s) '{}' table by {} condition".format(table,condition))

    @staticmethod
    def rand_data(table,n_rows,flag):
        if flag:
            print("Add in '{}' table {} rows of random data".format(table,n_rows))
        else:
            print("Can't add in '{}' table {} rows of random data".format(table,n_rows))

    @staticmethod
    def select(columns , tables,cursor,time):
        if cursor!=None:
            print("Select {} column(s) in {} table(s) is done\n".format(columns,tables))
            for x in columns:
                print("%-25s" % x,end='')
            print()
            for cur in cursor:
                for c in cur:
                    print("%-25s" % c,end='')
                print()
            print("\nTime of execution: {} seс".format(time))
        else:
            print("Can't select {} column(s) in {} table(s)".format(columns,tables))
import sys, os
from psycopg2 import sql

class View(object):

            
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

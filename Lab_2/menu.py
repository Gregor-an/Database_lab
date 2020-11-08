import Controller as cont
import model as mod
import view 
import psycopg2 as pc
import sys, os


def layer_1():
    print("Choose category:\n")
    print("1.Tables")
    print("2.Insert")
    print("3.Update")
    print("4.Delete")
    print("5.Select")
    print("6.Random data")
    print("7.Readme")
    print("8.Exit")

def layer_2_tables(c):
    print("Tables:\nWrite table to see columns\n")
    c.tables()
    print("\nExit")

def layer_2_insert(c):
    print("Insert:(Write table to insert or 'Exit'):")
    ch=input();
    if ch=="Exit":
        return
    else:
        os.system('cls')
        tab=ch
        values=[]
        columns=[]
        print("Insert:(Write columns to insert into):")
        while True:
            ch=input()
            if len(ch)==0:
                break
            columns.append(ch)
        tmp=0
        count=1
        print("Insert:\nWrite values to insert {}:(\'string\')".format(count))
        while True:
            if tmp ==len(columns):
                os.system('cls')
                count=count+1
                print("Insert:\nWrite values to insert {}:(\'string\')".format(count))
                tmp=0
            ch=input()
            tmp=tmp+1
            if len(ch)==0:
                break
            values.append(ch)
        c.insert(tab,columns,values,len(columns))
        input()

def layer_2_update(c):
    print("Update:(Write table to update or 'Exit'):")
    ch=input();
    if ch=="Exit":
        return
    else:
        os.system('cls')
        tab=ch
        values=[]
        columns=[]
        print("Update:(Write columns and values):")
        while True:
            ch=input()
            if len(ch)==0:
                break
            v=input()
            columns.append(ch)
            values.append(v)
        os.system('cls')
        print("Update:(Write condition):(\"table_name\",\'string\') ")
        cond=input()
        c.update(tab,columns,values,cond)
        input()

def layer_2_delete(c):
    print("Delete:(Write table to delete from or 'Exit'):")
    ch=input();
    if ch=="Exit":
        return
    else:
        os.system('cls')
        tab=ch
        print("Delete:\nWrite condition or press 't' to delete all\nPress 'Enter' to return back:\n(\"table_name\",\'string\')")
        ch=input()
        if len(ch)==0:
            return
        cond=ch
        c.delete(tab,cond)
        input()

def layer_2_r_d(c):
    print("Random Data:(Write table to add data or 'Exit'):")
    ch=input();
    if ch=="Exit":
        return
    else:
        os.system('cls')
        tab=ch
        try:
            print("Random Data:\nHow much rows to add?")
            rows=int(input())
            print("\nPlease wait...")
        except:
            return
        c.rand_data(tab,rows)
        input()

def layer_2_select(c):
    os.system('cls')
    condition=""
    tables=[]
    columns=[]
    print("Select:\nWrite table(s) to select from:")
    while True:
        ch=input()
        if len(ch)==0:
            break
        tables.append(ch)
    os.system('cls')
    print("Select:\nWrite columns to select:(* to all)")
    while True:
        ch=input()
        if len(ch)==0:
            break
        columns.append(ch)
    os.system('cls')
    print("Select:(Write condition or press 'Enter' to skip):")
    condition = input()
    c.select(columns,tables,condition)
    input()

def help():
    os.system('cls')
    print("Integer ---- just number ----- 3")
    print("String ---- using ' ---- 'just_string'")
    print("Date ---- using ' ---- 'year-month-day'")
    print("Press anything to return")
    input()

def menu():
    conn=pc.connect(dbname='Blog', user='postgres', password='Egor2708', host='localhost')
    cur=conn.cursor()
    c = cont.Controller(mod.Model(cur,conn), view.View())
    while True:
        os.system('cls')
        layer_1()
        ch= input()
        if ch=="1":
            while True:
                os.system('cls')
                layer_2_tables(c)
                print("Write 'Exit' to roll back...")
                ch=input()
                if ch=="Exit":
                    os.system('cls')
                    break
                else:
                    c.columns_in_tab(ch)
                    print("Write any button to roll back...")
                    input()
        
        elif ch== "2":
            os.system('cls')
            layer_2_insert(c)

        elif ch== "3":
            os.system('cls')
            layer_2_update(c)

        elif ch=="4":
            os.system('cls')
            layer_2_delete(c)

        elif ch=="5":
            os.system('cls')
            layer_2_select(c)

        elif ch=="6":
            os.system('cls')
            layer_2_r_d(c)

        elif ch=="7":
            os.system('cls')
            help()

        elif ch=="8":
            os.system('cls')
            break
        else:
            os.system('cls')




    cur.close()
    conn.close()




def main():
    menu()


if __name__ == '__main__':
    main() 

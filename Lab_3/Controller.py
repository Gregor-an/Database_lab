import backend_sql as bs
import sys, os
import time

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def layer_1(self):
        print("Choose category:\n")
        print("1.Insert")
        print("2.Update")
        print("3.Delete")
        print("4.Exit")

    def layer_2_tables(self):
        print("Tables:\nWrite table to see columns\n")
        self.tables()
        print("\nExit")

    def layer_2_insert(self):
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
            self.insert(tab,columns,values,len(columns))
            input()

    def layer_2_update(self):
        print("Update:(Write table to update or 'Exit'):")
        ch=input();
        if ch=="Exit":
            return
        else:
            os.system('cls')
            tab=ch
            values=[]
            columns=[]
            v=[]
            print("Update:(Write columns and values):")
            while True:
                ch=input()
                if len(ch)==0:
                    break
                v=ch.split('=')
                columns.append(v[0])
                values.append(v[1])
            os.system('cls')
            print("Update:(Write condition):(\"table_name\",\'string\') ")
            cond=input()
            self.update(tab,columns,values,cond)
            input()

    def layer_2_delete(self):
        print("Delete:(Write table to delete from or 'Exit'):")
        ch=input();
        if ch=="Exit":
            return
        else:
            os.system('cls')
            tab=ch
            print("Delete:\nWrite condition or press 't' to delete all\nPress 'Enter' to return back:")
            ch=input()
            if len(ch)==0:
                return
            self.delete(tab,ch)
            input()


    def  menu(self):
        while True:
            os.system('cls')
            self.layer_1()
            ch= input()
            if ch=="1":
               os.system('cls')
               self.layer_2_insert()
        
            elif ch== "2":
                os.system('cls')
                self.layer_2_update()

            elif ch== "3":
                os.system('cls')
                self.layer_2_delete()

            elif ch=="4":
                os.system('cls')
                break
            else:
                os.system('cls')


    def insert(self,table,columns,values,count):
       try:
            
            for x in range(len(values)):
                if values[x].isdigit():
                    values[x]=int(values[x])
                
            ind=int(len(values)/count)
            
            self.view.show_insert(table,columns,values,self.model.insert(table,columns,values,ind))
       except:
            return
            
        

    def update(self,table,columns,values,condition):
        try:
            cond=[]
            if len(condition)!=0:
                cond=condition.split('=')
        
            for x in range(len(values)):
                if values[x].isdigit():
                        values[x]=int(values[x])
            self.view.show_update(table,values,condition,self.model.update(table,columns,values,cond))
        except:
            return

    def delete(self,table,condition):
        try:
            cond=[]
            if condition!='t':
                cond=condition.split('=')
            else:
                cond.append(condition)
            flag=self.model.delete(table,cond)
            self.view.display_delete(table, condition,flag)
        except:
            return

    def select(self, columns , tables, condition):
            col=""
            tab=""
            for x in range(len(columns)):
                if x==len(columns)-1:
                    if columns[0]=="*":
                        col=columns[0]
                    else:
                        col=col+"\"" + columns[x] + "\""
                else:
                    col=col+"\"" + columns[x] + "\""+", "
            for x in range(len(tables)):
                if x==len(tables)-1:
                    tab=tab + "\""+ tables[x]+ "\""
                else:
                    tab=tab + "\""+ tables[x]+ "\"" +","
            if len(condition)== 0:
                condition="\'t\'"

            col_view=[]
            if columns[0]=="*":
                for x in tables:
                    t = "\'" + x +"\'"
                    for y in self.model.columns_in_tab(t):
                        col_view.append(y[0])
            else:
                col_view=columns
            
            start_time = time.time()
            self.view.select(col_view , tab,self.model.select(col,tab, condition),time.time() - start_time)

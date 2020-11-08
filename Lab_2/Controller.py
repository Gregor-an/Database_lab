import backend_sql as bs
import sys, os
import time

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def tables(self):
        self.model.cursor=self.model.table()
        cur=self.model.cursor
        self.view.show_tables(cur)

    def columns_in_tab(self,table):
        tab = "\'" + table +"\'"
        self.model.cursor=self.model.columns_in_tab(tab)
        cur=self.model.cursor
        self.view.show_table_columns(cur,table)

    def insert(self,table,columns,values,count):
       try:
            tab = "\"" + table +"\""
            col=""
            val=""
            for x in range(len(columns)):
                if x==len(columns)-1:
                    col=col+"\"" + columns[x] + "\""
                else:
                    col=col+"\"" + columns[x] + "\""+", "
            for x in range(len(values)):
                if isinstance(values[x], str):
                    values[x]="\'" + values[x] + "\'"
            tmp=0
            ind=int(len(values)/count)
            for i in range(ind):
                val=val+'('
                for x in range(count):
                    if x==count-1:
                        val=val + values[tmp+x]
                    else:
                        val=val + values[tmp+x] +","
                if i ==ind-1:
                    val=val+')'
                else:
                    val=val+'),'
                tmp=tmp+count
            self.view.show_insert(table,columns,values,self.model.insert(tab,col,val))
       except:
            return
            
        

    def update(self,table,columns,values,condition):
        if len(condition)==0:
            condition="\'t\'"
        tab = "\"" + table +"\""
        set=""
        for x in range(len(values)):
            if isinstance(values[x], str):
                values[x]="\'" + values[x] + "\'"
        for x in range(len(columns)):
            if x==len(columns)-1:
                set=set+"\"" + columns[x] + "\""+"="+  values[x]
            else:
                set=set+"\"" + columns[x] + "\""+"="+ values[x] +", "
        
        
        self.view.show_update(table,set,condition,self.model.update(tab,set,condition))

    def delete(self,table,condition):
        table="\""+table+"\""
        if table == "\"Users\"":
            flag=self.delete_user(table, condition)
        elif table == "\"Posts\"":
            flag=self.delete_post(table, condition)
        elif table == "\"Comments\"":
            flag=self.delete_comment(table, condition)
        elif table == "\"Ratings\"":
            flag=self.delete_rating(table, condition)
        else:
            flag=False
           
        self.view.display_delete(table, condition,flag)

    def delete_user(self,table, condition):
        try:
            f1=self.model.delete("\"Ratings\"","\"UserIDFK\" in (select \"UserID\" from \"Users\" where "+condition+")"
                                +"or \"PostIDFK\" in (select \"PostID\" from \"Posts\" where "
                                + "\"UserIDFK\" in (select \"UserID\" from \"Users\" where "+condition+"))")
            f2=self.model.delete("\"Comments\"","\"UserIDFK\" in (select \"UserID\" from \"Users\" where "+condition+")"
                                +"or \"PostIDFK\" in (select \"PostID\" from \"Posts\" where "
                                + "\"UserIDFK\" in (select \"UserID\" from \"Users\" where "+condition+"))")
            f3=self.model.delete("\"Posts\"","\"UserIDFK\" in (select \"UserID\" from \"Users\" where "+condition+")")
            if f1 and f2 and f3:
                return self.model.delete("\"Users\"",condition)
            else:
                return False
        except:
            return False;

    def delete_post(self,table, condition):
        try:
            f1=self.model.delete("\"Ratings\"","\"PostIDFK\" in (select \"PostID\" from \"Posts\" where "+condition+")")
            f2=self.model.delete("\"Comments\"","\"PostIDFK\" in (select \"PostID\" from \"Posts\" where "+condition+")")
            if f1 and f2 :
                return self.model.delete("\"Posts\"",condition)
            else:
                return False
        except:
            return False;

    def delete_comment(self,table, condition):
        try:
           return self.model.delete("\"Comments\"",condition)
        except:
            return False;

    def delete_rating(self,table, condition):
        try:
           return self.model.delete("\"Ratings\"",condition)
        except:
            return False;

    def rand_data(self,table,n_rows):
        if table == "Users":
            fl=self.model.rand_data_users(n_rows)
        elif table == "Posts":
            fl=self.model.rand_data_posts(n_rows)
        else:
            fl=False 
        self.view.rand_data(table,n_rows,fl)

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
        

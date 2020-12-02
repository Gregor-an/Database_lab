import backend_sql as bs

class Model(object):

        def __init__(self):
            pass

        def insert(self,table, columns ,values, ind):
            if bs.insert_into(table, columns,values,ind):
                return True
            else:
                return False
                

        def update(self,table,columns,values,where_cond):
            if bs.update(table,columns,values,where_cond):
                return True
            else:
                return False

        def delete(self,table,condition):
            if bs.delete(table,condition):
                return True
            else:
                return False

       

import backend_sql as bs

class Model(object):

        def __init__(self, cursor,conn):
            self._cursor = cursor
            self._conn = conn
        
        @property
        def cursor(self):
            return self._cursor
        
        @cursor.setter
        def cursor(self, new_cursor):
            self._cursor = new_cursor

        @property
        def conn(self):
            return self._conn
        
        @conn.setter
        def conn(self, new_conn):
            self._conn = new_conn

        def insert(self,table, columns , values):
            if bs.insert_into(self._cursor,table, columns,values):
                self._conn.commit()
                return True
            else:
                self._conn.rollback()
                return False
                

        def update(self,table,set,where_cond):
            if bs.update(self._cursor,table,set,where_cond):
                self._conn.commit()
                return True
            else:
                self._conn.rollback()
                return False

        def delete(self,table,condition):
            if bs.delete(self._cursor,table,condition):
                self._conn.commit()
                return True
            else:
                self._conn.rollback()
                return False

        def rand_t(self,table,count):
            if table == "\"Users\"":
                bs.rand_data_users(self._cursor,self.conn,count)
            elif table == "\"Posts\"":
                bs.rand_data_posts(self._cursor,self.conn,count)
            self._conn.commit()
        
        def select(self, columns , tables, condition):
           return bs.select(self._cursor,self._conn,columns,tables,condition)
                
        def table(self):
            return bs.tables(self._cursor)

        def columns_in_tab(self,table):
            return bs.columns_in_tab(self._cursor,table)
            
        def rand_data_users(self,n_rows):
           return bs.rand_data_users(self._cursor,self._conn,n_rows)
       
        def rand_data_posts(self,n_rows):
           return bs.rand_data_posts(self._cursor,self._conn,n_rows)




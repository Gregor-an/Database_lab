from psycopg2 import sql

###################INSERT######################
def insert_into(cursor,table, columns , values):
    try:
        str= "INSERT INTO "
        str=str + table +' ('
        str=str+columns+') '
        str=str+' VALUES '+ values
          
        cursor.execute(sql.SQL(str))
        return True
    except Exception as err:
        print("Error {} ".format(err))
        return False

##############UPDATE###########################  
def update(cursor,table,set,where_cond):
     try:
        str="UPDATE "
        str= str + table
        str= str + ' set ' + set
        str= str + ' where '+ where_cond 
        cursor.execute(sql.SQL(str))
        return True
     except Exception as err:
        print("Error {} ".format(err))
        return False


#################DELETE#######################
def delete(cursor, table,condition):
    try:
        str='DELETE FROM '+ table +' where '+ condition
        cursor.execute(sql.SQL(str))
        return True
    except Exception as err:
        print("Error {} ".format(err))
        return False

##############################################

def rand_data_users(cursor,conn,n_rows):
    x=0
    while x < n_rows:
        x= r_d_u(cursor,x,conn)
        x=x+1
    return True
###########################################################
def r_d_u(cursor,x,conn):
    try:
        str_ind=""" select setval('\"Users_UserID_seq\"',(select max(\"UserID\") from \"Users\"));"""
        cursor.execute(sql.SQL(str_ind))
        conn.commit()
    except:
        conn.rollback()
        return x-1
    try:
        str_rand="""
        insert into "Users" ("Name","E-mail","Numbers of subscribers")
        values (
        (select substr(md5(random()::varchar), 0, 6)),
        (select substr(md5(random()::varchar), 0, 6)),
        (random()*100));"""
        cursor.execute(sql.SQL(str_rand))
    except Exception as err:
        conn.rollback()
        return x-1
    else:
        conn.commit()
    return x
 
def rand_data_posts(cursor,conn,n_rows):
        x=0
        while x < n_rows:
            x= r_d_p(cursor,x,conn)
            x=x+1
        return True
 
def r_d_p(cursor,x,conn):
    try:    
        str_ind=""" select setval('\"Posts_PostID_seq\"',(select max(\"PostID\") from \"Posts\"));"""
        cursor.execute(sql.SQL(str_ind))
        conn.commit()
    except:
        conn.rollback()
        return x-1
    try:
        str_rand="""
        insert into "Posts" ("Topic of the post","Post","Time of creating","UserIDFK")
        values (
        (select substr(md5(random()::varchar), 0, 6)),
        (select substr(md5(random()::text), 0, 10)),
		(select NOW() -
       	random() * (NOW() -
                   timestamp '2014-01-10 10:00:00')),
        (SELECT "UserID" FROM "Users" 
		 OFFSET floor(random()*(select count("UserID") from "Users")) LIMIT 1));"""
        cursor.execute(sql.SQL(str_rand))
    except Exception as err:
        conn.rollback()
        return x-1
    else:
        conn.commit()
    return x
#############################################################################

def select(cursor,conn, columns , tables, condition):
    try:
        str= "SELECT " + columns
        str = str + " FROM " + tables
        str = str + " WHERE " +condition
        cursor.execute(sql.SQL(str)) 
        return cursor
    except Exception as err:
        print("Error {} ".format(err))
        conn.rollback()
        return []

def tables(cursor):
    try:
        str= """
            SELECT DISTINCT TABLE_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_CATALOG = 'Blog' AND TABLE_SCHEMA = 'public'
            """
        cursor.execute(sql.SQL(str))
        return cursor
    except Exception as err:
        print("Error {} ".format(err))

def columns_in_tab(cursor,table):
    try:
        str= """
            SELECT column_name
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = """ + table
            
        cursor.execute(sql.SQL(str))
        return cursor
    except Exception as err:
        print("Error {} ".format(err))
        

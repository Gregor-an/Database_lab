import Controller as cont
import model as mod
import view 
import psycopg2 as pc
import sys, os



def main():

    
    #ed_user = User(Name='Bogdan', Email='LLLLLLLLS', N_sub=2225)
    #session.add(ed_user)
    #session.commit()
    c = cont.Controller(mod.Model(), view.View())
    c.menu()


if __name__ == '__main__':
    main() 

#////////////////////////////////////////////////////////////






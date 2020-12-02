import sqlalchemy as alch
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
#//////////////////////////////////////////////////////////////////////
eng = alch.create_engine('postgresql://postgres:Egor2708@localhost/Blog')
Base = declarative_base()
Base.metadata.create_all(eng)
Session = sessionmaker(bind=eng)
session = Session()

class Users(Base):
    __tablename__ = 'Users'
    UserID = Column(Integer,Sequence('Users_UserID_seq'), primary_key=True)
    Name = Column(String,nullable=False)
    Email = Column(String,nullable=False)
    N_sub = Column(Integer,nullable=False)

    posts=relationship("Posts",back_populates="users",cascade="all, delete-orphan")
    comments=relationship("Comments",back_populates="users",cascade="all, delete-orphan")
    ratings=relationship("Ratings",back_populates="users",cascade="all, delete-orphan")
    def __repr__(self):
       return "<User(name='%s', email='%s', n_sub='%s')>" % (
                            self.Name, self.Email, self.N_sub)

class Posts(Base):
    __tablename__ = 'Posts'
    PostID = Column(Integer,Sequence('Posts_PostID_seq'), primary_key=True)
    Topic = Column(String(60),nullable=False)
    Post = Column(Text,nullable=False)
    Time_create = Column(Date,nullable=False)

    UserIDFK = Column('UserIDFK',Integer,ForeignKey('Users.UserID',ondelete="CASCADE",onupdate="CASCADE"),nullable=False)
    users=relationship("Users",back_populates="posts")
    comments=relationship("Comments",back_populates="posts",cascade="all, delete-orphan")
    ratings=relationship("Ratings",back_populates="posts",cascade="all, delete-orphan")
    def __repr__(self):
       return "<Post(Topic='%s', Post='%s', Time_create='%s')>" % (
                            self.Topic, self.Post, self.Time_create)

class Comments(Base):
    __tablename__ = 'Comments'
    CommentID = Column(Integer,Sequence('Comments_CommentID_seq'), primary_key=True)
    Comment = Column(Text,nullable=False)
    Time_create = Column(Date,nullable=False)

    UserIDFK = Column('UserIDFK',Integer,ForeignKey('Users.UserID',ondelete="CASCADE",onupdate="CASCADE"),nullable=False)
    users=relationship("Users",back_populates="comments")
    PostIDFK = Column('PostIDFK',Integer,ForeignKey('Posts.PostID',ondelete="CASCADE",onupdate="CASCADE"),nullable=False)
    posts=relationship("Posts",back_populates="comments")

    def __repr__(self):
       return "<Comments(Comment='%s', Time_create='%s')>" % (
                            self.Comment, self.Time_create)

class Ratings(Base):
    __tablename__ = 'Ratings'
    RatingID = Column(Integer,Sequence('Ratings_RatingID_seq'), primary_key=True)
    Rating = Column(Text,nullable=False)
    Time_create = Column(Date,nullable=False)

    UserIDFK = Column('UserIDFK',Integer,ForeignKey('Users.UserID',ondelete="CASCADE",onupdate="CASCADE"),nullable=False)
    users=relationship("Users",back_populates="ratings")
    PostIDFK = Column('PostIDFK',Integer,ForeignKey('Posts.PostID',ondelete="CASCADE",onupdate="CASCADE"),nullable=False)
    posts=relationship("Posts",back_populates="ratings")

    def __repr__(self):
       return "<Ratings(Rating='%s', Time_create='%s')>" % (
                            self.Rating, self.Time_create)
###################INSERT######################

def insert_into(table, columns, values, ind):
    try:
        add_list=[]
        col_length=len(columns)
        count=0
        for i in range(ind):
            obj=eval(table)()
            for j in range(col_length):
                setattr(obj,columns[j],values[count]) 
                count+=1
            add_list.append(obj)
        session.add_all(add_list)
        session.commit()
        return True
    except Exception as err:
        print("Error {} ".format(err))
        session.rollback();
        return False


##############UPDATE Users###########################  
def update_table(samples,columns,values):
    col_length=len(columns)
    for i in range(col_length):
        for j in samples:
            setattr(j,columns[i],values[i]) 
    return samples


##############UPDATE#################################
def update(table,columns,values,where_cond):
     try:
        if len(where_cond)==0:
            samples=session.query(eval(table))
        else:
            samples=session.query(eval(table)).filter(getattr(eval(table),where_cond[0])==where_cond[1])

        samples=update_table(samples,columns,values)
        session.commit()
        return True
     except Exception as err:
        print("Error {} ".format(err))
        session.rollback();
        return False


#################DELETE#######################

def delete(table,where_cond):
    try:
        if len(where_cond)=='t':
            samples=session.query(eval(table)).delete()
        else:
            samples=session.query(eval(table)).filter(getattr(eval(table),where_cond[0])==where_cond[1]).delete()
        session.commit()
        return True
    except Exception as err:
        print("Error {} ".format(err))
        return False
###############################################


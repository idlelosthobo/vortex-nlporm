from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from vortex import models
from vortex.base import Base
import nltk


class Core:
    db_engine = None
    db_engine_type = None
    db_session = None

    def __init__(self):
        self.set_db_engine('sqlite')
        self.build_db()

        Session = sessionmaker(bind=self.db_engine)
        self.db_session = Session()

    def set_db_engine(self, db_engine_choice):
        if db_engine_choice == 'sqlite':
            self.db_engine_type = db_engine_choice
            self.db_engine = create_engine('sqlite:///:memory:', echo=True)

    def build_db(self):
        Base.metadata.create_all(self.db_engine, checkfirst=True)

    def add_sentence(self):
        new_information = models.Information(word='taco', sentence='bring me a dozen tacos')
        self.db_session.add(new_information)

    def get_sentence(self):
        old_sentence = self.db_session.query(models.Information).filter_by(word='taco').first()
        print(old_sentence)

    def read_sentence(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        print(tokens)
        tagged = nltk.pos_tag(tokens)
        print(tagged)
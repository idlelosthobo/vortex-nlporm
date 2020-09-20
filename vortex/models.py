from sqlalchemy import Column, String, Integer
from vortex.base import Base


class Information(Base):
    __tablename__ = 'Information'

    id = Column(Integer, primary_key=True)
    word = Column(String)
    sentence = Column(String)

    def __repr__(self):
        return 'Word: %s Sentence: %s' % (self.word, self.sentence)
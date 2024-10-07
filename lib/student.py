#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name, knowledge=[]):
        super().__init__(first_name, last_name)
        self._knowledge = knowledge

    @property
    def knowledge(self):
        return self._knowledge
    
    @knowledge.setter
    def knowledge(self, str):
        self._knowledge.append(str)

    def learn(self, str):
        return self._knowledge.append(str)
#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value   

    def get_value(self):
        return self._value

    def set_value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return True if self.value[-1] == '.' else False

    def is_question(self):
        return True if self.value[-1] == '?' else False

    def is_exclamation(self):
        return True if self.value[-1] == '!' else False

    def count_sentences(self):
        modified = self.value.replace('!', '.').replace('?', '.')
        return len([s for s in modified.split(". ") if len(s) > 0])

    value = property(get_value, set_value)

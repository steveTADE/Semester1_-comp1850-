# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """_summary_
        initialise this class with the necessary variables
        """
        if not isinstance(name, str) or not isinstance(birth, date):
            raise TypeError()
        # stripping it so " " won't pass as true
        elif name.strip() == '':
            raise ValueError
        self.name  = name
        self.birth = birth
    
    def is_birthday(self) -> bool:
        """_summary_

        Returns:
            bool: check if today's is this person's b-day
        """
        today = date.today()
        cond1 = self.birth.month == today.month
        cond2 = self.birth.day   == today.day
        #print(cond1 and cond2) # debug line
        return cond1 and cond2

    def initials(self) -> str:
        """_summary_

        Returns:
            str: return the initials of a person by using his name
        """
        # split the words by the space THEN get the first letter of each word
        output = ''.join(words[0] for words in self.name.split(" ")).upper()
        #print(output) # debug line
        return output
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

if __name__ == "__main__": # debug code
    # HAPPY BIRTHDAY AURA MONSTER
    Person("daniel", "2026-05-15").initials()  
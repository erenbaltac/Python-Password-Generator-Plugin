
class createRandomizedPassword:
    """
    For Creating Randomized Passwords

    WordList: Randomized Words, Leave Empty (None) If You Want All Words,Numbers And Symbols.

    Lenght: The Lenght Of Randomized Words In The Password

    Repeat: The Amount Of Randomized Passwords

    UppercaseCharacters: Make It True For Uppercase Letters

    LowercaseCharacters: Make It True For Lowercase Letters

    Numbers: Make It True For Numbers

    Symbols: Make It True For Symbols ('!', '@', '#', '$', '&', '*', '?')

    MoreSymbols: Make It True For MoreSymbols (';', ':', "'", '"', ',', '.', '<', '>', '/', '`', '~', etc.)
    """
    def __init__(self, CharacterList = [], LineBetweenTheCharacters='-', Lenght=10, Repeat=1, UppercaseCharacters=True, LowercaseCharacters=True, Numbers=True, Symbols=True, MoreSymbols=False, ):
        if CharacterList is None:
            CharacterList = []
        self.CharacterList = CharacterList
        self.Lenght = Lenght
        self.Repeat = Repeat
        self.UppercaseCharacters = UppercaseCharacters
        self.LowercaseCharacters = LowercaseCharacters
        self.Numbers = Numbers
        self.Symbols = Symbols
        self.MoreSymbols = MoreSymbols
        self.LineBetweenTheCharacters = LineBetweenTheCharacters

    def showPassword(self,AsString=True):
        """
          For Showing The Randomized Password

          AsString: If True Show the Password As A String
                    If False Show The Password As A List
        """
        import random

        Uppers = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        Lowers = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        Symbols = ['!', '@', '#', '$', '&', '*', '?']

        MoreSymbols = [ '%', '^', '(', ')'  '_', '=', '+', '[', ']', '{', '}', '\\', '|',
                        ';', ':', "'", '"', ',', '.', '<', '>', '/', '`', '~'
]


        if not self.CharacterList:
             if self.UppercaseCharacters:
                 self.CharacterList.extend(Uppers)
             if self.LowercaseCharacters:
                 self.CharacterList.extend(Lowers)
             if self.Numbers:
                 self.CharacterList.extend(Numbers)
             if self.Symbols:
                 self.CharacterList.extend(Symbols)
             if self.MoreSymbols:
                 self.CharacterList.extend(MoreSymbols)
        for R in range(0, self.Repeat):
            i = 0
            i2 = 0
            New_Password = []
            while i < self.Lenght:

                RandomInt = random.randint(0, len(self.CharacterList) -1)
                New_Password.append(self.CharacterList[RandomInt])
                i += 1
            while i2 <= len(New_Password):
                i2 += random.randint(2, 6)
                New_Password.insert(i2, '-')
            if AsString:
                New_Password = ''.join(New_Password)
            else:
                New_Password = New_Password

        return New_Password
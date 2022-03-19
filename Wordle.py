import pandas as pd

class wordle:

    def __init__(self, fname="OfficialWordList.csv", MaxGuesses=6):
        self.indexList = ["i", "j", "k", "l", "m"]
        self.MaxGuesses = MaxGuesses
        self.fname = fname
        self._WipeList = []
        self._FiltList = []
        self.WipeList = []
        self.ElimList = []
        self.PartList = []
        self.FiltList = []
        self.GuessWord = ""
        self.GuessDNA = ""
        self.wordleDF = pd.read_csv(self.fname)
        self.MaxWords = len(self.wordleDF)
        self.outputName = "List1.csv"
        self.guess = 1
        print(f"Starting 5-letter Wordle Filter with {self.MaxGuesses} maximum guesses. Reading data, please wait a moment...")

    def ListCreator(self):
        self.GuessWord = input("Enter the Guess Word:")
        self.GuessDNA = input("Enter the DNA sequence:")
        self.GuessWord = self.GuessWord.upper()
        self.GuessDNA = self.GuessDNA.upper()
        print(f"Guess: {self.GuessWord}, DNA = {self.GuessDNA}")
        self.WipeList = []
        self.ElimList = []
        self.PartList = []
        self.FiltList = []

        for i in range(len(self.GuessDNA)):
            letter = self.GuessWord[i]
            value = ord(letter) - 65
            if self.GuessDNA[i] == "G":
                self.FiltList.append((i, value))
                self._FiltList.append((i, value))
            elif self.GuessDNA[i] == "Y":
                self.PartList.append((i, value))
            elif self.GuessDNA[i] == "B":
                count = self.GuessWord.count(self.GuessWord[i])
                if(count == 1):
                    self.WipeList.append(value)
                    self._WipeList.append(value)
                else:
                    counter = 0
                    for j in range(len(self.GuessDNA)):
                        if self.GuessWord[j] == self.GuessWord[i]:
                            if (self.GuessDNA[j] == "Y" or self.GuessDNA[j] == "G"):
                                counter += 1
                    if counter == 0:
                        self.WipeList.append(value)
                        self._WipeList.append(value)
                    else:
                        self.ElimList.append((i, value))

    def Simulator(self):
        
        while(self.guess <= self.MaxGuesses and self.MaxWords > 1):
            self.ListCreator()
            print(f"Word Guess {self.guess}:")
            print(f"Round {self.guess}: WipeList = {self.WipeList}, ElimList = {self.ElimList}, PartList = {self.PartList}, FiltList = {self.FiltList}")

            # Green letters
            # Retain dataframe entries only if the green word
            # is present in the specified location
            for entry in self.FiltList:
                index, val = entry
                self.wordleDF = self.wordleDF[self.wordleDF[self.indexList[index]] == val]
            # print("After FiltList, number of possible answer(s) = ", len(self.wordleDF))

            # Yellow letters
            # Step 1: Remove dataframe entries if the yellow letter
            #         is present in the specified location.
            # Step 2: Retain words that have this character atleast once
            for entry in self.PartList:
                index, val = entry
                self.wordleDF = self.wordleDF[self.wordleDF[self.indexList[index]] != val]
                self.wordleDF = self.wordleDF[(self.wordleDF["i"] == val) | 
                                    (self.wordleDF["j"] == val) |
                                    (self.wordleDF["k"] == val) |
                                    (self.wordleDF["l"] == val) |
                                    (self.wordleDF["m"] == val)]
            # print("After PartList, number of possible answer(s) = ", len(self.wordleDF))

            # Black letters with possible repeats being Yellow or Green
            # Remove dataframe entries if the black letter
            # is present in the specified location
            for entry in self.ElimList:
                index, val = entry
                self.wordleDF = self.wordleDF[self.wordleDF[self.indexList[index]] != val]
            # print("After ElimList, number of possible answer(s) = ", len(self.wordleDF))
            
            # Black letters with no repeats or all repeats being black
            # Remove dataframe entries if the black letter
            # is present anywhere in the word
            for entry in self.WipeList:
                for index in self.indexList:
                    self.wordleDF = self.wordleDF[self.wordleDF[index] != entry]
            
            print(f"After Round {self.guess}, number of possible answer(s) = ", len(self.wordleDF))

            self.wordleDF.to_csv(self.outputName, index=False)
            self.guess += 1
            self.MaxWords = len(self.wordleDF)

Solver = wordle()
Solver.Simulator()
import pandas as pd

indexList = ["i", "j", "k", "l", "m"]
MaxGuesses = 6
fname="OfficialWordList.csv"

def ListCreator():
    GuessWord = input("Enter the Guess Word:")
    GuessDNA = input("Enter the DNA sequence:")
    GuessWord = GuessWord.upper()
    GuessDNA = GuessDNA.upper()
    print(f"Guess: {GuessWord}, DNA = {GuessDNA}")
    WipeList = []
    ElimList = []
    PartList = []
    FiltList = []

    for i in range(len(GuessDNA)):
        letter = GuessWord[i]
        value = ord(letter) - 65
        if GuessDNA[i] == "G":
            FiltList.append((i, value))
        elif GuessDNA[i] == "Y":
            PartList.append((i, value))
        elif GuessDNA[i] == "B":
            count = GuessWord.count(GuessWord[i])
            if(count == 1):
                WipeList.append(value)
            else:
                counter = 0
                for j in range(len(GuessDNA)):
                    if GuessWord[j] == GuessWord[i]:
                        if (GuessDNA[j] == "Y" or GuessDNA[j] == "G"):
                            counter += 1
                if counter == 0:
                    WipeList.append(value)
                else:
                    ElimList.append((i, value))
        # print(f"Iteration {i}: WipeList = {WipeList} ElimList = {ElimList}, PartList = {PartList}, FiltList = {FiltList}")
    return WipeList, ElimList, PartList, FiltList

def WorldeSimulator():

    # MaxGuesses = int(input("Enter the Maximum number of guesses:"))
    print(f"Starting 5-letter Wordle Filter with {MaxGuesses} maximum guesses. Reading data, please wait a moment...")
    wordleDF = pd.read_csv(fname)
    MaxWords = len(wordleDF)
    guess = 1

    while(guess <= MaxGuesses and MaxWords > 1):
        WipeList, ElimList, PartList, FiltList = ListCreator()
        print(f"Word Guess {guess}:")
        print(f"Round {guess}: WipeList = {WipeList}, ElimList = {ElimList}, PartList = {PartList}, FiltList = {FiltList}")

        # Green letters
        # Retain dataframe entries only if the green word
        # is present in the specified location
        for entry in FiltList:
            index, val = entry
            wordleDF = wordleDF[wordleDF[indexList[index]] == val]
        print("After FiltList, number of possible answer(s) = ", len(wordleDF))
        # wordleDF.to_csv("sample.csv", index=False)
        # dummy = input("Enter any input to continue....:")

        # Yellow letters
        # Step 1: Remove dataframe entries if the yellow letter
        #         is present in the specified location.
        # Step 2: Retain words that have this character atleast once
        for entry in PartList:
            index, val = entry
            wordleDF = wordleDF[wordleDF[indexList[index]] != val]
            wordleDF = wordleDF[(wordleDF["i"] == val) | 
                                (wordleDF["j"] == val) |
                                (wordleDF["k"] == val) |
                                (wordleDF["l"] == val) |
                                (wordleDF["m"] == val)]
        print("After PartList, number of possible answer(s) = ", len(wordleDF))
        # wordleDF.to_csv("sample.csv", index=False)
        # dummy = input("Enter any input to continue....:")

        # Black letters with possible repeats being Yellow or Green
        # Remove dataframe entries if the black letter
        # is present in the specified location
        for entry in ElimList:
            index, val = entry
            wordleDF = wordleDF[wordleDF[indexList[index]] != val]
        print("After ElimList, number of possible answer(s) = ", len(wordleDF))
        
        # Black letters with no repeats or all repeats being black
        # Remove dataframe entries if the black letter
        # is present anywhere in the word
        for entry in WipeList:
            for index in indexList:
                wordleDF = wordleDF[wordleDF[index] != entry]
        print("After WipeList, number of possible answer(s) = ", len(wordleDF))

        wordleDF.to_csv("sample.csv", index=False)
        guess += 1
        MaxWords = len(wordleDF)

WorldeSimulator()
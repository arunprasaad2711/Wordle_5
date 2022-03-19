from alive_progress import alive_bar
import json
import csv

def wordlist5_txt(filename="BackupWordList.txt"):
    MaxCount = 11881376
    letterlist = [chr(i) for i in range(65, 91, 1)]
    wordleList = open(filename,"w")
    with alive_bar(MaxCount) as bar: 
        for i in range(0, 26):
            for j in range(0, 26):
                for k in range(0, 26):
                    for l in range(0, 26):
                        for m in range(0, 26):
                            word = letterlist[i] + letterlist[j] + letterlist[k] + letterlist[l] + letterlist[m] + "\n"
                            wordleList.write(word)
                            bar()
    wordleList.close()

def wordlist5_csv(filename="BackupWordList.csv"):
    MaxCount = 11881376
    letterlist = [chr(i) for i in range(65, 91, 1)]
    wordleList = open(filename, 'w', encoding='UTF8', newline='')
    writer = csv.writer(wordleList)
    writer.writerow(["word", "i", "j", "k", "l", "m"])
    with alive_bar(MaxCount) as bar: 
        for i in range(0, 26):
            for j in range(0, 26):
                for k in range(0, 26):
                    for l in range(0, 26):
                        for m in range(0, 26):
                            word = letterlist[i] + letterlist[j] + letterlist[k] + letterlist[l] + letterlist[m]
                            entries = [word, i, j, k, l, m]
                            writer.writerow(entries)
                            bar()
    wordleList.close()

def txt2json(IPFname="BackupWordList.txt", OPFname="BackupWordList.json"):
    file1 = open(IPFname, 'r')
    wordDict = {}
    index = 0
    for line in file1:
        word = line.strip("\n")
        wordDict[index] = word
        index += 1
    file1.close()

    with open(OPFname, "w") as file2:
        json.dump(wordDict, file2, indent=4)

def qsetjson(IPFname="BackupWordList.txt", OPFname="BackupQsetList.json"):
    file1 = open(IPFname, 'r')
    qsetDict = {}
    index = 0
    for line in file1:
        word = line.strip("\n")
        qset = []
        for letter in word:
            qset.append(ord(letter) - 65)
        qsetDict[index] = qset
        index += 1
    file1.close()

    with open(OPFname, "w") as file2:
        json.dump(qsetDict, file2, indent=4)

def txt2csv(IPFname="OfficialWordList.txt", OPFname="OfficialWordList.csv"):
    file1 = open(IPFname, 'r')
    wordleList = open(OPFname, 'w', encoding='UTF8', newline='')
    writer = csv.writer(wordleList)
    writer.writerow(["word", "i", "j", "k", "l", "m"])
    for line in file1:
        word = line.strip("\n").upper()
        entries = [word, ord(word[0]) - 65, ord(word[1]) - 65, ord(word[2]) - 65, ord(word[3]) - 65, ord(word[4]) - 65]
        writer.writerow(entries)
    wordleList.close()

txt2csv()
                        
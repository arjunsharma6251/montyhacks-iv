#Made by Arjun Sharma, Jennifer Tian, Nicholas Kang, and Gloria Yao for MontyHacks IV!

import random

print("What do you want to do? Do you want to input a 15 base DNA strand and see what amino acids it results in (and maybe see what amino acid is made from three base pairs)?\n Or do you want to test your understanding of various epidemiology terms?")
while(1==1):
    initialResponse = input("If you want to do the first one, answer 1. If you want to do the second one, answer 2.")
    if not initialResponse.isdigit():
        print("Please answer with 1 or 2 (the numbers explicitly)!")
    elif int(initialResponse) > 2:
        print("Please answer with 1 or 2 (nothing above that please)!")
    else:
        break
#transcription and translation to amino acid code so people can input a gene that has a mutation and see the effects it has on the amino acids, potentially giving someone insight on how a mutation can influence the proteins that are created
if int(initialResponse)==1:
    #transcription (DNA -> RNA)
    initialDNAStrand = input("Please input a 15 letter DNA strand (the direction of this template strand should be 3' to 5', and please input all of the bases in uppercase(example: ATGCTCGAGTACGTT))")

    initialDNAStrand = initialDNAStrand.replace("A", "U")
    initialDNAStrand = initialDNAStrand.replace("T", "A")
    initialDNAStrand = initialDNAStrand.replace("C", "i")
    initialDNAStrand = initialDNAStrand.replace("G", "C")
    initialDNAStrand = initialDNAStrand.replace("i", "G")

    newRNAStrand = initialDNAStrand

    print("The resulting RNA strand is " + newRNAStrand + ".")
    
    #translation (RNA -> Amino acids)
    aminoAcids = {"UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA" : "Leu", "CUG": "Leu", "AUU" : "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met", "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro", "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr", "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala", "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP", "UAG": "STOP", "CAU": "His", "CAC": "His", "CAA": "Glu", "CAG": "Glu", "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu", "UGU": "Cys", "UGC": "Cys", "UGA": "Stop Codon", "UGG": "Trp", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg", "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly", "GUU" : "Val", "GUC": "Val", "GUC" : "Val", "GUA": "Val"} 
 
    acidOne = ""
    acidTwo = ""
    acidThree = ""
    acidFour = ""
    acidFive = ""
    for i in range(len(newRNAStrand)):
        if i <= 2:
            acidOne += newRNAStrand[i]
        if i >= 3 and i <= 5:
            acidTwo += newRNAStrand[i]
        if i >= 6 and i <= 8:
            acidThree += newRNAStrand[i]
        if i >= 9 and i <= 11:
            acidFour += newRNAStrand[i]
        if i >= 12 and i <= 14:
            acidFive += newRNAStrand[i]

    #printing out the amino acids
    print("The chain of amino acids you made is: " + aminoAcids[acidOne] + " - " + aminoAcids[acidTwo] + " - " + aminoAcids[acidThree] + " - " + aminoAcids[acidFour] + " - " + aminoAcids[acidFive] + "!")
    print("If you get the stop/start codon in the middle of your code, it's a stop/start there!")

    #Make your own amino acid minigame :D
    responseTwo = input("Do you want to input three bases and see what it codes for (respond with Y if you want to!)?")
    if responseTwo == "Y":
        aminoAcids = {"UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline", "ACU": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine", "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine", "UAU": "Tyrosine", "UAC": "Tyrosine", "UAA": "a Stop Codon", "UAG": "a Stop Codon", "CAU": "Histidine", "CAC": "Histidine", "CAA": "Glutamine", "CAG": "Glutamine", "AAU": "Asparagine", "AAC": "Asparagine", "AAA": "Lysine", "AAG": "Lysine", "GAU": "Aspartic Acid", "GAC": "Aspartic Acid", "GAA": "Glutamic Acid", "GAG": "Glutamic Acid", "UGU": "Cysteine", "UGC": "Cysteine", "UGA": "Stop Codon", "UGG": "Tryptophan", "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine", "AGU": "Serine", "AGC": "Serine", "AGA": "Arginine", "AGG": "Arginine", "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine", "GUU" : "Valine", "GUC": "Valine", "GUC": "Valine", "GUA": "Valine"}
 
 
        userAcid = ""
        firstBase = input("Which base pair do you choose first - Enter Adenine, Guanine, Cytosine, or Uracil: ").lower()
        if firstBase == "adenine":
            userAcid = userAcid + "A"
        elif firstBase == "guanine":
            userAcid = userAcid + "G"
        elif firstBase == "cytosine":
            userAcid = userAcid + "C"
        elif firstBase == "uracil":
            userAcid = userAcid + "U"
        else:
            print("Invalid, please enter Adenine, Guanine, Cytosine, or Uracil")
        secondBase = input("Which base pair do you choose second - Enter Adenine, Guanine, Cytosine, or Uracil: ").lower()
        if secondBase == "adenine":
            userAcid = userAcid + "A"
        elif secondBase == "guanine":
            userAcid = userAcid + "G"
        elif secondBase == "cytosine":
            userAcid = userAcid + "C"
        elif secondBase == "uracil":
            userAcid = userAcid + "U"
        else:
          print("Invalid, enter Adenine, Guanine, Cytosine, or Uracil")
        thirdBase = input("Which base pair do you choose second - Enter Adenine, Guanine, Cytosine, or Uracil: ").lower()
        if thirdBase == "adenine":
            userAcid = userAcid + "A"
        elif thirdBase == "guanine":
            userAcid = userAcid + "G"
        elif thirdBase == "cytosine":
            userAcid = userAcid + "C"
        elif thirdBase == "uracil":
            userAcid = userAcid + "U"
        else:
            print("Invalid, enter Adenine, Guanine, Cytosine, or Uracil")
 
        print("Congrats! You made " + aminoAcids[userAcid] + "!")


    else:
        print("Thanks for playing!")
    
    
#start of PUBLIC HEALTH/EPIDEMIOLOGY GAME for students to learn terms of public health
if int(initialResponse)==2:
    
    questionbank = [{
    "definition": "A microbial organism with the ability to cause disease",
    "term": "agent"},
    {
    "definition": "showing no symptoms of disease",
    "term": "asymptomatic"},
    {
    "definition": "Agent leaves reservoir through portal of exit, and is conveyed by some mode of transmission, and enters the appropriate portal of entry to infect a susceptible host.",
    "term": "chain of infection"},
    {
    "definition": "An aggregation of cases over a particular period closely grouped in time and space, regardless of whether the number is more than the expected number.",
    "term": "cluster"},
    {
    "definition": "present at a continuous level throughout a population/geographic area; constant presence of an agent/health condition within a given geographic area/population; refers to the usual prevalence of an agent/condition. (hint: ______ disease)",
    "term": "endemic disease"},
    {
    "definition": "a widespread occurrence of an infectious disease in a community at a particular time.",
    "term": "epidemic"},
    {
    "definition": "study of the cause of disease",
    "term": "etiology"},
    {
    "definition": "A physical object that serves to transmit an infectious agent from person to person.",
    "term": "fomite"},
    {
    "definition": "condition produced by a physician (the unexpected results from a treatment prescribed by a physician)",
    "term": "iatrogenic"},
    {
    "definition": "The number or rate of new cases of a particular condition during a specific time.",
    "term": "incidence"},
    {
    "definition": "interval between initial infection and first signs and symptoms",
    "term": "incubation period"},
    {
    "definition": "the first patient found in an epidemiological investigation",
    "term": "index case"},
    {
    "definition": "time interval between when an individual or host is infected by a pathogen and when he or she becomes infectious",
    "term": "latent period"},
    {
    "definition": "incidence of a specific notifiable disease",
    "term": "morbidity"},
    {
    "definition": "death rate",
    "term": "mortality"},
    {
    "definition": "a disease caused by exposure to infection in the healthcare environment",
    "term": "nosocomial disease"},
    {
    "definition": "more cases of a particular disease than expected in a given area or among a specialized group of people over a particular period of time.",
    "term": "outbreak"},
    {
    "definition": "disease that occurs over a wide geographic area and affects a very high proportion of the population (one word only).",
    "term": "pandemic"},
    {
    "definition": "A prevalence rate that indicates the existence of a condition during an interval of time, often a year.",
    "term": "period prevalence"},
    {
    "definition": "a disease that spreads quickly and kills many people",
    "term": "plague"},
    {
    "definition": "The percentage of people in a given population who have a given disorder at any particular point in time.",
    "term": "point prevalence"},
    {
    "definition": "The number or proportion of cases of a particular disease or condition present in a population at a given time.",
    "term": "prevalence"},
    {
    "definition": "a situation involving exposure to danger",
    "term": "risk"},
    {
    "definition": "having to do with signs or symptoms, indicative",
    "term": "symptomatic"},
    {
    "definition": "An infectious disease that is transmissible from animals to humans (____ disease).",
    "term": "zoonotic disease"}
    ]

    correct = 0
    wrong = 0

    while(1==1):
        amountOfPractice = input("How many times do you want to quiz yourself? (answer with a #)")

        if not amountOfPractice.isdigit():
            print("Please answer with a DIGIT like 1 or 2!")
        else:
            break

    for i in range(int(amountOfPractice)):
        num = random.randint(0, 24)
        target = questionbank[num]["term"]

        print(questionbank[num]["definition"])
        playerAnswer = input("This term has " + str(len(target)) + " letters. Guess the term: \n")
        playerAnswer = playerAnswer.lower()

        if playerAnswer == target:
            correct += 1
        while playerAnswer != target:
            playerAnswer = input("Sorry, that isn’t right. Maybe think more about the definition and word length clue! Enter your next guess or enter quit to reveal the correct answer: \n").lower()
            wrong += 1
            if playerAnswer == "quit":
                break
    
        print("The term was " + target + "!\n")
        print("You currently have " + str(correct) + " correct and " + str(wrong) + " wrong.\n")
    print("Thanks for playing!")

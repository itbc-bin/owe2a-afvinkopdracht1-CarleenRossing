# Naam:
# Datum:
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    bestand = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
    headers, seqs = lees_inhoud(bestand)
    

# schrijf hier de rest van de code nodig om de aanroepen te doen
   
                
    for index in range(len(headers)):                           #leest het bestand en kijkt of het zoekwoord er in staat
        print(index)                                            #Als het zoekwoord er in staat, kijkt die of het DNA is of niet
        if zoekwoord in headers[index]:                         #Dan kijkt die of de restrictieenzymen er zijn.
            print(headers[index])
            if is_dna(seqs[index]):
                print("sequence", index, "is DNA")
                knipt(seqs[index])
                
            else:
                print("is geen DNA")
                
            
    
    

    
def lees_inhoud(bestand):
    try:
        bestand = open(bestand)
    except IOError:
        print("het bestandsnaam bestaat niet")
    headers = []
    seqs = []

    sequentie = ''
    
    for line in bestand:
        if line.startswith (">"):                           #Leest elke regel en kijkt of het een header is of niet
            headers.append(line)                            #Als het niet een header is zet het in de lijst van sequenties
            if not sequentie == '':
                seqs.append(sequentie)
                sequentie = ''
        else:
            sequentie = sequentie + line.strip('\n')
            
            
    seqs.append(sequentie)

    #print(headers, seqs, sequentie)
    
  
     
    return headers, seqs                                #Het script returnt de nieuwe lijsten

    
def is_dna(seq):

    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    
    for letter in seq:                                      #Als de sequentie deze letters bevat, is het een DNA
        if letter not in ['A','T','C','G']:
            return False
        
    return True
    

def knipt(seq):
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
    enzymen = open("enzymen.txt", 'r')

    for regel in enzymen:                                   #leest het bestand in en haalt allemaal stomme tekens weg
        regel = regel.replace("^", "")                      #Bekijkt of de enzymen in het grote bestand staan
        regel = regel.replace("\n", "")
        enzyme, knip = regel.split()
        if knip in seq:
            print(enzyme + " knipt in " + seq)

    
    
main()


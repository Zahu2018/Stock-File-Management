# Opereaza necesar
# Data here is fictional and does not reflect the company operations.


fisier_necesar = """
Unitatea: S.C. SIMLEU SHOES S.R.L., Oradea, Calea Borsului 23 W
          J05/304318/23/11/2021, C.U.I. 12345678
Punct de lucru: Simleu Silvaniei, Simion Barnutiu, Nr. 29  |  Magazia

                             SITUATIE NECESAR
-------------------------------------------------------------------
Cod: [{}]
Categorie: {}
Material: {} {}
U.M.: {}
-------------------------------------------------------------------------------
   Data     Felul si Numarul      Intrat     Necesar      Rest        Stoc     
              Documentului                                          
-------------------------------------------------------------------------------
     -    |          -         |     -     |     -     |          0|          0
"""

## CREAZA FISIERUL NEC
#with open("A_B_C_0.nec", "w") as x:
#    x.write(fisier_necesar)
  

def opereaza_necesar(nf, data_, document_, intrat, necesar_):  # nf = nume fisier
    try:
        necesar = float(necesar_)
    
        if "#$" in data_:
             # preia din entry-uri; TOKEN
             data = data_.split('#$')[0]
             document = document_.split('#$')[0]
        else:
            data = data_
            document = document_
    
        nume = nf.rstrip(".csv")
        nume_necesar = nume + ".nec"
        #print("{} data{} doc{} cant{} nec{}".format(nume_necesar, data, document, intrat, necesar))
        with open(nume_necesar, "r+") as f:
            continut = f.readlines()
            last_line = continut[-1]
            lista_last_line = last_line.split('|')
            stoc = lista_last_line[5].strip()
            stoc_nou = float(stoc) + intrat - necesar
            rest = intrat - necesar
            linia = '{:>10}|{:<20}|{:>11.2f}|{:>11.2f}|{:>11.2f}|{:>11.2f}\n'.format(data, document, intrat, necesar, rest, stoc_nou)
            f.write(linia)
    except ValueError as e:
        pass

        
if __name__ == "__main__":
        ...

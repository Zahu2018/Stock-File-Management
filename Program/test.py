import configparser

def get_lang(lang) -> dict:
    obj = configparser.ConfigParser()
    lan = lang + ".lang"
    obj.read(lan)
    
    return obj
        
 
if __name__ == "__main__":
    a = get_lang("eng")
    for i in a['days']:
        print(a['days'][i])

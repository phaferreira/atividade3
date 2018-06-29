import urllib
import urlparse, json
#op='consulta'
#estado='SP'
#b="http://localhost:8080/?op="+op+"&estado="+estado
#print b
#http://localhost:8080/?"+op+"&"+estado

def consultaCEP(op,estado):
    f = urllib.urlopen("http://localhost:8080/?op="+op+"&estado="+estado)
    contents = f.read()
    lista = json.loads(contents)
    results = lista['url']
    return results


def buscaCEP(cep):
    c = consultaCEP("consulta","SP")
    a = (c+"/?CEP="+cep)
    f = urllib.urlopen(a)
    contents = f.read()
    return contents

print buscaCEP('69301000')
    





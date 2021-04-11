from engine.translate import *;
namesrtfile = "legacies.s03e08.1080p.web.h264-cakes.srt"
t = Translate()

#cria arquivo
arquivo   = open(namesrtfile,"r")
tarquivo  = arquivo.read()
resultado = open("tradução.srt",'w')
#traduz
tfalas = []
falas = tarquivo.split('\n\n')
for fala in falas:
    linhas=fala.split('\n')
    if len(linhas)==3:
        tradu = t.traduzir(linhas[2])
    else:
        tradu = t.traduzir(linhas[2]+"</>" +linhas[3])
    print(tradu)
    tradus = linhas[0]+"\n"+ linhas[1]+"\n"+tradu.replace("</> ","\n")
    tradusi = tradus+"\n\n"
    resultado.write(tradusi)  
arquivo.close()
resultado.close()
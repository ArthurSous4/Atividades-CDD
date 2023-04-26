ano=int(input("digite a idade em anos: "))
mes=int(input("digite quantos meses: "))
dias=int(input("digite os dias: "))

anoParaDias=ano*365
mesParaDias=mes*30
totalDias=anoParaDias+mesParaDias+dias

print(f"idade em anos: {ano}\nidade em dias: {totalDias}")
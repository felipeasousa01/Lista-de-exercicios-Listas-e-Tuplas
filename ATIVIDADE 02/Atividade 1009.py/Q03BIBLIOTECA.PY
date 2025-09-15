# Use a biblioteca datetime para mostrar a data e hora atuais.
from datetime import datetime
agora = datetime.now()
print("Data e hora atuais:", agora.strftime("%d/%m/%Y %H:%M:%S"))

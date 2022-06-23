import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o telefone no formato +551140028922: ')

# a string repassada no input é convertida em numero ded telefone
# e recebida pelo objeto phone_number
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt-BR'))



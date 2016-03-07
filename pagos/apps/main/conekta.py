import conekta
import os


conekta.api_version = "2.0.0"
conekta.api_key = "key_UCM2jZsgd3yfdz1xrQ6x1Q"
conekta.locale = 'es'

def new_charge(card):
	charge = conekta.charge.create({
			amount : 20000,
	  		currency : "MXN",
	  		card: card,
	  		description : "Pago de servicio legal"

		}),
	return charge

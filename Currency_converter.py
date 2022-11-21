from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

#Currency list that was a pain in the ass to create, never wanting to do this again, fuck currency names.
Currency_list = ['AED','AFN','ALL','AMD','ANG','AOA','ARS','ATS','AUD','AWG','AZN','BAM','BBD','BDT','BEF','BGN'
,'BHD','BIF','BMD','BND','BOB','BRL','BSD','BTN','BWP','BZD','CAD','CDF','CHF','CLP','CNY','COP','CRC','CUC','CUP'
,'CVE','CYP','CZK','DJF','DKK','DMK','DOP','DZD','EEK','EGP','ESP','ETB','FIM','FJD','FKP','GBP','GEL','GHS','GIP','GMD'
,'GNF','GRD','GTQ','GYD','HKD','HNL','HRK','HTG','HUF','IDR','IED','ILS','INR','IQD','IRR','ISK','ITL','JMD','JOD','JPY','KES','KGS'
,'KHR','KMF','KPW','KRW','KWD','KYD','LAK','LBP','LKR','LRD','LSL','LTL','LUF','LVL','LYD','MAD','MDL','MGA','MKD','MMK','MNT'
,'MOP','MRO','MTL','MUR','MVR','MWK','MYR','MZN','NAD','NGN','NIO','NLG','NOK','NPR','NZD','OMR','PAB','PEN','PGK','PHP','PKR'
,'PLN','PTE','PYG','QAR','RON','RSD','RUB','RWF','SAR','SBD','SCR','SDG','SEK','SGD','SHP','SIT','SKK','SLL'
,'SOS','SRD','STD','SVC','SYP','SZL','THB','TMM','TND','TOP','TRY'
,'TTD','TWD','TZS','UAH','UGX','USD','UYU','VEB','VND','VUV','WST','XAF','XCD','XOF','XPF','YER','ZAR','ZMK','ZWD']

e = CurrencyCodes()
print(Currency_list)
is_currency = input('Please enter a currency name: ').upper()
#var = e.get_symbol(is_currency)
for i in Currency_list:
    if is_currency == i:
        print(''"{}"' seems to be a real currency.'.format(is_currency))
        

#Takes any currency abbrevation and returns its current symbol
d = CurrencyCodes()
currency = input('please enter the currency you want to get the symbol of: ').upper()
get_symbol = d.get_symbol(currency)
symbol = input('The symbol for '"{}"' is:'.format(currency) + ' ' + str(get_symbol))
print(symbol)

#Converts any 2 currencies against each other and convert their real time values
c = CurrencyRates()
user = int(input('Enter an amount sir. '))
from_currency = input('Which currency sir?: ').upper()
to_currency = input('Which currency would like to convert to sir?: ').upper()
conversion = input(from_currency + ' To ' + to_currency + ': ' + str(user))
print(conversion)
result = c.convert(from_currency, to_currency, user)
print(result)
#### [word,     cty_low, cty_mid, cty_high]
#### a simple find word matches against the text of a transactions descripotion
#### It is then used to categorise the transactions - lowest, middle highest abstraction

_matchers = [

['goldex',                                      'costa', 'soho', 'luxury'],
['storage king',                                'storage', 'utilities', 'utilities'],
['storageking',                                 'storage', 'utilities', 'utilities'],
['nexgen',                                      'internet', 'utilities', 'utilities'],
['smith and webb',                              'kitchen', 'homeware', 'house'],
['tomtom',                                      'gadgets', 'car', 'travel'],
['sains',                                       'sainsburys', '-', 'groceries'],
['waitrose',                                    'waitrose', '-', 'groceries'],
['asda',                                        'asda', '-', 'groceries'],
['tesco',                                       'tesco', '-', 'groceries'],
['ocado',                                       'ocado', '-', 'groceries'],
['the swan',                                    'eat out', 'eat out', 'leisure'],
['thai moom',                                   'eat out', 'eat out', 'leisure'],
['scared crow',                                 'eat out', 'eat out', 'leisure'],
['dominos pizza',                               'eat in', '-', 'eat in'],
['sino',                                        'eat out', 'eat out', 'leisure'],
['Esso Moto',                                   'eat out', 'eat out', 'leisure'],
['Gufaaraja',                                   'eat out', 'eat out', 'leisure'],
['The Hengist AYLESFORD',                       'eat out', 'eat out', 'leisure'],
['Woods Restaurant Ltd',                        'eat out', 'eat out', 'leisure'],
['Dhaka Tandoori',                              'eat out', 'eat out', 'leisure'],
['Id West Malling Ltd',                         'eat out', 'eat out', 'leisure'],
['Welcome Break',                               'eat out', 'eat out', 'leisure'],
['packing ware',                                'ebay', '-', 'ebay'],
['tonbridge and mall',                          'council tax', 'utilities', 'utilities'],
['TONBRIDGE & MALL',                            'council tax', 'utilities', 'utilities'],
['southern water',                              'water', 'utilities', 'utilities'],
['sky digital',                                 'sky ', 'utilities', 'utilities'],
['south east water',                            'water', 'utilities', 'utilities'],
['tv licence',                                  'tv', 'utilities', 'utilities'],
['gas',                                         'british gas', 'utilities', 'utilities'],
['bt group',                                    'phone', 'utilities', 'utilities'],
['O2',                                    'phone', 'utilities', 'utilities'],
['Carphone Warehouse',                                    'phone', 'utilities', 'utilities'],
['MID KENT WATER LTD',                          'water', 'utilities', 'utilities'],
['simplyhealth',                                'health', 'insurance', 'insurance'],

['david lloyd',                                 'gym', 'gym', 'health'],
['Kings Hill dental',                                 'dental', 'dental', 'health'],
['bmihealth',                                 'dental', 'dental', 'health'],
['SAntander mortgage',                          'mortgage', 'mortgage', 'mortgage'],
['pinn insu',                                   'insurance', '-', 'insurance'],
['PINNACLE INSURANCE',                          'insurance', '-', 'insurance'],
['premium credit',                              'insurance', '-', 'insurance'],
['scottish provident',                          'insurance', '-', 'insurance'],
['direct line',                                 'insurance', '-', 'insurance'],
['legal & gen mi',                              'insurance', '-', 'insurance'],
['aviva',                                       'insurance', '-', 'insurance'],
['L&G ASSCE SOC LTD',                           'insurance', '-', 'insurance'],
['Abbotsley Veterinary',                        'vet', '-', 'insurance'],
['0664/640 693 584',                            'transfer', '-', 'transfer'],
['0572/632 896 821',                            'transfer', '-', 'transfer'],
['paul brian',                                  'transfer', '-', 'transfer'],
['barclaycard',                            'transfer', '-', 'transfer'],
['hsbc card services',                          'transfer', '-', 'transfer'],
['NATIONWIDE C/CARD',                           'transfer', '-', 'transfer'],
['hsbc bank plc',                               'transfer', '-', 'transfer'],
['0220/648 872 431',                            'transfer', '-', 'transfer'],
['07-00-40',                                    'transfer', '-', 'transfer'],
['MIKADO SOFTW',                                'transfer', '-', 'transfer'],
['AMAZON.CO.UK',                                'books', 'books', 'house'],
['ITUNES.COM',                                  'itunes', 'books', 'house'],
['Autoglass',                                   'windscreen', 'car', 'travel'],
['BP Parkfoot S/Stn',                           'fuel', 'car', 'travel'],
['BP Three Elm S/Stn',                          'fuel', 'car', 'travel'],
['BT DIRECT DEBITS',                            'bt', 'utilities', 'utilities'],
['Cash machine',                                'cash', 'cash', 'cash'],
['Cash withdraw',                               'cash', 'cash', 'cash'],
['Cheque:',                                     'cheque', 'cheque', 'chequeout'],
['Clacket Lane Serv',                           'fuel', 'car', 'travel'],
['Down Swan Street',                            'gifts', 'gifts', 'gifts'],
['Cath Kidston',                            'gifts', 'clothes', 'clothes'],
['Kings Hill Pharmac',                          'medicince', 'medicine', 'medicine'],
['WWW.Johnlewis.Com',                           'homeware', 'homeware', 'house'],
['51*Jcrew Purchase 877-315-4709',              '-', '-', 'clothes'],
['Aldi Stores',                                 'aldi', '-', 'groceries'],
['Ape Concessions WAREHAM',                     'monkeyworld', '-', 'leisure'],
['Avis Maidstone E333046766',                   '-', '-', 'mikadoexpenses'],
['B & Q',                                       '-', 'diy', 'house'],
['Bailey Wighton Ltd',                          'bathroomflooring', 'diy', 'house'],
['Boots BLUEWATER',                             'pharamcy', '-', 'health'],
['Brands Hatch',                                'olympics', '-', 'leisure'],
['Cheque credit',                               '-', '-', 'paidin'],
['Co-Op Group',                                 '-', '-', 'groceries'],
['David & Goliath',                             '-', '-', 'gifts'],
['Enterprise 01622 663656',                     '-', 'carhire', 'travel'],
['Google *Appspremier GOOGLE.COM/CH',           '-', '-', 'mikadoexpenses'],
['HSA',                                         '-', '-', 'health'],
['Halfords',                                    '-', '-', 'kids'],
['Betty Lewis',                                    '-', '-', 'kids'],
['Hobbycraft Group L TUNBRIDGE WEL',            '-', 'crafts', 'kids'],
['jojo maman bebe',            '-', 'crafts', 'kids'],
['Clarks shop',            '-', 'crafts', 'kids'],
['Early learning',            '-', 'crafts', 'kids'],

['Homebase Ltd 072 AYLESFORD',                  '-', 'diy', 'house'],
['Humphreys of Kings Hill WEST MALLING',        'fish chips', '-', 'leisure'],
['Interest Charge',                             '-', 'bankcharges', 'bankcharge'],
['Interest On',                             '-', 'bankcharges', 'bankcharge'],
['Late Payment',                             '-', 'bankcharges', 'bankcharge'],
['MERCHANDISE INTEREST',                             '-', 'bankcharges', 'bankcharge'],
['Over Credit',                             '-', 'bankcharges', 'bankcharge'],
['JJB Sports',                                  '-', '-', 'clothes'],
['John Lewis',                                  '-', '-', 'clothes'],
['K J Edwards TONBRIDGE',                       '-', '-', 'clothes'],
['Kent Life MAIDSTONE',                         'days out', 'daysout', 'leisure'],
['Kings Hill Opticians Ltd',                    '-', 'opticians', 'health'],
['Learning Curve GALSAHIELS',                   'toys', '-', 'kids'],
['London & South Eas WEST MALLING',             '-', 'train', 'travel'],
['London 2012',                                 'olympics', 'daysout', 'leisure'],
['Lovely Takeaway WEST MALLING',                'eat out', 'eat out', 'leisure'],
['MACQUARIE STORAGE LUXCO 1 SARL',              '-', '-', 'unknown'],
['MRH Offham WEST MALLING',                     'eat out', 'eat out', 'leisure'],
['McDonalds Rest',                              'eat out', 'eat out', 'leisure'],
['Menkind Stores Ltd STREET',                   'gifts', '-', 'gifts'],
['Mexxa Mexxa MAIDSTONE 1',                     '-', '-', 'clothes'],
['Monkey World WAREHAM',                        '-', 'daysout', 'leisure'],
['Next 0',              '-', '-', 'clothes'],
['Old Rectory LEYBOURNE',                       '-', '-', '-'],
['Paid item fee',                               '-', '-', 'bankcharge'],
['Pets At Home Ltd MAIDSTONE',                  'pets', '-', 'pets'],
['Phase Eight WEBSTORE UK',                     '-', '-', 'clothes'],
['Pizza Express',                               'eat out', 'eat out', 'leisure'],
['Post and Packing KINGS HILL',                 'ebay', '-', 'ebay'],
['Pret A Manger',                               'eat out', 'eat out', 'leisure'],
['Returned direct debit',                       'bank charges', '-', 'bankcharge'],
['SELECT CREDIT CARD',                          'bank charges', '-', 'transferCC'],
['Shell Ham Hill SNODLAND',                     'fuel', 'car', 'travel'],
['Somerstown Coffee Hous LONDON',               'meeting', '-', 'expenses'],
['Spellbrook Leisure Ltd WALTHAM ABBEY',        'nazeing golf club', '-', 'eat out'],
['Spitfire WEST MALLING',                       'spitfire', '-', 'eat out'],
['Starbucks STAINES',                           'coffee', '-', 'luxury'],
['TFL CC/Lez Penalty 0333 200 1000',            'parkingfine', '-', 'car'],
['Texaco Broadwey Mo DORCHESTER',               'fuel', '-', 'car'],
['The King Harolds Head WALTHAM ABBEY',         'dad lunch', '-', 'eat out'],
['Ticketweb.Co.UK LONDON',                      '-', '-', 'leisure'],
['Unauth Overdraft Fee',                        'bank charges', '-', 'bankcharge'],
['Unpaid Direct Debit Fee',                     'bank charges', '-', 'bankcharge'],
['Villa Holidays MAIDSTONE',                    'unknown', '-', 'unknown'],
['WWW.Carseatsandpushcha 07812437959',          'car', 'car', 'car'],
['WWW.Dominos.Co.UK 01908 580000',              'eat out', 'eat out', 'leisure'],
['WWW.Dvla.Gov.UK VEHICLE LICEN',               'car', '-', 'car'],
['WWW.Nda.Ac.UK NOTTINGHAM',                    'annauni', '-', 'education'],
['WWW.Paultonspark.Co.UK ROMSEY',               'peppapig', 'daysout', 'leisure'],
['alexander house crawley',                     'spa', 'daysout', 'leisure'],
['rowhill reservations',                     'spa', 'daysout', 'leisure'],
['summer lodge',                     'spa', 'daysout', 'leisure'],

['phase eight',                     '-', '-', 'clothes'],
['next directory',                     '-', '-', 'clothes'],
['sweaty betty',                     '-', '-', 'clothes'],
['Peller GREENHITHE',                     '-', '-', 'clothes'],
['mintvelvet',                     '-', '-', 'clothes'],
['monsoon',                     '-', '-', 'clothes'],
['gap',                     '-', '-', 'clothes'],
['superdry',                     '-', '-', 'clothes'],
['fatface',                     '-', '-', 'clothes'],
['topshop',                     '-', '-', 'clothes'],


['WWW.Preciouslittleone. INTERNET',             'car', 'car', 'car'],
['WWW.Tickets.LONDON2012 LONDON  WC2H',         'olympics', 'daysout', 'leisure'],
['ROyal Albert Hall',         'GaryBarlow', 'daysout', 'leisure'],
['West Malling Flowers WEST MALLING',           'flowers', '-', 'leisure'],

['Ikea',           'furniture', 'furniture', 'house'],
['White Company',           'furniture', 'furniture', 'house'],
['Dunelm',           'furniture', 'furniture', 'house'],
['Sewing Room',           'furniture', 'furniture', 'house'],
['Laura Ashley',           'furniture', 'furniture', 'house'],
['Currys',           'TV', 'furniture', 'house'],
['House of Fraser',           '-', 'furniture', 'house'],

['Ticketline',           '-', '-', 'leisure'],
['Camping International',                       'CampingGear', 'Camping', 'house'],

    ['Alexander House',                       '', '', 'leisure'],


['RGOSTOLI',   'holiday-kef','','leisure'],
['KEFALLONIA', 'holiday-Kef','','leisure'],
['MATTWOODWARD','','','leisure'],
['KINGSHILL ESTATE', '','','house'],
['Passport', '','','leisure'],
    ['Soccer Elite', '','','kids'],
    ['Bupa Travel Svcs', 'Family Travel Insurance','','insurance'],
    ['Legoland','','','kids'],
    ['SERVECOM','plumber','','house'],
    ['Carluccio','','','leisure'],
    ['02 Online', '','','utilities'],
    ['DAWN - CLEANER','','','house'],
    ['Soles with heart','','','clothes'],
    ['02 UK','','','utilities'],
    ['London & South Eas','','','travel'],
    ['The Llama Park','','','leisure'],
    ['Camping & Caravan Club','','','leisure'],
    ['Restaurant','','','leisure'],
    ['Barclays Capital','','','luxury'],
    ['HSBC CREDIT CARD','','','transferCC'],
    ['Hays Travel','','','leisure'],
    ['Ulwell Cottage','','','leisure'],

    ['OOPSYDAISYPARTYBUS','','','kids'],
    ['SHAWBROOK','','','Debt'],
    ['070116 32896821','','','transfer'],
    ['070040 10579838','','','transfer'],
    ['070040 02268734','','','transfer'],
    ['INHERITANCE LAW','','','probate'],
    ['CHORUSLAW','','','probate'],
    ['WALKIES LTD','','','pets'],

    ['UTILITY WAREHOUSE','','','utilities'],
    ['AIG LIFE LIMITED','','','insurance'],
    ['VIRGIN ACTIVE','','','gym'],

    ['THE CHASER INN','','','eat out'],
    ['CHIQUITO','','','eat out'],
    ['WAGAMAMA','','','eat out'],
    ['FRANKIE & BENNYS','','','eat out'],
    ['BYRON HAMBURGERS','','','eat out'],


    ['UW CASHBACK CARD','','','utilities'],
    ['ATM Withdrawal','','','cash'],
    ['KENT MEDICAL IMAGING LTD','','','health'],
    ['Transfer to:074456 40693584','','','transfer'],
    ['WILLROSECLEANING','','','household'],
    ['VIRGIN ACTIVE','','','gym'],
    ['PRUDENTIAL','','','insurance'],
    ['BE WISER INSURANCE','','','insurance'],

##
    ['DISNEY STORE','','','kids'],
    ['THE HUNGRY GUEST','','','eat out'],
    ['KINGSHILL PHARMACY','','','health'],
    ['BRICKS 4 KIDZ','','','kids'],
    ['PRUDENTIAL','','','insurance'],

    ['PARTY BUS','','','kids'],
    ['WILLROSECLEANING','','','household'],
    ['VIRGIN ACTIVE','','','gym'],
    ['PRUDENTIAL','','','insurance'],
    ['BE WISER INSURANCE','','','insurance'],

    ['Transfer to:074456 40693584','','','transfer'],
    ['WILLROSECLEANING','','','household'],
    ['VIRGIN ACTIVE','','','gym'],
    ['PRUDENTIAL','','','insurance'],
    ['BE WISER INSURANCE','','','insurance'],


    ['ACE FX','','','cash'],
    ['71125063152','','','mortgage'],
    ['AIG LIFE','','','insurance'],
    ['EMMAMUMFORD','','','house'],
    ['VFAST','','','house'],

    ['DVLA','','','car'],
    ['NETFLIX','','','house'],
    ['ebbsfleet','','','travel'],

    ['REDWOOD IFA','','','insurance'],
    ['SELF ASSESSMENT TA','','','tax'],
    ['HAMLEYS','','','kids'],
    ['TOYS R US','','','kids'],
    ['TVLICENSING','','','house'],
    ['T.M. LEWIN','','','clothes'],
    ['MAMAS & PAPAS','','','kids'],
    ['PANDORA','','','luxury'],
    ['HOLBOROUGH SF CONNECT','','','travel'],

    ['bank credit mikado so','','','salary'],
    ['Transfer from::074456 40693584','','','transfer'],
    ['schuh','','','clothes'],


    ['costa','','','eat out'],
    ['starbucks','','','eat out'],
    ['Non-Sterling transaction fee','','','bankcharges'],


    ['costa','','','eat out'],
    ['starbucks','','','eat out'],
    ['Non-Sterling transaction fee','','','bankcharges'],

    ['TAYLOR ST','','','eat out'],
    ['TAXI FARE','','','travel'],
    ['Non-Sterling cash fee','','','bankcharges'],

    ['WINDOWCLEANERNEW','','','house'],
    ['WINDOW CLEAN','','','house'],
    ['Transfer to','','','transfer'],

    ['Unarranged Overdraft Interest','','','bankcharges'],
    ['Unpaid Transaction Fee -Direct Debit','','','bankcharges'],
    ['5 CANADA SQUARE LONDON GB','','','eat out'],

    ['APPLE STORE','','','house'],
    ['B AND Q','','','house'],
    ['BOOTS','','','groceries'],
    ['CENTER PARCS','','','holidays'],
    ['CLOSE PREMIUM','','','insurance'],
    ['EVANS CYCLES','','','health'],
    ['DART CHARGE','','','travel'],
    ['DART-CHARGE','','','travel'],
    ['GUFAA RAJA','','','eat out'],
    ['MCDONALDS','','','eat out'],

    ['PETS CORNER','','','pets'],
    ['NICHOLSON & GRIFFIN ','','','mikadoexpenses'],
    ['post office','','','ebay'],
    ['PREMIER INN','','','mikadoexpenses'],
    ['PADDOCK WOOD GARD','','','house'],
    ['ROBERT DYAS','','','house'],
    ['SMIGGLE','','','kids'],
    ['SMYTHS TOYS','','','kids'],

    ['TINY-TOWN','','','kids'],
    ['WATERSTONES','','','luxury'],
    ['HOSP P PEMBURY','','','eat out'],
    ['W M MORRISON','','','groceries'],
    ['WH SMITH','','','groceries'],
    ['ZOO ENTERPRISES','','','leisure'],

    ['SHOWCASE CINEMA','','','leisure'],
    ['SHELL','','','travel'],
    ['NOTES','','','mikadoexpenses'],
    ['SNAPPY SNAPS','','','leisure'],
    ['STORE FINANCIAL BLUEW','','','gifts'],
    ['MARKS&SPENCER','','','groceries'],
    ['MARKS & SPENCER','','','groceries'],
    ['MAIDSTONE HOSPITAL','','','health'],

    ['LEGO STORE','','','kids'],
    ['KENT LIFE HERITAGE','','','leisure'],
    ['GAME RETAIL LTD','','','kids'],
    ['CLINTONS','','','gifts'],
    ['CAR PARKS KENT','','','travel'],
    ['APCOA PARKING','','','travel'],
    ['DIXONS','','','house'],
    ['DLR CANARY WHARF','','','mikadoexpenses'],
    ['LUL TICKET','','','mikadoexpenses'],
    ['ISMASH UK TRADING','','','phone'],
    ['NESPRESSO','','','luxury'],
    ['THOMASCOOK AIRLINE','','','holiday'],
    ['TIGER CANARY','','','kids'],
    ['TIGER WESTFI','','','kids'],
    ['WEST MALLING TAXI','','','travel'],
    ['CARD FACTORY','','','gifts'],
    ['J.L F . S .','','','transferCC'],
    ['ASSEMBLY HALL TUNBRIDGE WEL', '','',   'kids'],

    ['CMT (UK) LTD - GLASGOW', '','', 'travel'],
    ['HOLMES PLACE', '','', 'health'],
    ['RUXLEY MANOR GARDE', '','Santa-Grotto', 'kids'],
    ['THE ENTERTAINER', '','', 'kids'],
    ['THE FARMHOUSE WEST MALLING', '','', 'eat out'],
    ['VITALITY LIFE', '','', 'insurance'],

    ['ALISON J BUTCHER', '','', 'health'],
    ['BABY EXPLORERS', '','', 'kids'],
    ['BARHAM CATTERY', '','', 'holidays'],

    ['EMMIESHOES', '','', 'kids'],
    ['H LAAKSONEN CUTLER', '','', 'gifts'],
    ['HAND4HIRE LTD', '','', 'household'],

    ['HEIDI EASBY PHOTO', '','', 'kids'],
    ['HOMEDICS GROUP', '','', 'health'],
    ['JAIME BLACKBURN', '','', 'kids'],
    ['AmazonPrime Membership','','', 'leisure'],
    ['MRS C A KEMP', '','','kids'],
    ['MRS N DAY', '', '', 'kids'],
    ['S MARSH', '','', 'kids'],
    ['STEPHANIE CHAPMAN', '','', 'kids'],
    ['SUPERSKILLS UK', '','', 'kids'],
    ['TRACY HATTERSLEY', '','', 'gifts'],

    ['BROWNS','','','eat out'],
    ['BUBBA GUMP SHRIMP','','', 'eat out'],
    ['PAPAS BARN','','','eat out'],

    ['OP/STOCKPORT CLIEN','','VWcar','transfer'],
]




if __name__ == '__main__':
    pass

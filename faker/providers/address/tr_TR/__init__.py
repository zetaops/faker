__author__ = 'zekiye'

from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_prefixes = ('San', 'Borgo', 'Sesto', 'Quarto', 'Settimo')
    city_suffixes = (
        'a mare', 'lido', 'ligure', 'del friuli', 'salentino', 'calabro', 'veneto', 'nell\'emilia', 'umbro', 'laziale',
        'terme', 'sardo')
    building_number_formats = ('###', '##', '#')
    street_suffixes = (
        'Meydan', 'Cadde', 'Üzeri', 'Köy', 'İl', 'İlçe', 'Geçit', 'Yol', 'Kanal', 'Kavşak', 'Sokak', 'Mahalle')
    postcode_formats = ('#####',)
    states = ('Adana', 'Adıyaman', 'Afyonkarahisar', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin', 'Aydın',
              'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale', 'Çankırı',
              'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir', 'Gaziantep',
              'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'İstanbul', 'İzmir', 'Kars', 'Kastamonu',
              'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 'Manisa',
              'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya', 'Samsun',
              'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak', 'Van',
              'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak', 'Bartın',
              'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce'
    )
    states_abbr = (
        'AF', 'DE', 'US', 'AL', 'AD', 'AO', 'AG', 'AR', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ',
        'BJ', 'BM', 'AE', 'BO', 'BA', 'BW', 'BR', 'BG', 'BF', 'BI', 'BT', 'GB', 'GI', 'DZ', 'DJ', 'TD', 'CZ', 'CN',
        'DK', 'DO', 'EC', 'GQ', 'SV', 'ID', 'ER', 'AM', 'EE', 'ET', 'FO', 'MA', 'FJ', 'CI', 'PH', 'PS', 'FI', 'FR',
        'GA', 'GM', 'GH', 'GN', 'GD', 'GL', 'GY', 'GT', 'ZA', 'KR', 'GE', 'HT', 'HR', 'IN', 'NL', 'HN', 'HK', 'IQ',
        'GB', 'IR', 'IE', 'ES', 'IL', 'SE', 'CH', 'IT', 'IS', 'JM', 'JP', 'KH', 'CM', 'CA', 'QA', 'KZ', 'KE', 'KG',
        'CY', 'CO', 'CG', 'CR', 'KW', 'KP', 'CU', 'LS', 'LV', 'LR', 'LY', 'LI', 'LT', 'LB', 'LU', 'HU', 'MG', 'MK',
        'MW', 'MV', 'MY', 'ML', 'MT', 'MX', 'EG', 'MN', 'MD', 'MC', 'MZ', 'MM', 'NA', 'NP', 'NI', 'NE', 'NG', 'NO',
        'CF', 'UZ', 'PK', 'PA', 'PG', 'PY', 'PE', 'PL', 'PT', 'PR', 'RO', 'RW', 'RU', 'WS', 'SM', 'SN', 'SC', 'CS',
        'SL', 'SG', 'SK', 'SI', 'SO', 'LK', 'SD', 'SR', 'SY', 'SA', 'SZ', 'CL', 'TJ', 'TZ', 'TH', 'TW', 'TG', 'TT',
        'TN', 'TR', 'TM', 'UG', 'UA', 'OM', 'UY', 'JO', 'VE', 'VN', 'YE', 'NZ', 'CV', 'GR', 'ZM', 'ZW'
    )
    countries = (
        'Afganistan', 'Almanya', 'Amerika Birleşik Devletleri', 'Arnavutluk', 'Andorra', 'Angola',
        'Antigua ve Barbuda', 'Arjantin', 'Avustralya', 'Avusturya', 'Azerbaycan', 'Bahamalar','Bahreyn',
        'Bangladeş', 'Barbados', 'Belarus', 'Belçika', 'Belize', 'Benin', 'Bermuda', 'Birleşik Arap Emirlikleri',
        'Bolivya', 'Bosna Hersek', 'Botswana', 'Brezilya', 'Bulgaristan', 'Burkina Faso', 'Burundi', 'Butan',
        'Büyük Britanya', 'Cebelitarık', 'Cezayir', 'Cibuti', 'Çad', 'Çek Cumhuriyeti', 'Çin Halk Cumhuriyeti', 'Danimarka',
        'Dominik Cumhuriyeti', 'Ekvador', 'Ekvator Ginesi', 'El Salvador', 'Endonezya', 'Eritre', 'Ermenistan',
        'Estonya', 'Etiyopya', 'Faroe Adaları', 'Fas', 'Fiji', 'Fildişi Sahilleri', 'Filipinler', 'Filistin',
        'Finlandiya', 'Fransa', 'Gabon', 'Gambiya', 'Gana', 'Gine', 'Grenada', 'Grönland', 'Guyana',
        'Guatemala', 'Güney Afrika Cumhuriyeti', 'Güney Kore', 'Gürcistan', 'Haiti', 'Hırvatistan', 'Hindistan',
        'Hollanda', 'Honduras', 'Hong Kong', 'Irak', 'İran', 'İrlanda', 'İspanya',
        'İsrail', 'İsveç', 'İsviçre', 'İtalya', 'İzlanda', 'Jamaika', 'Japonya', 'Kamboçya', 'Kamerun', 'Kanada',
        'Karadağ', 'Katar', 'Kazakistan', 'Kenya', 'Kırgızistan', 'Kıbrıs Cumhuriyeti', 'Kolombiya', 'Kongo',
        'Kosta Rika', 'Kuveyt', 'Kuzey Kıbrıs Türk Cumhuriyeti', 'Kuzey Kore', 'Küba', 'Lesotho', 'Letonya',
        'Liberya', 'Libya', 'Lihtenştayn', 'Litvanya', 'Lübnan', 'Lüksemburg', 'Macaristan', 'Madagaskar',
        'Makedonya Cumhuriyeti', 'Malavi', 'Maldivler', 'Malezya', 'Mali', 'Malta', 'Meksika', 'Mısır',
        'Moğolistan', 'Moldova', 'Monako Krallığı', 'Mozambik', 'Myanmar', 'Namibya', 'Nepal', 'Nikaragua',
        'Nijer', 'Nijerya', 'Norveç', 'Orta Afrika Cumhuriyeti', 'Özbekistan', 'Pakistan', 'Panama',
        'Papua Yeni Gine', 'Paraguay', 'Peru', 'Polonya', 'Portekiz', 'Porto Riko', 'Romanya', 'Ruanda',
        'Rusya Federasyonu', 'Samoa', 'San Marino', 'Senegal', 'Seyşeller', 'Sırbistan',  'Sierra Leone',
        'Singapur', 'Slovakya', 'Slovenya', 'Somali', 'Sri Lanka', 'Sudan', 'Surinam', 'Suriye', 'Suudi Arabistan',
        'Svaziland', 'Şili', 'Tacikistan', 'Tanzanya', 'Tayland', 'Tayvan', 'Togo', 'Trinidad Tobago', 'Tunus',
        'Türkiye', 'Türkmenistan', 'Uganda', 'Ukrayna', 'Umman', 'Uruguay', 'Ürdün', 'Vatikan', 'Venezuela',
        'Vietnam', 'Yemen', 'Yeni Zelanda', 'Yeşil Burun Adaları', 'Yunanistan', 'Zambiya', 'Zimbabve'
    )

    city_formats = (
        '{{city_prefix}} {{first_name}} {{city_suffix}}',
        '{{city_prefix}} {{first_name}}',
        '{{first_name}} {{city_suffix}}',
        '{{last_name}} {{city_suffix}}',
    )
    street_name_formats = (
        '{{street_suffix}} {{first_name}}',
        '{{street_suffix}} {{last_name}}'
    )
    street_address_formats = (
        '{{street_name}} {{building_number}}',
        '{{street_name}} {{building_number}} {{secondary_address}}',
    )
    address_formats = (
        "{{street_address}}\n{{city}}, {{postcode}} {{state}} ({{state_abbr}})",
    )
    secondary_address_formats = ('Appartamento ##', 'Piano #')

    @classmethod
    def city_prefix(cls):
        return cls.random_element(cls.city_prefixes)

    @classmethod
    def secondary_address(cls):
        return cls.numerify(cls.random_element(cls.secondary_address_formats))

    @classmethod
    def state(cls):
        return cls.random_element(cls.states)

    @classmethod
    def state_abbr(cls):
        return cls.random_element(cls.states_abbr)

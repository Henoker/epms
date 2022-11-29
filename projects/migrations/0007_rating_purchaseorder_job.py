# Generated by Django 4.0.8 on 2022-11-29 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0006_invoice_remove_project_currency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=200)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, 'Below Expectation greater than 0.02'), (2, 'Meet Expectaion 0.02'), (3, 'Exceed Expectaions less than 0.02')])),
                ('reviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluated_vendor', to='projects.vendor')),
                ('reviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.CharField(blank=True, max_length=100, null=True)),
                ('dueDate', models.DateField(blank=True, null=True)),
                ('paymentTerms', models.CharField(choices=[('30 days', '30 days'), ('45 days', '45 days'), ('60 days', '60 days'), ('Contract', 'Contract')], default='14 days', max_length=100)),
                ('status', models.CharField(choices=[('CURRENT', 'CURRENT'), ('EMAIL_SENT', 'EMAIL_SENT'), ('OVERDUE', 'OVERDUE'), ('PAID', 'PAID')], default='CURRENT', max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('source_language', models.CharField(blank=True, choices=[('Afar', 'Afar'), ('Abkhazian', 'Abkhazian'), ('Achinese', 'Achinese'), ('Acoli', 'Acoli'), ('Adangme', 'Adangme'), ('Adyghe; Adygei', 'Adyghe; Adygei'), ('Afro-Asiatic languages', 'Afro-Asiatic languages'), ('Afrihili', 'Afrihili'), ('Afrikaans', 'Afrikaans'), ('Ainu', 'Ainu'), ('Akan', 'Akan'), ('Akkadian', 'Akkadian'), ('Albanian', 'Albanian'), ('Aleut', 'Aleut'), ('Algonquian languages', 'Algonquian languages'), ('Southern Altai', 'Southern Altai'), ('Amharic', 'Amharic'), ('Angika', 'Angika'), ('Apache languages', 'Apache languages'), ('Arabic', 'Arabic'), ('Aragonese', 'Aragonese'), ('Armenian', 'Armenian'), ('Mapudungun; Mapuche', 'Mapudungun; Mapuche'), ('Arapaho', 'Arapaho'), ('Artificial languages', 'Artificial languages'), ('Arawak', 'Arawak'), ('Assamese', 'Assamese'), ('Athapascan languages', 'Athapascan languages'), ('Australian languages', 'Australian languages'), ('Avaric', 'Avaric'), ('Avestan', 'Avestan'), ('Awadhi', 'Awadhi'), ('Aymara', 'Aymara'), ('Azerbaijani', 'Azerbaijani'), ('Banda languages', 'Banda languages'), ('Bamileke languages', 'Bamileke languages'), ('Bashkir', 'Bashkir'), ('Baluchi', 'Baluchi'), ('Bambara', 'Bambara'), ('Balinese', 'Balinese'), ('Basque', 'Basque'), ('Basa', 'Basa'), ('Baltic languages', 'Baltic languages'), ('Beja; Bedawiyet', 'Beja; Bedawiyet'), ('Belarusian', 'Belarusian'), ('Bemba', 'Bemba'), ('Bengali', 'Bengali'), ('Berber languages', 'Berber languages'), ('Bhojpuri', 'Bhojpuri'), ('Bihari languages', 'Bihari languages'), ('Bikol', 'Bikol'), ('Bini; Edo', 'Bini; Edo'), ('Bislama', 'Bislama'), ('Siksika', 'Siksika'), ('Bantu (Other)', 'Bantu (Other)'), ('Bosnian', 'Bosnian'), ('Braj', 'Braj'), ('Breton', 'Breton'), ('Batak languages', 'Batak languages'), ('Buriat', 'Buriat'), ('Buginese', 'Buginese'), ('Bulgarian', 'Bulgarian'), ('Burmese', 'Burmese'), ('Blin; Bilin', 'Blin; Bilin'), ('Caddo', 'Caddo'), ('Central American Indian languages', 'Central American Indian languages'), ('Galibi Carib', 'Galibi Carib'), ('Catalan; Valencian', 'Catalan; Valencian'), ('Caucasian languages', 'Caucasian languages'), ('Cebuano', 'Cebuano'), ('Celtic languages', 'Celtic languages'), ('Chamorro', 'Chamorro'), ('Chibcha', 'Chibcha'), ('Chechen', 'Chechen'), ('Chagatai', 'Chagatai'), ('Chinese', 'Chinese'), ('Chuukese', 'Chuukese'), ('Mari', 'Mari'), ('Chinook jargon', 'Chinook jargon'), ('Choctaw', 'Choctaw'), ('Chipewyan; Dene Suline', 'Chipewyan; Dene Suline'), ('Cherokee', 'Cherokee'), ('Chuvash', 'Chuvash'), ('Cheyenne', 'Cheyenne'), ('Chamic languages', 'Chamic languages'), ('Coptic', 'Coptic'), ('Cornish', 'Cornish'), ('Corsican', 'Corsican'), ('Cree', 'Cree'), ('Crimean Tatar; Crimean Turkish', 'Crimean Tatar; Crimean Turkish'), ('Creoles and pidgins ', 'Creoles and pidgins '), ('Kashubian', 'Kashubian'), ('Cushitic languages', 'Cushitic languages'), ('Czech', 'Czech'), ('Dakota', 'Dakota'), ('Danish', 'Danish'), ('Dargwa', 'Dargwa'), ('Land Dayak languages', 'Land Dayak languages'), ('Delaware', 'Delaware'), ('Slave (Athapascan)', 'Slave (Athapascan)'), ('Dogrib', 'Dogrib'), ('Dinka', 'Dinka'), ('Divehi; Dhivehi; Maldivian', 'Divehi; Dhivehi; Maldivian'), ('Dogri', 'Dogri'), ('Dravidian languages', 'Dravidian languages'), ('Lower Sorbian', 'Lower Sorbian'), ('Duala', 'Duala'), ('Dutch', 'Dutch'), ('Dyula', 'Dyula'), ('Dzongkha', 'Dzongkha'), ('Efik', 'Efik'), ('Egyptian (Ancient)', 'Egyptian (Ancient)'), ('Ekajuk', 'Ekajuk'), ('Elamite', 'Elamite'), ('English', 'English'), ('Esperanto', 'Esperanto'), ('Estonian', 'Estonian'), ('Ewe', 'Ewe'), ('Ewondo', 'Ewondo'), ('Fang', 'Fang'), ('Faroese', 'Faroese'), ('Fanti', 'Fanti'), ('Fijian', 'Fijian'), ('Filipino; Pilipino', 'Filipino; Pilipino'), ('Finnish', 'Finnish'), ('Finno-Ugrian languages', 'Finno-Ugrian languages'), ('Fon', 'Fon'), ('French', 'French'), ('Northern Frisian', 'Northern Frisian'), ('Eastern Frisian', 'Eastern Frisian'), ('Western Frisian', 'Western Frisian'), ('Fulah', 'Fulah'), ('Friulian', 'Friulian'), ('Ga', 'Ga'), ('Gayo', 'Gayo'), ('Gbaya', 'Gbaya'), ('Germanic languages', 'Germanic languages'), ('Georgian', 'Georgian'), ('German', 'German'), ('Geez', 'Geez'), ('Gilbertese', 'Gilbertese'), ('Gaelic; Scottish Gaelic', 'Gaelic; Scottish Gaelic'), ('Irish', 'Irish'), ('Galician', 'Galician'), ('Manx', 'Manx'), ('German', 'German'), ('Gondi', 'Gondi'), ('Gorontalo', 'Gorontalo'), ('Gothic', 'Gothic'), ('Grebo', 'Grebo'), ('Greek', 'Greek'), ('Guarani', 'Guarani'), ('Swiss German; Alemannic; Alsatian', 'Swiss German; Alemannic; Alsatian'), ('Gujarati', 'Gujarati'), ("Gwich'in", "Gwich'in"), ('Haida', 'Haida'), ('Haitian; Haitian Creole', 'Haitian; Haitian Creole'), ('Hausa', 'Hausa'), ('Hawaiian', 'Hawaiian'), ('Hebrew', 'Hebrew'), ('Herero', 'Herero'), ('Hiligaynon', 'Hiligaynon'), ('Himachali languages; Western Pahari languages', 'Himachali languages; Western Pahari languages'), ('Hindi', 'Hindi'), ('Hittite', 'Hittite'), ('Hmong; Mong', 'Hmong; Mong'), ('Hiri Motu', 'Hiri Motu'), ('Croatian', 'Croatian'), ('Upper Sorbian', 'Upper Sorbian'), ('Hungarian', 'Hungarian'), ('Hupa', 'Hupa'), ('Iban', 'Iban'), ('Igbo', 'Igbo'), ('Icelandic', 'Icelandic'), ('Ido', 'Ido'), ('Sichuan Yi; Nuosu', 'Sichuan Yi; Nuosu'), ('Ijo languages', 'Ijo languages'), ('Inuktitut', 'Inuktitut'), ('Interlingue; Occidental', 'Interlingue; Occidental'), ('Iloko', 'Iloko'), ('Indic languages', 'Indic languages'), ('Indonesian', 'Indonesian'), ('Indo-European languages', 'Indo-European languages'), ('Ingush', 'Ingush'), ('Inupiaq', 'Inupiaq'), ('Iranian languages', 'Iranian languages'), ('Iroquoian languages', 'Iroquoian languages'), ('Italian', 'Italian'), ('Javanese', 'Javanese'), ('Lojban', 'Lojban'), ('Japanese', 'Japanese'), ('Judeo-Persian', 'Judeo-Persian'), ('Judeo-Arabic', 'Judeo-Arabic'), ('Kara-Kalpak', 'Kara-Kalpak'), ('Kabyle', 'Kabyle'), ('Kachin; Jingpho', 'Kachin; Jingpho'), ('Kalaallisut; Greenlandic', 'Kalaallisut; Greenlandic'), ('Kamba', 'Kamba'), ('Kannada', 'Kannada'), ('Karen languages', 'Karen languages'), ('Kashmiri', 'Kashmiri'), ('Kanuri', 'Kanuri'), ('Kawi', 'Kawi'), ('Kazakh', 'Kazakh'), ('Kabardian', 'Kabardian'), ('Khasi', 'Khasi'), ('Khoisan languages', 'Khoisan languages'), ('Central Khmer', 'Central Khmer'), ('Khotanese; Sakan', 'Khotanese; Sakan'), ('Kikuyu; Gikuyu', 'Kikuyu; Gikuyu'), ('Kinyarwanda', 'Kinyarwanda'), ('Kirghiz; Kyrgyz', 'Kirghiz; Kyrgyz'), ('Kimbundu', 'Kimbundu'), ('Konkani', 'Konkani'), ('Komi', 'Komi'), ('Kongo', 'Kongo'), ('Korean', 'Korean'), ('Kosraean', 'Kosraean'), ('Kpelle', 'Kpelle'), ('Karachay-Balkar', 'Karachay-Balkar'), ('Karelian', 'Karelian'), ('Kru languages', 'Kru languages'), ('Kurukh', 'Kurukh'), ('Kuanyama; Kwanyama', 'Kuanyama; Kwanyama'), ('Kumyk', 'Kumyk'), ('Kunama', 'Kunama'), ('Kurdish', 'Kurdish'), ('Kutenai', 'Kutenai'), ('Ladino', 'Ladino'), ('Lahnda', 'Lahnda'), ('Lamba', 'Lamba'), ('Lao', 'Lao'), ('Latin', 'Latin'), ('Latvian', 'Latvian'), ('Lezghian', 'Lezghian'), ('Limburgan; Limburger; Limburgish', 'Limburgan; Limburger; Limburgish'), ('Lingala', 'Lingala'), ('Lithuanian', 'Lithuanian'), ('Mongo', 'Mongo'), ('Lozi', 'Lozi'), ('Luxembourgish; Letzeburgesch', 'Luxembourgish; Letzeburgesch'), ('Luba-Lulua', 'Luba-Lulua'), ('Luba-Katanga', 'Luba-Katanga'), ('Ganda', 'Ganda'), ('Luiseno', 'Luiseno'), ('Lunda', 'Lunda'), ('Luo (Kenya and Tanzania)', 'Luo (Kenya and Tanzania)'), ('Lushai', 'Lushai'), ('Macedonian', 'Macedonian'), ('Madurese', 'Madurese'), ('Magahi', 'Magahi'), ('Marshallese', 'Marshallese'), ('Maithili', 'Maithili'), ('Makasar', 'Makasar'), ('Malayalam', 'Malayalam'), ('Mandingo', 'Mandingo'), ('Maori', 'Maori'), ('Austronesian languages', 'Austronesian languages'), ('Marathi', 'Marathi'), ('Masai', 'Masai'), ('Malay', 'Malay'), ('Moksha', 'Moksha'), ('Mandar', 'Mandar'), ('Mende', 'Mende'), ('Irish', 'Irish'), ("Mi'kmaq; Micmac", "Mi'kmaq; Micmac"), ('Minangkabau', 'Minangkabau'), ('Uncoded languages', 'Uncoded languages'), ('Mon-Khmer languages', 'Mon-Khmer languages'), ('Malagasy', 'Malagasy'), ('Maltese', 'Maltese'), ('Manchu', 'Manchu'), ('Manipuri', 'Manipuri'), ('Manobo languages', 'Manobo languages'), ('Mohawk', 'Mohawk'), ('Mongolian', 'Mongolian'), ('Mossi', 'Mossi'), ('Multiple languages', 'Multiple languages'), ('Munda languages', 'Munda languages'), ('Creek', 'Creek'), ('Mirandese', 'Mirandese'), ('Marwari', 'Marwari'), ('Mayan languages', 'Mayan languages'), ('Erzya', 'Erzya'), ('Nahuatl languages', 'Nahuatl languages'), ('North American Indian languages', 'North American Indian languages'), ('Neapolitan', 'Neapolitan'), ('Nauru', 'Nauru'), ('Navajo; Navaho', 'Navajo; Navaho'), ('Ndebele, South; South Ndebele', 'Ndebele, South; South Ndebele'), ('Ndebele, North; North Ndebele', 'Ndebele, North; North Ndebele'), ('Ndonga', 'Ndonga'), ('Nepali', 'Nepali'), ('Nepal Bhasa; Newari', 'Nepal Bhasa; Newari'), ('Nias', 'Nias'), ('Niger-Kordofanian languages', 'Niger-Kordofanian languages'), ('Niuean', 'Niuean'), ('Nogai', 'Nogai'), ('Norse, Old', 'Norse, Old'), ('Norwegian', 'Norwegian'), ("N'Ko", "N'Ko"), ('Pedi; Sepedi; Northern Sotho', 'Pedi; Sepedi; Northern Sotho'), ('Nubian languages', 'Nubian languages'), ('Chichewa; Chewa; Nyanja', 'Chichewa; Chewa; Nyanja'), ('Nyamwezi', 'Nyamwezi'), ('Nyankole', 'Nyankole'), ('Nyoro', 'Nyoro'), ('Nzima', 'Nzima'), ('Occitan (post 1500); Provençal', 'Occitan (post 1500); Provençal'), ('Ojibwa', 'Ojibwa'), ('Oriya', 'Oriya'), ('Oromo', 'Oromo'), ('Osage', 'Osage'), ('Ossetian; Ossetic', 'Ossetian; Ossetic'), ('Turkish, Ottoman (1500-1928)', 'Turkish, Ottoman (1500-1928)'), ('Otomian languages', 'Otomian languages'), ('Papuan languages', 'Papuan languages'), ('Pangasinan', 'Pangasinan'), ('Pahlavi', 'Pahlavi'), ('Pampanga; Kapampangan', 'Pampanga; Kapampangan'), ('Panjabi; Punjabi', 'Panjabi; Punjabi'), ('Papiamento', 'Papiamento'), ('Palauan', 'Palauan'), ('Persian, Old (ca.600-400 B.C.)', 'Persian, Old (ca.600-400 B.C.)'), ('Persian', 'Persian'), ('Philippine languages', 'Philippine languages'), ('Phoenician', 'Phoenician'), ('Pali', 'Pali'), ('Polish', 'Polish'), ('Pohnpeian', 'Pohnpeian'), ('Portuguese', 'Portuguese'), ('Prakrit languages', 'Prakrit languages'), ('Provençal, Old (to 1500)', 'Provençal, Old (to 1500)'), ('Pushto; Pashto', 'Pushto; Pashto'), ('Reserved for local use', 'Reserved for local use'), ('Quechua', 'Quechua'), ('Rajasthani', 'Rajasthani'), ('Rapanui', 'Rapanui'), ('Rarotongan; Cook Islands Maori', 'Rarotongan; Cook Islands Maori'), ('Romance languages', 'Romance languages'), ('Romansh', 'Romansh'), ('Romany', 'Romany'), ('Romanian; Moldavian; Moldovan', 'Romanian; Moldavian; Moldovan'), ('Rundi', 'Rundi'), ('Russian', 'Russian'), ('Sandawe', 'Sandawe'), ('Sango', 'Sango'), ('Yakut', 'Yakut'), ('South American Indian (Other)', 'South American Indian (Other)'), ('Salishan languages', 'Salishan languages'), ('Samaritan Aramaic', 'Samaritan Aramaic'), ('Sanskrit', 'Sanskrit'), ('Sasak', 'Sasak'), ('Santali', 'Santali'), ('Sicilian', 'Sicilian'), ('Scots', 'Scots'), ('Selkup', 'Selkup'), ('Semitic languages', 'Semitic languages'), ('Irish, Old (to 900)', 'Irish, Old (to 900)'), ('Sign Languages', 'Sign Languages'), ('Shan', 'Shan'), ('Sidamo', 'Sidamo'), ('Sinhala; Sinhalese', 'Sinhala; Sinhalese'), ('Siouan languages', 'Siouan languages'), ('Sino-Tibetan languages', 'Sino-Tibetan languages'), ('Slavic languages', 'Slavic languages'), ('Slovak', 'Slovak'), ('Slovenian', 'Slovenian'), ('Southern Sami', 'Southern Sami'), ('Northern Sami', 'Northern Sami'), ('Sami languages', 'Sami languages'), ('Lule Sami', 'Lule Sami'), ('Inari Sami', 'Inari Sami'), ('Samoan', 'Samoan'), ('Skolt Sami', 'Skolt Sami'), ('Shona', 'Shona'), ('Sindhi', 'Sindhi'), ('Soninke', 'Soninke'), ('Sogdian', 'Sogdian'), ('Somali', 'Somali'), ('Songhai languages', 'Songhai languages'), ('Sotho, Southern', 'Sotho, Southern'), ('Spanish; Castilian', 'Spanish; Castilian'), ('Sardinian', 'Sardinian'), ('Sranan Tongo', 'Sranan Tongo'), ('Serbian', 'Serbian'), ('Serer', 'Serer'), ('Nilo-Saharan languages', 'Nilo-Saharan languages'), ('Swati', 'Swati'), ('Sukuma', 'Sukuma'), ('Sundanese', 'Sundanese'), ('Susu', 'Susu'), ('Sumerian', 'Sumerian'), ('Swahili', 'Swahili'), ('Swedish', 'Swedish'), ('Classical Syriac', 'Classical Syriac'), ('Syriac', 'Syriac'), ('Tahitian', 'Tahitian'), ('Tai languages', 'Tai languages'), ('Tamil', 'Tamil'), ('Tatar', 'Tatar'), ('Telugu', 'Telugu'), ('Timne', 'Timne'), ('Tereno', 'Tereno'), ('Tetum', 'Tetum'), ('Tajik', 'Tajik'), ('Tagalog', 'Tagalog'), ('Thai', 'Thai'), ('Tibetan', 'Tibetan'), ('Tigre', 'Tigre'), ('Tigrinya', 'Tigrinya'), ('Tiv', 'Tiv'), ('Tokelau', 'Tokelau'), ('Klingon; tlhIngan-Hol', 'Klingon; tlhIngan-Hol'), ('Tlingit', 'Tlingit'), ('Tamashek', 'Tamashek'), ('Tonga (Nyasa)', 'Tonga (Nyasa)'), ('Tonga (Tonga Islands)', 'Tonga (Tonga Islands)'), ('Tok Pisin', 'Tok Pisin'), ('Tsimshian', 'Tsimshian'), ('Tswana', 'Tswana'), ('Tsonga', 'Tsonga'), ('Turkmen', 'Turkmen'), ('Tumbuka', 'Tumbuka'), ('Tupi languages', 'Tupi languages'), ('Turkish', 'Turkish'), ('Altaic languages', 'Altaic languages'), ('Tuvalu', 'Tuvalu'), ('Twi', 'Twi'), ('Tuvinian', 'Tuvinian'), ('Udmurt', 'Udmurt'), ('Ugaritic', 'Ugaritic'), ('Uighur; Uyghur', 'Uighur; Uyghur'), ('Ukrainian', 'Ukrainian'), ('Umbundu', 'Umbundu'), ('Undetermined', 'Undetermined'), ('Urdu', 'Urdu'), ('Uzbek', 'Uzbek'), ('Vai', 'Vai'), ('Venda', 'Venda'), ('Vietnamese', 'Vietnamese'), ('Volapük', 'Volapük'), ('Votic', 'Votic'), ('Wakashan languages', 'Wakashan languages'), ('Walamo', 'Walamo'), ('Waray', 'Waray'), ('Washo', 'Washo'), ('Welsh', 'Welsh'), ('Sorbian languages', 'Sorbian languages'), ('Walloon', 'Walloon'), ('Wolof', 'Wolof'), ('Kalmyk; Oirat', 'Kalmyk; Oirat'), ('Xhosa', 'Xhosa'), ('Yao', 'Yao'), ('Yapese', 'Yapese'), ('Yiddish', 'Yiddish'), ('Yoruba', 'Yoruba'), ('Yupik languages', 'Yupik languages'), ('Zapotec', 'Zapotec'), ('Blissymbols; Blissymbolics; Bliss', 'Blissymbols; Blissymbolics; Bliss'), ('Zenaga', 'Zenaga'), ('Standard Moroccan Tamazight', 'Standard Moroccan Tamazight'), ('Zhuang; Chuang', 'Zhuang; Chuang'), ('Zande languages', 'Zande languages'), ('Zulu', 'Zulu'), ('Zuni', 'Zuni'), ('No linguistic content; Not applicable', 'No linguistic content; Not applicable'), ('Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki', 'Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki')], max_length=300)),
                ('target_language', models.CharField(blank=True, choices=[('Afar', 'Afar'), ('Abkhazian', 'Abkhazian'), ('Achinese', 'Achinese'), ('Acoli', 'Acoli'), ('Adangme', 'Adangme'), ('Adyghe; Adygei', 'Adyghe; Adygei'), ('Afro-Asiatic languages', 'Afro-Asiatic languages'), ('Afrihili', 'Afrihili'), ('Afrikaans', 'Afrikaans'), ('Ainu', 'Ainu'), ('Akan', 'Akan'), ('Akkadian', 'Akkadian'), ('Albanian', 'Albanian'), ('Aleut', 'Aleut'), ('Algonquian languages', 'Algonquian languages'), ('Southern Altai', 'Southern Altai'), ('Amharic', 'Amharic'), ('Angika', 'Angika'), ('Apache languages', 'Apache languages'), ('Arabic', 'Arabic'), ('Aragonese', 'Aragonese'), ('Armenian', 'Armenian'), ('Mapudungun; Mapuche', 'Mapudungun; Mapuche'), ('Arapaho', 'Arapaho'), ('Artificial languages', 'Artificial languages'), ('Arawak', 'Arawak'), ('Assamese', 'Assamese'), ('Athapascan languages', 'Athapascan languages'), ('Australian languages', 'Australian languages'), ('Avaric', 'Avaric'), ('Avestan', 'Avestan'), ('Awadhi', 'Awadhi'), ('Aymara', 'Aymara'), ('Azerbaijani', 'Azerbaijani'), ('Banda languages', 'Banda languages'), ('Bamileke languages', 'Bamileke languages'), ('Bashkir', 'Bashkir'), ('Baluchi', 'Baluchi'), ('Bambara', 'Bambara'), ('Balinese', 'Balinese'), ('Basque', 'Basque'), ('Basa', 'Basa'), ('Baltic languages', 'Baltic languages'), ('Beja; Bedawiyet', 'Beja; Bedawiyet'), ('Belarusian', 'Belarusian'), ('Bemba', 'Bemba'), ('Bengali', 'Bengali'), ('Berber languages', 'Berber languages'), ('Bhojpuri', 'Bhojpuri'), ('Bihari languages', 'Bihari languages'), ('Bikol', 'Bikol'), ('Bini; Edo', 'Bini; Edo'), ('Bislama', 'Bislama'), ('Siksika', 'Siksika'), ('Bantu (Other)', 'Bantu (Other)'), ('Bosnian', 'Bosnian'), ('Braj', 'Braj'), ('Breton', 'Breton'), ('Batak languages', 'Batak languages'), ('Buriat', 'Buriat'), ('Buginese', 'Buginese'), ('Bulgarian', 'Bulgarian'), ('Burmese', 'Burmese'), ('Blin; Bilin', 'Blin; Bilin'), ('Caddo', 'Caddo'), ('Central American Indian languages', 'Central American Indian languages'), ('Galibi Carib', 'Galibi Carib'), ('Catalan; Valencian', 'Catalan; Valencian'), ('Caucasian languages', 'Caucasian languages'), ('Cebuano', 'Cebuano'), ('Celtic languages', 'Celtic languages'), ('Chamorro', 'Chamorro'), ('Chibcha', 'Chibcha'), ('Chechen', 'Chechen'), ('Chagatai', 'Chagatai'), ('Chinese', 'Chinese'), ('Chuukese', 'Chuukese'), ('Mari', 'Mari'), ('Chinook jargon', 'Chinook jargon'), ('Choctaw', 'Choctaw'), ('Chipewyan; Dene Suline', 'Chipewyan; Dene Suline'), ('Cherokee', 'Cherokee'), ('Chuvash', 'Chuvash'), ('Cheyenne', 'Cheyenne'), ('Chamic languages', 'Chamic languages'), ('Coptic', 'Coptic'), ('Cornish', 'Cornish'), ('Corsican', 'Corsican'), ('Cree', 'Cree'), ('Crimean Tatar; Crimean Turkish', 'Crimean Tatar; Crimean Turkish'), ('Creoles and pidgins ', 'Creoles and pidgins '), ('Kashubian', 'Kashubian'), ('Cushitic languages', 'Cushitic languages'), ('Czech', 'Czech'), ('Dakota', 'Dakota'), ('Danish', 'Danish'), ('Dargwa', 'Dargwa'), ('Land Dayak languages', 'Land Dayak languages'), ('Delaware', 'Delaware'), ('Slave (Athapascan)', 'Slave (Athapascan)'), ('Dogrib', 'Dogrib'), ('Dinka', 'Dinka'), ('Divehi; Dhivehi; Maldivian', 'Divehi; Dhivehi; Maldivian'), ('Dogri', 'Dogri'), ('Dravidian languages', 'Dravidian languages'), ('Lower Sorbian', 'Lower Sorbian'), ('Duala', 'Duala'), ('Dutch', 'Dutch'), ('Dyula', 'Dyula'), ('Dzongkha', 'Dzongkha'), ('Efik', 'Efik'), ('Egyptian (Ancient)', 'Egyptian (Ancient)'), ('Ekajuk', 'Ekajuk'), ('Elamite', 'Elamite'), ('English', 'English'), ('Esperanto', 'Esperanto'), ('Estonian', 'Estonian'), ('Ewe', 'Ewe'), ('Ewondo', 'Ewondo'), ('Fang', 'Fang'), ('Faroese', 'Faroese'), ('Fanti', 'Fanti'), ('Fijian', 'Fijian'), ('Filipino; Pilipino', 'Filipino; Pilipino'), ('Finnish', 'Finnish'), ('Finno-Ugrian languages', 'Finno-Ugrian languages'), ('Fon', 'Fon'), ('French', 'French'), ('Northern Frisian', 'Northern Frisian'), ('Eastern Frisian', 'Eastern Frisian'), ('Western Frisian', 'Western Frisian'), ('Fulah', 'Fulah'), ('Friulian', 'Friulian'), ('Ga', 'Ga'), ('Gayo', 'Gayo'), ('Gbaya', 'Gbaya'), ('Germanic languages', 'Germanic languages'), ('Georgian', 'Georgian'), ('German', 'German'), ('Geez', 'Geez'), ('Gilbertese', 'Gilbertese'), ('Gaelic; Scottish Gaelic', 'Gaelic; Scottish Gaelic'), ('Irish', 'Irish'), ('Galician', 'Galician'), ('Manx', 'Manx'), ('German', 'German'), ('Gondi', 'Gondi'), ('Gorontalo', 'Gorontalo'), ('Gothic', 'Gothic'), ('Grebo', 'Grebo'), ('Greek', 'Greek'), ('Guarani', 'Guarani'), ('Swiss German; Alemannic; Alsatian', 'Swiss German; Alemannic; Alsatian'), ('Gujarati', 'Gujarati'), ("Gwich'in", "Gwich'in"), ('Haida', 'Haida'), ('Haitian; Haitian Creole', 'Haitian; Haitian Creole'), ('Hausa', 'Hausa'), ('Hawaiian', 'Hawaiian'), ('Hebrew', 'Hebrew'), ('Herero', 'Herero'), ('Hiligaynon', 'Hiligaynon'), ('Himachali languages; Western Pahari languages', 'Himachali languages; Western Pahari languages'), ('Hindi', 'Hindi'), ('Hittite', 'Hittite'), ('Hmong; Mong', 'Hmong; Mong'), ('Hiri Motu', 'Hiri Motu'), ('Croatian', 'Croatian'), ('Upper Sorbian', 'Upper Sorbian'), ('Hungarian', 'Hungarian'), ('Hupa', 'Hupa'), ('Iban', 'Iban'), ('Igbo', 'Igbo'), ('Icelandic', 'Icelandic'), ('Ido', 'Ido'), ('Sichuan Yi; Nuosu', 'Sichuan Yi; Nuosu'), ('Ijo languages', 'Ijo languages'), ('Inuktitut', 'Inuktitut'), ('Interlingue; Occidental', 'Interlingue; Occidental'), ('Iloko', 'Iloko'), ('Indic languages', 'Indic languages'), ('Indonesian', 'Indonesian'), ('Indo-European languages', 'Indo-European languages'), ('Ingush', 'Ingush'), ('Inupiaq', 'Inupiaq'), ('Iranian languages', 'Iranian languages'), ('Iroquoian languages', 'Iroquoian languages'), ('Italian', 'Italian'), ('Javanese', 'Javanese'), ('Lojban', 'Lojban'), ('Japanese', 'Japanese'), ('Judeo-Persian', 'Judeo-Persian'), ('Judeo-Arabic', 'Judeo-Arabic'), ('Kara-Kalpak', 'Kara-Kalpak'), ('Kabyle', 'Kabyle'), ('Kachin; Jingpho', 'Kachin; Jingpho'), ('Kalaallisut; Greenlandic', 'Kalaallisut; Greenlandic'), ('Kamba', 'Kamba'), ('Kannada', 'Kannada'), ('Karen languages', 'Karen languages'), ('Kashmiri', 'Kashmiri'), ('Kanuri', 'Kanuri'), ('Kawi', 'Kawi'), ('Kazakh', 'Kazakh'), ('Kabardian', 'Kabardian'), ('Khasi', 'Khasi'), ('Khoisan languages', 'Khoisan languages'), ('Central Khmer', 'Central Khmer'), ('Khotanese; Sakan', 'Khotanese; Sakan'), ('Kikuyu; Gikuyu', 'Kikuyu; Gikuyu'), ('Kinyarwanda', 'Kinyarwanda'), ('Kirghiz; Kyrgyz', 'Kirghiz; Kyrgyz'), ('Kimbundu', 'Kimbundu'), ('Konkani', 'Konkani'), ('Komi', 'Komi'), ('Kongo', 'Kongo'), ('Korean', 'Korean'), ('Kosraean', 'Kosraean'), ('Kpelle', 'Kpelle'), ('Karachay-Balkar', 'Karachay-Balkar'), ('Karelian', 'Karelian'), ('Kru languages', 'Kru languages'), ('Kurukh', 'Kurukh'), ('Kuanyama; Kwanyama', 'Kuanyama; Kwanyama'), ('Kumyk', 'Kumyk'), ('Kunama', 'Kunama'), ('Kurdish', 'Kurdish'), ('Kutenai', 'Kutenai'), ('Ladino', 'Ladino'), ('Lahnda', 'Lahnda'), ('Lamba', 'Lamba'), ('Lao', 'Lao'), ('Latin', 'Latin'), ('Latvian', 'Latvian'), ('Lezghian', 'Lezghian'), ('Limburgan; Limburger; Limburgish', 'Limburgan; Limburger; Limburgish'), ('Lingala', 'Lingala'), ('Lithuanian', 'Lithuanian'), ('Mongo', 'Mongo'), ('Lozi', 'Lozi'), ('Luxembourgish; Letzeburgesch', 'Luxembourgish; Letzeburgesch'), ('Luba-Lulua', 'Luba-Lulua'), ('Luba-Katanga', 'Luba-Katanga'), ('Ganda', 'Ganda'), ('Luiseno', 'Luiseno'), ('Lunda', 'Lunda'), ('Luo (Kenya and Tanzania)', 'Luo (Kenya and Tanzania)'), ('Lushai', 'Lushai'), ('Macedonian', 'Macedonian'), ('Madurese', 'Madurese'), ('Magahi', 'Magahi'), ('Marshallese', 'Marshallese'), ('Maithili', 'Maithili'), ('Makasar', 'Makasar'), ('Malayalam', 'Malayalam'), ('Mandingo', 'Mandingo'), ('Maori', 'Maori'), ('Austronesian languages', 'Austronesian languages'), ('Marathi', 'Marathi'), ('Masai', 'Masai'), ('Malay', 'Malay'), ('Moksha', 'Moksha'), ('Mandar', 'Mandar'), ('Mende', 'Mende'), ('Irish', 'Irish'), ("Mi'kmaq; Micmac", "Mi'kmaq; Micmac"), ('Minangkabau', 'Minangkabau'), ('Uncoded languages', 'Uncoded languages'), ('Mon-Khmer languages', 'Mon-Khmer languages'), ('Malagasy', 'Malagasy'), ('Maltese', 'Maltese'), ('Manchu', 'Manchu'), ('Manipuri', 'Manipuri'), ('Manobo languages', 'Manobo languages'), ('Mohawk', 'Mohawk'), ('Mongolian', 'Mongolian'), ('Mossi', 'Mossi'), ('Multiple languages', 'Multiple languages'), ('Munda languages', 'Munda languages'), ('Creek', 'Creek'), ('Mirandese', 'Mirandese'), ('Marwari', 'Marwari'), ('Mayan languages', 'Mayan languages'), ('Erzya', 'Erzya'), ('Nahuatl languages', 'Nahuatl languages'), ('North American Indian languages', 'North American Indian languages'), ('Neapolitan', 'Neapolitan'), ('Nauru', 'Nauru'), ('Navajo; Navaho', 'Navajo; Navaho'), ('Ndebele, South; South Ndebele', 'Ndebele, South; South Ndebele'), ('Ndebele, North; North Ndebele', 'Ndebele, North; North Ndebele'), ('Ndonga', 'Ndonga'), ('Nepali', 'Nepali'), ('Nepal Bhasa; Newari', 'Nepal Bhasa; Newari'), ('Nias', 'Nias'), ('Niger-Kordofanian languages', 'Niger-Kordofanian languages'), ('Niuean', 'Niuean'), ('Nogai', 'Nogai'), ('Norse, Old', 'Norse, Old'), ('Norwegian', 'Norwegian'), ("N'Ko", "N'Ko"), ('Pedi; Sepedi; Northern Sotho', 'Pedi; Sepedi; Northern Sotho'), ('Nubian languages', 'Nubian languages'), ('Chichewa; Chewa; Nyanja', 'Chichewa; Chewa; Nyanja'), ('Nyamwezi', 'Nyamwezi'), ('Nyankole', 'Nyankole'), ('Nyoro', 'Nyoro'), ('Nzima', 'Nzima'), ('Occitan (post 1500); Provençal', 'Occitan (post 1500); Provençal'), ('Ojibwa', 'Ojibwa'), ('Oriya', 'Oriya'), ('Oromo', 'Oromo'), ('Osage', 'Osage'), ('Ossetian; Ossetic', 'Ossetian; Ossetic'), ('Turkish, Ottoman (1500-1928)', 'Turkish, Ottoman (1500-1928)'), ('Otomian languages', 'Otomian languages'), ('Papuan languages', 'Papuan languages'), ('Pangasinan', 'Pangasinan'), ('Pahlavi', 'Pahlavi'), ('Pampanga; Kapampangan', 'Pampanga; Kapampangan'), ('Panjabi; Punjabi', 'Panjabi; Punjabi'), ('Papiamento', 'Papiamento'), ('Palauan', 'Palauan'), ('Persian, Old (ca.600-400 B.C.)', 'Persian, Old (ca.600-400 B.C.)'), ('Persian', 'Persian'), ('Philippine languages', 'Philippine languages'), ('Phoenician', 'Phoenician'), ('Pali', 'Pali'), ('Polish', 'Polish'), ('Pohnpeian', 'Pohnpeian'), ('Portuguese', 'Portuguese'), ('Prakrit languages', 'Prakrit languages'), ('Provençal, Old (to 1500)', 'Provençal, Old (to 1500)'), ('Pushto; Pashto', 'Pushto; Pashto'), ('Reserved for local use', 'Reserved for local use'), ('Quechua', 'Quechua'), ('Rajasthani', 'Rajasthani'), ('Rapanui', 'Rapanui'), ('Rarotongan; Cook Islands Maori', 'Rarotongan; Cook Islands Maori'), ('Romance languages', 'Romance languages'), ('Romansh', 'Romansh'), ('Romany', 'Romany'), ('Romanian; Moldavian; Moldovan', 'Romanian; Moldavian; Moldovan'), ('Rundi', 'Rundi'), ('Russian', 'Russian'), ('Sandawe', 'Sandawe'), ('Sango', 'Sango'), ('Yakut', 'Yakut'), ('South American Indian (Other)', 'South American Indian (Other)'), ('Salishan languages', 'Salishan languages'), ('Samaritan Aramaic', 'Samaritan Aramaic'), ('Sanskrit', 'Sanskrit'), ('Sasak', 'Sasak'), ('Santali', 'Santali'), ('Sicilian', 'Sicilian'), ('Scots', 'Scots'), ('Selkup', 'Selkup'), ('Semitic languages', 'Semitic languages'), ('Irish, Old (to 900)', 'Irish, Old (to 900)'), ('Sign Languages', 'Sign Languages'), ('Shan', 'Shan'), ('Sidamo', 'Sidamo'), ('Sinhala; Sinhalese', 'Sinhala; Sinhalese'), ('Siouan languages', 'Siouan languages'), ('Sino-Tibetan languages', 'Sino-Tibetan languages'), ('Slavic languages', 'Slavic languages'), ('Slovak', 'Slovak'), ('Slovenian', 'Slovenian'), ('Southern Sami', 'Southern Sami'), ('Northern Sami', 'Northern Sami'), ('Sami languages', 'Sami languages'), ('Lule Sami', 'Lule Sami'), ('Inari Sami', 'Inari Sami'), ('Samoan', 'Samoan'), ('Skolt Sami', 'Skolt Sami'), ('Shona', 'Shona'), ('Sindhi', 'Sindhi'), ('Soninke', 'Soninke'), ('Sogdian', 'Sogdian'), ('Somali', 'Somali'), ('Songhai languages', 'Songhai languages'), ('Sotho, Southern', 'Sotho, Southern'), ('Spanish; Castilian', 'Spanish; Castilian'), ('Sardinian', 'Sardinian'), ('Sranan Tongo', 'Sranan Tongo'), ('Serbian', 'Serbian'), ('Serer', 'Serer'), ('Nilo-Saharan languages', 'Nilo-Saharan languages'), ('Swati', 'Swati'), ('Sukuma', 'Sukuma'), ('Sundanese', 'Sundanese'), ('Susu', 'Susu'), ('Sumerian', 'Sumerian'), ('Swahili', 'Swahili'), ('Swedish', 'Swedish'), ('Classical Syriac', 'Classical Syriac'), ('Syriac', 'Syriac'), ('Tahitian', 'Tahitian'), ('Tai languages', 'Tai languages'), ('Tamil', 'Tamil'), ('Tatar', 'Tatar'), ('Telugu', 'Telugu'), ('Timne', 'Timne'), ('Tereno', 'Tereno'), ('Tetum', 'Tetum'), ('Tajik', 'Tajik'), ('Tagalog', 'Tagalog'), ('Thai', 'Thai'), ('Tibetan', 'Tibetan'), ('Tigre', 'Tigre'), ('Tigrinya', 'Tigrinya'), ('Tiv', 'Tiv'), ('Tokelau', 'Tokelau'), ('Klingon; tlhIngan-Hol', 'Klingon; tlhIngan-Hol'), ('Tlingit', 'Tlingit'), ('Tamashek', 'Tamashek'), ('Tonga (Nyasa)', 'Tonga (Nyasa)'), ('Tonga (Tonga Islands)', 'Tonga (Tonga Islands)'), ('Tok Pisin', 'Tok Pisin'), ('Tsimshian', 'Tsimshian'), ('Tswana', 'Tswana'), ('Tsonga', 'Tsonga'), ('Turkmen', 'Turkmen'), ('Tumbuka', 'Tumbuka'), ('Tupi languages', 'Tupi languages'), ('Turkish', 'Turkish'), ('Altaic languages', 'Altaic languages'), ('Tuvalu', 'Tuvalu'), ('Twi', 'Twi'), ('Tuvinian', 'Tuvinian'), ('Udmurt', 'Udmurt'), ('Ugaritic', 'Ugaritic'), ('Uighur; Uyghur', 'Uighur; Uyghur'), ('Ukrainian', 'Ukrainian'), ('Umbundu', 'Umbundu'), ('Undetermined', 'Undetermined'), ('Urdu', 'Urdu'), ('Uzbek', 'Uzbek'), ('Vai', 'Vai'), ('Venda', 'Venda'), ('Vietnamese', 'Vietnamese'), ('Volapük', 'Volapük'), ('Votic', 'Votic'), ('Wakashan languages', 'Wakashan languages'), ('Walamo', 'Walamo'), ('Waray', 'Waray'), ('Washo', 'Washo'), ('Welsh', 'Welsh'), ('Sorbian languages', 'Sorbian languages'), ('Walloon', 'Walloon'), ('Wolof', 'Wolof'), ('Kalmyk; Oirat', 'Kalmyk; Oirat'), ('Xhosa', 'Xhosa'), ('Yao', 'Yao'), ('Yapese', 'Yapese'), ('Yiddish', 'Yiddish'), ('Yoruba', 'Yoruba'), ('Yupik languages', 'Yupik languages'), ('Zapotec', 'Zapotec'), ('Blissymbols; Blissymbolics; Bliss', 'Blissymbols; Blissymbolics; Bliss'), ('Zenaga', 'Zenaga'), ('Standard Moroccan Tamazight', 'Standard Moroccan Tamazight'), ('Zhuang; Chuang', 'Zhuang; Chuang'), ('Zande languages', 'Zande languages'), ('Zulu', 'Zulu'), ('Zuni', 'Zuni'), ('No linguistic content; Not applicable', 'No linguistic content; Not applicable'), ('Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki', 'Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki')], max_length=300)),
                ('job_type', models.CharField(choices=[('TRANSLATION', 'TRANSLATION'), ('REVISION', 'REVISION'), ('EDITING', 'EDITING'), ('TRANSCREATION', 'TRANSCREATION'), ('COPY WRITING', 'COPY WRITING'), ('PROOFREADING', 'PROOFREADING'), ('DTP', 'DTP'), ('SUBTITLING', 'SUBTITLING'), ('INTREPRETATION', 'INTREPRETATION'), ('VOICEOVER', 'VOICEOVER')], default='TRANSLATION', max_length=100)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(choices=[('ETB', 'BIRR'), ('$', 'USD')], default='ETB', max_length=100)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('deadlineDate', models.DateField(blank=True, null=True)),
                ('evaluated', models.BooleanField(default=False)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Job_owner', to='projects.vendor')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Main_Project', to='projects.project')),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_by', to=settings.AUTH_USER_MODEL)),
                ('purchaseOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.purchaseorder')),
            ],
        ),
    ]
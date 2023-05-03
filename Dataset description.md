# Dataset description
Dataset pozostáva zo 40000 stiahnutých básničiek zo stránky http://www.basnicky.sk/.
Na stránke by sa mali nachádzať slovenské (môžu byť aj v inom jazyku) básničky písané amaterskými básnikmi.
Kvalita básni sa líši (gramatika, dĺžne, ...).


Ukladanie fungovalo na princípe hľadaní daných HTML tagov a extrakte textu z elementov.
Uložené dáta jednej básničky sa skladajú zo šiestich atribútov: 
'author', 'title', 'text', 'category', 'date', 'link' + jedného navyše s názvom 'index' značiaci pozíciu básne v datasete.
V prípade, že sa jeden zo spomenutých atribútov nenašiel na stránke tak v datasete ma value='NOT_FOUND'.
Príklad:
```
index                                                       3
author                                                 Joe690
title                      * * * Twenty Happy Birthdays * * *
text        rokov dvadcat nikdy nezacni zivota chut straca...
category                                              Priania
date                                        20. 2. 2007 20:44
link                    http://www.basnicky.sk/basnicky/12035
```

----------------------------------------------------
----------------------------------------------------

#### Počet básni per autor:
```
>>> df['author'].value_counts()
NOT_FOUND       4886 # prípad, že sa nenašiel autor na stránke
patrik598        912
milson5          879
Jano1351         602
nickmyname49     524
                ... 
nemozna            1
Scar               1
noricius           1
šašuľka            1
ankh               1
Name: author, Length: 4549, dtype: int64
```
----------------------------------------------------
----------------------------------------------------
#### Počet básni per kategórie:
```
>>> df['category'].value_counts()
Ostatné         13129
Smutné          12364
Zaľúbené        10375
Vyznania         2448
Priania           709
Cudzojazyčné      446
Próza             316
Sviatočné         213
Name: category, dtype: int64
```
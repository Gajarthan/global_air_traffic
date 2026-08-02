# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_11:30:44_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-08-02 11:30:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 11:30:44 UTC

- **166,313** saved flights
- **54,493** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **166,313** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,002,828.2 tonnes** estimated CO2 emissions
- **116,105,981 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6635 |
| 2 | SkyWest Airlines | 6059 |
| 3 | EJA | 3293 |
| 4 | IndiGo | 2933 |
| 5 | American Airlines | 2623 |
| 6 | Southwest Airlines | 2614 |
| 7 | ENY | 2068 |
| 8 | Delta Air Lines | 1985 |
| 9 | LATAM Airlines | 1547 |
| 10 | Lufthansa | 1541 |
| 11 | AZU | 1455 |
| 12 | WIF | 1391 |
| 13 | Vueling | 1373 |
| 14 | LXJ | 1290 |
| 15 | AXM | 1151 |
| 16 | Swiss International | 1143 |
| 17 | easyJet | 1101 |
| 18 | Alaska Airlines | 1026 |
| 19 | EJU | 1022 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1016 |
| 22 | VIV | 916 |
| 23 | Cathay Pacific | 887 |
| 24 | CXK | 886 |
| 25 | United Airlines | 877 |
| 26 | AEE | 874 |
| 27 | GLO | 870 |
| 28 | Air France | 860 |
| 29 | MXY | 857 |
| 30 | JetBlue | 840 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143427 |
| 2 | 🇪🇸 ES | 10633 |
| 3 | 🇧🇷 BR | 9451 |
| 4 | 🇦🇺 AU | 9338 |
| 5 | 🇮🇳 IN | 9196 |
| 6 | 🇨🇦 CA | 9023 |
| 7 | 🇮🇹 IT | 8600 |
| 8 | 🇩🇪 DE | 8313 |
| 9 | 🇬🇧 GB | 7678 |
| 10 | 🇯🇵 JP | 6727 |
| 11 | 🇫🇷 FR | 6594 |
| 12 | 🇨🇴 CO | 5975 |
| 13 | 🇬🇷 GR | 4810 |
| 14 | 🇲🇽 MX | 4760 |
| 15 | 🇨🇭 CH | 4381 |
| 16 | 🇳🇴 NO | 4353 |
| 17 | 🇹🇷 TR | 4009 |
| 18 | 🇲🇾 MY | 2998 |
| 19 | 🇵🇱 PL | 2812 |
| 20 | 🇿🇦 ZA | 2707 |
| 21 | 🇳🇿 NZ | 2430 |
| 22 | 🇹🇭 TH | 2407 |
| 23 | 🇵🇭 PH | 2206 |
| 24 | 🇰🇷 KR | 2143 |
| 25 | 🇬🇹 GT | 2141 |
| 26 | 🇲🇦 MA | 1675 |
| 27 | 🇭🇷 HR | 1582 |
| 28 | 🇲🇪 ME | 1547 |
| 29 | 🇳🇱 NL | 1513 |
| 30 | 🇲🇴 MO | 1420 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3399 |
| 2 | Denver International Airport |  | US | 2766 |
| 3 | Tokyo International Airport |  | JP | 2113 |
| 4 | Guaymaral Airport |  | CO | 2082 |
| 5 | Indira Gandhi International Airport |  | IN | 2040 |
| 6 | Harry Reid International Airport |  | US | 2005 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1829 |
| 8 | Zurich Airport |  | CH | 1775 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1745 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1539 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Frankfurt am Main International Airport |  | DE | 1503 |
| 14 | Chicago O'Hare International Airport |  | US | 1500 |
| 15 | Salt Lake City International Airport |  | US | 1490 |
| 16 | Macau International Airport |  | MO | 1420 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1385 |
| 18 | Congonhas Airport |  | BR | 1370 |
| 19 | Madrid Barajas International Airport |  | ES | 1309 |
| 20 | Capua Airport |  | IT | 1298 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1264 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1175 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1173 |
| 24 | Charlotte/Douglas International Airport |  | US | 1162 |
| 25 | Charles de Gaulle International Airport |  | FR | 1137 |
| 26 | Kuala Lumpur International Airport |  | MY | 1135 |
| 27 | Malpensa International Airport |  | IT | 1115 |
| 28 | Bengaluru International Airport |  | IN | 1086 |
| 29 | Ninoy Aquino International Airport |  | PH | 1036 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1024 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1019 |
| 32 | Barcelona International Airport |  | ES | 981 |
| 33 | Daniel K Inouye International Airport |  | US | 970 |
| 34 | Seattle-Tacoma International Airport |  | US | 965 |
| 35 | Calgary International Airport |  | CA | 944 |
| 36 | Viracopos International Airport |  | BR | 941 |
| 37 | Tenerife Norte Airport |  | ES | 927 |
| 38 | Scottsdale Airport |  | US | 926 |
| 39 | Oslo Gardermoen Airport |  | NO | 922 |
| 40 | Reno/Tahoe International Airport |  | US | 917 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 606 | 21m | 244 km | 2,551.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 379 | 1h 9m | 770 km | 5,034.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 313 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 244 | 19m | 165 km | 694.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 241 | 44m | 241 km | 1,001.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 229 | 1h 47m | 1,423 km | 5,620.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 219 | 20m | 250 km | 945.9 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 216 | 26m | 215 km | 800.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 210 | 31m | 49 km | 177.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 196 | 19m | 144 km | 487.5 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 192 | 31m | 369 km | 1,222.1 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 179 | 24m | 218 km | 674.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PHSMX | PHS | Texel Airport (EHTX) | Rotterdam Airport (EHRD) | 2026-08-02 10:46 UTC | 2026-08-02 11:30 UTC | 43m |
| CFE42A | CFE | London Stansted Airport (EGSS) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-02 09:24 UTC | 2026-08-02 11:21 UTC | 1h 56m |
| GCPSS | GCP | Netheravon Airfield (EGDN) | Netheravon Airfield (EGDN) | 2026-08-02 10:39 UTC | 2026-08-02 11:19 UTC | 39m |
| GOMPH | GOM | RNAS Lee-On-Solent (EGHF) | Bembridge Airport (EGHJ) | 2026-08-02 11:06 UTC | 2026-08-02 11:10 UTC | 3m |
| SPSDW | SPS | Lubin Airport (EPLU) | Lubin Airport (EPLU) | 2026-08-02 10:08 UTC | 2026-08-02 11:09 UTC | 1h 1m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-02 10:08 UTC | 2026-08-02 10:56 UTC | 48m |
| GCKYL | GCK | Compton Abbas Aerodrome (EGHA) | Henstridge Airfield (EGHS) | 2026-08-02 10:37 UTC | 2026-08-02 10:54 UTC | 17m |
| GCGWE | GCG | Glasgow Prestwick Airport (EGPK) | Glasgow Prestwick Airport (EGPK) | 2026-08-02 10:39 UTC | 2026-08-02 10:49 UTC | 9m |
| EWG55UW | EWG | Eleftherios Venizelos International Airport (LGAV) | Stuttgart Airport (EDDS) | 2026-08-02 08:27 UTC | 2026-08-02 10:47 UTC | 2h 20m |
| EJU926U | EJU | Malpensa International Airport (LIMC) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-02 09:54 UTC | 2026-08-02 10:47 UTC | 52m |
| GCLNC | GCL | Cambridge Airport (EGSC) | Cambridge Airport (EGSC) | 2026-08-02 10:28 UTC | 2026-08-02 10:45 UTC | 16m |
| IGO7642 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-08-02 10:10 UTC | 2026-08-02 10:44 UTC | 34m |
| UPEM014 | UPE | Berlin Brandenburg Airport (EDDB) | Smolensk North Airport (XUBS) | 2026-08-02 09:17 UTC | 2026-08-02 10:39 UTC | 1h 21m |
| BNO1R | BNO | Brønnøysund Airport (ENBN) | Svolvær Helle Airport (ENSH) | 2026-08-02 09:53 UTC | 2026-08-02 10:35 UTC | 41m |
| SAW2915 | SAW | Mohammed V International Airport (GMMN) | Rabat-Sale Airport (GMME) | 2026-08-02 10:11 UTC | 2026-08-02 10:33 UTC | 22m |
| CAN11 | CAN | Malpensa International Airport (LIMC) | Calcinate Del Pesce Airport (LILC) | 2026-08-02 09:12 UTC | 2026-08-02 10:33 UTC | 1h 20m |
| AEZ7813 | AEZ | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-02 10:03 UTC | 2026-08-02 10:28 UTC | 25m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-02 10:17 UTC | 2026-08-02 10:28 UTC | 10m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-08-02 09:51 UTC | 2026-08-02 10:27 UTC | 35m |
| TFBMW | TFB | Reykjavik Airport (BIRK) | Hrauneyjarfoss Airport (BIHX) | 2026-08-02 09:45 UTC | 2026-08-02 10:27 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

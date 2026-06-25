# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_22:57:34_UTC-green)

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

**Latest saved flight:** 2026-06-25 22:57:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-25 22:57:34 UTC

- **120,460** saved flights
- **41,421** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **120,460** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,456,464.2 tonnes** estimated CO2 emissions
- **84,432,709 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4942 |
| 2 | SkyWest Airlines | 4453 |
| 3 | EJA | 2332 |
| 4 | IndiGo | 2309 |
| 5 | American Airlines | 1869 |
| 6 | Southwest Airlines | 1797 |
| 7 | ENY | 1504 |
| 8 | Delta Air Lines | 1426 |
| 9 | Lufthansa | 1317 |
| 10 | Vueling | 1082 |
| 11 | LATAM Airlines | 1069 |
| 12 | WIF | 1067 |
| 13 | AZU | 1005 |
| 14 | AXM | 978 |
| 15 | LXJ | 918 |
| 16 | Swiss International | 843 |
| 17 | All Nippon Airways | 820 |
| 18 | Alaska Airlines | 794 |
| 19 | easyJet | 775 |
| 20 | QLK | 769 |
| 21 | EJU | 754 |
| 22 | Cathay Pacific | 676 |
| 23 | AEE | 670 |
| 24 | VIV | 660 |
| 25 | Air France | 659 |
| 26 | United Airlines | 659 |
| 27 | CXK | 645 |
| 28 | MXY | 632 |
| 29 | JetBlue | 600 |
| 30 | AXB | 598 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 102217 |
| 2 | 🇪🇸 ES | 8169 |
| 3 | 🇮🇳 IN | 7258 |
| 4 | 🇦🇺 AU | 7074 |
| 5 | 🇧🇷 BR | 6634 |
| 6 | 🇩🇪 DE | 6428 |
| 7 | 🇮🇹 IT | 6409 |
| 8 | 🇨🇦 CA | 6335 |
| 9 | 🇯🇵 JP | 5353 |
| 10 | 🇬🇧 GB | 5292 |
| 11 | 🇫🇷 FR | 4786 |
| 12 | 🇨🇴 CO | 4018 |
| 13 | 🇲🇽 MX | 3515 |
| 14 | 🇬🇷 GR | 3438 |
| 15 | 🇳🇴 NO | 3311 |
| 16 | 🇨🇭 CH | 3087 |
| 17 | 🇲🇾 MY | 2539 |
| 18 | 🇹🇷 TR | 2474 |
| 19 | 🇿🇦 ZA | 2021 |
| 20 | 🇵🇱 PL | 1980 |
| 21 | 🇳🇿 NZ | 1948 |
| 22 | 🇹🇭 TH | 1916 |
| 23 | 🇰🇷 KR | 1904 |
| 24 | 🇵🇭 PH | 1723 |
| 25 | 🇬🇹 GT | 1680 |
| 26 | 🇲🇦 MA | 1299 |
| 27 | 🇲🇪 ME | 1199 |
| 28 | 🇲🇴 MO | 1174 |
| 29 | 🇳🇱 NL | 1150 |
| 30 | 🇭🇷 HR | 1040 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2532 |
| 2 | Denver International Airport |  | US | 2027 |
| 3 | Tokyo International Airport |  | JP | 1772 |
| 4 | Indira Gandhi International Airport |  | IN | 1597 |
| 5 | Guaymaral Airport |  | CO | 1508 |
| 6 | Harry Reid International Airport |  | US | 1502 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1459 |
| 8 | Zurich Airport |  | CH | 1339 |
| 9 | La Aurora Airport |  | GT | 1297 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1281 |
| 11 | Frankfurt am Main International Airport |  | DE | 1271 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1191 |
| 13 | Macau International Airport |  | MO | 1174 |
| 14 | Chicago O'Hare International Airport |  | US | 1174 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1043 |
| 17 | Capua Airport |  | IT | 1035 |
| 18 | Madrid Barajas International Airport |  | ES | 1011 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1002 |
| 20 | Kuala Lumpur International Airport |  | MY | 982 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 938 |
| 22 | Congonhas Airport |  | BR | 927 |
| 23 | Charlotte/Douglas International Airport |  | US | 912 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 892 |
| 25 | Charles de Gaulle International Airport |  | FR | 883 |
| 26 | Bengaluru International Airport |  | IN | 874 |
| 27 | Malpensa International Airport |  | IT | 840 |
| 28 | Ninoy Aquino International Airport |  | PH | 798 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 787 |
| 30 | Daniel K Inouye International Airport |  | US | 775 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 761 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 741 |
| 34 | Calgary International Airport |  | CA | 704 |
| 35 | Vitoria/Foronda Airport |  | ES | 702 |
| 36 | Amsterdam Airport Schiphol |  | NL | 696 |
| 37 | Don Mueang International Airport |  | TH | 694 |
| 38 | Seattle-Tacoma International Airport |  | US | 693 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 689 |
| 40 | Scottsdale Airport |  | US | 686 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 628 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 436 | 21m | 244 km | 1,835.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 315 | 24m | 225 km | 1,222.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 308 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 291 | 1h 25m | 910 km | 4,566.5 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 289 | 1h 10m | 770 km | 3,839.1 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 237 | 26m | 275 km | 1,123.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 223 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 174 | 27m | 215 km | 644.4 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 173 | 20m | 99 km | 296.3 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 165 | 44m | 241 km | 685.4 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 161 | 27m | 152 km | 420.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 150 | 1h 44m | 1,423 km | 3,681.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 150 | 18m | 144 km | 373.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 141 | 1h 38m | 1,156 km | 2,812.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 136 | 1h 17m | 961 km | 2,254.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XBBFI | XBB | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-06-25 22:31 UTC | 2026-06-25 22:57 UTC | 25m |
| CXK398 | CXK | Baton Rouge Metro, Ryan Field (KBTR) | False River Regional Airport (KHZR) | 2026-06-25 21:27 UTC | 2026-06-25 22:55 UTC | 1h 27m |
| N301PT |  | Ted Stevens Anchorage International Airport (PANC) | Valdez Pioneer Field (PAVD) | 2026-06-25 22:07 UTC | 2026-06-25 22:49 UTC | 41m |
| N405DD |  | CL24 (CL24) | Lake Tahoe Airport (KTVL) | 2026-06-25 22:18 UTC | 2026-06-25 22:48 UTC | 30m |
| XSN25 | XSN | Thunder Ridge Airpark (UT83) | San Carlos Airport (KSQL) | 2026-06-25 20:17 UTC | 2026-06-25 22:48 UTC | 2h 30m |
| N4735H |  | Norwood Memorial Airport (KOWD) | Norwood Memorial Airport (KOWD) | 2026-06-25 22:47 UTC | 2026-06-25 22:47 UTC | 0m |
| FTO388 | FTO | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-06-25 22:10 UTC | 2026-06-25 22:46 UTC | 35m |
| FTN5 | FTN | Oakland San Francisco Bay Airport (KOAK) | Pueblo Memorial Airport (KPUB) | 2026-06-25 20:48 UTC | 2026-06-25 22:44 UTC | 1h 56m |
| N489BJ |  | Brookhaven Airport (KHWV) | Brookhaven Airport (KHWV) | 2026-06-25 22:23 UTC | 2026-06-25 22:38 UTC | 15m |
| N71PW |  | Presque Isle International Airport (KPQI) | Augusta State Airport (KAUG) | 2026-06-25 21:56 UTC | 2026-06-25 22:37 UTC | 40m |
| NDU72 | NDU | 84MN (84MN) | NA01 (NA01) | 2026-06-25 22:31 UTC | 2026-06-25 22:35 UTC | 4m |
| PNC0619 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-25 22:19 UTC | 2026-06-25 22:34 UTC | 15m |
| N7350W |  | Fall River Mills Airport (KO89) | Rogers Field (KO05) | 2026-06-25 22:06 UTC | 2026-06-25 22:32 UTC | 25m |
| N825AV |  | Meadows Field (KBFL) | Palm Springs International Airport (KPSP) | 2026-06-25 22:02 UTC | 2026-06-25 22:32 UTC | 29m |
| JBU1351 | JetBlue | Nantucket Memorial Airport (KACK) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-25 22:07 UTC | 2026-06-25 22:30 UTC | 23m |
| N2NJ |  | Teterboro Airport (KTEB) | Linden Airport (KLDJ) | 2026-06-25 22:18 UTC | 2026-06-25 22:29 UTC | 11m |
| N207MM |  | Presque Isle International Airport (KPQI) | ME36 (ME36) | 2026-06-25 21:58 UTC | 2026-06-25 22:28 UTC | 30m |
| N169BA |  | Salaika Aviation Airport (07TA) | TE77 (TE77) | 2026-06-25 22:16 UTC | 2026-06-25 22:27 UTC | 10m |
| DEVIL53 | DEV | Laughlin Afb Aux Nr 1 Airport (KT70) | Dunbar Ranch Airport (0XS8) | 2026-06-25 22:13 UTC | 2026-06-25 22:26 UTC | 12m |
| STY543 | STY | Poolsbrook Aerodrome (NY72) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-25 21:50 UTC | 2026-06-25 22:25 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

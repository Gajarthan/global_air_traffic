# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_09:34:18_UTC-green)

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

**Latest saved flight:** 2026-07-11 09:34:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-11 09:34:18 UTC

- **136,649** saved flights
- **46,125** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **136,649** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,642,534.8 tonnes** estimated CO2 emissions
- **95,219,409 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5541 |
| 2 | SkyWest Airlines | 5014 |
| 3 | EJA | 2679 |
| 4 | IndiGo | 2522 |
| 5 | American Airlines | 2148 |
| 6 | Southwest Airlines | 2060 |
| 7 | ENY | 1715 |
| 8 | Delta Air Lines | 1628 |
| 9 | Lufthansa | 1402 |
| 10 | LATAM Airlines | 1252 |
| 11 | Vueling | 1184 |
| 12 | WIF | 1184 |
| 13 | AZU | 1171 |
| 14 | LXJ | 1051 |
| 15 | AXM | 1030 |
| 16 | Swiss International | 973 |
| 17 | All Nippon Airways | 890 |
| 18 | easyJet | 885 |
| 19 | Alaska Airlines | 864 |
| 20 | QLK | 856 |
| 21 | EJU | 840 |
| 22 | VIV | 747 |
| 23 | AEE | 740 |
| 24 | CXK | 729 |
| 25 | Air France | 728 |
| 26 | Cathay Pacific | 726 |
| 27 | JetBlue | 718 |
| 28 | United Airlines | 718 |
| 29 | MXY | 709 |
| 30 | GLO | 697 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 117358 |
| 2 | 🇪🇸 ES | 8999 |
| 3 | 🇮🇳 IN | 7907 |
| 4 | 🇦🇺 AU | 7873 |
| 5 | 🇧🇷 BR | 7696 |
| 6 | 🇨🇦 CA | 7215 |
| 7 | 🇩🇪 DE | 7125 |
| 8 | 🇮🇹 IT | 7095 |
| 9 | 🇬🇧 GB | 6182 |
| 10 | 🇯🇵 JP | 5804 |
| 11 | 🇫🇷 FR | 5428 |
| 12 | 🇨🇴 CO | 4284 |
| 13 | 🇲🇽 MX | 3964 |
| 14 | 🇬🇷 GR | 3887 |
| 15 | 🇳🇴 NO | 3689 |
| 16 | 🇨🇭 CH | 3543 |
| 17 | 🇹🇷 TR | 3162 |
| 18 | 🇲🇾 MY | 2677 |
| 19 | 🇵🇱 PL | 2270 |
| 20 | 🇿🇦 ZA | 2247 |
| 21 | 🇳🇿 NZ | 2121 |
| 22 | 🇹🇭 TH | 2083 |
| 23 | 🇰🇷 KR | 1996 |
| 24 | 🇵🇭 PH | 1877 |
| 25 | 🇬🇹 GT | 1834 |
| 26 | 🇲🇦 MA | 1434 |
| 27 | 🇲🇪 ME | 1355 |
| 28 | 🇳🇱 NL | 1273 |
| 29 | 🇭🇷 HR | 1226 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2844 |
| 2 | Denver International Airport |  | US | 2290 |
| 3 | Tokyo International Airport |  | JP | 1895 |
| 4 | Indira Gandhi International Airport |  | IN | 1745 |
| 5 | Harry Reid International Airport |  | US | 1713 |
| 6 | Guaymaral Airport |  | CO | 1654 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1591 |
| 8 | Zurich Airport |  | CH | 1518 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1446 |
| 10 | La Aurora Airport |  | GT | 1417 |
| 11 | Frankfurt am Main International Airport |  | DE | 1358 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1312 |
| 13 | Chicago O'Hare International Airport |  | US | 1293 |
| 14 | El Dorado International Airport |  | CO | 1214 |
| 15 | Salt Lake City International Airport |  | US | 1212 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1180 |
| 18 | Madrid Barajas International Airport |  | ES | 1111 |
| 19 | Capua Airport |  | IT | 1109 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1107 |
| 21 | Congonhas Airport |  | BR | 1093 |
| 22 | Kuala Lumpur International Airport |  | MY | 1038 |
| 23 | Charlotte/Douglas International Airport |  | US | 1000 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 990 |
| 25 | Charles de Gaulle International Airport |  | FR | 972 |
| 26 | Bengaluru International Airport |  | IN | 951 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 940 |
| 28 | Malpensa International Airport |  | IT | 895 |
| 29 | Ninoy Aquino International Airport |  | PH | 873 |
| 30 | Daniel K Inouye International Airport |  | US | 842 |
| 31 | Barcelona International Airport |  | ES | 833 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 832 |
| 33 | Tenerife Norte Airport |  | ES | 811 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 806 |
| 35 | Calgary International Airport |  | CA | 797 |
| 36 | Scottsdale Airport |  | US | 784 |
| 37 | Viracopos International Airport |  | BR | 780 |
| 38 | Seattle-Tacoma International Airport |  | US | 780 |
| 39 | Vitoria/Foronda Airport |  | ES | 770 |
| 40 | Amsterdam Airport Schiphol |  | NL | 764 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 696 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 493 | 21m | 244 km | 2,075.9 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 339 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 337 | 24m | 225 km | 1,307.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 329 | 1h 9m | 770 km | 4,370.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 292 | 14m | 114 km | 572.7 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 255 | 26m | 275 km | 1,208.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 250 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 201 | 22m | 55 km | 191.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 188 | 26m | 215 km | 696.3 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 183 | 1h 46m | 1,423 km | 4,491.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 181 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 169 | 20m | 250 km | 730.0 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 168 | 31m | 369 km | 1,069.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 164 | 18m | 144 km | 407.9 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 164 | 30m | 49 km | 138.6 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THY6128 | Turkish Airlines | Istanbul Airport (LTFM) | Jomo Kenyatta International Airport (HKJK) | 2026-07-10 21:09 UTC | 2026-07-11 09:34 UTC | 12h 24m |
| SPSMH | SPS | Poznań-Kobylnica Airport (EPPK) | Poznań-Kobylnica Airport (EPPK) | 2026-07-11 09:17 UTC | 2026-07-11 09:33 UTC | 16m |
| AAO13 | AAO | Paris-Le Bourget Airport (LFPB) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-11 08:12 UTC | 2026-07-11 09:23 UTC | 1h 11m |
| WIF36E | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-11 08:39 UTC | 2026-07-11 09:15 UTC | 35m |
| TJD800 | TJD | Bologna / Borgo Panigale Airport (LIPE) | Olbia / Costa Smeralda Airport (LIEO) | 2026-07-11 08:35 UTC | 2026-07-11 09:14 UTC | 38m |
| DFPRO | DFP | Frankfurt-Egelsbach Airport (EDFE) | Otocac Airport (LDRO) | 2026-07-11 07:15 UTC | 2026-07-11 09:00 UTC | 1h 45m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-11 08:06 UTC | 2026-07-11 08:57 UTC | 51m |
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-07-11 08:34 UTC | 2026-07-11 08:56 UTC | 21m |
| CEB905 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-07-11 08:19 UTC | 2026-07-11 08:46 UTC | 26m |
| EZY615E | easyJet | Bristol International Airport (EGGD) | Glasgow International Airport (EGPF) | 2026-07-11 07:47 UTC | 2026-07-11 08:46 UTC | 58m |
| HBZNP | HBZ | Buochs Airport (LSZC) | Buochs Airport (LSZC) | 2026-07-11 07:45 UTC | 2026-07-11 08:44 UTC | 58m |
| SHT6L | SHT | London Heathrow Airport (EGLL) | Glasgow International Airport (EGPF) | 2026-07-11 07:45 UTC | 2026-07-11 08:42 UTC | 57m |
| HBZYI | HBZ | Samedan Airport (LSZS) | Emmen Airport (LSME) | 2026-07-11 08:21 UTC | 2026-07-11 08:37 UTC | 15m |
| ANA297 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-07-11 07:55 UTC | 2026-07-11 08:37 UTC | 41m |
| VOE8SX | VOE | Calvi-Sainte-Catherine Airport (LFKC) | Lille-Lesquin Airport (LFQQ) | 2026-07-11 07:08 UTC | 2026-07-11 08:35 UTC | 1h 26m |
| DFARO | DFA | Nevers-Fourchambault Airport (LFQG) | Nevers-Fourchambault Airport (LFQG) | 2026-07-11 07:58 UTC | 2026-07-11 08:33 UTC | 34m |
| EWG6L | EWG | Palma De Mallorca Airport (LEPA) | Cologne Bonn Airport (EDDK) | 2026-07-11 06:40 UTC | 2026-07-11 08:33 UTC | 1h 53m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-07-11 08:10 UTC | 2026-07-11 08:30 UTC | 19m |
| SXS3RT | SXS | Antalya International Airport (LTAI) | Saarbrucken Airport (EDDR) | 2026-07-11 05:04 UTC | 2026-07-11 08:30 UTC | 3h 25m |
| NOZ6CF | Norwegian Air | Oslo Gardermoen Airport (ENGM) | ENEN (ENEN) | 2026-07-11 07:22 UTC | 2026-07-11 08:27 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

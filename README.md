# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_12:42:34_UTC-green)

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

**Latest saved flight:** 2026-07-25 12:42:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 12:42:34 UTC

- **149,872** saved flights
- **49,906** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **149,872** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,794,011.6 tonnes** estimated CO2 emissions
- **104,000,670 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6045 |
| 2 | SkyWest Airlines | 5479 |
| 3 | EJA | 2967 |
| 4 | IndiGo | 2680 |
| 5 | American Airlines | 2380 |
| 6 | Southwest Airlines | 2273 |
| 7 | ENY | 1863 |
| 8 | Delta Air Lines | 1764 |
| 9 | Lufthansa | 1464 |
| 10 | LATAM Airlines | 1379 |
| 11 | AZU | 1293 |
| 12 | WIF | 1275 |
| 13 | Vueling | 1264 |
| 14 | LXJ | 1153 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1057 |
| 17 | easyJet | 972 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 936 |
| 20 | QLK | 931 |
| 21 | EJU | 913 |
| 22 | VIV | 827 |
| 23 | CXK | 800 |
| 24 | AEE | 790 |
| 25 | JetBlue | 782 |
| 26 | Air France | 781 |
| 27 | Cathay Pacific | 781 |
| 28 | MXY | 779 |
| 29 | GLO | 774 |
| 30 | United Airlines | 772 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129216 |
| 2 | 🇪🇸 ES | 9682 |
| 3 | 🇦🇺 AU | 8505 |
| 4 | 🇧🇷 BR | 8446 |
| 5 | 🇮🇳 IN | 8442 |
| 6 | 🇨🇦 CA | 8026 |
| 7 | 🇮🇹 IT | 7733 |
| 8 | 🇩🇪 DE | 7661 |
| 9 | 🇬🇧 GB | 6867 |
| 10 | 🇯🇵 JP | 6247 |
| 11 | 🇫🇷 FR | 5934 |
| 12 | 🇨🇴 CO | 5046 |
| 13 | 🇲🇽 MX | 4335 |
| 14 | 🇬🇷 GR | 4259 |
| 15 | 🇳🇴 NO | 3991 |
| 16 | 🇨🇭 CH | 3939 |
| 17 | 🇹🇷 TR | 3546 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2537 |
| 20 | 🇿🇦 ZA | 2443 |
| 21 | 🇳🇿 NZ | 2263 |
| 22 | 🇹🇭 TH | 2190 |
| 23 | 🇰🇷 KR | 2064 |
| 24 | 🇵🇭 PH | 2005 |
| 25 | 🇬🇹 GT | 1949 |
| 26 | 🇲🇦 MA | 1524 |
| 27 | 🇲🇪 ME | 1475 |
| 28 | 🇳🇱 NL | 1384 |
| 29 | 🇭🇷 HR | 1364 |
| 30 | 🇲🇴 MO | 1246 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3080 |
| 2 | Denver International Airport |  | US | 2515 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Indira Gandhi International Airport |  | IN | 1872 |
| 5 | Guaymaral Airport |  | CO | 1870 |
| 6 | Harry Reid International Airport |  | US | 1857 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1686 |
| 8 | Zurich Airport |  | CH | 1637 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1573 |
| 10 | La Aurora Airport |  | GT | 1509 |
| 11 | Frankfurt am Main International Airport |  | DE | 1414 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1405 |
| 13 | Chicago O'Hare International Airport |  | US | 1383 |
| 14 | Salt Lake City International Airport |  | US | 1348 |
| 15 | El Dorado International Airport |  | CO | 1343 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1286 |
| 17 | Macau International Airport |  | MO | 1246 |
| 18 | Congonhas Airport |  | BR | 1210 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1192 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1162 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1066 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1050 |
| 26 | Charles de Gaulle International Airport |  | FR | 1031 |
| 27 | Bengaluru International Airport |  | IN | 1007 |
| 28 | Malpensa International Airport |  | IT | 975 |
| 29 | Ninoy Aquino International Airport |  | PH | 939 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 911 |
| 31 | Barcelona International Airport |  | ES | 900 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 898 |
| 33 | Daniel K Inouye International Airport |  | US | 897 |
| 34 | Seattle-Tacoma International Airport |  | US | 861 |
| 35 | Tenerife Norte Airport |  | ES | 859 |
| 36 | Calgary International Airport |  | CA | 854 |
| 37 | Scottsdale Airport |  | US | 849 |
| 38 | Viracopos International Airport |  | BR | 844 |
| 39 | Amsterdam Airport Schiphol |  | NL | 832 |
| 40 | Oslo Gardermoen Airport |  | NO | 828 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 789 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 543 | 21m | 244 km | 2,286.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 362 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 273 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 268 | 27m | 275 km | 1,269.9 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 223 | 22m | 55 km | 212.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 201 | 1h 47m | 1,423 km | 4,932.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 197 | 20m | 99 km | 337.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 185 | 20m | 250 km | 799.1 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 176 | 1h 16m | 961 km | 2,917.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 176 | 18m | 144 km | 437.8 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 169 | 1h 1m | 695 km | 2,025.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 168 | 1h 39m | 1,156 km | 3,351.5 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 163 | 55m | 136 km | 382.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PHBAR | PHB | Seppe Airport (EHSE) | Seppe Airport (EHSE) | 2026-07-25 12:19 UTC | 2026-07-25 12:42 UTC | 23m |
| N893AP |  | Laguardia Airport (KLGA) | Francis S Gabreski Airport (KFOK) | 2026-07-25 12:10 UTC | 2026-07-25 12:41 UTC | 30m |
| N546B |  | Centennial Airport (KAPA) | Laramie Regional Airport (KLAR) | 2026-07-25 11:26 UTC | 2026-07-25 12:29 UTC | 1h 2m |
| N2222V |  | Arthur Dunn Air Park (KX21) | Jumbolair Airport (17FL) | 2026-07-25 11:37 UTC | 2026-07-25 12:25 UTC | 47m |
| GCPSS | GCP | Netheravon Airfield (EGDN) | Netheravon Airfield (EGDN) | 2026-07-25 11:05 UTC | 2026-07-25 12:20 UTC | 1h 15m |
| N580Z |  | Cincinnati Municipal/Lunken Field (KLUK) | Grayling Army Air Field (KGOV) | 2026-07-25 11:07 UTC | 2026-07-25 12:14 UTC | 1h 6m |
| A7GQD |  | Al Khawr Airport (OTBK) | Persian Gulf International Airport (OIBP) | 2026-07-25 12:06 UTC | 2026-07-25 12:11 UTC | 5m |
| EIN643 | Aer Lingus | Václav Havel Airport (LKPR) | Dublin Airport (EIDW) | 2026-07-25 10:08 UTC | 2026-07-25 12:11 UTC | 2h 2m |
| N3300D |  | Crisp County-Cordele Airport (KCKF) | Sylvester Airport (KSYV) | 2026-07-25 10:35 UTC | 2026-07-25 12:09 UTC | 1h 33m |
| N738YZ |  | Willow Run Airport (KYIP) | Willow Run Airport (KYIP) | 2026-07-25 11:23 UTC | 2026-07-25 12:08 UTC | 44m |
| GEIV01 | GEI | Santos Dumont Airport (SBRJ) | Congonhas Airport (SBSP) | 2026-07-25 11:15 UTC | 2026-07-25 12:06 UTC | 51m |
| CGSCB | CGS | Peterborough Airport (CYPQ) | CME2 (CME2) | 2026-07-25 11:58 UTC | 2026-07-25 12:05 UTC | 6m |
| MRA633 | MRA | Gregg Airport (7OK1) | Mc Alester Regional Airport (KMLC) | 2026-07-25 11:44 UTC | 2026-07-25 12:01 UTC | 17m |
| N227MF |  | Rocky Mountain Metro Airport (KBJC) | Telluride Regional Airport (KTEX) | 2026-07-25 11:09 UTC | 2026-07-25 12:00 UTC | 51m |
| N472LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-07-25 10:56 UTC | 2026-07-25 11:58 UTC | 1h 2m |
| N502EM |  | Fulton County Airport (KUSE) | Nietz Airport (6OH7) | 2026-07-25 11:26 UTC | 2026-07-25 11:57 UTC | 30m |
| ZKIDH | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-07-25 11:51 UTC | 2026-07-25 11:57 UTC | 5m |
| FDR981 | FDR | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-07-25 11:27 UTC | 2026-07-25 11:56 UTC | 29m |
| CXK461 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-25 11:29 UTC | 2026-07-25 11:54 UTC | 25m |
| N504RP |  | Indianapolis International Airport (KIND) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-25 10:38 UTC | 2026-07-25 11:50 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

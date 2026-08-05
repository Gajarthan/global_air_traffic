# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_09:45:03_UTC-green)

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

**Latest saved flight:** 2026-08-05 09:45:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 09:45:03 UTC

- **171,917** saved flights
- **55,860** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **171,917** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,072,396.3 tonnes** estimated CO2 emissions
- **120,138,915 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6837 |
| 2 | SkyWest Airlines | 6294 |
| 3 | EJA | 3413 |
| 4 | IndiGo | 3016 |
| 5 | Southwest Airlines | 2708 |
| 6 | American Airlines | 2707 |
| 7 | ENY | 2140 |
| 8 | Delta Air Lines | 2043 |
| 9 | LATAM Airlines | 1590 |
| 10 | Lufthansa | 1569 |
| 11 | AZU | 1513 |
| 12 | WIF | 1437 |
| 13 | Vueling | 1415 |
| 14 | LXJ | 1344 |
| 15 | AXM | 1183 |
| 16 | Swiss International | 1169 |
| 17 | easyJet | 1158 |
| 18 | QLK | 1055 |
| 19 | Alaska Airlines | 1051 |
| 20 | EJU | 1050 |
| 21 | All Nippon Airways | 1044 |
| 22 | VIV | 947 |
| 23 | Cathay Pacific | 930 |
| 24 | CXK | 913 |
| 25 | GLO | 902 |
| 26 | United Airlines | 902 |
| 27 | AEE | 896 |
| 28 | Air France | 882 |
| 29 | MXY | 872 |
| 30 | JetBlue | 862 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 148148 |
| 2 | 🇪🇸 ES | 10995 |
| 3 | 🇧🇷 BR | 9767 |
| 4 | 🇦🇺 AU | 9640 |
| 5 | 🇮🇳 IN | 9456 |
| 6 | 🇨🇦 CA | 9390 |
| 7 | 🇮🇹 IT | 8888 |
| 8 | 🇩🇪 DE | 8535 |
| 9 | 🇬🇧 GB | 7963 |
| 10 | 🇯🇵 JP | 6930 |
| 11 | 🇫🇷 FR | 6818 |
| 12 | 🇨🇴 CO | 6265 |
| 13 | 🇬🇷 GR | 4996 |
| 14 | 🇲🇽 MX | 4921 |
| 15 | 🇨🇭 CH | 4528 |
| 16 | 🇳🇴 NO | 4478 |
| 17 | 🇹🇷 TR | 4201 |
| 18 | 🇲🇾 MY | 3076 |
| 19 | 🇵🇱 PL | 2880 |
| 20 | 🇿🇦 ZA | 2776 |
| 21 | 🇹🇭 TH | 2506 |
| 22 | 🇳🇿 NZ | 2494 |
| 23 | 🇵🇭 PH | 2277 |
| 24 | 🇬🇹 GT | 2200 |
| 25 | 🇰🇷 KR | 2168 |
| 26 | 🇲🇦 MA | 1729 |
| 27 | 🇭🇷 HR | 1655 |
| 28 | 🇲🇪 ME | 1580 |
| 29 | 🇳🇱 NL | 1557 |
| 30 | 🇲🇴 MO | 1482 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3545 |
| 2 | Denver International Airport |  | US | 2849 |
| 3 | Tokyo International Airport |  | JP | 2169 |
| 4 | Guaymaral Airport |  | CO | 2128 |
| 5 | Indira Gandhi International Airport |  | IN | 2101 |
| 6 | Harry Reid International Airport |  | US | 2061 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1873 |
| 8 | Zurich Airport |  | CH | 1815 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1805 |
| 10 | La Aurora Airport |  | GT | 1698 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1590 |
| 12 | Chicago O'Hare International Airport |  | US | 1559 |
| 13 | El Dorado International Airport |  | CO | 1557 |
| 14 | Salt Lake City International Airport |  | US | 1542 |
| 15 | Frankfurt am Main International Airport |  | DE | 1532 |
| 16 | Macau International Airport |  | MO | 1482 |
| 17 | Congonhas Airport |  | BR | 1409 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1407 |
| 19 | Madrid Barajas International Airport |  | ES | 1342 |
| 20 | Capua Airport |  | IT | 1341 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1299 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1211 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1203 |
| 24 | Charlotte/Douglas International Airport |  | US | 1192 |
| 25 | Charles de Gaulle International Airport |  | FR | 1166 |
| 26 | Kuala Lumpur International Airport |  | MY | 1159 |
| 27 | Malpensa International Airport |  | IT | 1158 |
| 28 | Bengaluru International Airport |  | IN | 1125 |
| 29 | Ninoy Aquino International Airport |  | PH | 1072 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1069 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1059 |
| 32 | Barcelona International Airport |  | ES | 1018 |
| 33 | Daniel K Inouye International Airport |  | US | 997 |
| 34 | Seattle-Tacoma International Airport |  | US | 995 |
| 35 | Viracopos International Airport |  | BR | 977 |
| 36 | Calgary International Airport |  | CA | 974 |
| 37 | Reno/Tahoe International Airport |  | US | 968 |
| 38 | Oslo Gardermoen Airport |  | NO | 955 |
| 39 | Tenerife Norte Airport |  | ES | 952 |
| 40 | Scottsdale Airport |  | US | 942 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 881 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 629 | 21m | 244 km | 2,648.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 405 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 391 | 1h 8m | 770 km | 5,194.1 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 319 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 256 | 44m | 241 km | 1,063.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 255 | 22m | 55 km | 242.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 236 | 1h 48m | 1,423 km | 5,791.8 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 219 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 206 | 50m | 556 km | 1,974.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 204 | 1h 15m | 961 km | 3,381.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 201 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 200 | 31m | 369 km | 1,273.0 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 195 | 1h 38m | 1,156 km | 3,890.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 191 | 24m | 218 km | 719.6 t |
| 29 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 189 | 8m | - | - |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 187 | 1h 1m | 695 km | 2,241.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GRIT98 | GRI | Ansbach-Petersdorf Airport (EDQF) | Bad Windsheim Airport (EDQB) | 2026-08-05 09:18 UTC | 2026-08-05 09:45 UTC | 26m |
| SHT7S | SHT | Bicester Airfield (EGDD) | Denham Aerodrome (EGLD) | 2026-08-05 09:21 UTC | 2026-08-05 09:34 UTC | 13m |
| CTM1282 | CTM | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-05 08:57 UTC | 2026-08-05 09:30 UTC | 32m |
| FR140 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-05 08:27 UTC | 2026-08-05 09:30 UTC | 1h 2m |
| UAL228 | United Airlines | Washington Dulles International Airport (KIAD) | Dublin Airport (EIDW) | 2026-08-05 02:58 UTC | 2026-08-05 09:28 UTC | 6h 29m |
| UPS61 | UPS | Chek Lap Kok International Airport (VHHH) | Hsinchu Air Base (RCPO) | 2026-08-05 08:18 UTC | 2026-08-05 09:26 UTC | 1h 8m |
| EVA197 | EVA Air | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-05 06:44 UTC | 2026-08-05 09:24 UTC | 2h 39m |
|  |  | Ostend-Bruges International Airport (EBOS) | Ostend-Bruges International Airport (EBOS) | 2026-08-05 09:19 UTC | 2026-08-05 09:20 UTC | 0m |
| HBZWE | HBZ | Sion Airport (LSGS) | Sion Airport (LSGS) | 2026-08-05 08:57 UTC | 2026-08-05 09:19 UTC | 21m |
| GOGJC | GOG | City Airport Manchester (EGCB) | City Airport Manchester (EGCB) | 2026-08-05 09:16 UTC | 2026-08-05 09:18 UTC | 2m |
| HBJIM | HBJ | Zurich Airport (LSZH) | Friedrichshafen Airport (EDNY) | 2026-08-05 08:57 UTC | 2026-08-05 09:17 UTC | 20m |
| CAL153 | CAL | Kansai International Airport (RJBB) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-05 06:59 UTC | 2026-08-05 09:14 UTC | 2h 14m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-08-04 21:45 UTC | 2026-08-05 09:10 UTC | 11h 25m |
| CHX50 | CHX | Hamburg-Finkenwerder Airport (EDHI) | Hamburg Airport (EDDH) | 2026-08-05 09:06 UTC | 2026-08-05 09:10 UTC | 4m |
| FGTYB | FGT | Grenoble-Isere Airport (LFLS) | Saint-Etienne-Boutheon Airport (LFMH) | 2026-08-05 07:50 UTC | 2026-08-05 09:08 UTC | 1h 17m |
| SEG13 | SEG | Ostend-Bruges International Airport (EBOS) | Ostend-Bruges International Airport (EBOS) | 2026-08-05 08:47 UTC | 2026-08-05 09:06 UTC | 19m |
| WIF824 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-05 08:54 UTC | 2026-08-05 09:06 UTC | 11m |
| MILAN73 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-08-05 08:53 UTC | 2026-08-05 09:04 UTC | 11m |
| AFR45LB | Air France | Charles de Gaulle International Airport (LFPG) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-08-05 08:06 UTC | 2026-08-05 09:04 UTC | 57m |
| XHE | XHE | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-05 08:15 UTC | 2026-08-05 09:04 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

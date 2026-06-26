# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_22:35:49_UTC-green)

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

**Latest saved flight:** 2026-06-26 22:35:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-26 22:35:49 UTC

- **121,654** saved flights
- **41,782** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **121,654** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,470,504.1 tonnes** estimated CO2 emissions
- **85,246,611 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4983 |
| 2 | SkyWest Airlines | 4503 |
| 3 | EJA | 2355 |
| 4 | IndiGo | 2324 |
| 5 | American Airlines | 1882 |
| 6 | Southwest Airlines | 1825 |
| 7 | ENY | 1517 |
| 8 | Delta Air Lines | 1441 |
| 9 | Lufthansa | 1321 |
| 10 | Vueling | 1084 |
| 11 | LATAM Airlines | 1083 |
| 12 | WIF | 1076 |
| 13 | AZU | 1020 |
| 14 | AXM | 983 |
| 15 | LXJ | 927 |
| 16 | Swiss International | 848 |
| 17 | All Nippon Airways | 825 |
| 18 | Alaska Airlines | 800 |
| 19 | easyJet | 784 |
| 20 | QLK | 774 |
| 21 | EJU | 764 |
| 22 | Cathay Pacific | 682 |
| 23 | AEE | 672 |
| 24 | Air France | 666 |
| 25 | VIV | 663 |
| 26 | United Airlines | 659 |
| 27 | CXK | 649 |
| 28 | MXY | 636 |
| 29 | JetBlue | 607 |
| 30 | AXB | 603 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 103396 |
| 2 | 🇪🇸 ES | 8222 |
| 3 | 🇮🇳 IN | 7307 |
| 4 | 🇦🇺 AU | 7129 |
| 5 | 🇧🇷 BR | 6708 |
| 6 | 🇩🇪 DE | 6476 |
| 7 | 🇮🇹 IT | 6464 |
| 8 | 🇨🇦 CA | 6398 |
| 9 | 🇯🇵 JP | 5390 |
| 10 | 🇬🇧 GB | 5347 |
| 11 | 🇫🇷 FR | 4822 |
| 12 | 🇨🇴 CO | 4024 |
| 13 | 🇲🇽 MX | 3536 |
| 14 | 🇬🇷 GR | 3468 |
| 15 | 🇳🇴 NO | 3352 |
| 16 | 🇨🇭 CH | 3122 |
| 17 | 🇲🇾 MY | 2549 |
| 18 | 🇹🇷 TR | 2516 |
| 19 | 🇿🇦 ZA | 2027 |
| 20 | 🇵🇱 PL | 1996 |
| 21 | 🇳🇿 NZ | 1968 |
| 22 | 🇹🇭 TH | 1921 |
| 23 | 🇰🇷 KR | 1917 |
| 24 | 🇵🇭 PH | 1744 |
| 25 | 🇬🇹 GT | 1692 |
| 26 | 🇲🇦 MA | 1306 |
| 27 | 🇲🇪 ME | 1212 |
| 28 | 🇲🇴 MO | 1175 |
| 29 | 🇳🇱 NL | 1159 |
| 30 | 🇭🇷 HR | 1052 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2553 |
| 2 | Denver International Airport |  | US | 2048 |
| 3 | Tokyo International Airport |  | JP | 1784 |
| 4 | Indira Gandhi International Airport |  | IN | 1610 |
| 5 | Harry Reid International Airport |  | US | 1520 |
| 6 | Guaymaral Airport |  | CO | 1514 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1469 |
| 8 | Zurich Airport |  | CH | 1346 |
| 9 | La Aurora Airport |  | GT | 1307 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1297 |
| 11 | Frankfurt am Main International Airport |  | DE | 1275 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1197 |
| 13 | Chicago O'Hare International Airport |  | US | 1181 |
| 14 | Macau International Airport |  | MO | 1175 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1060 |
| 17 | Capua Airport |  | IT | 1040 |
| 18 | Madrid Barajas International Airport |  | ES | 1018 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1015 |
| 20 | Kuala Lumpur International Airport |  | MY | 988 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 955 |
| 22 | Congonhas Airport |  | BR | 941 |
| 23 | Charlotte/Douglas International Airport |  | US | 917 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 900 |
| 25 | Charles de Gaulle International Airport |  | FR | 891 |
| 26 | Bengaluru International Airport |  | IN | 877 |
| 27 | Malpensa International Airport |  | IT | 848 |
| 28 | Ninoy Aquino International Airport |  | PH | 808 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 791 |
| 30 | Daniel K Inouye International Airport |  | US | 783 |
| 31 | Barcelona International Airport |  | ES | 763 |
| 32 | Tenerife Norte Airport |  | ES | 762 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 745 |
| 34 | Calgary International Airport |  | CA | 712 |
| 35 | Vitoria/Foronda Airport |  | ES | 708 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 703 |
| 37 | Amsterdam Airport Schiphol |  | NL | 702 |
| 38 | Scottsdale Airport |  | US | 702 |
| 39 | Seattle-Tacoma International Airport |  | US | 698 |
| 40 | Don Mueang International Airport |  | TH | 694 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 631 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 443 | 21m | 244 km | 1,865.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 318 | 24m | 225 km | 1,233.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 309 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 293 | 1h 10m | 770 km | 3,892.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 292 | 1h 25m | 910 km | 4,582.2 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 239 | 26m | 275 km | 1,132.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 225 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 175 | 26m | 215 km | 648.1 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 174 | 20m | 99 km | 298.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 166 | 44m | 241 km | 689.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 165 | 27m | 152 km | 431.2 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 153 | 1h 44m | 1,423 km | 3,754.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 152 | 18m | 144 km | 378.1 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 142 | 1h 38m | 1,156 km | 2,832.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 138 | 1h 17m | 961 km | 2,287.4 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 137 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 136 | 29m | 49 km | 115.0 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-06-26 21:37 UTC | 2026-06-26 22:35 UTC | 58m |
| SKW6299 | SkyWest Airlines | Dallas-Fort Worth International Airport (KDFW) | NM76 (NM76) | 2026-06-26 21:32 UTC | 2026-06-26 22:33 UTC | 1h 0m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-06-26 17:56 UTC | 2026-06-26 22:26 UTC | 4h 30m |
| N248FS |  | Gillespie Field (KSEE) | Hemet-Ryan Airport (KHMT) | 2026-06-26 21:33 UTC | 2026-06-26 22:21 UTC | 47m |
| N100BW |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-26 21:18 UTC | 2026-06-26 22:20 UTC | 1h 1m |
| N144NE |  | Boire Field (KASH) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-26 22:03 UTC | 2026-06-26 22:20 UTC | 16m |
| XSN90 | XSN | Palo Alto Airport (KPAO) | KM90 (KM90) | 2026-06-26 21:53 UTC | 2026-06-26 22:17 UTC | 24m |
| N235DA |  | Soldotna Airport (PASX) | Ted Stevens Anchorage International Airport (PANC) | 2026-06-26 20:12 UTC | 2026-06-26 22:14 UTC | 2h 2m |
| SIL1405 | SIL | Ted Stevens Anchorage International Airport (PANC) | Homer Airport (PAHO) | 2026-06-26 21:38 UTC | 2026-06-26 22:09 UTC | 31m |
| N56BU |  | Scottsdale Airport (KSDL) | Helblad Airport (04MN) | 2026-06-26 19:48 UTC | 2026-06-26 22:04 UTC | 2h 16m |
| N976E |  | Bob Baker Memorial Airport (PAIK) | Ambler Airport (PAFM) | 2026-06-26 21:35 UTC | 2026-06-26 22:02 UTC | 26m |
| N918WA |  | Dallas Love Field (KDAL) | Perry Lefors Field (KPPA) | 2026-06-26 21:09 UTC | 2026-06-26 22:01 UTC | 52m |
| ZKIDU | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-06-26 21:46 UTC | 2026-06-26 21:59 UTC | 12m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-06-26 11:17 UTC | 2026-06-26 21:59 UTC | 10h 42m |
| BULET41 | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-06-26 21:55 UTC | 2026-06-26 21:56 UTC | 0m |
| N510PR |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-26 21:20 UTC | 2026-06-26 21:55 UTC | 34m |
| N565TA |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-26 21:20 UTC | 2026-06-26 21:55 UTC | 34m |
| RGA01 | RGA | Konstanz Airport (EDTZ) | Birrfeld Airport (LSZF) | 2026-06-26 21:34 UTC | 2026-06-26 21:55 UTC | 21m |
| N55169 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-06-26 21:35 UTC | 2026-06-26 21:52 UTC | 17m |
| N479LT |  | Springdale Municipal Airport (KASG) | Russellville Regional Airport (KRUE) | 2026-06-26 21:32 UTC | 2026-06-26 21:52 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

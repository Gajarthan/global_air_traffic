# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_15:13:44_UTC-green)

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

**Latest saved flight:** 2026-08-07 15:13:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 15:13:44 UTC

- **175,535** saved flights
- **56,667** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **175,535** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,112,041.4 tonnes** estimated CO2 emissions
- **122,437,180 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6965 |
| 2 | SkyWest Airlines | 6394 |
| 3 | EJA | 3462 |
| 4 | IndiGo | 3084 |
| 5 | Southwest Airlines | 2759 |
| 6 | American Airlines | 2738 |
| 7 | ENY | 2174 |
| 8 | Delta Air Lines | 2075 |
| 9 | LATAM Airlines | 1624 |
| 10 | Lufthansa | 1583 |
| 11 | AZU | 1557 |
| 12 | WIF | 1475 |
| 13 | Vueling | 1447 |
| 14 | LXJ | 1374 |
| 15 | Swiss International | 1198 |
| 16 | AXM | 1196 |
| 17 | easyJet | 1193 |
| 18 | QLK | 1082 |
| 19 | EJU | 1073 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1065 |
| 22 | VIV | 964 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 931 |
| 25 | GLO | 922 |
| 26 | AEE | 916 |
| 27 | United Airlines | 908 |
| 28 | Air France | 905 |
| 29 | MXY | 883 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150716 |
| 2 | 🇪🇸 ES | 11245 |
| 3 | 🇧🇷 BR | 9994 |
| 4 | 🇦🇺 AU | 9950 |
| 5 | 🇮🇳 IN | 9667 |
| 6 | 🇨🇦 CA | 9594 |
| 7 | 🇮🇹 IT | 9066 |
| 8 | 🇩🇪 DE | 8711 |
| 9 | 🇬🇧 GB | 8138 |
| 10 | 🇯🇵 JP | 7076 |
| 11 | 🇫🇷 FR | 6983 |
| 12 | 🇨🇴 CO | 6443 |
| 13 | 🇬🇷 GR | 5111 |
| 14 | 🇲🇽 MX | 5017 |
| 15 | 🇨🇭 CH | 4662 |
| 16 | 🇳🇴 NO | 4585 |
| 17 | 🇹🇷 TR | 4332 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2928 |
| 20 | 🇿🇦 ZA | 2864 |
| 21 | 🇹🇭 TH | 2623 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2326 |
| 24 | 🇬🇹 GT | 2233 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1773 |
| 27 | 🇭🇷 HR | 1715 |
| 28 | 🇲🇪 ME | 1604 |
| 29 | 🇳🇱 NL | 1585 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3612 |
| 2 | Denver International Airport |  | US | 2894 |
| 3 | Tokyo International Airport |  | JP | 2208 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2146 |
| 6 | Harry Reid International Airport |  | US | 2092 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1905 |
| 8 | Zurich Airport |  | CH | 1865 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1833 |
| 10 | La Aurora Airport |  | GT | 1719 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1606 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1577 |
| 14 | Salt Lake City International Airport |  | US | 1565 |
| 15 | Frankfurt am Main International Airport |  | DE | 1545 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1443 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1423 |
| 19 | Capua Airport |  | IT | 1371 |
| 20 | Madrid Barajas International Airport |  | ES | 1369 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1308 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1236 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1194 |
| 26 | Charles de Gaulle International Airport |  | FR | 1194 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1149 |
| 29 | Ninoy Aquino International Airport |  | PH | 1094 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1085 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1084 |
| 32 | Barcelona International Airport |  | ES | 1039 |
| 33 | Daniel K Inouye International Airport |  | US | 1009 |
| 34 | Seattle-Tacoma International Airport |  | US | 1008 |
| 35 | Viracopos International Airport |  | BR | 999 |
| 36 | Calgary International Airport |  | CA | 994 |
| 37 | Reno/Tahoe International Airport |  | US | 992 |
| 38 | Oslo Gardermoen Airport |  | NO | 981 |
| 39 | Tenerife Norte Airport |  | ES | 968 |
| 40 | Amsterdam Airport Schiphol |  | NL | 952 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 640 | 21m | 244 km | 2,694.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 409 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 323 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 295 | 27m | 275 km | 1,397.9 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 267 | 44m | 241 km | 1,109.1 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 265 | 22m | 55 km | 251.9 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 241 | 1h 48m | 1,423 km | 5,914.5 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 230 | 20m | 250 km | 993.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 224 | 26m | 215 km | 829.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 224 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 216 | 20m | 99 km | 370.0 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 210 | 51m | 556 km | 2,013.0 t |
| 22 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 209 | 8m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 209 | 19m | 144 km | 519.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 208 | 1h 15m | 961 km | 3,447.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 204 | 1h 38m | 1,156 km | 4,069.7 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 199 | 24m | 218 km | 749.7 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 191 | 43m | 452 km | 1,488.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4287Q |  | Lakewood Airport (KN12) | Ocean County Airport (KMJX) | 2026-08-07 15:00 UTC | 2026-08-07 15:13 UTC | 13m |
| CAN14 | CAN | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Sarzana / Luni Military Airport (LIQW) | 2026-08-07 14:24 UTC | 2026-08-07 15:10 UTC | 45m |
| G08070 |  | Cypress Lakes Airport (GA35) | Hunter Army Air Field (KSVN) | 2026-08-07 14:54 UTC | 2026-08-07 15:06 UTC | 11m |
| NJE350U | NJE | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-08-07 14:29 UTC | 2026-08-07 14:56 UTC | 27m |
| N42715 |  | North Las Vegas Airport (KVGT) | Music Mountain Air Ranch Airport (68AZ) | 2026-08-07 13:59 UTC | 2026-08-07 14:52 UTC | 53m |
| NGF5565 | NGF | Lubbock Preston Smith International Airport (KLBB) | City Of Tulia/Swisher County Municipal Airport (KI06) | 2026-08-07 14:34 UTC | 2026-08-07 14:52 UTC | 17m |
| FAM3207 | FAM | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-07 14:24 UTC | 2026-08-07 14:51 UTC | 26m |
| N266AJ |  | Geary A Bates/Jefferson County Airpark (K2G2) | Greenbrier Valley Airport (KLWB) | 2026-08-07 14:24 UTC | 2026-08-07 14:50 UTC | 25m |
| RYR77HE | Ryanair | Ciampino Airport (LIRA) | Sliac Airport (LZSL) | 2026-08-07 13:35 UTC | 2026-08-07 14:49 UTC | 1h 14m |
| UAL2331 | United Airlines | Tampa International Airport (KTPA) | Washington Dulles International Airport (KIAD) | 2026-08-07 13:02 UTC | 2026-08-07 14:46 UTC | 1h 43m |
| N400DC |  | Colonel James Jabara Airport (KAAO) | Gunnison-Crested Butte Regional Airport (KGUC) | 2026-08-07 13:31 UTC | 2026-08-07 14:45 UTC | 1h 14m |
| SJN7 | SJN | Bellingham International Airport (KBLI) | Anacortes Airport (K74S) | 2026-08-07 14:38 UTC | 2026-08-07 14:45 UTC | 7m |
|  |  | Bessemer Ntl Airport (KEKY) | Bessemer Ntl Airport (KEKY) | 2026-08-07 14:44 UTC | 2026-08-07 14:44 UTC | 0m |
| CFSUG | CFS | Edmonton International Airport (CYEG) | Bow Island Airport (CEF3) | 2026-08-07 13:57 UTC | 2026-08-07 14:43 UTC | 45m |
| LVS100 | LVS | Moron Airport (SADM) | Mariano Moreno Airport (SADJ) | 2026-08-07 14:27 UTC | 2026-08-07 14:42 UTC | 15m |
| N5618Y |  | Fort Smith Landing Strip (K5U7) | Fort Smith Landing Strip (K5U7) | 2026-08-07 14:31 UTC | 2026-08-07 14:42 UTC | 10m |
| HBZVQ | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-08-07 14:38 UTC | 2026-08-07 14:41 UTC | 2m |
| N569FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-07 14:23 UTC | 2026-08-07 14:40 UTC | 17m |
| N228KT |  | Castle Lakes Airport (CD32) | Santa Fe Regional Airport (KSAF) | 2026-08-07 14:25 UTC | 2026-08-07 14:40 UTC | 14m |
| AZU4590 | AZU | Viracopos International Airport (SBKP) | Capao da Cruz Airport (SWMC) | 2026-08-07 14:00 UTC | 2026-08-07 14:37 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

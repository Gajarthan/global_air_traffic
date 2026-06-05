# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_01:23:46_UTC-green)

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

**Latest saved flight:** 2026-06-05 01:23:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-05 01:23:46 UTC

- **102,641** saved flights
- **36,340** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **102,641** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,252,779.3 tonnes** estimated CO2 emissions
- **72,624,886 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4214 |
| 2 | SkyWest Airlines | 3859 |
| 3 | IndiGo | 2048 |
| 4 | EJA | 1969 |
| 5 | American Airlines | 1659 |
| 6 | Southwest Airlines | 1553 |
| 7 | ENY | 1275 |
| 8 | Delta Air Lines | 1207 |
| 9 | Lufthansa | 1189 |
| 10 | Vueling | 947 |
| 11 | LATAM Airlines | 909 |
| 12 | WIF | 901 |
| 13 | AXM | 883 |
| 14 | AZU | 828 |
| 15 | LXJ | 773 |
| 16 | Swiss International | 741 |
| 17 | All Nippon Airways | 721 |
| 18 | Alaska Airlines | 718 |
| 19 | QLK | 691 |
| 20 | easyJet | 666 |
| 21 | EJU | 643 |
| 22 | Cathay Pacific | 616 |
| 23 | AEE | 596 |
| 24 | VIV | 590 |
| 25 | Air France | 587 |
| 26 | United Airlines | 571 |
| 27 | MXY | 558 |
| 28 | CXK | 552 |
| 29 | Japan Airlines | 510 |
| 30 | AXB | 505 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 86388 |
| 2 | 🇪🇸 ES | 7066 |
| 3 | 🇮🇳 IN | 6478 |
| 4 | 🇦🇺 AU | 6243 |
| 5 | 🇧🇷 BR | 5625 |
| 6 | 🇩🇪 DE | 5509 |
| 7 | 🇮🇹 IT | 5445 |
| 8 | 🇨🇦 CA | 5343 |
| 9 | 🇯🇵 JP | 4725 |
| 10 | 🇬🇧 GB | 4332 |
| 11 | 🇫🇷 FR | 4066 |
| 12 | 🇨🇴 CO | 3536 |
| 13 | 🇲🇽 MX | 3093 |
| 14 | 🇬🇷 GR | 2914 |
| 15 | 🇳🇴 NO | 2853 |
| 16 | 🇨🇭 CH | 2629 |
| 17 | 🇲🇾 MY | 2252 |
| 18 | 🇹🇷 TR | 1941 |
| 19 | 🇿🇦 ZA | 1776 |
| 20 | 🇳🇿 NZ | 1727 |
| 21 | 🇹🇭 TH | 1695 |
| 22 | 🇰🇷 KR | 1665 |
| 23 | 🇵🇱 PL | 1638 |
| 24 | 🇬🇹 GT | 1506 |
| 25 | 🇵🇭 PH | 1500 |
| 26 | 🇲🇦 MA | 1135 |
| 27 | 🇲🇴 MO | 1076 |
| 28 | 🇳🇱 NL | 1015 |
| 29 | 🇲🇪 ME | 968 |
| 30 | 🇭🇷 HR | 902 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2228 |
| 2 | Denver International Airport |  | US | 1759 |
| 3 | Tokyo International Airport |  | JP | 1566 |
| 4 | Indira Gandhi International Airport |  | IN | 1408 |
| 5 | Harry Reid International Airport |  | US | 1318 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1308 |
| 7 | Guaymaral Airport |  | CO | 1284 |
| 8 | Frankfurt am Main International Airport |  | DE | 1189 |
| 9 | Zurich Airport |  | CH | 1169 |
| 10 | La Aurora Airport |  | GT | 1159 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1110 |
| 12 | El Dorado International Airport |  | CO | 1081 |
| 13 | Macau International Airport |  | MO | 1076 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1041 |
| 15 | Chicago O'Hare International Airport |  | US | 1027 |
| 16 | Madrid Barajas International Airport |  | ES | 898 |
| 17 | Kuala Lumpur International Airport |  | MY | 889 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 882 |
| 19 | Salt Lake City International Airport |  | US | 865 |
| 20 | Capua Airport |  | IT | 853 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 799 |
| 22 | Charlotte/Douglas International Airport |  | US | 798 |
| 23 | Charles de Gaulle International Airport |  | FR | 781 |
| 24 | Congonhas Airport |  | BR | 781 |
| 25 | Bengaluru International Airport |  | IN | 773 |
| 26 | Malpensa International Airport |  | IT | 772 |
| 27 | Daniel K Inouye International Airport |  | US | 709 |
| 28 | Tenerife Norte Airport |  | ES | 702 |
| 29 | Ninoy Aquino International Airport |  | PH | 686 |
| 30 | Barcelona International Airport |  | ES | 673 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 666 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 664 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 656 |
| 34 | Amsterdam Airport Schiphol |  | NL | 627 |
| 35 | Don Mueang International Airport |  | TH | 620 |
| 36 | Vitoria/Foronda Airport |  | ES | 620 |
| 37 | Calgary International Airport |  | CA | 607 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 593 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 581 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 530 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 377 | 21m | 244 km | 1,587.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 272 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 270 | 24m | 225 km | 1,047.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 257 | 14m | 114 km | 504.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 250 | 1h 26m | 910 km | 3,923.1 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 247 | 28m | 304 km | 1,294.8 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 236 | 1h 10m | 770 km | 3,135.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 143 | 27m | 152 km | 373.7 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 137 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 135 | 20m | 250 km | 583.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 133 | 18m | 144 km | 330.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 132 | 20m | 147 km | 334.0 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 116 | 44m | 241 km | 481.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N709KA |  | Blakely Island Airport (38WA) | Boeing Field/King County International Airport (KBFI) | 2026-06-05 00:46 UTC | 2026-06-05 01:23 UTC | 36m |
| WVU | WVU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-06-05 01:00 UTC | 2026-06-05 01:14 UTC | 13m |
| FMX | FMX | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-06-05 00:55 UTC | 2026-06-05 01:10 UTC | 15m |
| N27DX |  | Republic Airport (KFRG) | Teterboro Airport (KTEB) | 2026-06-05 00:54 UTC | 2026-06-05 01:09 UTC | 15m |
| N8VB |  | Van Nuys Airport (KVNY) | Moffett Federal Airfield (KNUQ) | 2026-06-05 00:20 UTC | 2026-06-05 01:08 UTC | 48m |
| LBQ792 | LBQ | Reading Regional/Carl A Spaatz Field (KRDG) | Akm Airfield (PN54) | 2026-06-05 00:37 UTC | 2026-06-05 01:08 UTC | 30m |
| BHA200D | BHA | Tribhuvan International Airport (VNKT) | Langtang Airport (VNLT) | 2026-06-05 00:48 UTC | 2026-06-05 00:59 UTC | 11m |
| N747DS |  | Delaware Airpark (K33N) | 5PN5 (5PN5) | 2026-06-05 00:05 UTC | 2026-06-05 00:56 UTC | 50m |
| CGALN | CGA | Calgary / Springbank Airport (CYBW) | 75WT (75WT) | 2026-06-05 00:13 UTC | 2026-06-05 00:53 UTC | 39m |
| N2YV |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-04 23:54 UTC | 2026-06-05 00:52 UTC | 57m |
| N444WT |  | Van Nuys Airport (KVNY) | Henderson Executive Airport (KHND) | 2026-06-05 00:07 UTC | 2026-06-05 00:48 UTC | 41m |
| PCM7679 | PCM | Monterey Regional Airport (KMRY) | Oakland San Francisco Bay Airport (KOAK) | 2026-06-05 00:03 UTC | 2026-06-05 00:48 UTC | 44m |
| SVR1337 | SVR | Sochi International Airport (URSS) | Kemerovo Airport (UNEE) | 2026-06-04 20:03 UTC | 2026-06-05 00:47 UTC | 4h 44m |
| SWA4769 | Southwest Airlines | San Diego International Airport (KSAN) | Mcchord Field (Joint Base Lewis-Mcchord) Airport (KTCM) | 2026-06-04 22:11 UTC | 2026-06-05 00:45 UTC | 2h 34m |
| RSCU209 | RSC | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-06-04 23:16 UTC | 2026-06-05 00:44 UTC | 1h 28m |
| N876AD |  | Mount Sterling/Montgomery County Airport (KIOB) | Tweed/New Haven Airport (KHVN) | 2026-06-04 23:02 UTC | 2026-06-05 00:41 UTC | 1h 38m |
| AMF1901 | AMF | Inyokern Airport (KIYK) | Mojave Air & Space Port/Rutan Field (KMHV) | 2026-06-05 00:24 UTC | 2026-06-05 00:38 UTC | 13m |
| N337FB |  | Republic Airport (KFRG) | Groton-New London Airport (KGON) | 2026-06-04 23:50 UTC | 2026-06-05 00:36 UTC | 45m |
| N9055F |  | Red Dog Airport (PADG) | Kivalina Airport (PAVL) | 2026-06-05 00:14 UTC | 2026-06-05 00:35 UTC | 21m |
| N450PD |  | Roberts Field (KRDM) | South Fork Ranch Airport (0ID0) | 2026-06-05 00:01 UTC | 2026-06-05 00:35 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_19:27:38_UTC-green)

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

**Latest saved flight:** 2026-06-06 19:27:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 19:27:38 UTC

- **104,529** saved flights
- **36,856** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **104,529** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,277,186.1 tonnes** estimated CO2 emissions
- **74,039,774 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4295 |
| 2 | SkyWest Airlines | 3933 |
| 3 | IndiGo | 2088 |
| 4 | EJA | 1998 |
| 5 | American Airlines | 1680 |
| 6 | Southwest Airlines | 1578 |
| 7 | ENY | 1305 |
| 8 | Delta Air Lines | 1238 |
| 9 | Lufthansa | 1201 |
| 10 | Vueling | 965 |
| 11 | LATAM Airlines | 923 |
| 12 | WIF | 914 |
| 13 | AXM | 897 |
| 14 | AZU | 838 |
| 15 | LXJ | 786 |
| 16 | Swiss International | 755 |
| 17 | All Nippon Airways | 734 |
| 18 | Alaska Airlines | 727 |
| 19 | QLK | 697 |
| 20 | easyJet | 679 |
| 21 | EJU | 656 |
| 22 | Cathay Pacific | 622 |
| 23 | AEE | 605 |
| 24 | VIV | 603 |
| 25 | Air France | 602 |
| 26 | United Airlines | 578 |
| 27 | MXY | 566 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 522 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 87958 |
| 2 | 🇪🇸 ES | 7202 |
| 3 | 🇮🇳 IN | 6595 |
| 4 | 🇦🇺 AU | 6310 |
| 5 | 🇧🇷 BR | 5706 |
| 6 | 🇩🇪 DE | 5620 |
| 7 | 🇮🇹 IT | 5557 |
| 8 | 🇨🇦 CA | 5431 |
| 9 | 🇯🇵 JP | 4819 |
| 10 | 🇬🇧 GB | 4411 |
| 11 | 🇫🇷 FR | 4147 |
| 12 | 🇨🇴 CO | 3614 |
| 13 | 🇲🇽 MX | 3136 |
| 14 | 🇬🇷 GR | 2979 |
| 15 | 🇳🇴 NO | 2901 |
| 16 | 🇨🇭 CH | 2670 |
| 17 | 🇲🇾 MY | 2296 |
| 18 | 🇹🇷 TR | 1997 |
| 19 | 🇿🇦 ZA | 1804 |
| 20 | 🇳🇿 NZ | 1744 |
| 21 | 🇹🇭 TH | 1723 |
| 22 | 🇰🇷 KR | 1722 |
| 23 | 🇵🇱 PL | 1693 |
| 24 | 🇵🇭 PH | 1531 |
| 25 | 🇬🇹 GT | 1521 |
| 26 | 🇲🇦 MA | 1157 |
| 27 | 🇲🇴 MO | 1098 |
| 28 | 🇳🇱 NL | 1027 |
| 29 | 🇲🇪 ME | 990 |
| 30 | 🇭🇷 HR | 915 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2273 |
| 2 | Denver International Airport |  | US | 1786 |
| 3 | Tokyo International Airport |  | JP | 1599 |
| 4 | Indira Gandhi International Airport |  | IN | 1432 |
| 5 | Harry Reid International Airport |  | US | 1338 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1328 |
| 7 | Guaymaral Airport |  | CO | 1316 |
| 8 | Frankfurt am Main International Airport |  | DE | 1198 |
| 9 | Zurich Airport |  | CH | 1185 |
| 10 | La Aurora Airport |  | GT | 1169 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1128 |
| 12 | El Dorado International Airport |  | CO | 1101 |
| 13 | Macau International Airport |  | MO | 1098 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1057 |
| 15 | Chicago O'Hare International Airport |  | US | 1049 |
| 16 | Madrid Barajas International Airport |  | ES | 912 |
| 17 | Kuala Lumpur International Airport |  | MY | 900 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 893 |
| 19 | Salt Lake City International Airport |  | US | 889 |
| 20 | Capua Airport |  | IT | 877 |
| 21 | Charlotte/Douglas International Airport |  | US | 810 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 798 |
| 24 | Congonhas Airport |  | BR | 793 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 783 |
| 27 | Daniel K Inouye International Airport |  | US | 717 |
| 28 | Tenerife Norte Airport |  | ES | 714 |
| 29 | Ninoy Aquino International Airport |  | PH | 699 |
| 30 | Barcelona International Airport |  | ES | 687 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 676 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 676 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 669 |
| 34 | Amsterdam Airport Schiphol |  | NL | 636 |
| 35 | Don Mueang International Airport |  | TH | 630 |
| 36 | Vitoria/Foronda Airport |  | ES | 630 |
| 37 | Calgary International Airport |  | CA | 618 |
| 38 | Seattle-Tacoma International Airport |  | US | 606 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 603 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 593 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 543 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 385 | 21m | 244 km | 1,621.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 280 | 1h 7m | 706 km | 3,409.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 274 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 265 | 14m | 114 km | 519.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 257 | 1h 25m | 910 km | 4,032.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 256 | 28m | 304 km | 1,342.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 241 | 1h 10m | 770 km | 3,201.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 209 | 26m | 275 km | 990.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 144 | 31m | 369 km | 916.6 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 135 | 18m | 144 km | 335.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6026Y |  | Burlington/Alamance Regional Airport (KBUY) | K5W8 (K5W8) | 2026-06-06 18:38 UTC | 2026-06-06 19:27 UTC | 48m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-06-06 19:04 UTC | 2026-06-06 19:23 UTC | 19m |
| N88765 |  | Helio Airport (2AK7) | Talkeetna Airport (PATK) | 2026-06-06 19:01 UTC | 2026-06-06 19:20 UTC | 18m |
| N36371 |  | Diamond Point Airstrip (2WA1) | Boeing Field/King County International Airport (KBFI) | 2026-06-06 18:54 UTC | 2026-06-06 19:19 UTC | 25m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-06-06 19:03 UTC | 2026-06-06 19:18 UTC | 14m |
| AFR27QN | Air France | Charles de Gaulle International Airport (LFPG) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-06 18:11 UTC | 2026-06-06 19:17 UTC | 1h 5m |
| N76VY |  | CL35 (CL35) | Hemet-Ryan Airport (KHMT) | 2026-06-06 18:55 UTC | 2026-06-06 19:15 UTC | 20m |
| N73784 |  | Denton Enterprise Airport (KDTO) | Jim Sears Airport (3TA7) | 2026-06-06 18:46 UTC | 2026-06-06 19:12 UTC | 26m |
| N100BW |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-06 18:52 UTC | 2026-06-06 19:12 UTC | 19m |
| N782AZ |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-06-06 19:05 UTC | 2026-06-06 19:10 UTC | 4m |
| N2363K |  | Meadows Field (KBFL) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-06-06 18:08 UTC | 2026-06-06 19:08 UTC | 1h 0m |
| SCHNR66 | SCH | Los Alamitos Army Air Field (KSLI) | Los Alamitos Army Air Field (KSLI) | 2026-06-06 18:25 UTC | 2026-06-06 19:07 UTC | 42m |
| N653ND |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-06-06 18:47 UTC | 2026-06-06 19:06 UTC | 19m |
| N91099 |  | JAMI (JAMI) | JAMI (JAMI) | 2026-06-06 18:45 UTC | 2026-06-06 19:05 UTC | 20m |
| N5726B |  | Mariposa-Yosemite Airport (KMPI) | Mariposa-Yosemite Airport (KMPI) | 2026-06-06 18:37 UTC | 2026-06-06 19:03 UTC | 25m |
| BYF30 | BYF | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-06-06 18:48 UTC | 2026-06-06 19:03 UTC | 14m |
| N11024 |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-06-06 18:04 UTC | 2026-06-06 19:03 UTC | 58m |
| TRP1 | TRP | Martin State Airport (KMTN) | Kent Fort Manor Airport (7MD8) | 2026-06-06 18:50 UTC | 2026-06-06 19:01 UTC | 11m |
| N747EE |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-06-06 18:37 UTC | 2026-06-06 19:01 UTC | 23m |
| N34852 |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-06-06 18:42 UTC | 2026-06-06 18:58 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

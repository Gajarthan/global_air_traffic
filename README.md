# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_12:33:08_UTC-green)

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

**Latest saved flight:** 2026-08-02 12:33:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 12:33:08 UTC

- **166,415** saved flights
- **54,516** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **166,415** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,004,478.7 tonnes** estimated CO2 emissions
- **116,201,666 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6640 |
| 2 | SkyWest Airlines | 6059 |
| 3 | EJA | 3293 |
| 4 | IndiGo | 2937 |
| 5 | American Airlines | 2623 |
| 6 | Southwest Airlines | 2616 |
| 7 | ENY | 2068 |
| 8 | Delta Air Lines | 1985 |
| 9 | LATAM Airlines | 1548 |
| 10 | Lufthansa | 1541 |
| 11 | AZU | 1457 |
| 12 | WIF | 1392 |
| 13 | Vueling | 1374 |
| 14 | LXJ | 1291 |
| 15 | AXM | 1153 |
| 16 | Swiss International | 1143 |
| 17 | easyJet | 1104 |
| 18 | Alaska Airlines | 1026 |
| 19 | EJU | 1023 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1017 |
| 22 | VIV | 916 |
| 23 | Cathay Pacific | 887 |
| 24 | CXK | 886 |
| 25 | United Airlines | 878 |
| 26 | AEE | 874 |
| 27 | GLO | 870 |
| 28 | Air France | 860 |
| 29 | MXY | 857 |
| 30 | JetBlue | 840 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143447 |
| 2 | 🇪🇸 ES | 10650 |
| 3 | 🇧🇷 BR | 9461 |
| 4 | 🇦🇺 AU | 9340 |
| 5 | 🇮🇳 IN | 9208 |
| 6 | 🇨🇦 CA | 9023 |
| 7 | 🇮🇹 IT | 8602 |
| 8 | 🇩🇪 DE | 8320 |
| 9 | 🇬🇧 GB | 7694 |
| 10 | 🇯🇵 JP | 6740 |
| 11 | 🇫🇷 FR | 6598 |
| 12 | 🇨🇴 CO | 5975 |
| 13 | 🇬🇷 GR | 4815 |
| 14 | 🇲🇽 MX | 4760 |
| 15 | 🇨🇭 CH | 4385 |
| 16 | 🇳🇴 NO | 4358 |
| 17 | 🇹🇷 TR | 4018 |
| 18 | 🇲🇾 MY | 3005 |
| 19 | 🇵🇱 PL | 2813 |
| 20 | 🇿🇦 ZA | 2711 |
| 21 | 🇳🇿 NZ | 2430 |
| 22 | 🇹🇭 TH | 2415 |
| 23 | 🇵🇭 PH | 2211 |
| 24 | 🇰🇷 KR | 2145 |
| 25 | 🇬🇹 GT | 2141 |
| 26 | 🇲🇦 MA | 1678 |
| 27 | 🇭🇷 HR | 1582 |
| 28 | 🇲🇪 ME | 1549 |
| 29 | 🇳🇱 NL | 1514 |
| 30 | 🇲🇴 MO | 1421 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3399 |
| 2 | Denver International Airport |  | US | 2766 |
| 3 | Tokyo International Airport |  | JP | 2117 |
| 4 | Guaymaral Airport |  | CO | 2082 |
| 5 | Indira Gandhi International Airport |  | IN | 2042 |
| 6 | Harry Reid International Airport |  | US | 2005 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1831 |
| 8 | Zurich Airport |  | CH | 1776 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1745 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1539 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Frankfurt am Main International Airport |  | DE | 1504 |
| 14 | Chicago O'Hare International Airport |  | US | 1500 |
| 15 | Salt Lake City International Airport |  | US | 1490 |
| 16 | Macau International Airport |  | MO | 1421 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1385 |
| 18 | Congonhas Airport |  | BR | 1370 |
| 19 | Madrid Barajas International Airport |  | ES | 1311 |
| 20 | Capua Airport |  | IT | 1299 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1264 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1175 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1174 |
| 24 | Charlotte/Douglas International Airport |  | US | 1162 |
| 25 | Charles de Gaulle International Airport |  | FR | 1137 |
| 26 | Kuala Lumpur International Airport |  | MY | 1135 |
| 27 | Malpensa International Airport |  | IT | 1115 |
| 28 | Bengaluru International Airport |  | IN | 1088 |
| 29 | Ninoy Aquino International Airport |  | PH | 1039 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1024 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1019 |
| 32 | Barcelona International Airport |  | ES | 982 |
| 33 | Daniel K Inouye International Airport |  | US | 971 |
| 34 | Seattle-Tacoma International Airport |  | US | 965 |
| 35 | Calgary International Airport |  | CA | 944 |
| 36 | Viracopos International Airport |  | BR | 943 |
| 37 | Tenerife Norte Airport |  | ES | 928 |
| 38 | Scottsdale Airport |  | US | 926 |
| 39 | Oslo Gardermoen Airport |  | NO | 924 |
| 40 | Reno/Tahoe International Airport |  | US | 917 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 606 | 21m | 244 km | 2,551.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 313 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 286 | 27m | 275 km | 1,355.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 244 | 19m | 165 km | 694.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 241 | 44m | 241 km | 1,001.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 229 | 1h 47m | 1,423 km | 5,620.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 220 | 20m | 250 km | 950.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 216 | 26m | 215 km | 800.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 210 | 31m | 49 km | 177.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 196 | 19m | 144 km | 487.5 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 194 | 31m | 369 km | 1,234.9 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 180 | 24m | 218 km | 678.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N534CA |  | Dallas Executive Airport (KRBD) | Lancaster Regional Airport (KLNC) | 2026-08-02 11:38 UTC | 2026-08-02 12:33 UTC | 54m |
| LXJ600 | LXJ | Naples Municipal Airport (KAPF) | Witham Field (KSUA) | 2026-08-02 11:54 UTC | 2026-08-02 12:18 UTC | 23m |
| ENSA34 | ENS | Fazenda Fittipaldi Citrus Airport (SDFF) | Mirassol Airport (SDMH) | 2026-08-02 11:58 UTC | 2026-08-02 12:17 UTC | 19m |
| KXP833 | KXP | Kota Kinabalu International Airport (WBKK) | Zhuhai Airport (ZGSD) | 2026-08-02 09:35 UTC | 2026-08-02 12:16 UTC | 2h 40m |
| OKBUD69 | OKB | Rana Loumy Airport (LKRA) | Roudnice Mad Airport (LKRO) | 2026-08-02 12:08 UTC | 2026-08-02 12:13 UTC | 4m |
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-08-02 11:25 UTC | 2026-08-02 12:09 UTC | 43m |
| N87SE |  | Naples Municipal Airport (KAPF) | Marco Island Executive Airport (KMKY) | 2026-08-02 11:51 UTC | 2026-08-02 12:05 UTC | 14m |
| SIA919 | Singapore Airlines | Ninoy Aquino International Airport (RPLL) | Changi Air Base (WSAC) | 2026-08-02 09:09 UTC | 2026-08-02 12:05 UTC | 2h 55m |
| QTR8454 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-02 00:46 UTC | 2026-08-02 12:02 UTC | 11h 15m |
| GAF198 | GAF | Friedrichshafen Airport (EDNY) | Friedrichshafen Airport (EDNY) | 2026-08-02 11:11 UTC | 2026-08-02 12:01 UTC | 50m |
| HB2562 |  | Raron Airport (LSTA) | Raron Airport (LSTA) | 2026-08-02 10:59 UTC | 2026-08-02 12:00 UTC | 1h 0m |
| RVR12DP | RVR | Inverness Airport (EGPE) | Southampton Airport (EGHI) | 2026-08-02 10:07 UTC | 2026-08-02 11:56 UTC | 1h 49m |
| FGJFI | FGJ | Lezignan-Corbieres Airport (LFMZ) | Lezignan-Corbieres Airport (LFMZ) | 2026-08-02 10:38 UTC | 2026-08-02 11:53 UTC | 1h 14m |
| GSIRT | GSI | Coventry Airport (EGBE) | RAF Brize Norton (EGVN) | 2026-08-02 11:34 UTC | 2026-08-02 11:47 UTC | 12m |
| N183TS |  | Columbus Airport (KCSG) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-02 11:14 UTC | 2026-08-02 11:44 UTC | 29m |
| SGA2552 | SGA | Sharjah International Airport (OMSJ) | Zhuhai Airport (ZGSD) | 2026-08-01 13:01 UTC | 2026-08-02 11:42 UTC | 22h 41m |
| SRG336 | SRG | Caernarfon Airport (EGCK) | Caernarfon Airport (EGCK) | 2026-08-02 11:34 UTC | 2026-08-02 11:41 UTC | 7m |
| AZU4158 | AZU | Viracopos International Airport (SBKP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-08-02 10:49 UTC | 2026-08-02 11:40 UTC | 50m |
| GTI8523 | GTI | Na-San Airport (VVNS) | Macau International Airport (VMMC) | 2026-08-02 10:41 UTC | 2026-08-02 11:40 UTC | 59m |
| PRIBT | PRI | Serra da Capivara Airport (SWKQ) | Casa Nova Airport (SDFX) | 2026-08-02 11:12 UTC | 2026-08-02 11:40 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

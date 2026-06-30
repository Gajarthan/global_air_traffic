# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_14:54:18_UTC-green)

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

**Latest saved flight:** 2026-06-30 14:54:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-30 14:54:18 UTC

- **124,778** saved flights
- **42,688** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **124,778** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,507,013.7 tonnes** estimated CO2 emissions
- **87,363,114 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5082 |
| 2 | SkyWest Airlines | 4630 |
| 3 | EJA | 2441 |
| 4 | IndiGo | 2370 |
| 5 | American Airlines | 1931 |
| 6 | Southwest Airlines | 1873 |
| 7 | ENY | 1567 |
| 8 | Delta Air Lines | 1485 |
| 9 | Lufthansa | 1338 |
| 10 | LATAM Airlines | 1123 |
| 11 | Vueling | 1108 |
| 12 | WIF | 1104 |
| 13 | AZU | 1053 |
| 14 | AXM | 992 |
| 15 | LXJ | 967 |
| 16 | Swiss International | 875 |
| 17 | All Nippon Airways | 840 |
| 18 | Alaska Airlines | 819 |
| 19 | easyJet | 795 |
| 20 | QLK | 780 |
| 21 | EJU | 777 |
| 22 | Cathay Pacific | 694 |
| 23 | AEE | 690 |
| 24 | VIV | 683 |
| 25 | Air France | 677 |
| 26 | United Airlines | 667 |
| 27 | CXK | 665 |
| 28 | MXY | 651 |
| 29 | JetBlue | 639 |
| 30 | GLO | 626 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 106491 |
| 2 | 🇪🇸 ES | 8358 |
| 3 | 🇮🇳 IN | 7434 |
| 4 | 🇦🇺 AU | 7278 |
| 5 | 🇧🇷 BR | 6939 |
| 6 | 🇩🇪 DE | 6609 |
| 7 | 🇮🇹 IT | 6590 |
| 8 | 🇨🇦 CA | 6557 |
| 9 | 🇬🇧 GB | 5505 |
| 10 | 🇯🇵 JP | 5481 |
| 11 | 🇫🇷 FR | 4929 |
| 12 | 🇨🇴 CO | 4032 |
| 13 | 🇲🇽 MX | 3631 |
| 14 | 🇬🇷 GR | 3560 |
| 15 | 🇳🇴 NO | 3429 |
| 16 | 🇨🇭 CH | 3192 |
| 17 | 🇹🇷 TR | 2622 |
| 18 | 🇲🇾 MY | 2568 |
| 19 | 🇿🇦 ZA | 2051 |
| 20 | 🇵🇱 PL | 2045 |
| 21 | 🇳🇿 NZ | 2019 |
| 22 | 🇹🇭 TH | 1955 |
| 23 | 🇰🇷 KR | 1939 |
| 24 | 🇵🇭 PH | 1770 |
| 25 | 🇬🇹 GT | 1729 |
| 26 | 🇲🇦 MA | 1342 |
| 27 | 🇲🇪 ME | 1240 |
| 28 | 🇳🇱 NL | 1178 |
| 29 | 🇲🇴 MO | 1178 |
| 30 | 🇧🇸 BS | 1081 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2617 |
| 2 | Denver International Airport |  | US | 2109 |
| 3 | Tokyo International Airport |  | JP | 1811 |
| 4 | Indira Gandhi International Airport |  | IN | 1637 |
| 5 | Harry Reid International Airport |  | US | 1559 |
| 6 | Guaymaral Airport |  | CO | 1520 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1498 |
| 8 | Zurich Airport |  | CH | 1382 |
| 9 | La Aurora Airport |  | GT | 1335 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1333 |
| 11 | Frankfurt am Main International Airport |  | DE | 1291 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1229 |
| 13 | Chicago O'Hare International Airport |  | US | 1207 |
| 14 | Macau International Airport |  | MO | 1178 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1101 |
| 17 | Capua Airport |  | IT | 1061 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1040 |
| 19 | Madrid Barajas International Airport |  | ES | 1034 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1008 |
| 21 | Kuala Lumpur International Airport |  | MY | 999 |
| 22 | Congonhas Airport |  | BR | 971 |
| 23 | Charlotte/Douglas International Airport |  | US | 942 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 916 |
| 25 | Charles de Gaulle International Airport |  | FR | 906 |
| 26 | Bengaluru International Airport |  | IN | 896 |
| 27 | Malpensa International Airport |  | IT | 861 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 828 |
| 29 | Ninoy Aquino International Airport |  | PH | 821 |
| 30 | Daniel K Inouye International Airport |  | US | 799 |
| 31 | Barcelona International Airport |  | ES | 781 |
| 32 | Tenerife Norte Airport |  | ES | 768 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 764 |
| 34 | Calgary International Airport |  | CA | 736 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 730 |
| 36 | Seattle-Tacoma International Airport |  | US | 721 |
| 37 | Vitoria/Foronda Airport |  | ES | 720 |
| 38 | Scottsdale Airport |  | US | 719 |
| 39 | Amsterdam Airport Schiphol |  | NL | 715 |
| 40 | Viracopos International Airport |  | BR | 709 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 455 | 21m | 244 km | 1,915.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 323 | 24m | 225 km | 1,253.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 314 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 299 | 1h 10m | 770 km | 3,972.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 186 | 22m | 55 km | 176.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 174 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 173 | 44m | 241 km | 718.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 171 | 27m | 152 km | 446.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 159 | 1h 44m | 1,423 km | 3,902.1 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 146 | 1h 38m | 1,156 km | 2,912.6 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 146 | 1h 1m | 695 km | 1,750.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 142 | 1h 17m | 961 km | 2,353.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 139 | 30m | 49 km | 117.5 t |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 136 | 1h 1m | 611 km | 1,434.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N231SV |  | Sky Ranch Airport (TN98) | Hilton Head Airport (KHXD) | 2026-06-30 14:06 UTC | 2026-06-30 14:54 UTC | 47m |
| CXK491 | CXK | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | 2026-06-30 13:54 UTC | 2026-06-30 14:53 UTC | 59m |
| N758RF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-06-30 14:34 UTC | 2026-06-30 14:51 UTC | 16m |
| N5NJ |  | Trenton Mercer Airport (KTTN) | Essex County Airport (KCDW) | 2026-06-30 13:58 UTC | 2026-06-30 14:49 UTC | 51m |
| N244ME |  | Lake Village Municipal Airport (KM32) | Belzoni Municipal Airport (K1M2) | 2026-06-30 13:24 UTC | 2026-06-30 14:47 UTC | 1h 23m |
| N839SP |  | Roberts Field (KRDM) | Prineville Airport (KS39) | 2026-06-30 14:30 UTC | 2026-06-30 14:42 UTC | 11m |
| UAE9832 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-06-30 07:44 UTC | 2026-06-30 14:41 UTC | 6h 57m |
| N6937T |  | Tucson International Airport (KTUS) | Benson Airport (31AZ) | 2026-06-30 14:19 UTC | 2026-06-30 14:38 UTC | 18m |
| N135RF |  | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Casas Adobes Airpark (NM69) | 2026-06-30 13:56 UTC | 2026-06-30 14:37 UTC | 41m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-30 14:23 UTC | 2026-06-30 14:35 UTC | 11m |
| N184K |  | Pennridge Airport (KCKZ) | Pennridge Airport (KCKZ) | 2026-06-30 14:32 UTC | 2026-06-30 14:34 UTC | 1m |
| N7912X |  | Atlanta Regional Falcon Field (KFFC) | Newnan Coweta County Airport (KCCO) | 2026-06-30 14:20 UTC | 2026-06-30 14:31 UTC | 11m |
| N783EA |  | Southern Wisconsin Regional Airport (KJVL) | Southern Wisconsin Regional Airport (KJVL) | 2026-06-30 13:54 UTC | 2026-06-30 14:26 UTC | 32m |
| N7198Q |  | Tampa Executive Airport (KVDF) | Tampa Executive Airport (KVDF) | 2026-06-30 14:10 UTC | 2026-06-30 14:25 UTC | 15m |
| SEH010 | SEH | Eleftherios Venizelos International Airport (LGAV) | Astypalaia Airport (LGPL) | 2026-06-30 13:46 UTC | 2026-06-30 14:24 UTC | 37m |
| UAY84 | UAY | DCAE Cosford Airport (EGWC) | DCAE Cosford Airport (EGWC) | 2026-06-30 14:00 UTC | 2026-06-30 14:23 UTC | 22m |
| N4953G |  | Casper/Natrona County International Airport (KCPR) | Iberlin Ranch Nr 2 Airport (WY18) | 2026-06-30 14:04 UTC | 2026-06-30 14:21 UTC | 17m |
| IGO1054 | IndiGo | Suvarnabhumi Airport (VTBS) | Naypyidaw Airport (VYEL) | 2026-06-30 13:34 UTC | 2026-06-30 14:20 UTC | 46m |
| RYR7352 | Ryanair | Edinburgh Airport (EGPH) | Wevelgem Airport (EBKT) | 2026-06-30 12:57 UTC | 2026-06-30 14:19 UTC | 1h 21m |
| ESR861 | ESR | Incheon International Airport (RKSI) | Chek Lap Kok International Airport (VHHH) | 2026-06-30 11:18 UTC | 2026-06-30 14:18 UTC | 2h 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_11:24:11_UTC-green)

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

**Latest saved flight:** 2026-07-09 11:24:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-09 11:24:11 UTC

- **133,900** saved flights
- **45,319** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **133,900** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,611,916.7 tonnes** estimated CO2 emissions
- **93,444,445 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5437 |
| 2 | SkyWest Airlines | 4937 |
| 3 | EJA | 2623 |
| 4 | IndiGo | 2495 |
| 5 | American Airlines | 2092 |
| 6 | Southwest Airlines | 2009 |
| 7 | ENY | 1681 |
| 8 | Delta Air Lines | 1600 |
| 9 | Lufthansa | 1386 |
| 10 | LATAM Airlines | 1227 |
| 11 | Vueling | 1174 |
| 12 | WIF | 1168 |
| 13 | AZU | 1137 |
| 14 | LXJ | 1026 |
| 15 | AXM | 1021 |
| 16 | Swiss International | 954 |
| 17 | All Nippon Airways | 878 |
| 18 | easyJet | 867 |
| 19 | Alaska Airlines | 851 |
| 20 | QLK | 841 |
| 21 | EJU | 822 |
| 22 | VIV | 738 |
| 23 | AEE | 727 |
| 24 | Air France | 721 |
| 25 | Cathay Pacific | 720 |
| 26 | CXK | 719 |
| 27 | United Airlines | 709 |
| 28 | JetBlue | 705 |
| 29 | MXY | 693 |
| 30 | GLO | 681 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 114752 |
| 2 | 🇪🇸 ES | 8887 |
| 3 | 🇮🇳 IN | 7824 |
| 4 | 🇦🇺 AU | 7764 |
| 5 | 🇧🇷 BR | 7526 |
| 6 | 🇨🇦 CA | 7063 |
| 7 | 🇩🇪 DE | 6996 |
| 8 | 🇮🇹 IT | 6961 |
| 9 | 🇬🇧 GB | 6019 |
| 10 | 🇯🇵 JP | 5754 |
| 11 | 🇫🇷 FR | 5322 |
| 12 | 🇨🇴 CO | 4173 |
| 13 | 🇲🇽 MX | 3896 |
| 14 | 🇬🇷 GR | 3828 |
| 15 | 🇳🇴 NO | 3634 |
| 16 | 🇨🇭 CH | 3474 |
| 17 | 🇹🇷 TR | 3042 |
| 18 | 🇲🇾 MY | 2651 |
| 19 | 🇵🇱 PL | 2211 |
| 20 | 🇿🇦 ZA | 2207 |
| 21 | 🇳🇿 NZ | 2103 |
| 22 | 🇹🇭 TH | 2058 |
| 23 | 🇰🇷 KR | 1983 |
| 24 | 🇵🇭 PH | 1847 |
| 25 | 🇬🇹 GT | 1810 |
| 26 | 🇲🇦 MA | 1423 |
| 27 | 🇲🇪 ME | 1333 |
| 28 | 🇳🇱 NL | 1255 |
| 29 | 🇭🇷 HR | 1193 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2789 |
| 2 | Denver International Airport |  | US | 2262 |
| 3 | Tokyo International Airport |  | JP | 1878 |
| 4 | Indira Gandhi International Airport |  | IN | 1727 |
| 5 | Harry Reid International Airport |  | US | 1664 |
| 6 | Guaymaral Airport |  | CO | 1627 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1571 |
| 8 | Zurich Airport |  | CH | 1493 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1421 |
| 10 | La Aurora Airport |  | GT | 1398 |
| 11 | Frankfurt am Main International Airport |  | DE | 1340 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1292 |
| 13 | Chicago O'Hare International Airport |  | US | 1278 |
| 14 | Salt Lake City International Airport |  | US | 1191 |
| 15 | Macau International Airport |  | MO | 1186 |
| 16 | El Dorado International Airport |  | CO | 1184 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1158 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1096 |
| 19 | Madrid Barajas International Airport |  | ES | 1096 |
| 20 | Capua Airport |  | IT | 1096 |
| 21 | Congonhas Airport |  | BR | 1065 |
| 22 | Kuala Lumpur International Airport |  | MY | 1030 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 975 |
| 25 | Charles de Gaulle International Airport |  | FR | 961 |
| 26 | Bengaluru International Airport |  | IN | 943 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 917 |
| 28 | Malpensa International Airport |  | IT | 884 |
| 29 | Ninoy Aquino International Airport |  | PH | 859 |
| 30 | Daniel K Inouye International Airport |  | US | 832 |
| 31 | Barcelona International Airport |  | ES | 826 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 817 |
| 33 | Tenerife Norte Airport |  | ES | 804 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 787 |
| 35 | Calgary International Airport |  | CA | 776 |
| 36 | Seattle-Tacoma International Airport |  | US | 767 |
| 37 | Scottsdale Airport |  | US | 764 |
| 38 | Viracopos International Airport |  | BR | 761 |
| 39 | Vitoria/Foronda Airport |  | ES | 758 |
| 40 | Amsterdam Airport Schiphol |  | NL | 754 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 684 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 484 | 21m | 244 km | 2,038.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 334 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 324 | 1h 10m | 770 km | 4,304.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 243 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 196 | 22m | 55 km | 186.3 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 186 | 26m | 215 km | 688.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 180 | 1h 46m | 1,423 km | 4,417.5 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 162 | 20m | 250 km | 699.7 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 160 | 44m | 452 km | 1,247.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 155 | 1h 16m | 961 km | 2,569.2 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPRTN60 | SPR | Ota Airport (LPOT) | Ota Airport (LPOT) | 2026-07-09 10:43 UTC | 2026-07-09 11:24 UTC | 40m |
| HB1972 |  | Bex Airport (LSGB) | Bex Airport (LSGB) | 2026-07-09 10:50 UTC | 2026-07-09 11:15 UTC | 25m |
| N166DR |  | Noland Farms Airport (3IS3) | Noland Farms Airport (3IS3) | 2026-07-09 11:03 UTC | 2026-07-09 11:14 UTC | 10m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-07-09 08:12 UTC | 2026-07-09 11:08 UTC | 2h 55m |
| A7GAA |  | Al Khawr Airport (OTBK) | Al Khawr Airport (OTBK) | 2026-07-09 10:40 UTC | 2026-07-09 11:03 UTC | 23m |
| SAVER20 | SAV | Mo i Rana Airport Rossvoll (ENRA) | Sandnessjoen Airport Stokka (ENST) | 2026-07-09 09:33 UTC | 2026-07-09 11:03 UTC | 1h 29m |
| N278FG |  | Trenton Mercer Airport (KTTN) | Flying W Airport (KN14) | 2026-07-09 10:45 UTC | 2026-07-09 10:59 UTC | 13m |
| RYR4PJ | Ryanair | Eleftherios Venizelos International Airport (LGAV) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-09 08:29 UTC | 2026-07-09 10:50 UTC | 2h 21m |
|  |  | Megeve Airport (LFHM) | Sion Airport (LSGS) | 2026-07-09 10:49 UTC | 2026-07-09 10:49 UTC | 0m |
| ZKIUY | ZKI | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-09 10:39 UTC | 2026-07-09 10:47 UTC | 7m |
| JOKER88 | JOK | Wurzburg-Schenkenturm Airport (EDFW) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-07-09 09:19 UTC | 2026-07-09 10:44 UTC | 1h 25m |
| ASA436 | Alaska Airlines | Portland International Airport (KPDX) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-09 05:54 UTC | 2026-07-09 10:44 UTC | 4h 50m |
| HBEZE | HBE | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-07-09 09:49 UTC | 2026-07-09 10:43 UTC | 54m |
| CPA820 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Toronto Pearson International Airport (CYYZ) | 2026-07-08 20:02 UTC | 2026-07-09 10:42 UTC | 14h 40m |
| SCR762 | SCR | RAF Northolt (EGWU) | Samedan Airport (LSZS) | 2026-07-09 09:12 UTC | 2026-07-09 10:40 UTC | 1h 28m |
| SWE52L | SWE | Stockholm-Bromma Airport (ESSB) | Visingso Airport (ESSI) | 2026-07-09 10:13 UTC | 2026-07-09 10:38 UTC | 25m |
| DLH7LL | Lufthansa | Munich International Airport (EDDM) | Munster Osnabruck Airport (EDDG) | 2026-07-09 09:46 UTC | 2026-07-09 10:37 UTC | 50m |
| CTM1275 | CTM | Paris-Orly Airport (LFPO) | Bergen Airport Flesland (ENBR) | 2026-07-09 08:37 UTC | 2026-07-09 10:33 UTC | 1h 56m |
| CX |  | Innsbruck Airport (LOWI) | Innsbruck Airport (LOWI) | 2026-07-09 10:20 UTC | 2026-07-09 10:30 UTC | 10m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-07-09 09:55 UTC | 2026-07-09 10:28 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

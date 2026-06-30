# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_05:39:43_UTC-green)

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

**Latest saved flight:** 2026-06-30 05:39:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-30 05:39:43 UTC

- **124,582** saved flights
- **42,646** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **124,582** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,505,401.4 tonnes** estimated CO2 emissions
- **87,269,648 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5077 |
| 2 | SkyWest Airlines | 4627 |
| 3 | EJA | 2437 |
| 4 | IndiGo | 2366 |
| 5 | American Airlines | 1929 |
| 6 | Southwest Airlines | 1872 |
| 7 | ENY | 1565 |
| 8 | Delta Air Lines | 1483 |
| 9 | Lufthansa | 1337 |
| 10 | LATAM Airlines | 1122 |
| 11 | Vueling | 1105 |
| 12 | WIF | 1101 |
| 13 | AZU | 1047 |
| 14 | AXM | 992 |
| 15 | LXJ | 966 |
| 16 | Swiss International | 875 |
| 17 | All Nippon Airways | 839 |
| 18 | Alaska Airlines | 819 |
| 19 | easyJet | 794 |
| 20 | QLK | 780 |
| 21 | EJU | 776 |
| 22 | Cathay Pacific | 694 |
| 23 | AEE | 688 |
| 24 | VIV | 680 |
| 25 | Air France | 676 |
| 26 | United Airlines | 667 |
| 27 | CXK | 664 |
| 28 | MXY | 650 |
| 29 | JetBlue | 638 |
| 30 | GLO | 623 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 106305 |
| 2 | 🇪🇸 ES | 8348 |
| 3 | 🇮🇳 IN | 7426 |
| 4 | 🇦🇺 AU | 7278 |
| 5 | 🇧🇷 BR | 6918 |
| 6 | 🇩🇪 DE | 6604 |
| 7 | 🇮🇹 IT | 6585 |
| 8 | 🇨🇦 CA | 6539 |
| 9 | 🇬🇧 GB | 5488 |
| 10 | 🇯🇵 JP | 5480 |
| 11 | 🇫🇷 FR | 4926 |
| 12 | 🇨🇴 CO | 4032 |
| 13 | 🇲🇽 MX | 3625 |
| 14 | 🇬🇷 GR | 3551 |
| 15 | 🇳🇴 NO | 3423 |
| 16 | 🇨🇭 CH | 3184 |
| 17 | 🇹🇷 TR | 2619 |
| 18 | 🇲🇾 MY | 2568 |
| 19 | 🇿🇦 ZA | 2047 |
| 20 | 🇵🇱 PL | 2043 |
| 21 | 🇳🇿 NZ | 2019 |
| 22 | 🇹🇭 TH | 1952 |
| 23 | 🇰🇷 KR | 1937 |
| 24 | 🇵🇭 PH | 1768 |
| 25 | 🇬🇹 GT | 1718 |
| 26 | 🇲🇦 MA | 1340 |
| 27 | 🇲🇪 ME | 1239 |
| 28 | 🇳🇱 NL | 1178 |
| 29 | 🇲🇴 MO | 1177 |
| 30 | 🇧🇸 BS | 1078 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2615 |
| 2 | Denver International Airport |  | US | 2107 |
| 3 | Tokyo International Airport |  | JP | 1810 |
| 4 | Indira Gandhi International Airport |  | IN | 1636 |
| 5 | Harry Reid International Airport |  | US | 1559 |
| 6 | Guaymaral Airport |  | CO | 1520 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1496 |
| 8 | Zurich Airport |  | CH | 1378 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1332 |
| 10 | La Aurora Airport |  | GT | 1326 |
| 11 | Frankfurt am Main International Airport |  | DE | 1290 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1228 |
| 13 | Chicago O'Hare International Airport |  | US | 1207 |
| 14 | Macau International Airport |  | MO | 1177 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1101 |
| 17 | Capua Airport |  | IT | 1061 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1040 |
| 19 | Madrid Barajas International Airport |  | ES | 1032 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1005 |
| 21 | Kuala Lumpur International Airport |  | MY | 999 |
| 22 | Congonhas Airport |  | BR | 971 |
| 23 | Charlotte/Douglas International Airport |  | US | 941 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 916 |
| 25 | Charles de Gaulle International Airport |  | FR | 905 |
| 26 | Bengaluru International Airport |  | IN | 894 |
| 27 | Malpensa International Airport |  | IT | 861 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 825 |
| 29 | Ninoy Aquino International Airport |  | PH | 820 |
| 30 | Daniel K Inouye International Airport |  | US | 799 |
| 31 | Barcelona International Airport |  | ES | 778 |
| 32 | Tenerife Norte Airport |  | ES | 767 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 762 |
| 34 | Calgary International Airport |  | CA | 735 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 729 |
| 36 | Seattle-Tacoma International Airport |  | US | 720 |
| 37 | Vitoria/Foronda Airport |  | ES | 719 |
| 38 | Amsterdam Airport Schiphol |  | NL | 715 |
| 39 | Scottsdale Airport |  | US | 715 |
| 40 | Viracopos International Airport |  | BR | 704 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 455 | 21m | 244 km | 1,915.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 323 | 24m | 225 km | 1,253.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 312 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 299 | 1h 10m | 770 km | 3,972.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 185 | 22m | 55 km | 175.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 176 | 20m | 99 km | 301.5 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 174 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 172 | 44m | 241 km | 714.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 168 | 27m | 152 km | 439.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 159 | 1h 44m | 1,423 km | 3,902.1 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 156 | 18m | 144 km | 388.0 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 152 | 20m | 250 km | 656.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 145 | 1h 38m | 1,156 km | 2,892.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 144 | 1h 1m | 695 km | 1,726.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 142 | 1h 17m | 961 km | 2,353.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 139 | 30m | 49 km | 117.5 t |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 136 | 1h 1m | 611 km | 1,434.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CHH424 | CHH | Suvarnabhumi Airport (VTBS) | Luang Namtha Airport (VLLN) | 2026-06-30 04:33 UTC | 2026-06-30 05:39 UTC | 1h 6m |
| THA132 | Thai Airways | Suvarnabhumi Airport (VTBS) | Chiang Rai Airport (VTCR) | 2026-06-30 04:44 UTC | 2026-06-30 05:39 UTC | 54m |
| TLM537 | TLM | Chiang Rai International Airport (VTCT) | Uttaradit Airport (VTPU) | 2026-06-30 05:18 UTC | 2026-06-30 05:39 UTC | 21m |
| TCUUM | TCU | Istanbul Hezarfen Airfield (LTBW) | Istanbul Hezarfen Airfield (LTBW) | 2026-06-30 04:46 UTC | 2026-06-30 05:38 UTC | 51m |
| N294DS |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-06-30 04:53 UTC | 2026-06-30 05:30 UTC | 36m |
| J1009KT |  | Adi Sutjipto International Airport (WARJ) | Adi Sutjipto International Airport (WARJ) | 2026-06-30 04:58 UTC | 2026-06-30 05:26 UTC | 27m |
| RYR70WE | Ryanair | Stockholm-Arlanda Airport (ESSA) | Olanda Airport (ESMZ) | 2026-06-30 04:56 UTC | 2026-06-30 05:21 UTC | 25m |
| SWA4875 | Southwest Airlines | San Diego International Airport (KSAN) | NV13 (NV13) | 2026-06-30 04:11 UTC | 2026-06-30 05:16 UTC | 1h 5m |
| N901XM |  | Bangor International Airport (KBGR) | Bangor International Airport (KBGR) | 2026-06-30 05:03 UTC | 2026-06-30 05:07 UTC | 4m |
| XSN06 | XSN | Sacramento Executive Airport (KSAC) | San Carlos Airport (KSQL) | 2026-06-30 04:44 UTC | 2026-06-30 05:05 UTC | 21m |
| G20931 |  | Los Alamitos Army Air Field (KSLI) | Los Alamitos Army Air Field (KSLI) | 2026-06-30 03:55 UTC | 2026-06-30 05:05 UTC | 1h 9m |
| AYT251 | AYT | Hatzor Air Base (LLHS) | Nevatim Air Base (LLNV) | 2026-06-30 04:47 UTC | 2026-06-30 05:02 UTC | 14m |
| MMA780 | MMA | Yangon International Airport (VYYY) | Kalay Airport (VYKL) | 2026-06-30 03:22 UTC | 2026-06-30 04:59 UTC | 1h 37m |
| UBA582 | UBA | Monywar Airport (VYMY) | Phonngbyin Airport (VYPB) | 2026-06-30 04:31 UTC | 2026-06-30 04:58 UTC | 27m |
| JBU247 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | Cavok Ranch Airport (UT90) | 2026-06-29 23:56 UTC | 2026-06-30 04:58 UTC | 5h 1m |
| DLH07Y | Lufthansa | Salzburg Airport (LOWS) | Frankfurt am Main International Airport (EDDF) | 2026-06-30 04:03 UTC | 2026-06-30 04:53 UTC | 49m |
| SOUND21 | SOU | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-06-30 04:29 UTC | 2026-06-30 04:52 UTC | 23m |
| JST884 | JST | Melbourne International Airport (YMML) | Hervey Bay Airport (YHBA) | 2026-06-30 02:41 UTC | 2026-06-30 04:52 UTC | 2h 10m |
| AE974 |  | Gold Coast Airport (YBCG) | Cassilis Rotherw Airport (YCSI) | 2026-06-30 03:48 UTC | 2026-06-30 04:51 UTC | 1h 3m |
| VAR488 | VAR | Buckeye Municipal Airport (KBXK) | Phoenix Goodyear Airport (KGYR) | 2026-06-30 03:41 UTC | 2026-06-30 04:51 UTC | 1h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_13:01:25_UTC-green)

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

**Latest saved flight:** 2026-07-03 13:01:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-03 13:01:25 UTC

- **127,112** saved flights
- **43,369** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **127,112** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,534,058.5 tonnes** estimated CO2 emissions
- **88,930,930 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5153 |
| 2 | SkyWest Airlines | 4692 |
| 3 | EJA | 2499 |
| 4 | IndiGo | 2403 |
| 5 | American Airlines | 1951 |
| 6 | Southwest Airlines | 1904 |
| 7 | ENY | 1594 |
| 8 | Delta Air Lines | 1512 |
| 9 | Lufthansa | 1353 |
| 10 | LATAM Airlines | 1158 |
| 11 | Vueling | 1126 |
| 12 | WIF | 1119 |
| 13 | AZU | 1072 |
| 14 | AXM | 1002 |
| 15 | LXJ | 990 |
| 16 | Swiss International | 882 |
| 17 | All Nippon Airways | 853 |
| 18 | Alaska Airlines | 825 |
| 19 | easyJet | 812 |
| 20 | QLK | 803 |
| 21 | EJU | 786 |
| 22 | Cathay Pacific | 706 |
| 23 | VIV | 698 |
| 24 | AEE | 696 |
| 25 | Air France | 694 |
| 26 | CXK | 684 |
| 27 | United Airlines | 674 |
| 28 | MXY | 660 |
| 29 | JetBlue | 652 |
| 30 | GLO | 640 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 108693 |
| 2 | 🇪🇸 ES | 8471 |
| 3 | 🇮🇳 IN | 7534 |
| 4 | 🇦🇺 AU | 7445 |
| 5 | 🇧🇷 BR | 7104 |
| 6 | 🇩🇪 DE | 6701 |
| 7 | 🇨🇦 CA | 6680 |
| 8 | 🇮🇹 IT | 6665 |
| 9 | 🇬🇧 GB | 5611 |
| 10 | 🇯🇵 JP | 5565 |
| 11 | 🇫🇷 FR | 5022 |
| 12 | 🇨🇴 CO | 4050 |
| 13 | 🇲🇽 MX | 3688 |
| 14 | 🇬🇷 GR | 3610 |
| 15 | 🇳🇴 NO | 3471 |
| 16 | 🇨🇭 CH | 3234 |
| 17 | 🇹🇷 TR | 2694 |
| 18 | 🇲🇾 MY | 2597 |
| 19 | 🇿🇦 ZA | 2103 |
| 20 | 🇵🇱 PL | 2074 |
| 21 | 🇳🇿 NZ | 2057 |
| 22 | 🇹🇭 TH | 1987 |
| 23 | 🇰🇷 KR | 1958 |
| 24 | 🇵🇭 PH | 1804 |
| 25 | 🇬🇹 GT | 1743 |
| 26 | 🇲🇦 MA | 1362 |
| 27 | 🇲🇪 ME | 1256 |
| 28 | 🇳🇱 NL | 1196 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇧🇸 BS | 1098 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2655 |
| 2 | Denver International Airport |  | US | 2141 |
| 3 | Tokyo International Airport |  | JP | 1835 |
| 4 | Indira Gandhi International Airport |  | IN | 1658 |
| 5 | Harry Reid International Airport |  | US | 1589 |
| 6 | Guaymaral Airport |  | CO | 1537 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1510 |
| 8 | Zurich Airport |  | CH | 1397 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1351 |
| 10 | La Aurora Airport |  | GT | 1347 |
| 11 | Frankfurt am Main International Airport |  | DE | 1307 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1244 |
| 13 | Chicago O'Hare International Airport |  | US | 1227 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1121 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1053 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1047 |
| 20 | Madrid Barajas International Airport |  | ES | 1044 |
| 21 | Kuala Lumpur International Airport |  | MY | 1010 |
| 22 | Congonhas Airport |  | BR | 998 |
| 23 | Charlotte/Douglas International Airport |  | US | 952 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 935 |
| 25 | Charles de Gaulle International Airport |  | FR | 925 |
| 26 | Bengaluru International Airport |  | IN | 910 |
| 27 | Malpensa International Airport |  | IT | 869 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 852 |
| 29 | Ninoy Aquino International Airport |  | PH | 836 |
| 30 | Daniel K Inouye International Airport |  | US | 807 |
| 31 | Barcelona International Airport |  | ES | 792 |
| 32 | Tenerife Norte Airport |  | ES | 776 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 771 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 745 |
| 35 | Calgary International Airport |  | CA | 742 |
| 36 | Scottsdale Airport |  | US | 736 |
| 37 | Seattle-Tacoma International Airport |  | US | 734 |
| 38 | Vitoria/Foronda Airport |  | ES | 729 |
| 39 | Viracopos International Airport |  | BR | 723 |
| 40 | Amsterdam Airport Schiphol |  | NL | 722 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 641 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 462 | 21m | 244 km | 1,945.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 318 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 309 | 1h 10m | 770 km | 4,104.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 243 | 26m | 275 km | 1,151.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 236 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 187 | 22m | 55 km | 177.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 180 | 26m | 215 km | 666.6 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 177 | 44m | 241 km | 735.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 164 | 1h 45m | 1,423 km | 4,024.8 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 162 | 31m | 369 km | 1,031.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 154 | 20m | 250 km | 665.2 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 152 | 30m | 49 km | 128.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 148 | 1h 1m | 695 km | 1,774.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 147 | 1h 17m | 961 km | 2,436.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 144 | 54m | 136 km | 337.6 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFIAQ | CFI | Wilderman Farm Airport (CFT2) | CEB4 (CEB4) | 2026-07-03 12:45 UTC | 2026-07-03 13:01 UTC | 15m |
| N7368F |  | Lee Airport (KANP) | Cambridge-Dorchester Regional Airport (KCGE) | 2026-07-03 12:20 UTC | 2026-07-03 12:58 UTC | 38m |
| N850FS |  | Page Field (KFMY) | La Belle Municipal Airport (KX14) | 2026-07-03 12:28 UTC | 2026-07-03 12:52 UTC | 23m |
| N32097 |  | Lee Airport (KANP) | Easton/Newnam Field (KESN) | 2026-07-03 12:21 UTC | 2026-07-03 12:48 UTC | 26m |
| N911BT |  | Donalsonville Municipal Airport (K17J) | Donalsonville Municipal Airport (K17J) | 2026-07-03 12:02 UTC | 2026-07-03 12:41 UTC | 38m |
| N15760 |  | Chester Airport (KSNC) | Newport State Airport (KUUU) | 2026-07-03 12:04 UTC | 2026-07-03 12:41 UTC | 36m |
| N961KS |  | Cameron Park Airport (KO61) | Lake Tahoe Airport (KTVL) | 2026-07-03 11:19 UTC | 2026-07-03 12:36 UTC | 1h 17m |
| N104VA |  | Manassas Regional/Harry P Davis Field (KHEF) | Culpeper Regional Airport (KCJR) | 2026-07-03 12:01 UTC | 2026-07-03 12:27 UTC | 26m |
| DCIFM | DCI | Dusseldorf International Airport (EDDL) | Friedrichshafen Airport (EDNY) | 2026-07-03 11:40 UTC | 2026-07-03 12:21 UTC | 41m |
| TKJ4615 | TKJ | Sivas Airport (LTAR) | Milas Bodrum International Airport (LTFE) | 2026-07-03 10:58 UTC | 2026-07-03 12:19 UTC | 1h 21m |
| HBXCL | HBX | Courchevel Airport (LFLJ) | Megeve Airport (LFHM) | 2026-07-03 11:46 UTC | 2026-07-03 12:17 UTC | 31m |
| CXK557 | CXK | Ogden-Hinckley Airport (KOGD) | Ogden-Hinckley Airport (KOGD) | 2026-07-03 11:43 UTC | 2026-07-03 12:15 UTC | 31m |
| N949SP |  | St Mary's County Regional Airport (K2W6) | Cambridge-Dorchester Regional Airport (KCGE) | 2026-07-03 11:47 UTC | 2026-07-03 12:14 UTC | 26m |
| HBXYF | HBX | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-07-03 11:55 UTC | 2026-07-03 12:12 UTC | 16m |
| GBZDA | GBZ | White Waltham Airfield (EGLM) | Llanbedr Airport (EGOD) | 2026-07-03 10:41 UTC | 2026-07-03 12:11 UTC | 1h 29m |
| N7693Y |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-07-03 12:07 UTC | 2026-07-03 12:08 UTC | 0m |
| CXK1012 | CXK | Jacksonville Executive At Craig Airport (KCRG) | Nassau Airport (83FL) | 2026-07-03 12:02 UTC | 2026-07-03 12:08 UTC | 5m |
| SIRIUS1 | SIR | Pirassununga Airport (SDPY) | Usina Santa Rita Airport (SDSQ) | 2026-07-03 11:54 UTC | 2026-07-03 12:07 UTC | 12m |
| PNC0490 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-03 11:45 UTC | 2026-07-03 12:05 UTC | 20m |
| FDR364 | FDR | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-07-03 11:30 UTC | 2026-07-03 12:01 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

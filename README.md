# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_15:43:51_UTC-green)

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

**Latest saved flight:** 2026-07-01 15:43:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-01 15:43:51 UTC

- **125,499** saved flights
- **42,898** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **125,499** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,514,677.7 tonnes** estimated CO2 emissions
- **87,807,406 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5112 |
| 2 | SkyWest Airlines | 4638 |
| 3 | EJA | 2451 |
| 4 | IndiGo | 2389 |
| 5 | American Airlines | 1935 |
| 6 | Southwest Airlines | 1877 |
| 7 | ENY | 1576 |
| 8 | Delta Air Lines | 1496 |
| 9 | Lufthansa | 1342 |
| 10 | LATAM Airlines | 1131 |
| 11 | Vueling | 1118 |
| 12 | WIF | 1110 |
| 13 | AZU | 1059 |
| 14 | AXM | 996 |
| 15 | LXJ | 970 |
| 16 | Swiss International | 877 |
| 17 | All Nippon Airways | 845 |
| 18 | Alaska Airlines | 820 |
| 19 | easyJet | 800 |
| 20 | QLK | 784 |
| 21 | EJU | 780 |
| 22 | Cathay Pacific | 696 |
| 23 | AEE | 692 |
| 24 | Air France | 686 |
| 25 | VIV | 685 |
| 26 | CXK | 670 |
| 27 | United Airlines | 669 |
| 28 | MXY | 653 |
| 29 | JetBlue | 642 |
| 30 | GLO | 631 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 107081 |
| 2 | 🇪🇸 ES | 8403 |
| 3 | 🇮🇳 IN | 7487 |
| 4 | 🇦🇺 AU | 7323 |
| 5 | 🇧🇷 BR | 6988 |
| 6 | 🇩🇪 DE | 6635 |
| 7 | 🇮🇹 IT | 6616 |
| 8 | 🇨🇦 CA | 6592 |
| 9 | 🇬🇧 GB | 5553 |
| 10 | 🇯🇵 JP | 5508 |
| 11 | 🇫🇷 FR | 4969 |
| 12 | 🇨🇴 CO | 4038 |
| 13 | 🇲🇽 MX | 3641 |
| 14 | 🇬🇷 GR | 3586 |
| 15 | 🇳🇴 NO | 3446 |
| 16 | 🇨🇭 CH | 3199 |
| 17 | 🇹🇷 TR | 2642 |
| 18 | 🇲🇾 MY | 2576 |
| 19 | 🇿🇦 ZA | 2080 |
| 20 | 🇵🇱 PL | 2058 |
| 21 | 🇳🇿 NZ | 2027 |
| 22 | 🇹🇭 TH | 1970 |
| 23 | 🇰🇷 KR | 1946 |
| 24 | 🇵🇭 PH | 1778 |
| 25 | 🇬🇹 GT | 1736 |
| 26 | 🇲🇦 MA | 1350 |
| 27 | 🇲🇪 ME | 1246 |
| 28 | 🇳🇱 NL | 1187 |
| 29 | 🇲🇴 MO | 1182 |
| 30 | 🇧🇸 BS | 1086 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2627 |
| 2 | Denver International Airport |  | US | 2114 |
| 3 | Tokyo International Airport |  | JP | 1819 |
| 4 | Indira Gandhi International Airport |  | IN | 1645 |
| 5 | Harry Reid International Airport |  | US | 1567 |
| 6 | Guaymaral Airport |  | CO | 1525 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1504 |
| 8 | Zurich Airport |  | CH | 1388 |
| 9 | La Aurora Airport |  | GT | 1342 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1337 |
| 11 | Frankfurt am Main International Airport |  | DE | 1296 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1229 |
| 13 | Chicago O'Hare International Airport |  | US | 1212 |
| 14 | Macau International Airport |  | MO | 1182 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1101 |
| 17 | Capua Airport |  | IT | 1064 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1044 |
| 19 | Madrid Barajas International Airport |  | ES | 1039 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1019 |
| 21 | Kuala Lumpur International Airport |  | MY | 1003 |
| 22 | Congonhas Airport |  | BR | 978 |
| 23 | Charlotte/Douglas International Airport |  | US | 944 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 920 |
| 25 | Charles de Gaulle International Airport |  | FR | 913 |
| 26 | Bengaluru International Airport |  | IN | 904 |
| 27 | Malpensa International Airport |  | IT | 863 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 835 |
| 29 | Ninoy Aquino International Airport |  | PH | 824 |
| 30 | Daniel K Inouye International Airport |  | US | 802 |
| 31 | Barcelona International Airport |  | ES | 789 |
| 32 | Tenerife Norte Airport |  | ES | 771 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 764 |
| 34 | Calgary International Airport |  | CA | 736 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 732 |
| 36 | Seattle-Tacoma International Airport |  | US | 724 |
| 37 | Scottsdale Airport |  | US | 724 |
| 38 | Vitoria/Foronda Airport |  | ES | 723 |
| 39 | Amsterdam Airport Schiphol |  | NL | 717 |
| 40 | Viracopos International Airport |  | BR | 712 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 635 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 458 | 21m | 244 km | 1,928.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 324 | 24m | 225 km | 1,257.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 317 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 302 | 1h 10m | 770 km | 4,011.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 243 | 26m | 275 km | 1,151.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 233 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 186 | 22m | 55 km | 176.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 173 | 44m | 241 km | 718.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 161 | 1h 45m | 1,423 km | 3,951.2 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 146 | 1h 1m | 695 km | 1,750.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 143 | 1h 17m | 961 km | 2,370.3 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 141 | 30m | 49 km | 119.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 140 | 54m | 136 km | 328.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EJA214 | EJA | Martha's Vineyard Airport (KMVY) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-01 15:20 UTC | 2026-07-01 15:43 UTC | 23m |
| N734GA |  | Fort Lauderdale Executive Airport (KFXE) | Fort Lauderdale Executive Airport (KFXE) | 2026-07-01 14:49 UTC | 2026-07-01 15:41 UTC | 52m |
| ERU16 | ERU | Massey Farm Airport (AZ34) | Lake Havasu City Airport (KHII) | 2026-07-01 15:19 UTC | 2026-07-01 15:41 UTC | 21m |
| CGAIT | CGA | Camrose Airport (CEQ3) | Camrose Airport (CEQ3) | 2026-07-01 15:25 UTC | 2026-07-01 15:39 UTC | 14m |
| MILAN78 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Beziers-Vias Airport (LFMU) | 2026-07-01 15:24 UTC | 2026-07-01 15:38 UTC | 14m |
| CXK1003 | CXK | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-07-01 14:39 UTC | 2026-07-01 15:38 UTC | 58m |
| N2589W |  | Geary Ranch Airport (CO65) | 1CO7 (1CO7) | 2026-07-01 15:26 UTC | 2026-07-01 15:38 UTC | 12m |
| N615SM |  | Ogden-Hinckley Airport (KOGD) | Logan-Cache Airport (KLGU) | 2026-07-01 15:24 UTC | 2026-07-01 15:37 UTC | 13m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-07-01 15:19 UTC | 2026-07-01 15:37 UTC | 17m |
| XSN90 | XSN | Buchanan Field (KCCR) | CA38 (CA38) | 2026-07-01 15:04 UTC | 2026-07-01 15:37 UTC | 32m |
| N358EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-07-01 14:35 UTC | 2026-07-01 15:34 UTC | 58m |
| N106RF |  | Chloride Airport (NM51) | Chloride Airport (NM51) | 2026-07-01 15:11 UTC | 2026-07-01 15:31 UTC | 20m |
| TOPCT92 | TOP | Offutt Afb Airport (KOFF) | Mott Municipal Airport (K3P3) | 2026-07-01 14:25 UTC | 2026-07-01 15:29 UTC | 1h 3m |
| N158TS |  | Bellefontaine Regional Airport (KEDJ) | Bellefontaine Regional Airport (KEDJ) | 2026-07-01 14:34 UTC | 2026-07-01 15:28 UTC | 54m |
| N7269T |  | Fredonia Airport (K1K7) | Neodesha Municipal Airport (K2K7) | 2026-07-01 14:54 UTC | 2026-07-01 15:28 UTC | 34m |
| N13887 |  | Rachel's Landing Airport (8TN6) | Smyrna Airport (KMQY) | 2026-07-01 15:19 UTC | 2026-07-01 15:28 UTC | 8m |
| DMZSH | DMZ | Borken-Hoxfeld Airport (EDLY) | Hamm-Lippewiesen Airport (EDLH) | 2026-07-01 15:02 UTC | 2026-07-01 15:27 UTC | 25m |
| N67ZT |  | Lake Havasu City Airport (KHII) | Lake Havasu City Airport (KHII) | 2026-07-01 14:58 UTC | 2026-07-01 15:25 UTC | 26m |
| N197MC |  | Lewis University Airport (KLOT) | Southwest Michigan Regional Airport (KBEH) | 2026-07-01 14:39 UTC | 2026-07-01 15:25 UTC | 45m |
| N850UW |  | Southern Wisconsin Regional Airport (KJVL) | Platteville Municipal Airport (KPVB) | 2026-07-01 14:52 UTC | 2026-07-01 15:24 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

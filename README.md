# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_19:49:09_UTC-green)

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

**Latest saved flight:** 2026-08-04 19:49:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-04 19:49:09 UTC

- **171,030** saved flights
- **55,673** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **171,030** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,060,694.3 tonnes** estimated CO2 emissions
- **119,460,540 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6814 |
| 2 | SkyWest Airlines | 6245 |
| 3 | EJA | 3396 |
| 4 | IndiGo | 3005 |
| 5 | Southwest Airlines | 2692 |
| 6 | American Airlines | 2689 |
| 7 | ENY | 2130 |
| 8 | Delta Air Lines | 2035 |
| 9 | LATAM Airlines | 1584 |
| 10 | Lufthansa | 1564 |
| 11 | AZU | 1502 |
| 12 | WIF | 1433 |
| 13 | Vueling | 1405 |
| 14 | LXJ | 1340 |
| 15 | AXM | 1176 |
| 16 | Swiss International | 1166 |
| 17 | easyJet | 1152 |
| 18 | EJU | 1046 |
| 19 | Alaska Airlines | 1043 |
| 20 | QLK | 1041 |
| 21 | All Nippon Airways | 1036 |
| 22 | VIV | 943 |
| 23 | Cathay Pacific | 916 |
| 24 | CXK | 911 |
| 25 | United Airlines | 900 |
| 26 | GLO | 895 |
| 27 | AEE | 893 |
| 28 | Air France | 879 |
| 29 | MXY | 870 |
| 30 | JetBlue | 857 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 147414 |
| 2 | 🇪🇸 ES | 10966 |
| 3 | 🇧🇷 BR | 9718 |
| 4 | 🇦🇺 AU | 9521 |
| 5 | 🇮🇳 IN | 9413 |
| 6 | 🇨🇦 CA | 9323 |
| 7 | 🇮🇹 IT | 8854 |
| 8 | 🇩🇪 DE | 8505 |
| 9 | 🇬🇧 GB | 7933 |
| 10 | 🇯🇵 JP | 6872 |
| 11 | 🇫🇷 FR | 6785 |
| 12 | 🇨🇴 CO | 6218 |
| 13 | 🇬🇷 GR | 4976 |
| 14 | 🇲🇽 MX | 4895 |
| 15 | 🇨🇭 CH | 4497 |
| 16 | 🇳🇴 NO | 4469 |
| 17 | 🇹🇷 TR | 4180 |
| 18 | 🇲🇾 MY | 3057 |
| 19 | 🇵🇱 PL | 2874 |
| 20 | 🇿🇦 ZA | 2768 |
| 21 | 🇹🇭 TH | 2486 |
| 22 | 🇳🇿 NZ | 2471 |
| 23 | 🇵🇭 PH | 2255 |
| 24 | 🇬🇹 GT | 2199 |
| 25 | 🇰🇷 KR | 2161 |
| 26 | 🇲🇦 MA | 1721 |
| 27 | 🇭🇷 HR | 1646 |
| 28 | 🇲🇪 ME | 1573 |
| 29 | 🇳🇱 NL | 1555 |
| 30 | 🇲🇴 MO | 1461 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3519 |
| 2 | Denver International Airport |  | US | 2827 |
| 3 | Tokyo International Airport |  | JP | 2156 |
| 4 | Guaymaral Airport |  | CO | 2119 |
| 5 | Indira Gandhi International Airport |  | IN | 2088 |
| 6 | Harry Reid International Airport |  | US | 2052 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1868 |
| 8 | Zurich Airport |  | CH | 1809 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1800 |
| 10 | La Aurora Airport |  | GT | 1697 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1577 |
| 12 | Chicago O'Hare International Airport |  | US | 1551 |
| 13 | El Dorado International Airport |  | CO | 1550 |
| 14 | Salt Lake City International Airport |  | US | 1534 |
| 15 | Frankfurt am Main International Airport |  | DE | 1527 |
| 16 | Macau International Airport |  | MO | 1461 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1403 |
| 18 | Congonhas Airport |  | BR | 1399 |
| 19 | Madrid Barajas International Airport |  | ES | 1341 |
| 20 | Capua Airport |  | IT | 1336 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1291 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1207 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1193 |
| 24 | Charlotte/Douglas International Airport |  | US | 1186 |
| 25 | Charles de Gaulle International Airport |  | FR | 1160 |
| 26 | Malpensa International Airport |  | IT | 1153 |
| 27 | Kuala Lumpur International Airport |  | MY | 1151 |
| 28 | Bengaluru International Airport |  | IN | 1120 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1062 |
| 30 | Ninoy Aquino International Airport |  | PH | 1061 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1054 |
| 32 | Barcelona International Airport |  | ES | 1012 |
| 33 | Daniel K Inouye International Airport |  | US | 992 |
| 34 | Seattle-Tacoma International Airport |  | US | 987 |
| 35 | Viracopos International Airport |  | BR | 970 |
| 36 | Calgary International Airport |  | CA | 969 |
| 37 | Reno/Tahoe International Airport |  | US | 962 |
| 38 | Oslo Gardermoen Airport |  | NO | 954 |
| 39 | Tenerife Norte Airport |  | ES | 951 |
| 40 | Scottsdale Airport |  | US | 940 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 878 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 625 | 21m | 244 km | 2,631.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 405 | 24m | 225 km | 1,571.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 405 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 387 | 1h 8m | 770 km | 5,141.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 318 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 256 | 44m | 241 km | 1,063.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 255 | 22m | 55 km | 242.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 235 | 1h 47m | 1,423 km | 5,767.3 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 222 | 26m | 215 km | 822.2 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 218 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 203 | 1h 15m | 961 km | 3,364.8 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 203 | 50m | 556 km | 1,945.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 24 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 199 | 12m | - | - |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 194 | 1h 38m | 1,156 km | 3,870.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 188 | 24m | 218 km | 708.3 t |
| 29 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 188 | 8m | - | - |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 186 | 1h 1m | 695 km | 2,229.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N508TJ |  | NY40 (NY40) | Fort Erie Airport (CNJ3) | 2026-08-04 19:36 UTC | 2026-08-04 19:49 UTC | 12m |
| GIZMO11 | GIZ | 75OK (75OK) | Cherokee Municipal Airport (K4O5) | 2026-08-04 19:23 UTC | 2026-08-04 19:46 UTC | 22m |
| N42AA |  | Muskeget Island Airport (MA55) | Provincetown Municipal Airport (KPVC) | 2026-08-04 19:25 UTC | 2026-08-04 19:42 UTC | 17m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-08-04 19:28 UTC | 2026-08-04 19:41 UTC | 13m |
| FLC72 | FLC | Cecil Ranch Airport (37CN) | Truckee-Tahoe Airport (KTRK) | 2026-08-04 19:04 UTC | 2026-08-04 19:38 UTC | 34m |
| SWR259T | Swiss International | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Zurich Airport (LSZH) | 2026-08-04 18:31 UTC | 2026-08-04 19:37 UTC | 1h 6m |
| CXK674 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-04 18:44 UTC | 2026-08-04 19:34 UTC | 50m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-04 18:57 UTC | 2026-08-04 19:34 UTC | 36m |
| N252AH |  | Oak Lake Air Strip (MN42) | Fosston Municipal/Anderson Field (KFSE) | 2026-08-04 19:21 UTC | 2026-08-04 19:25 UTC | 4m |
| N275MG |  | Santa Barbara Municipal Airport (KSBA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-08-04 17:59 UTC | 2026-08-04 19:24 UTC | 1h 24m |
| ENSA47 | ENS | Santa Paula Airport (SISP) | Mirassol Airport (SDMH) | 2026-08-04 19:11 UTC | 2026-08-04 19:23 UTC | 11m |
| WMT5454 | WMT | Venezia / Tessera -  Marco Polo Airport (LIPZ) | UGMS (UGMS) | 2026-08-04 16:15 UTC | 2026-08-04 19:22 UTC | 3h 6m |
| N38BL |  | John F Kennedy International Airport (KJFK) | John F Kennedy International Airport (KJFK) | 2026-08-04 18:47 UTC | 2026-08-04 19:14 UTC | 26m |
| N383TA |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-04 18:29 UTC | 2026-08-04 19:09 UTC | 40m |
| SFE1 | SFE | Bud Dryden Airport (TX05) | Crosswinds Airfield (TE96) | 2026-08-04 18:58 UTC | 2026-08-04 19:08 UTC | 9m |
| RYR3QK | Ryanair | Melsbroek Air Base (EBMB) | Dublin Airport (EIDW) | 2026-08-04 17:47 UTC | 2026-08-04 19:07 UTC | 1h 19m |
| SLG3 | SLG | Saskatoon John G. Diefenbaker International Airport (CYXE) | Dore Lake Airport (CJE2) | 2026-08-04 18:28 UTC | 2026-08-04 19:06 UTC | 38m |
| ANE80FD | ANE | Madrid Barajas International Airport (LEMD) | Jayena Airport (LE84) | 2026-08-04 18:36 UTC | 2026-08-04 19:06 UTC | 29m |
| G20634 |  | Capital City Airport (KFFT) | Capital City Airport (KFFT) | 2026-08-04 19:05 UTC | 2026-08-04 19:05 UTC | 0m |
| R20792 |  | John Nichol's Field (0CL3) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-04 18:46 UTC | 2026-08-04 19:05 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

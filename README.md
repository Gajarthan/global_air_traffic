# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_16:13:52_UTC-green)

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

**Latest saved flight:** 2026-08-01 16:13:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 16:13:52 UTC

- **164,833** saved flights
- **54,156** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **164,833** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,981,526.9 tonnes** estimated CO2 emissions
- **114,871,125 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6585 |
| 2 | SkyWest Airlines | 5992 |
| 3 | EJA | 3265 |
| 4 | IndiGo | 2905 |
| 5 | American Airlines | 2595 |
| 6 | Southwest Airlines | 2584 |
| 7 | ENY | 2047 |
| 8 | Delta Air Lines | 1963 |
| 9 | LATAM Airlines | 1537 |
| 10 | Lufthansa | 1535 |
| 11 | AZU | 1448 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1362 |
| 14 | LXJ | 1277 |
| 15 | AXM | 1141 |
| 16 | Swiss International | 1131 |
| 17 | easyJet | 1082 |
| 18 | Alaska Airlines | 1017 |
| 19 | QLK | 1011 |
| 20 | All Nippon Airways | 1009 |
| 21 | EJU | 1006 |
| 22 | VIV | 908 |
| 23 | CXK | 883 |
| 24 | Cathay Pacific | 876 |
| 25 | United Airlines | 866 |
| 26 | GLO | 864 |
| 27 | AEE | 863 |
| 28 | Air France | 851 |
| 29 | MXY | 851 |
| 30 | JetBlue | 839 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 142208 |
| 2 | 🇪🇸 ES | 10553 |
| 3 | 🇧🇷 BR | 9402 |
| 4 | 🇦🇺 AU | 9259 |
| 5 | 🇮🇳 IN | 9121 |
| 6 | 🇨🇦 CA | 8955 |
| 7 | 🇮🇹 IT | 8508 |
| 8 | 🇩🇪 DE | 8262 |
| 9 | 🇬🇧 GB | 7590 |
| 10 | 🇯🇵 JP | 6659 |
| 11 | 🇫🇷 FR | 6538 |
| 12 | 🇨🇴 CO | 5931 |
| 13 | 🇬🇷 GR | 4745 |
| 14 | 🇲🇽 MX | 4717 |
| 15 | 🇨🇭 CH | 4341 |
| 16 | 🇳🇴 NO | 4339 |
| 17 | 🇹🇷 TR | 3949 |
| 18 | 🇲🇾 MY | 2967 |
| 19 | 🇵🇱 PL | 2801 |
| 20 | 🇿🇦 ZA | 2687 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2368 |
| 23 | 🇵🇭 PH | 2172 |
| 24 | 🇬🇹 GT | 2135 |
| 25 | 🇰🇷 KR | 2132 |
| 26 | 🇲🇦 MA | 1662 |
| 27 | 🇭🇷 HR | 1556 |
| 28 | 🇲🇪 ME | 1543 |
| 29 | 🇳🇱 NL | 1498 |
| 30 | 🇲🇴 MO | 1399 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3362 |
| 2 | Denver International Airport |  | US | 2732 |
| 3 | Tokyo International Airport |  | JP | 2095 |
| 4 | Guaymaral Airport |  | CO | 2079 |
| 5 | Indira Gandhi International Airport |  | IN | 2018 |
| 6 | Harry Reid International Airport |  | US | 1992 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1813 |
| 8 | Zurich Airport |  | CH | 1756 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1730 |
| 10 | La Aurora Airport |  | GT | 1652 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1524 |
| 12 | El Dorado International Airport |  | CO | 1512 |
| 13 | Frankfurt am Main International Airport |  | DE | 1494 |
| 14 | Chicago O'Hare International Airport |  | US | 1485 |
| 15 | Salt Lake City International Airport |  | US | 1479 |
| 16 | Macau International Airport |  | MO | 1399 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1380 |
| 18 | Congonhas Airport |  | BR | 1362 |
| 19 | Madrid Barajas International Airport |  | ES | 1301 |
| 20 | Capua Airport |  | IT | 1289 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1253 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1165 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 24 | Charlotte/Douglas International Airport |  | US | 1155 |
| 25 | Charles de Gaulle International Airport |  | FR | 1124 |
| 26 | Kuala Lumpur International Airport |  | MY | 1124 |
| 27 | Malpensa International Airport |  | IT | 1094 |
| 28 | Bengaluru International Airport |  | IN | 1081 |
| 29 | Ninoy Aquino International Airport |  | PH | 1021 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1008 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1008 |
| 32 | Barcelona International Airport |  | ES | 975 |
| 33 | Daniel K Inouye International Airport |  | US | 960 |
| 34 | Seattle-Tacoma International Airport |  | US | 952 |
| 35 | Calgary International Airport |  | CA | 938 |
| 36 | Viracopos International Airport |  | BR | 936 |
| 37 | Scottsdale Airport |  | US | 920 |
| 38 | Tenerife Norte Airport |  | ES | 919 |
| 39 | Oslo Gardermoen Airport |  | NO | 918 |
| 40 | Reno/Tahoe International Airport |  | US | 903 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 598 | 21m | 244 km | 2,518.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 396 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 377 | 1h 9m | 770 km | 5,008.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 308 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 250 | 22m | 55 km | 237.6 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 242 | 19m | 165 km | 688.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 226 | 1h 47m | 1,423 km | 5,546.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 213 | 20m | 250 km | 920.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 202 | 31m | 49 km | 170.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 196 | 1h 15m | 961 km | 3,248.8 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 194 | 19m | 144 km | 482.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 191 | 31m | 369 km | 1,215.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 188 | 50m | 556 km | 1,802.1 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 184 | 1h 39m | 1,156 km | 3,670.7 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PCM8713 | PCM | Santa Barbara Municipal Airport (KSBA) | Ontario International Airport (KONT) | 2026-08-01 15:25 UTC | 2026-08-01 16:13 UTC | 48m |
| RPA4635 | Republic Airways | Poolsbrook Aerodrome (NY72) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-01 15:25 UTC | 2026-08-01 16:11 UTC | 46m |
| LCO3606 | LCO | Miami International Airport (KMIA) | Brussels Airport (EBBR) | 2026-08-01 07:39 UTC | 2026-08-01 16:07 UTC | 8h 28m |
| CRK337 | CRK | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-08-01 13:33 UTC | 2026-08-01 16:05 UTC | 2h 31m |
| PIZ64 | PIZ | La Mole Airport (LFTZ) | Samedan Airport (LSZS) | 2026-08-01 14:50 UTC | 2026-08-01 16:04 UTC | 1h 14m |
| CPA3132 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-08-01 10:56 UTC | 2026-08-01 16:03 UTC | 5h 6m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-01 15:29 UTC | 2026-08-01 16:01 UTC | 31m |
| QTR8082 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-08-01 08:02 UTC | 2026-08-01 15:59 UTC | 7h 57m |
| N6548J |  | David Wayne Hooks Memorial Airport (KDWH) | Brenham Municipal Airport (K11R) | 2026-08-01 15:13 UTC | 2026-08-01 15:58 UTC | 45m |
| CKS703 | CKS | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-08-01 06:56 UTC | 2026-08-01 15:57 UTC | 9h 0m |
| N141DZ |  | Warrenton/Fauquier Airport (KHWY) | Flying Circus Aerodrome (3VA3) | 2026-08-01 15:30 UTC | 2026-08-01 15:56 UTC | 26m |
| GPJCD | GPJ | Norwich International Airport (EGSH) | Norwich International Airport (EGSH) | 2026-08-01 15:43 UTC | 2026-08-01 15:54 UTC | 10m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-08-01 15:41 UTC | 2026-08-01 15:50 UTC | 9m |
| N407MZ |  | Santa Fe Regional Airport (KSAF) | Albuquerque International Sunport Airport (KABQ) | 2026-08-01 15:35 UTC | 2026-08-01 15:50 UTC | 14m |
| N8929W |  | 2XS4 (2XS4) | Dreamland Airport (XA48) | 2026-08-01 15:18 UTC | 2026-08-01 15:48 UTC | 29m |
| TGRWC | TGR | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-08-01 15:24 UTC | 2026-08-01 15:47 UTC | 23m |
| N1971X |  | Double Eagle Ii Airport (KAEG) | Los Alamos Airport (KLAM) | 2026-08-01 15:21 UTC | 2026-08-01 15:47 UTC | 26m |
| SPMOC | SPM | Nowy Sącz-Łososina Dolna Airport  (EPNL) | Nowy Sącz-Łososina Dolna Airport  (EPNL) | 2026-08-01 15:35 UTC | 2026-08-01 15:46 UTC | 11m |
| N5136C |  | Lebanon Municipal Airport (KLEB) | Lebanon Municipal Airport (KLEB) | 2026-08-01 15:40 UTC | 2026-08-01 15:45 UTC | 5m |
| N2353H |  | 50NM (50NM) | Santa Fe Regional Airport (KSAF) | 2026-08-01 15:15 UTC | 2026-08-01 15:45 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

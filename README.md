# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_14:32:45_UTC-green)

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

**Latest saved flight:** 2026-07-31 14:32:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 14:32:45 UTC

- **162,461** saved flights
- **53,557** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **162,461** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,949,418.2 tonnes** estimated CO2 emissions
- **113,009,748 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6488 |
| 2 | SkyWest Airlines | 5911 |
| 3 | EJA | 3213 |
| 4 | IndiGo | 2850 |
| 5 | American Airlines | 2563 |
| 6 | Southwest Airlines | 2540 |
| 7 | ENY | 2019 |
| 8 | Delta Air Lines | 1929 |
| 9 | Lufthansa | 1528 |
| 10 | LATAM Airlines | 1527 |
| 11 | AZU | 1428 |
| 12 | WIF | 1372 |
| 13 | Vueling | 1348 |
| 14 | LXJ | 1262 |
| 15 | AXM | 1131 |
| 16 | Swiss International | 1118 |
| 17 | easyJet | 1069 |
| 18 | Alaska Airlines | 1007 |
| 19 | QLK | 1003 |
| 20 | EJU | 1000 |
| 21 | All Nippon Airways | 999 |
| 22 | VIV | 895 |
| 23 | CXK | 868 |
| 24 | Cathay Pacific | 856 |
| 25 | United Airlines | 855 |
| 26 | GLO | 852 |
| 27 | AEE | 851 |
| 28 | Air France | 841 |
| 29 | MXY | 840 |
| 30 | JetBlue | 828 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 140179 |
| 2 | 🇪🇸 ES | 10413 |
| 3 | 🇧🇷 BR | 9292 |
| 4 | 🇦🇺 AU | 9200 |
| 5 | 🇮🇳 IN | 8962 |
| 6 | 🇨🇦 CA | 8823 |
| 7 | 🇮🇹 IT | 8377 |
| 8 | 🇩🇪 DE | 8190 |
| 9 | 🇬🇧 GB | 7467 |
| 10 | 🇯🇵 JP | 6587 |
| 11 | 🇫🇷 FR | 6430 |
| 12 | 🇨🇴 CO | 5783 |
| 13 | 🇬🇷 GR | 4665 |
| 14 | 🇲🇽 MX | 4656 |
| 15 | 🇳🇴 NO | 4289 |
| 16 | 🇨🇭 CH | 4274 |
| 17 | 🇹🇷 TR | 3878 |
| 18 | 🇲🇾 MY | 2938 |
| 19 | 🇵🇱 PL | 2763 |
| 20 | 🇿🇦 ZA | 2641 |
| 21 | 🇳🇿 NZ | 2383 |
| 22 | 🇹🇭 TH | 2316 |
| 23 | 🇵🇭 PH | 2134 |
| 24 | 🇰🇷 KR | 2119 |
| 25 | 🇬🇹 GT | 2082 |
| 26 | 🇲🇦 MA | 1637 |
| 27 | 🇲🇪 ME | 1532 |
| 28 | 🇭🇷 HR | 1521 |
| 29 | 🇳🇱 NL | 1483 |
| 30 | 🇲🇴 MO | 1360 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3314 |
| 2 | Denver International Airport |  | US | 2696 |
| 3 | Tokyo International Airport |  | JP | 2076 |
| 4 | Guaymaral Airport |  | CO | 2043 |
| 5 | Indira Gandhi International Airport |  | IN | 1993 |
| 6 | Harry Reid International Airport |  | US | 1970 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1793 |
| 8 | Zurich Airport |  | CH | 1735 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1706 |
| 10 | La Aurora Airport |  | GT | 1616 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1507 |
| 12 | El Dorado International Airport |  | CO | 1484 |
| 13 | Frankfurt am Main International Airport |  | DE | 1481 |
| 14 | Chicago O'Hare International Airport |  | US | 1468 |
| 15 | Salt Lake City International Airport |  | US | 1458 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1361 |
| 17 | Macau International Airport |  | MO | 1360 |
| 18 | Congonhas Airport |  | BR | 1348 |
| 19 | Madrid Barajas International Airport |  | ES | 1282 |
| 20 | Capua Airport |  | IT | 1275 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1239 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1152 |
| 24 | Charlotte/Douglas International Airport |  | US | 1140 |
| 25 | Kuala Lumpur International Airport |  | MY | 1118 |
| 26 | Charles de Gaulle International Airport |  | FR | 1108 |
| 27 | Malpensa International Airport |  | IT | 1075 |
| 28 | Bengaluru International Airport |  | IN | 1063 |
| 29 | Ninoy Aquino International Airport |  | PH | 1002 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 993 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 984 |
| 32 | Barcelona International Airport |  | ES | 963 |
| 33 | Daniel K Inouye International Airport |  | US | 953 |
| 34 | Seattle-Tacoma International Airport |  | US | 942 |
| 35 | Calgary International Airport |  | CA | 928 |
| 36 | Viracopos International Airport |  | BR | 926 |
| 37 | Tenerife Norte Airport |  | ES | 911 |
| 38 | Scottsdale Airport |  | US | 910 |
| 39 | Oslo Gardermoen Airport |  | NO | 907 |
| 40 | Reno/Tahoe International Airport |  | US | 890 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 857 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 591 | 21m | 244 km | 2,488.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 387 | 24m | 225 km | 1,501.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 387 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 300 | 32m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 239 | 22m | 55 km | 227.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 236 | 44m | 241 km | 980.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 206 | 20m | 250 km | 889.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 205 | 20m | 99 km | 351.1 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 198 | 30m | 49 km | 167.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 194 | 1h 15m | 961 km | 3,215.7 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 194 | 28m | 152 km | 507.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 191 | 18m | 144 km | 475.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 180 | 1h 1m | 695 km | 2,157.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 49m | 1,304 km | 3,914.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GCPSS | GCP | Netheravon Airfield (EGDN) | Netheravon Airfield (EGDN) | 2026-07-31 14:17 UTC | 2026-07-31 14:32 UTC | 15m |
| DEGBD | DEG | Schonhagen Airport (EDAZ) | Oehna Airport (EDBO) | 2026-07-31 14:09 UTC | 2026-07-31 14:27 UTC | 18m |
| QTR816 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-07-31 06:52 UTC | 2026-07-31 14:23 UTC | 7h 31m |
| SAMU13 | SAM | Salon-de-Provence (BA 701) Air Base (LFMY) | Marseille Provence Airport (LFML) | 2026-07-31 14:03 UTC | 2026-07-31 14:19 UTC | 15m |
| UAE9774 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-07-31 03:09 UTC | 2026-07-31 14:17 UTC | 11h 8m |
| ENSAIO97 | ENS | Ibiporanga da Felicidade Airport (SJVC) | Mirassol Airport (SDMH) | 2026-07-31 13:37 UTC | 2026-07-31 14:14 UTC | 36m |
| C2310 |  | 26AL (26AL) | Garcon Field (24FL) | 2026-07-31 13:45 UTC | 2026-07-31 14:12 UTC | 27m |
| N4347K |  | Cambridge-Dorchester Regional Airport (KCGE) | Easton/Newnam Field (KESN) | 2026-07-31 13:45 UTC | 2026-07-31 14:12 UTC | 26m |
| MESSY16 | MES | Cairns Army Air Field (Fort Rucker) Airport (KOZR) | Montgomery Regional (Dannelly Field) Airport (KMGM) | 2026-07-31 12:58 UTC | 2026-07-31 14:09 UTC | 1h 10m |
| AUB1747 | AUB | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-07-31 13:43 UTC | 2026-07-31 14:07 UTC | 24m |
| BPX202 | BPX | Cobb County International/Mccollum Field (KRYY) | Cobb County International/Mccollum Field (KRYY) | 2026-07-31 13:38 UTC | 2026-07-31 14:07 UTC | 29m |
| SCX253 | SCX | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-31 11:42 UTC | 2026-07-31 14:07 UTC | 2h 24m |
| N739DB |  | Melbourne Orlando International Airport (KMLB) | Valkaria Airport (KX59) | 2026-07-31 13:21 UTC | 2026-07-31 14:01 UTC | 39m |
| HK1479G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-31 13:55 UTC | 2026-07-31 14:00 UTC | 5m |
| MTN8310 | MTN | Newark Liberty International Airport (KEWR) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-31 12:45 UTC | 2026-07-31 14:00 UTC | 1h 14m |
| N70075 |  | Bolinder Field/Tooele Valley Airport (KTVY) | UT99 (UT99) | 2026-07-31 13:34 UTC | 2026-07-31 13:59 UTC | 25m |
| N472AT |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-31 13:35 UTC | 2026-07-31 13:59 UTC | 23m |
| N239ST |  | Dugger Field (0FD3) | Vero Beach Regional Airport (KVRB) | 2026-07-31 11:44 UTC | 2026-07-31 13:57 UTC | 2h 12m |
|  |  | Cambridge-Dorchester Regional Airport (KCGE) | Cambridge-Dorchester Regional Airport (KCGE) | 2026-07-31 13:55 UTC | 2026-07-31 13:56 UTC | 0m |
| 5YSLQ |  | Nairobi Wilson Airport (HKNW) | HKMG (HKMG) | 2026-07-31 13:38 UTC | 2026-07-31 13:55 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

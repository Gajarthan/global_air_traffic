# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_10:01:08_UTC-green)

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

**Latest saved flight:** 2026-07-31 10:01:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 10:01:08 UTC

- **162,122** saved flights
- **53,457** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **162,122** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,945,540.1 tonnes** estimated CO2 emissions
- **112,784,936 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6477 |
| 2 | SkyWest Airlines | 5910 |
| 3 | EJA | 3210 |
| 4 | IndiGo | 2840 |
| 5 | American Airlines | 2562 |
| 6 | Southwest Airlines | 2539 |
| 7 | ENY | 2018 |
| 8 | Delta Air Lines | 1925 |
| 9 | Lufthansa | 1527 |
| 10 | LATAM Airlines | 1523 |
| 11 | AZU | 1423 |
| 12 | WIF | 1370 |
| 13 | Vueling | 1344 |
| 14 | LXJ | 1261 |
| 15 | AXM | 1127 |
| 16 | Swiss International | 1114 |
| 17 | easyJet | 1060 |
| 18 | Alaska Airlines | 1007 |
| 19 | QLK | 1003 |
| 20 | All Nippon Airways | 998 |
| 21 | EJU | 998 |
| 22 | VIV | 892 |
| 23 | CXK | 865 |
| 24 | Cathay Pacific | 856 |
| 25 | United Airlines | 855 |
| 26 | AEE | 850 |
| 27 | GLO | 850 |
| 28 | Air France | 841 |
| 29 | MXY | 840 |
| 30 | JetBlue | 827 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 140011 |
| 2 | 🇪🇸 ES | 10381 |
| 3 | 🇧🇷 BR | 9254 |
| 4 | 🇦🇺 AU | 9200 |
| 5 | 🇮🇳 IN | 8940 |
| 6 | 🇨🇦 CA | 8815 |
| 7 | 🇮🇹 IT | 8355 |
| 8 | 🇩🇪 DE | 8169 |
| 9 | 🇬🇧 GB | 7429 |
| 10 | 🇯🇵 JP | 6573 |
| 11 | 🇫🇷 FR | 6412 |
| 12 | 🇨🇴 CO | 5756 |
| 13 | 🇬🇷 GR | 4656 |
| 14 | 🇲🇽 MX | 4651 |
| 15 | 🇳🇴 NO | 4279 |
| 16 | 🇨🇭 CH | 4256 |
| 17 | 🇹🇷 TR | 3866 |
| 18 | 🇲🇾 MY | 2927 |
| 19 | 🇵🇱 PL | 2752 |
| 20 | 🇿🇦 ZA | 2621 |
| 21 | 🇳🇿 NZ | 2383 |
| 22 | 🇹🇭 TH | 2300 |
| 23 | 🇵🇭 PH | 2132 |
| 24 | 🇰🇷 KR | 2115 |
| 25 | 🇬🇹 GT | 2077 |
| 26 | 🇲🇦 MA | 1631 |
| 27 | 🇲🇪 ME | 1530 |
| 28 | 🇭🇷 HR | 1513 |
| 29 | 🇳🇱 NL | 1481 |
| 30 | 🇲🇴 MO | 1357 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3312 |
| 2 | Denver International Airport |  | US | 2694 |
| 3 | Tokyo International Airport |  | JP | 2074 |
| 4 | Guaymaral Airport |  | CO | 2035 |
| 5 | Indira Gandhi International Airport |  | IN | 1990 |
| 6 | Harry Reid International Airport |  | US | 1968 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1790 |
| 8 | Zurich Airport |  | CH | 1728 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1703 |
| 10 | La Aurora Airport |  | GT | 1613 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1507 |
| 12 | El Dorado International Airport |  | CO | 1483 |
| 13 | Frankfurt am Main International Airport |  | DE | 1476 |
| 14 | Chicago O'Hare International Airport |  | US | 1468 |
| 15 | Salt Lake City International Airport |  | US | 1458 |
| 16 | Macau International Airport |  | MO | 1357 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1353 |
| 18 | Congonhas Airport |  | BR | 1345 |
| 19 | Madrid Barajas International Airport |  | ES | 1280 |
| 20 | Capua Airport |  | IT | 1274 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1238 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1149 |
| 24 | Charlotte/Douglas International Airport |  | US | 1140 |
| 25 | Kuala Lumpur International Airport |  | MY | 1115 |
| 26 | Charles de Gaulle International Airport |  | FR | 1108 |
| 27 | Malpensa International Airport |  | IT | 1071 |
| 28 | Bengaluru International Airport |  | IN | 1061 |
| 29 | Ninoy Aquino International Airport |  | PH | 1001 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 991 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 984 |
| 32 | Barcelona International Airport |  | ES | 961 |
| 33 | Daniel K Inouye International Airport |  | US | 953 |
| 34 | Seattle-Tacoma International Airport |  | US | 942 |
| 35 | Calgary International Airport |  | CA | 928 |
| 36 | Viracopos International Airport |  | BR | 922 |
| 37 | Tenerife Norte Airport |  | ES | 908 |
| 38 | Scottsdale Airport |  | US | 908 |
| 39 | Oslo Gardermoen Airport |  | NO | 903 |
| 40 | Reno/Tahoe International Airport |  | US | 889 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 853 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 591 | 21m | 244 km | 2,488.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 387 | 24m | 225 km | 1,501.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 387 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 372 | 1h 9m | 770 km | 4,941.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 298 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 283 | 27m | 275 km | 1,341.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 239 | 22m | 55 km | 227.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 238 | 19m | 165 km | 677.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 234 | 44m | 241 km | 972.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 205 | 20m | 250 km | 885.5 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 204 | 20m | 99 km | 349.4 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 198 | 30m | 49 km | 167.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 193 | 1h 15m | 961 km | 3,199.1 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 193 | 28m | 152 km | 504.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 191 | 18m | 144 km | 475.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 180 | 1h 1m | 695 km | 2,157.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 49m | 1,304 km | 3,892.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SWR4TL | Swiss International | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Zurich Airport (LSZH) | 2026-07-31 08:51 UTC | 2026-07-31 10:01 UTC | 1h 9m |
| JJP519 | JJP | Narita International Airport (RJAA) | Ashiya Airport (RJFA) | 2026-07-31 08:41 UTC | 2026-07-31 09:56 UTC | 1h 14m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-07-30 19:21 UTC | 2026-07-31 09:56 UTC | 14h 34m |
| GTI612 | GTI | Noi Bai International Airport (VVNB) | Macau International Airport (VMMC) | 2026-07-31 08:39 UTC | 2026-07-31 09:42 UTC | 1h 2m |
| ZKIDU | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-07-31 09:28 UTC | 2026-07-31 09:41 UTC | 12m |
| UAE382 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-07-31 02:50 UTC | 2026-07-31 09:41 UTC | 6h 51m |
| HBZYO | HBZ | Speck-Fehraltorf Airport (LSZK) | Wangen-Lachen Airport (LSPV) | 2026-07-31 09:27 UTC | 2026-07-31 09:39 UTC | 12m |
| COTOS61 | COT | El Berriel Aeroc Airport (GCLB) | Hierro Airport (GCHI) | 2026-07-31 08:52 UTC | 2026-07-31 09:36 UTC | 44m |
| YGN | YGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-31 08:54 UTC | 2026-07-31 09:31 UTC | 36m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-07-31 09:17 UTC | 2026-07-31 09:27 UTC | 10m |
| HBZNH | HBZ | St Stephan Airport (LSTS) | Bern Belp Airport (LSZB) | 2026-07-31 08:29 UTC | 2026-07-31 09:26 UTC | 57m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-07-30 22:01 UTC | 2026-07-31 09:22 UTC | 11h 20m |
| DAL2061 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-07-31 06:24 UTC | 2026-07-31 09:21 UTC | 2h 57m |
| N54DD |  | Harry Reid International Airport (KLAS) | San Francisco International Airport (KSFO) | 2026-07-31 08:07 UTC | 2026-07-31 09:15 UTC | 1h 7m |
| KLM1303 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-07-31 07:56 UTC | 2026-07-31 09:14 UTC | 1h 17m |
| AFL1963 | AFL | Maksimovka Airport (UWUM) | Sheremetyevo International Airport (UUEE) | 2026-07-30 16:03 UTC | 2026-07-31 09:08 UTC | 17h 5m |
| TZ8 |  | Castellón De La Plana Airport (LECN) | Castellón De La Plana Airport (LECN) | 2026-07-31 09:04 UTC | 2026-07-31 09:08 UTC | 4m |
| AFR45LB | Air France | Charles de Gaulle International Airport (LFPG) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-07-31 08:12 UTC | 2026-07-31 09:06 UTC | 53m |
| CSN382 | China Southern | Brisbane International Airport (YBBN) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-07-31 00:23 UTC | 2026-07-31 09:03 UTC | 8h 40m |
| QTR8422 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-07-31 01:18 UTC | 2026-07-31 09:03 UTC | 7h 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

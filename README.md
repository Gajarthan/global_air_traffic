# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_21:50:32_UTC-green)

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

**Latest saved flight:** 2026-08-02 21:50:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 21:50:32 UTC

- **167,808** saved flights
- **54,881** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **167,808** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,022,918.8 tonnes** estimated CO2 emissions
- **117,270,656 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6700 |
| 2 | SkyWest Airlines | 6122 |
| 3 | EJA | 3338 |
| 4 | IndiGo | 2952 |
| 5 | American Airlines | 2649 |
| 6 | Southwest Airlines | 2640 |
| 7 | ENY | 2090 |
| 8 | Delta Air Lines | 2004 |
| 9 | LATAM Airlines | 1554 |
| 10 | Lufthansa | 1543 |
| 11 | AZU | 1475 |
| 12 | WIF | 1401 |
| 13 | Vueling | 1383 |
| 14 | LXJ | 1316 |
| 15 | AXM | 1154 |
| 16 | Swiss International | 1151 |
| 17 | easyJet | 1130 |
| 18 | EJU | 1033 |
| 19 | Alaska Airlines | 1029 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1017 |
| 22 | VIV | 924 |
| 23 | Cathay Pacific | 893 |
| 24 | CXK | 892 |
| 25 | United Airlines | 887 |
| 26 | GLO | 881 |
| 27 | AEE | 880 |
| 28 | Air France | 865 |
| 29 | MXY | 863 |
| 30 | JetBlue | 847 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 144738 |
| 2 | 🇪🇸 ES | 10757 |
| 3 | 🇧🇷 BR | 9552 |
| 4 | 🇦🇺 AU | 9344 |
| 5 | 🇮🇳 IN | 9255 |
| 6 | 🇨🇦 CA | 9097 |
| 7 | 🇮🇹 IT | 8673 |
| 8 | 🇩🇪 DE | 8368 |
| 9 | 🇬🇧 GB | 7798 |
| 10 | 🇯🇵 JP | 6740 |
| 11 | 🇫🇷 FR | 6660 |
| 12 | 🇨🇴 CO | 6046 |
| 13 | 🇬🇷 GR | 4878 |
| 14 | 🇲🇽 MX | 4798 |
| 15 | 🇨🇭 CH | 4417 |
| 16 | 🇳🇴 NO | 4385 |
| 17 | 🇹🇷 TR | 4060 |
| 18 | 🇲🇾 MY | 3009 |
| 19 | 🇵🇱 PL | 2830 |
| 20 | 🇿🇦 ZA | 2723 |
| 21 | 🇳🇿 NZ | 2434 |
| 22 | 🇹🇭 TH | 2424 |
| 23 | 🇵🇭 PH | 2211 |
| 24 | 🇬🇹 GT | 2171 |
| 25 | 🇰🇷 KR | 2147 |
| 26 | 🇲🇦 MA | 1702 |
| 27 | 🇭🇷 HR | 1608 |
| 28 | 🇲🇪 ME | 1552 |
| 29 | 🇳🇱 NL | 1527 |
| 30 | 🇲🇴 MO | 1426 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3446 |
| 2 | Denver International Airport |  | US | 2789 |
| 3 | Tokyo International Airport |  | JP | 2117 |
| 4 | Guaymaral Airport |  | CO | 2092 |
| 5 | Indira Gandhi International Airport |  | IN | 2050 |
| 6 | Harry Reid International Airport |  | US | 2018 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1841 |
| 8 | Zurich Airport |  | CH | 1786 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1764 |
| 10 | La Aurora Airport |  | GT | 1677 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1547 |
| 12 | Chicago O'Hare International Airport |  | US | 1522 |
| 13 | El Dorado International Airport |  | CO | 1521 |
| 14 | Frankfurt am Main International Airport |  | DE | 1510 |
| 15 | Salt Lake City International Airport |  | US | 1504 |
| 16 | Macau International Airport |  | MO | 1426 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1393 |
| 18 | Congonhas Airport |  | BR | 1377 |
| 19 | Madrid Barajas International Airport |  | ES | 1324 |
| 20 | Capua Airport |  | IT | 1307 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1276 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1183 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1176 |
| 24 | Charlotte/Douglas International Airport |  | US | 1170 |
| 25 | Charles de Gaulle International Airport |  | FR | 1144 |
| 26 | Kuala Lumpur International Airport |  | MY | 1137 |
| 27 | Malpensa International Airport |  | IT | 1129 |
| 28 | Bengaluru International Airport |  | IN | 1096 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1039 |
| 30 | Ninoy Aquino International Airport |  | PH | 1039 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1030 |
| 32 | Barcelona International Airport |  | ES | 990 |
| 33 | Daniel K Inouye International Airport |  | US | 977 |
| 34 | Seattle-Tacoma International Airport |  | US | 974 |
| 35 | Viracopos International Airport |  | BR | 955 |
| 36 | Calgary International Airport |  | CA | 948 |
| 37 | Tenerife Norte Airport |  | ES | 937 |
| 38 | Reno/Tahoe International Airport |  | US | 932 |
| 39 | Oslo Gardermoen Airport |  | NO | 932 |
| 40 | Scottsdale Airport |  | US | 930 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 870 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 610 | 21m | 244 km | 2,568.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 401 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 316 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 245 | 19m | 165 km | 696.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 244 | 44m | 241 km | 1,013.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 231 | 1h 47m | 1,423 km | 5,669.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 221 | 20m | 250 km | 954.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 218 | 26m | 215 km | 807.4 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 215 | 31m | 49 km | 181.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 199 | 19m | 144 km | 495.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 194 | 31m | 369 km | 1,234.9 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 194 | 50m | 556 km | 1,859.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 193 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 187 | 1h 38m | 1,156 km | 3,730.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 184 | 24m | 218 km | 693.2 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 183 | 1h 1m | 695 km | 2,193.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N508TJ |  | Scott's Sky Ranch Airport (NY70) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-02 21:33 UTC | 2026-08-02 21:50 UTC | 17m |
| EVANS11 | EVA Air | Buckley Space Force Base Airport (KBKF) | Elk Park Ranch Airport (34CD) | 2026-08-02 20:45 UTC | 2026-08-02 21:47 UTC | 1h 1m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-08-02 17:04 UTC | 2026-08-02 21:44 UTC | 4h 39m |
| N3603S |  | Litchfield Municipal Airport (K3LF) | Norfleet Airport (1LL4) | 2026-08-02 21:25 UTC | 2026-08-02 21:42 UTC | 17m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-08-02 10:48 UTC | 2026-08-02 21:39 UTC | 10h 51m |
| TORA21 | TOR | Hutchinson Regional Airport (KHUT) | Medford Municipal Airport (KO53) | 2026-08-02 21:02 UTC | 2026-08-02 21:38 UTC | 36m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-08-02 11:06 UTC | 2026-08-02 21:37 UTC | 10h 30m |
|  |  | 28TS (28TS) | Hidden Valley Airpark (5TX0) | 2026-08-02 21:20 UTC | 2026-08-02 21:37 UTC | 16m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-02 21:22 UTC | 2026-08-02 21:35 UTC | 12m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-08-02 10:43 UTC | 2026-08-02 21:33 UTC | 10h 50m |
| N2043A |  | Martha's Vineyard Airport (KMVY) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-02 20:54 UTC | 2026-08-02 21:29 UTC | 34m |
| UPS504 | UPS | Ted Stevens Anchorage International Airport (PANC) | Eaglesham (South) Airport (CGL4) | 2026-08-02 19:12 UTC | 2026-08-02 21:28 UTC | 2h 15m |
| N23SB |  | Redding Regional Airport (KRDD) | Redding Regional Airport (KRDD) | 2026-08-02 21:05 UTC | 2026-08-02 21:26 UTC | 21m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-08-02 17:32 UTC | 2026-08-02 21:24 UTC | 3h 52m |
| N938GC |  | Laguardia Airport (KLGA) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-02 18:59 UTC | 2026-08-02 21:18 UTC | 2h 18m |
| N119BJ |  | Falcon Field (KFFZ) | Julian Hinds Pump Plant Airstrip (73CL) | 2026-08-02 19:50 UTC | 2026-08-02 21:17 UTC | 1h 27m |
| N341CW |  | Lovell Field (KCHA) | Southwest Florida International Airport (KRSW) | 2026-08-02 19:40 UTC | 2026-08-02 21:15 UTC | 1h 34m |
| LXJ427 | LXJ | North Las Vegas Airport (KVGT) | Van Nuys Airport (KVNY) | 2026-08-02 20:28 UTC | 2026-08-02 21:13 UTC | 45m |
| LXJ387 | LXJ | Oakland San Francisco Bay Airport (KOAK) | Truckee-Tahoe Airport (KTRK) | 2026-08-02 20:37 UTC | 2026-08-02 21:07 UTC | 30m |
| ASP875 | ASP | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-08-02 21:00 UTC | 2026-08-02 21:04 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

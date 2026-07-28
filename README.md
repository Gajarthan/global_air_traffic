# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_08:52:15_UTC-green)

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

**Latest saved flight:** 2026-07-28 08:52:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-28 08:52:15 UTC

- **156,036** saved flights
- **51,880** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **156,036** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,872,736.8 tonnes** estimated CO2 emissions
- **108,564,450 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6273 |
| 2 | SkyWest Airlines | 5725 |
| 3 | EJA | 3095 |
| 4 | IndiGo | 2761 |
| 5 | American Airlines | 2491 |
| 6 | Southwest Airlines | 2458 |
| 7 | ENY | 1950 |
| 8 | Delta Air Lines | 1859 |
| 9 | Lufthansa | 1501 |
| 10 | LATAM Airlines | 1454 |
| 11 | AZU | 1365 |
| 12 | WIF | 1316 |
| 13 | Vueling | 1306 |
| 14 | LXJ | 1199 |
| 15 | AXM | 1101 |
| 16 | Swiss International | 1084 |
| 17 | easyJet | 1017 |
| 18 | Alaska Airlines | 979 |
| 19 | All Nippon Airways | 972 |
| 20 | QLK | 972 |
| 21 | EJU | 956 |
| 22 | VIV | 858 |
| 23 | United Airlines | 836 |
| 24 | CXK | 826 |
| 25 | AEE | 816 |
| 26 | GLO | 816 |
| 27 | MXY | 815 |
| 28 | Cathay Pacific | 813 |
| 29 | JetBlue | 812 |
| 30 | Air France | 807 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134791 |
| 2 | 🇪🇸 ES | 10045 |
| 3 | 🇧🇷 BR | 8899 |
| 4 | 🇦🇺 AU | 8843 |
| 5 | 🇮🇳 IN | 8680 |
| 6 | 🇨🇦 CA | 8409 |
| 7 | 🇮🇹 IT | 8044 |
| 8 | 🇩🇪 DE | 7915 |
| 9 | 🇬🇧 GB | 7147 |
| 10 | 🇯🇵 JP | 6406 |
| 11 | 🇫🇷 FR | 6155 |
| 12 | 🇨🇴 CO | 5409 |
| 13 | 🇲🇽 MX | 4479 |
| 14 | 🇬🇷 GR | 4436 |
| 15 | 🇳🇴 NO | 4116 |
| 16 | 🇨🇭 CH | 4068 |
| 17 | 🇹🇷 TR | 3724 |
| 18 | 🇲🇾 MY | 2869 |
| 19 | 🇵🇱 PL | 2651 |
| 20 | 🇿🇦 ZA | 2518 |
| 21 | 🇳🇿 NZ | 2327 |
| 22 | 🇹🇭 TH | 2245 |
| 23 | 🇰🇷 KR | 2090 |
| 24 | 🇵🇭 PH | 2062 |
| 25 | 🇬🇹 GT | 2012 |
| 26 | 🇲🇦 MA | 1590 |
| 27 | 🇲🇪 ME | 1511 |
| 28 | 🇭🇷 HR | 1433 |
| 29 | 🇳🇱 NL | 1426 |
| 30 | 🇲🇴 MO | 1287 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3211 |
| 2 | Denver International Airport |  | US | 2624 |
| 3 | Tokyo International Airport |  | JP | 2031 |
| 4 | Guaymaral Airport |  | CO | 1955 |
| 5 | Indira Gandhi International Airport |  | IN | 1925 |
| 6 | Harry Reid International Airport |  | US | 1917 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1732 |
| 8 | Zurich Airport |  | CH | 1682 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1636 |
| 10 | La Aurora Airport |  | GT | 1559 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1453 |
| 12 | Frankfurt am Main International Airport |  | DE | 1450 |
| 13 | Chicago O'Hare International Airport |  | US | 1422 |
| 14 | Salt Lake City International Airport |  | US | 1409 |
| 15 | El Dorado International Airport |  | CO | 1409 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1320 |
| 17 | Macau International Airport |  | MO | 1287 |
| 18 | Congonhas Airport |  | BR | 1273 |
| 19 | Madrid Barajas International Airport |  | ES | 1239 |
| 20 | Capua Airport |  | IT | 1229 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1200 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1124 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1109 |
| 24 | Charlotte/Douglas International Airport |  | US | 1106 |
| 25 | Kuala Lumpur International Airport |  | MY | 1099 |
| 26 | Charles de Gaulle International Airport |  | FR | 1065 |
| 27 | Bengaluru International Airport |  | IN | 1034 |
| 28 | Malpensa International Airport |  | IT | 1023 |
| 29 | Ninoy Aquino International Airport |  | PH | 966 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 950 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 944 |
| 32 | Barcelona International Airport |  | ES | 928 |
| 33 | Daniel K Inouye International Airport |  | US | 923 |
| 34 | Seattle-Tacoma International Airport |  | US | 911 |
| 35 | Calgary International Airport |  | CA | 894 |
| 36 | Tenerife Norte Airport |  | ES | 891 |
| 37 | Viracopos International Airport |  | BR | 886 |
| 38 | Scottsdale Airport |  | US | 883 |
| 39 | Amsterdam Airport Schiphol |  | NL | 862 |
| 40 | Oslo Gardermoen Airport |  | NO | 855 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 821 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 562 | 21m | 244 km | 2,366.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 376 | 24m | 225 km | 1,458.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 360 | 1h 9m | 770 km | 4,782.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 288 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 231 | 22m | 55 km | 219.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 215 | 44m | 241 km | 893.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 208 | 1h 47m | 1,423 km | 5,104.6 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 200 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 197 | 20m | 250 km | 850.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 184 | 1h 15m | 961 km | 3,049.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 184 | 18m | 144 km | 457.7 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 182 | 31m | 369 km | 1,158.5 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 176 | 50m | 556 km | 1,687.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 175 | 1h 39m | 1,156 km | 3,491.2 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 1m | 695 km | 2,073.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 50m | 1,304 km | 3,712.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZKICB | ZKI | Ardmore Airport (NZAR) | Ardmore Airport (NZAR) | 2026-07-28 08:35 UTC | 2026-07-28 08:52 UTC | 17m |
| SFJ51 | SFJ | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-07-28 07:37 UTC | 2026-07-28 08:50 UTC | 1h 13m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-07-27 21:41 UTC | 2026-07-28 08:50 UTC | 11h 9m |
| FIAMM01 | FIA | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | LIAT (LIAT) | 2026-07-28 08:21 UTC | 2026-07-28 08:39 UTC | 17m |
| YGU | YGU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-28 08:10 UTC | 2026-07-28 08:33 UTC | 23m |
| HNL24A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-07-28 08:03 UTC | 2026-07-28 08:32 UTC | 29m |
| AHX106 | AHX | Fukuoka Airport (RJFF) | Kumamoto Airport (RJFT) | 2026-07-28 08:18 UTC | 2026-07-28 08:31 UTC | 13m |
| CJT570 | CJT | Winnipeg James Armstrong Richardson International Airport (CYWG) | Montréal (Mirabel) Airport (CYMX) | 2026-07-28 06:13 UTC | 2026-07-28 08:28 UTC | 2h 15m |
| M28A |  | Mengen-Hohentengen Airport (EDTM) | Mengen-Hohentengen Airport (EDTM) | 2026-07-28 08:01 UTC | 2026-07-28 08:23 UTC | 21m |
| ECISV | ECI | Ampuriabrava Airport (LEAP) | Ampuriabrava Airport (LEAP) | 2026-07-28 08:15 UTC | 2026-07-28 08:23 UTC | 7m |
| ANA259 | All Nippon Airways | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-07-28 06:53 UTC | 2026-07-28 08:20 UTC | 1h 26m |
| YOJ | YOJ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-28 07:39 UTC | 2026-07-28 08:17 UTC | 38m |
|  |  | Le Havre Octeville Airport (LFOH) | Le Havre Octeville Airport (LFOH) | 2026-07-28 08:17 UTC | 2026-07-28 08:17 UTC | 0m |
| AHK | AHK | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-07-28 07:24 UTC | 2026-07-28 08:10 UTC | 46m |
| EZY825P | easyJet | Belfast International Airport (EGAA) | Glasgow International Airport (EGPF) | 2026-07-28 07:40 UTC | 2026-07-28 08:09 UTC | 28m |
| RYR49RV | Ryanair | Cologne Bonn Airport (EDDK) | Ireland West Knock Airport (EIKN) | 2026-07-28 06:20 UTC | 2026-07-28 08:06 UTC | 1h 45m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-07-27 20:59 UTC | 2026-07-28 07:55 UTC | 10h 56m |
| JAL323 | Japan Airlines | Tokyo International Airport (RJTT) | Ozuki Airport (RJOZ) | 2026-07-28 06:47 UTC | 2026-07-28 07:52 UTC | 1h 4m |
| RYR7946 | Ryanair | Luqa Airport (LMML) | Otocac Airport (LDRO) | 2026-07-28 06:23 UTC | 2026-07-28 07:51 UTC | 1h 28m |
| HBZYO | HBZ | Speck-Fehraltorf Airport (LSZK) | LSMF (LSMF) | 2026-07-28 07:07 UTC | 2026-07-28 07:51 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

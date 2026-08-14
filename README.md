# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_14:41:22_UTC-green)

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

**Latest saved flight:** 2026-08-14 14:41:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 14:41:22 UTC

- **195,346** saved flights
- **61,421** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **195,346** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,334,256.0 tonnes** estimated CO2 emissions
- **135,319,189 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7777 |
| 2 | SkyWest Airlines | 7017 |
| 3 | EJA | 3838 |
| 4 | IndiGo | 3371 |
| 5 | Southwest Airlines | 3032 |
| 6 | American Airlines | 3016 |
| 7 | ENY | 2410 |
| 8 | Delta Air Lines | 2301 |
| 9 | LATAM Airlines | 1830 |
| 10 | AZU | 1759 |
| 11 | Lufthansa | 1689 |
| 12 | Vueling | 1631 |
| 13 | WIF | 1616 |
| 14 | LXJ | 1545 |
| 15 | easyJet | 1347 |
| 16 | Swiss International | 1324 |
| 17 | AXM | 1277 |
| 18 | EJU | 1209 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1158 |
| 22 | VIV | 1073 |
| 23 | GLO | 1050 |
| 24 | Air France | 1028 |
| 25 | PGT | 1017 |
| 26 | AEE | 1004 |
| 27 | United Airlines | 996 |
| 28 | CXK | 992 |
| 29 | WMT | 978 |
| 30 | Wizz Air | 968 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 165940 |
| 2 | 🇪🇸 ES | 12619 |
| 3 | 🇧🇷 BR | 11214 |
| 4 | 🇦🇺 AU | 11009 |
| 5 | 🇨🇦 CA | 10674 |
| 6 | 🇮🇳 IN | 10551 |
| 7 | 🇮🇹 IT | 10176 |
| 8 | 🇩🇪 DE | 9712 |
| 9 | 🇬🇧 GB | 9198 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7799 |
| 12 | 🇨🇴 CO | 7604 |
| 13 | 🇬🇷 GR | 5743 |
| 14 | 🇲🇽 MX | 5514 |
| 15 | 🇹🇷 TR | 5301 |
| 16 | 🇨🇭 CH | 5292 |
| 17 | 🇳🇴 NO | 5010 |
| 18 | 🇲🇾 MY | 3341 |
| 19 | 🇿🇦 ZA | 3304 |
| 20 | 🇵🇱 PL | 3228 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2589 |
| 24 | 🇬🇹 GT | 2472 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2036 |
| 27 | 🇲🇦 MA | 1983 |
| 28 | 🇳🇱 NL | 1762 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1580 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4055 |
| 2 | Denver International Airport |  | US | 3187 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2420 |
| 5 | Indira Gandhi International Airport |  | IN | 2383 |
| 6 | Harry Reid International Airport |  | US | 2254 |
| 7 | Zurich Airport |  | CH | 2068 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2067 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2018 |
| 10 | La Aurora Airport |  | GT | 1900 |
| 11 | El Dorado International Airport |  | CO | 1780 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1734 |
| 14 | Chicago O'Hare International Airport |  | US | 1703 |
| 15 | Frankfurt am Main International Airport |  | DE | 1653 |
| 16 | Congonhas Airport |  | BR | 1631 |
| 17 | Madrid Barajas International Airport |  | ES | 1539 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1497 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1494 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1438 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1402 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 24 | Malpensa International Airport |  | IT | 1354 |
| 25 | Charles de Gaulle International Airport |  | FR | 1342 |
| 26 | Charlotte/Douglas International Airport |  | US | 1293 |
| 27 | Kuala Lumpur International Airport |  | MY | 1245 |
| 28 | Bengaluru International Airport |  | IN | 1240 |
| 29 | Ninoy Aquino International Airport |  | PH | 1224 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1217 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1197 |
| 32 | Barcelona International Airport |  | ES | 1174 |
| 33 | Viracopos International Airport |  | BR | 1133 |
| 34 | Seattle-Tacoma International Airport |  | US | 1121 |
| 35 | Calgary International Airport |  | CA | 1113 |
| 36 | Reno/Tahoe International Airport |  | US | 1107 |
| 37 | Oslo Gardermoen Airport |  | NO | 1102 |
| 38 | Daniel K Inouye International Airport |  | US | 1087 |
| 39 | Vitoria/Foronda Airport |  | ES | 1070 |
| 40 | Tenerife Norte Airport |  | ES | 1069 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 999 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 715 | 21m | 244 km | 3,010.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 455 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 336 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 328 | 27m | 275 km | 1,554.3 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 323 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 292 | 44m | 241 km | 1,212.9 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 281 | 1h 49m | 1,423 km | 6,896.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 277 | 22m | 55 km | 263.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 243 | 27m | 215 km | 900.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 240 | 24m | 218 km | 904.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 230 | 1h 38m | 1,156 km | 4,588.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 229 | 19m | 144 km | 569.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 212 | 1h 3m | 695 km | 2,541.2 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SFY112 | SFY | Vero Beach Regional Airport (KVRB) | The 2A Ranch Airport (0FD0) | 2026-08-14 13:36 UTC | 2026-08-14 14:41 UTC | 1h 4m |
| N470AK |  | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-14 14:17 UTC | 2026-08-14 14:36 UTC | 18m |
| N701LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Brookneal/Campbell County Airport (K0V4) | 2026-08-14 13:37 UTC | 2026-08-14 14:33 UTC | 55m |
| N467CS |  | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-08-14 14:14 UTC | 2026-08-14 14:32 UTC | 17m |
| N28JA |  | Lakewood Airport (KN12) | Old Bridge Airport (K3N6) | 2026-08-14 14:18 UTC | 2026-08-14 14:31 UTC | 13m |
| N145SH |  | Michael J Smith Field (KMRH) | Michael J Smith Field (KMRH) | 2026-08-14 13:55 UTC | 2026-08-14 14:29 UTC | 34m |
| AFR46HJ | Air France | Charles de Gaulle International Airport (LFPG) | Capua Airport (LIAU) | 2026-08-14 12:48 UTC | 2026-08-14 14:28 UTC | 1h 39m |
| EDGE91 | EDG | 4XA5 (4XA5) | OK79 (OK79) | 2026-08-14 13:46 UTC | 2026-08-14 14:24 UTC | 37m |
| N734NA |  | Sky Manor Airport (KN40) | Solberg/Hunterdon Airport (KN51) | 2026-08-14 13:58 UTC | 2026-08-14 14:24 UTC | 25m |
| CXK369 | CXK | Essex County Airport (KCDW) | Lancaster Airport (KLNS) | 2026-08-14 13:16 UTC | 2026-08-14 14:24 UTC | 1h 8m |
| N38HF |  | Westchester County Airport (KHPN) | Laguardia Airport (KLGA) | 2026-08-14 14:07 UTC | 2026-08-14 14:22 UTC | 15m |
| FTO501 | FTO | Essex County Airport (KCDW) | Laguardia Airport (KLGA) | 2026-08-14 14:06 UTC | 2026-08-14 14:22 UTC | 15m |
| N7018G |  | Chatham Municipal Airport (KCQX) | Chatham Municipal Airport (KCQX) | 2026-08-14 13:16 UTC | 2026-08-14 14:21 UTC | 1h 5m |
| N21ME |  | Blairsville Airport (KDZJ) | Pine Mountain Airpark (6AR9) | 2026-08-14 13:17 UTC | 2026-08-14 14:21 UTC | 1h 4m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-14 14:04 UTC | 2026-08-14 14:20 UTC | 16m |
| N543TC |  | Meadows Field (KBFL) | Santa Monica Municipal Airport (KSMO) | 2026-08-14 13:31 UTC | 2026-08-14 14:15 UTC | 43m |
| SCU48 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Barcus Field (95OK) | 2026-08-14 13:34 UTC | 2026-08-14 14:09 UTC | 35m |
| 72285 |  | Lakehurst Maxfield Field (KNEL) | Trenton Mercer Airport (KTTN) | 2026-08-14 13:53 UTC | 2026-08-14 14:07 UTC | 14m |
| N8024Q |  | Trenton Mercer Airport (KTTN) | Northeast Philadelphia Airport (KPNE) | 2026-08-14 13:21 UTC | 2026-08-14 14:07 UTC | 45m |
| N2350E |  | Melbourne Orlando International Airport (KMLB) | Sebastian Municipal Airport (KX26) | 2026-08-14 13:38 UTC | 2026-08-14 14:07 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

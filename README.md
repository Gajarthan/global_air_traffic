# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_18:12:39_UTC-green)

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

**Latest saved flight:** 2026-08-14 18:12:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 18:12:39 UTC

- **196,118** saved flights
- **61,603** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **196,118** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,341,845.5 tonnes** estimated CO2 emissions
- **135,759,160 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7797 |
| 2 | SkyWest Airlines | 7041 |
| 3 | EJA | 3861 |
| 4 | IndiGo | 3383 |
| 5 | Southwest Airlines | 3041 |
| 6 | American Airlines | 3027 |
| 7 | ENY | 2423 |
| 8 | Delta Air Lines | 2313 |
| 9 | LATAM Airlines | 1836 |
| 10 | AZU | 1767 |
| 11 | Lufthansa | 1694 |
| 12 | Vueling | 1638 |
| 13 | WIF | 1624 |
| 14 | LXJ | 1551 |
| 15 | easyJet | 1348 |
| 16 | Swiss International | 1326 |
| 17 | AXM | 1277 |
| 18 | EJU | 1215 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1159 |
| 22 | VIV | 1076 |
| 23 | GLO | 1056 |
| 24 | Air France | 1034 |
| 25 | PGT | 1022 |
| 26 | AEE | 1009 |
| 27 | CXK | 1003 |
| 28 | United Airlines | 998 |
| 29 | WMT | 982 |
| 30 | Wizz Air | 970 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 166679 |
| 2 | 🇪🇸 ES | 12672 |
| 3 | 🇧🇷 BR | 11254 |
| 4 | 🇦🇺 AU | 11009 |
| 5 | 🇨🇦 CA | 10727 |
| 6 | 🇮🇳 IN | 10583 |
| 7 | 🇮🇹 IT | 10220 |
| 8 | 🇩🇪 DE | 9749 |
| 9 | 🇬🇧 GB | 9222 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7827 |
| 12 | 🇨🇴 CO | 7670 |
| 13 | 🇬🇷 GR | 5770 |
| 14 | 🇲🇽 MX | 5540 |
| 15 | 🇹🇷 TR | 5336 |
| 16 | 🇨🇭 CH | 5309 |
| 17 | 🇳🇴 NO | 5031 |
| 18 | 🇲🇾 MY | 3341 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3240 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2589 |
| 24 | 🇬🇹 GT | 2499 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2047 |
| 27 | 🇲🇦 MA | 1986 |
| 28 | 🇳🇱 NL | 1769 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1584 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4073 |
| 2 | Denver International Airport |  | US | 3196 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2431 |
| 5 | Indira Gandhi International Airport |  | IN | 2390 |
| 6 | Harry Reid International Airport |  | US | 2257 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2076 |
| 8 | Zurich Airport |  | CH | 2074 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2027 |
| 10 | La Aurora Airport |  | GT | 1917 |
| 11 | El Dorado International Airport |  | CO | 1789 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1750 |
| 13 | Salt Lake City International Airport |  | US | 1739 |
| 14 | Chicago O'Hare International Airport |  | US | 1709 |
| 15 | Frankfurt am Main International Airport |  | DE | 1661 |
| 16 | Congonhas Airport |  | BR | 1640 |
| 17 | Madrid Barajas International Airport |  | ES | 1545 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1502 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1496 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1446 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1407 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 24 | Malpensa International Airport |  | IT | 1359 |
| 25 | Charles de Gaulle International Airport |  | FR | 1349 |
| 26 | Charlotte/Douglas International Airport |  | US | 1300 |
| 27 | Kuala Lumpur International Airport |  | MY | 1245 |
| 28 | Bengaluru International Airport |  | IN | 1244 |
| 29 | Ninoy Aquino International Airport |  | PH | 1224 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1222 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1199 |
| 32 | Barcelona International Airport |  | ES | 1180 |
| 33 | Viracopos International Airport |  | BR | 1136 |
| 34 | Seattle-Tacoma International Airport |  | US | 1123 |
| 35 | Calgary International Airport |  | CA | 1116 |
| 36 | Reno/Tahoe International Airport |  | US | 1109 |
| 37 | Oslo Gardermoen Airport |  | NO | 1106 |
| 38 | Daniel K Inouye International Airport |  | US | 1090 |
| 39 | Vitoria/Foronda Airport |  | ES | 1078 |
| 40 | Tenerife Norte Airport |  | ES | 1074 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1004 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 718 | 21m | 244 km | 3,023.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 457 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 337 | 32m | - | - |
| 7 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 334 | 8m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 294 | 44m | 241 km | 1,221.2 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 284 | 1h 49m | 1,423 km | 6,969.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 280 | 22m | 55 km | 266.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 242 | 24m | 218 km | 911.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 238 | 1h 15m | 961 km | 3,945.0 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 238 | 19m | 99 km | 407.7 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 231 | 1h 38m | 1,156 km | 4,608.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 230 | 19m | 144 km | 572.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 214 | 28m | 152 km | 559.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 213 | 1h 3m | 695 km | 2,553.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1976F |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-14 17:46 UTC | 2026-08-14 18:12 UTC | 26m |
| N784DS |  | Palo Alto Airport (KPAO) | Modesto City-County-Harry Sham Field (KMOD) | 2026-08-14 17:13 UTC | 2026-08-14 18:11 UTC | 58m |
| PAT820 | PAT | K4SD (K4SD) | Sacramento Mather Airport (KMHR) | 2026-08-14 16:21 UTC | 2026-08-14 18:05 UTC | 1h 43m |
| DFL5720 | DFL | Visingso Airport (ESSI) | Stockholm-Bromma Airport (ESSB) | 2026-08-14 17:12 UTC | 2026-08-14 17:58 UTC | 45m |
| N733PN |  | Northeast Philadelphia Airport (KPNE) | Monmouth Executive Airport (KBLM) | 2026-08-14 17:32 UTC | 2026-08-14 17:57 UTC | 25m |
| LUZON41 | LUZ | Randolph Afb Airport (KRND) | Weiblen Airport (TE13) | 2026-08-14 17:28 UTC | 2026-08-14 17:57 UTC | 28m |
| N9522S |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-08-14 17:21 UTC | 2026-08-14 17:54 UTC | 32m |
| N65NG |  | Oakland County International Airport (KPTK) | Lakes Of The North Airport (K4Y4) | 2026-08-14 17:09 UTC | 2026-08-14 17:53 UTC | 43m |
| N396FS |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-08-14 17:28 UTC | 2026-08-14 17:51 UTC | 23m |
| N25XM |  | North Las Vegas Airport (KVGT) | Henderson Executive Airport (KHND) | 2026-08-14 17:39 UTC | 2026-08-14 17:51 UTC | 11m |
| N78RK |  | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | Mesa 1 Airport (81CO) | 2026-08-14 14:21 UTC | 2026-08-14 17:50 UTC | 3h 29m |
| N34MA |  | Arlington Municipal Airport (KAWO) | Bayview Farms Airport (WN51) | 2026-08-14 17:17 UTC | 2026-08-14 17:50 UTC | 32m |
| HK4717 |  | Santa Ana Airport (SKGO) | Santa Ana Airport (SKGO) | 2026-08-14 17:42 UTC | 2026-08-14 17:49 UTC | 7m |
| N247JH |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | South Fox Island Airport (3MI2) | 2026-08-14 17:07 UTC | 2026-08-14 17:48 UTC | 40m |
| N28SU |  | Orange County Airport (KMGJ) | New York Stewart International Airport (KSWF) | 2026-08-14 17:19 UTC | 2026-08-14 17:48 UTC | 29m |
| N949WW |  | Atlantic City International Airport (KACY) | Capital City Airport (KCXY) | 2026-08-14 17:16 UTC | 2026-08-14 17:48 UTC | 31m |
| N530TH |  | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-08-14 16:01 UTC | 2026-08-14 17:47 UTC | 1h 46m |
| TCTSS | TCT | Ataturk International Airport (LTBA) | Isparta Airport (LTBM) | 2026-08-14 16:59 UTC | 2026-08-14 17:47 UTC | 47m |
| THY165 | Turkish Airlines | Luang Namtha Airport (VLLN) | Chanmyathazi Airport (VYCZ) | 2026-08-14 17:05 UTC | 2026-08-14 17:44 UTC | 39m |
| N118RF |  | Amedee Army Air Field (KAHC) | Amedee Army Air Field (KAHC) | 2026-08-14 17:27 UTC | 2026-08-14 17:44 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

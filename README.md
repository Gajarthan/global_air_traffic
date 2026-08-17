# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_15:15:32_UTC-green)

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

**Latest saved flight:** 2026-08-17 15:15:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 15:15:32 UTC

- **208,460** saved flights
- **66,271** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **208,460** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,507,047.6 tonnes** estimated CO2 emissions
- **145,336,093 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8246 |
| 2 | SkyWest Airlines | 7472 |
| 3 | EJA | 4054 |
| 4 | IndiGo | 3568 |
| 5 | American Airlines | 3463 |
| 6 | Southwest Airlines | 3340 |
| 7 | Delta Air Lines | 2672 |
| 8 | ENY | 2590 |
| 9 | LATAM Airlines | 1967 |
| 10 | AZU | 1887 |
| 11 | Lufthansa | 1759 |
| 12 | Vueling | 1735 |
| 13 | WIF | 1680 |
| 14 | LXJ | 1646 |
| 15 | easyJet | 1438 |
| 16 | Swiss International | 1388 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1310 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1271 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1147 |
| 24 | GLO | 1126 |
| 25 | Air France | 1118 |
| 26 | PGT | 1117 |
| 27 | JetBlue | 1066 |
| 28 | AEE | 1064 |
| 29 | WMT | 1054 |
| 30 | Wizz Air | 1034 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176498 |
| 2 | 🇪🇸 ES | 13341 |
| 3 | 🇧🇷 BR | 11959 |
| 4 | 🇦🇺 AU | 11745 |
| 5 | 🇨🇦 CA | 11502 |
| 6 | 🇮🇳 IN | 11132 |
| 7 | 🇮🇹 IT | 10900 |
| 8 | 🇩🇪 DE | 10301 |
| 9 | 🇬🇧 GB | 9730 |
| 10 | 🇯🇵 JP | 8643 |
| 11 | 🇨🇴 CO | 8293 |
| 12 | 🇫🇷 FR | 8262 |
| 13 | 🇬🇷 GR | 6146 |
| 14 | 🇹🇷 TR | 5931 |
| 15 | 🇲🇽 MX | 5855 |
| 16 | 🇨🇭 CH | 5553 |
| 17 | 🇳🇴 NO | 5202 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3506 |
| 20 | 🇵🇱 PL | 3442 |
| 21 | 🇹🇭 TH | 3350 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2773 |
| 24 | 🇬🇹 GT | 2678 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2238 |
| 27 | 🇲🇦 MA | 2103 |
| 28 | 🇳🇱 NL | 1856 |
| 29 | 🇲🇪 ME | 1770 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4372 |
| 2 | Denver International Airport |  | US | 3397 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2531 |
| 5 | Guaymaral Airport |  | CO | 2506 |
| 6 | Harry Reid International Airport |  | US | 2350 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2173 |
| 8 | Zurich Airport |  | CH | 2172 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2154 |
| 10 | La Aurora Airport |  | GT | 2036 |
| 11 | Chicago O'Hare International Airport |  | US | 1926 |
| 12 | El Dorado International Airport |  | CO | 1903 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1858 |
| 14 | Salt Lake City International Airport |  | US | 1842 |
| 15 | Congonhas Airport |  | BR | 1738 |
| 16 | Frankfurt am Main International Airport |  | DE | 1715 |
| 17 | Madrid Barajas International Airport |  | ES | 1637 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1582 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1578 |
| 20 | Capua Airport |  | IT | 1575 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1519 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1467 |
| 24 | Malpensa International Airport |  | IT | 1446 |
| 25 | Charles de Gaulle International Airport |  | FR | 1430 |
| 26 | Charlotte/Douglas International Airport |  | US | 1414 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1314 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1288 |
| 30 | Bengaluru International Airport |  | IN | 1287 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1262 |
| 32 | Barcelona International Airport |  | ES | 1251 |
| 33 | Seattle-Tacoma International Airport |  | US | 1239 |
| 34 | Viracopos International Airport |  | BR | 1210 |
| 35 | Calgary International Airport |  | CA | 1179 |
| 36 | Oslo Gardermoen Airport |  | NO | 1154 |
| 37 | Vitoria/Foronda Airport |  | ES | 1148 |
| 38 | Reno/Tahoe International Airport |  | US | 1144 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1119 |
| 40 | Don Mueang International Airport |  | TH | 1112 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1030 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 473 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 406 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 349 | 27m | 275 km | 1,653.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 345 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 305 | 44m | 241 km | 1,266.9 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 304 | 1h 49m | 1,423 km | 7,460.6 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 261 | 19m | 99 km | 447.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 255 | 27m | 215 km | 944.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 249 | 1h 37m | 1,156 km | 4,967.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 239 | 19m | 144 km | 594.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 228 | 28m | 152 km | 595.8 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 224 | 1h 49m | 1,304 km | 5,039.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TOM9LG | TOM | Dionysios Solomos Airport (LGZA) | London Gatwick Airport (EGKK) | 2026-08-17 11:50 UTC | 2026-08-17 15:15 UTC | 3h 25m |
| N673MA |  | Lewis University Airport (KLOT) | K1C2 (K1C2) | 2026-08-17 14:36 UTC | 2026-08-17 15:14 UTC | 37m |
| MIG1 | MIG | Eglin Afb/Destin-Ft Walton Beach Airport (KVPS) | Bird Nest Airport (4MS5) | 2026-08-17 14:59 UTC | 2026-08-17 15:11 UTC | 12m |
| N625PL |  | Hammond Northshore Regional Airport (KHDC) | LA30 (LA30) | 2026-08-17 13:11 UTC | 2026-08-17 15:11 UTC | 1h 59m |
| N104PF |  | Lewis University Airport (KLOT) | K1C2 (K1C2) | 2026-08-17 14:32 UTC | 2026-08-17 15:11 UTC | 38m |
| N723AG |  | Oakland County International Airport (KPTK) | Saginaw County/H W Browne Airport (KHYX) | 2026-08-17 14:47 UTC | 2026-08-17 15:11 UTC | 23m |
| N99981 |  | Midway Lake Airport (79FD) | Lakeland Linder International Airport (KLAL) | 2026-08-17 14:39 UTC | 2026-08-17 15:09 UTC | 30m |
| N9157A |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-17 14:03 UTC | 2026-08-17 15:08 UTC | 1h 4m |
| WING81 | WIN | Pope Army Air Field (KPOB) | Florence Regional Airport (KFLO) | 2026-08-17 14:22 UTC | 2026-08-17 15:07 UTC | 45m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-17 14:37 UTC | 2026-08-17 15:07 UTC | 29m |
| N51KC |  | Johnson County Executive Airport (KOJC) | Steciak Strip (1OL2) | 2026-08-17 13:35 UTC | 2026-08-17 15:07 UTC | 1h 31m |
| EAG76L | EAG | George Best Belfast City Airport (EGAC) | HUDDERSFIELD (Crosland Moor) (EGND) | 2026-08-17 13:51 UTC | 2026-08-17 15:06 UTC | 1h 15m |
| RYR87MM | Ryanair | Gdańsk Lech Wałęsa Airport (EPGD) | Sandtoft Airfield (EGCF) | 2026-08-17 12:32 UTC | 2026-08-17 15:04 UTC | 2h 32m |
| RYR1GX | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | HUDDERSFIELD (Crosland Moor) (EGND) | 2026-08-17 12:20 UTC | 2026-08-17 15:04 UTC | 2h 44m |
| LOG89LT | LOG | Birmingham International Airport (EGBB) | RAF Woodvale (EGOW) | 2026-08-17 13:59 UTC | 2026-08-17 15:03 UTC | 1h 4m |
| N872FA |  | Lewis University Airport (KLOT) | LL40 (LL40) | 2026-08-17 14:34 UTC | 2026-08-17 15:03 UTC | 28m |
| N388BB |  | Houma-Terrebonne Airport (KHUM) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-08-17 14:51 UTC | 2026-08-17 15:02 UTC | 11m |
| UAE383 | Emirates | Chek Lap Kok International Airport (VHHH) | Chanmyathazi Airport (VYCZ) | 2026-08-17 12:43 UTC | 2026-08-17 15:02 UTC | 2h 18m |
| WZZ88 | Wizz Air | Vilnius International Airport (EYVI) | Wesel-Romerwardt Airport (EDLX) | 2026-08-17 12:23 UTC | 2026-08-17 15:02 UTC | 2h 38m |
| N4776E |  | Clearwater Executive Airport (KCLW) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-08-17 14:42 UTC | 2026-08-17 15:01 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

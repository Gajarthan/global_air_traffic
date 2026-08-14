# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_23:03:03_UTC-green)

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

**Latest saved flight:** 2026-08-14 23:03:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 23:03:03 UTC

- **197,053** saved flights
- **61,832** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **197,053** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,352,745.5 tonnes** estimated CO2 emissions
- **136,391,043 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7836 |
| 2 | SkyWest Airlines | 7097 |
| 3 | EJA | 3888 |
| 4 | IndiGo | 3387 |
| 5 | Southwest Airlines | 3056 |
| 6 | American Airlines | 3052 |
| 7 | ENY | 2439 |
| 8 | Delta Air Lines | 2330 |
| 9 | LATAM Airlines | 1848 |
| 10 | AZU | 1785 |
| 11 | Lufthansa | 1696 |
| 12 | Vueling | 1645 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1567 |
| 15 | easyJet | 1354 |
| 16 | Swiss International | 1329 |
| 17 | AXM | 1277 |
| 18 | EJU | 1222 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1165 |
| 22 | VIV | 1085 |
| 23 | GLO | 1067 |
| 24 | Air France | 1034 |
| 25 | PGT | 1025 |
| 26 | AEE | 1010 |
| 27 | United Airlines | 1007 |
| 28 | CXK | 1005 |
| 29 | WMT | 986 |
| 30 | Wizz Air | 974 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 167713 |
| 2 | 🇪🇸 ES | 12717 |
| 3 | 🇧🇷 BR | 11348 |
| 4 | 🇦🇺 AU | 11015 |
| 5 | 🇨🇦 CA | 10801 |
| 6 | 🇮🇳 IN | 10589 |
| 7 | 🇮🇹 IT | 10270 |
| 8 | 🇩🇪 DE | 9770 |
| 9 | 🇬🇧 GB | 9251 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7843 |
| 12 | 🇨🇴 CO | 7775 |
| 13 | 🇬🇷 GR | 5784 |
| 14 | 🇲🇽 MX | 5578 |
| 15 | 🇹🇷 TR | 5369 |
| 16 | 🇨🇭 CH | 5315 |
| 17 | 🇳🇴 NO | 5041 |
| 18 | 🇲🇾 MY | 3342 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3252 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2743 |
| 23 | 🇵🇭 PH | 2593 |
| 24 | 🇬🇹 GT | 2524 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2063 |
| 27 | 🇲🇦 MA | 1993 |
| 28 | 🇳🇱 NL | 1770 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1584 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4108 |
| 2 | Denver International Airport |  | US | 3211 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2442 |
| 5 | Indira Gandhi International Airport |  | IN | 2392 |
| 6 | Harry Reid International Airport |  | US | 2262 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2079 |
| 8 | Zurich Airport |  | CH | 2079 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2044 |
| 10 | La Aurora Airport |  | GT | 1935 |
| 11 | El Dorado International Airport |  | CO | 1804 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1762 |
| 13 | Salt Lake City International Airport |  | US | 1752 |
| 14 | Chicago O'Hare International Airport |  | US | 1732 |
| 15 | Frankfurt am Main International Airport |  | DE | 1663 |
| 16 | Congonhas Airport |  | BR | 1657 |
| 17 | Madrid Barajas International Airport |  | ES | 1548 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1506 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1503 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1454 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1421 |
| 23 | Malpensa International Airport |  | IT | 1369 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1363 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1305 |
| 27 | Kuala Lumpur International Airport |  | MY | 1246 |
| 28 | Bengaluru International Airport |  | IN | 1244 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1229 |
| 30 | Ninoy Aquino International Airport |  | PH | 1226 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1207 |
| 32 | Barcelona International Airport |  | ES | 1182 |
| 33 | Viracopos International Airport |  | BR | 1147 |
| 34 | Seattle-Tacoma International Airport |  | US | 1132 |
| 35 | Calgary International Airport |  | CA | 1122 |
| 36 | Reno/Tahoe International Airport |  | US | 1114 |
| 37 | Oslo Gardermoen Airport |  | NO | 1110 |
| 38 | Daniel K Inouye International Airport |  | US | 1093 |
| 39 | Vitoria/Foronda Airport |  | ES | 1082 |
| 40 | Tenerife Norte Airport |  | ES | 1077 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 721 | 21m | 244 km | 3,035.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 354 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 337 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 297 | 44m | 241 km | 1,233.7 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 284 | 1h 49m | 1,423 km | 6,969.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 280 | 22m | 55 km | 266.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 243 | 24m | 218 km | 915.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 240 | 19m | 99 km | 411.1 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 232 | 1h 38m | 1,156 km | 4,628.3 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 223 | 31m | 369 km | 1,419.5 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 213 | 1h 3m | 695 km | 2,553.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N243EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-14 20:21 UTC | 2026-08-14 23:03 UTC | 2h 41m |
| N456MT |  | Ocean County Airport (KMJX) | Monmouth Executive Airport (KBLM) | 2026-08-14 22:49 UTC | 2026-08-14 23:00 UTC | 11m |
| N13807 |  | Cleveland Municipal Airport (KRNV) | Ruleville-Drew Airport (KM37) | 2026-08-14 22:30 UTC | 2026-08-14 22:56 UTC | 26m |
| N539SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-14 22:24 UTC | 2026-08-14 22:55 UTC | 31m |
| XSN40 | XSN | Yucca Valley Airport (KL22) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-14 21:28 UTC | 2026-08-14 22:55 UTC | 1h 26m |
| N43957 |  | Van Nuys Airport (KVNY) | Santa Monica Municipal Airport (KSMO) | 2026-08-14 22:16 UTC | 2026-08-14 22:54 UTC | 38m |
| MAFFS6 | MAF | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-14 22:42 UTC | 2026-08-14 22:53 UTC | 10m |
| N543TC |  | Wonderful Pistachios & Almonds Airport (2CN4) | Santa Monica Municipal Airport (KSMO) | 2026-08-14 22:00 UTC | 2026-08-14 22:51 UTC | 50m |
| N7931D |  | Quad Cities International Airport (KMLI) | Jefferson City Memorial Airport (KJEF) | 2026-08-14 21:54 UTC | 2026-08-14 22:50 UTC | 56m |
| TKR136 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | Big Muddy Ranch Airport (2OR1) | 2026-08-14 22:36 UTC | 2026-08-14 22:47 UTC | 10m |
| N7580 |  | Stockton Metro Airport (KSCK) | Tracy Municipal Airport (KTCY) | 2026-08-14 21:43 UTC | 2026-08-14 22:46 UTC | 1h 3m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-14 22:30 UTC | 2026-08-14 22:45 UTC | 15m |
| BDIT27 | BDI | Moose Jaw Air Vice Marshal C. M. McEwen Airport (CYMJ) | Swift Current Airport (CYYN) | 2026-08-14 22:29 UTC | 2026-08-14 22:45 UTC | 16m |
| N757MC |  | Van Nuys Airport (KVNY) | Mc Clellan-Palomar Airport (KCRQ) | 2026-08-14 22:11 UTC | 2026-08-14 22:45 UTC | 33m |
| N560ZF |  | Norman Y Mineta San Jose International Airport (KSJC) | Truckee-Tahoe Airport (KTRK) | 2026-08-14 22:13 UTC | 2026-08-14 22:42 UTC | 29m |
| N37ET |  | Huntingburg Airport (KHNB) | Twentynine Palms Airport (KTNP) | 2026-08-14 18:05 UTC | 2026-08-14 22:40 UTC | 4h 35m |
| N61NG |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-08-14 22:02 UTC | 2026-08-14 22:35 UTC | 32m |
| TKR164 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | Collins Landing Strip (04OR) | 2026-08-14 22:20 UTC | 2026-08-14 22:31 UTC | 10m |
| N8844 |  | Tombstone Municipal Airport (KP29) | AZ86 (AZ86) | 2026-08-14 21:45 UTC | 2026-08-14 22:30 UTC | 44m |
| N2530B |  | 46MI (46MI) | 46MI (46MI) | 2026-08-14 22:02 UTC | 2026-08-14 22:29 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_16:56:01_UTC-green)

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

**Latest saved flight:** 2026-08-22 16:56:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 16:56:01 UTC

- **226,167** saved flights
- **70,295** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **226,167** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,725,068.5 tonnes** estimated CO2 emissions
- **157,974,986 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9079 |
| 2 | SkyWest Airlines | 8017 |
| 3 | EJA | 4364 |
| 4 | IndiGo | 3825 |
| 5 | American Airlines | 3709 |
| 6 | Southwest Airlines | 3527 |
| 7 | Delta Air Lines | 2890 |
| 8 | ENY | 2764 |
| 9 | LATAM Airlines | 2164 |
| 10 | AZU | 2090 |
| 11 | Vueling | 1915 |
| 12 | Lufthansa | 1856 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1782 |
| 15 | easyJet | 1567 |
| 16 | Swiss International | 1507 |
| 17 | AXM | 1493 |
| 18 | EJU | 1428 |
| 19 | United Airlines | 1423 |
| 20 | QLK | 1421 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1258 |
| 24 | PGT | 1244 |
| 25 | VIV | 1235 |
| 26 | Air France | 1233 |
| 27 | WMT | 1221 |
| 28 | Wizz Air | 1173 |
| 29 | JetBlue | 1130 |
| 30 | AEE | 1126 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 189268 |
| 2 | 🇪🇸 ES | 14502 |
| 3 | 🇧🇷 BR | 13188 |
| 4 | 🇦🇺 AU | 12778 |
| 5 | 🇨🇦 CA | 12513 |
| 6 | 🇮🇹 IT | 12154 |
| 7 | 🇮🇳 IN | 11924 |
| 8 | 🇩🇪 DE | 11147 |
| 9 | 🇬🇧 GB | 10629 |
| 10 | 🇨🇴 CO | 9297 |
| 11 | 🇯🇵 JP | 9194 |
| 12 | 🇫🇷 FR | 9061 |
| 13 | 🇹🇷 TR | 6630 |
| 14 | 🇬🇷 GR | 6617 |
| 15 | 🇲🇽 MX | 6283 |
| 16 | 🇨🇭 CH | 5980 |
| 17 | 🇳🇴 NO | 5592 |
| 18 | 🇲🇾 MY | 3981 |
| 19 | 🇿🇦 ZA | 3913 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3763 |
| 22 | 🇳🇿 NZ | 3140 |
| 23 | 🇵🇭 PH | 3087 |
| 24 | 🇬🇹 GT | 2862 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2552 |
| 27 | 🇲🇦 MA | 2283 |
| 28 | 🇲🇪 ME | 2033 |
| 29 | 🇳🇱 NL | 2023 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4718 |
| 2 | Denver International Airport |  | US | 3680 |
| 3 | Tokyo International Airport |  | JP | 2748 |
| 4 | Indira Gandhi International Airport |  | IN | 2746 |
| 5 | Guaymaral Airport |  | CO | 2635 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2350 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2310 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2287 |
| 10 | La Aurora Airport |  | GT | 2180 |
| 11 | El Dorado International Airport |  | CO | 2081 |
| 12 | Chicago O'Hare International Airport |  | US | 2051 |
| 13 | Salt Lake City International Airport |  | US | 1985 |
| 14 | Congonhas Airport |  | BR | 1929 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 16 | Frankfurt am Main International Airport |  | DE | 1822 |
| 17 | Madrid Barajas International Airport |  | ES | 1765 |
| 18 | Capua Airport |  | IT | 1751 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1684 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1682 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1638 |
| 22 | Malpensa International Airport |  | IT | 1602 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 25 | Charles de Gaulle International Airport |  | FR | 1568 |
| 26 | Charlotte/Douglas International Airport |  | US | 1484 |
| 27 | Ninoy Aquino International Airport |  | PH | 1476 |
| 28 | Kuala Lumpur International Airport |  | MY | 1446 |
| 29 | Barcelona International Airport |  | ES | 1407 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1372 |
| 31 | Bengaluru International Airport |  | IN | 1345 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1337 |
| 33 | Viracopos International Airport |  | BR | 1337 |
| 34 | Seattle-Tacoma International Airport |  | US | 1330 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1319 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1259 |
| 39 | Vitoria/Foronda Airport |  | ES | 1244 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1224 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1074 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 817 | 21m | 244 km | 3,440.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 563 | 1h 6m | 770 km | 7,479.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 534 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 511 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 341 | 1h 50m | 1,423 km | 8,368.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 302 | 22m | 55 km | 287.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 293 | 44m | 555 km | 2,805.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 289 | 1h 38m | 1,156 km | 5,765.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 287 | 24m | 218 km | 1,081.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 283 | 19m | 99 km | 484.8 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 266 | 1h 14m | 961 km | 4,409.1 t |
| 22 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 258 | 19m | 144 km | 641.8 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N245EM |  | South St Paul Municipal/Richard E Fleming Field (KSGS) | South St Paul Municipal/Richard E Fleming Field (KSGS) | 2026-08-22 15:56 UTC | 2026-08-22 16:56 UTC | 59m |
| N5659K |  | Abraham Lincoln Capital Airport (KSPI) | Minder Airport (37IL) | 2026-08-22 16:40 UTC | 2026-08-22 16:53 UTC | 13m |
| N113BB |  | Gillespie Field (KSEE) | Hemet-Ryan Airport (KHMT) | 2026-08-22 16:22 UTC | 2026-08-22 16:53 UTC | 30m |
| N511MT |  | Vinton Veterans Memorial Airpark (KVTI) | Iowa City Municipal Airport (KIOW) | 2026-08-22 16:34 UTC | 2026-08-22 16:50 UTC | 16m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-22 16:28 UTC | 2026-08-22 16:45 UTC | 16m |
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-22 15:49 UTC | 2026-08-22 16:43 UTC | 53m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-22 16:24 UTC | 2026-08-22 16:37 UTC | 12m |
| N31536 |  | Rattlesnake Island Airport (58OH) | Rattlesnake Island Airport (58OH) | 2026-08-22 16:28 UTC | 2026-08-22 16:33 UTC | 5m |
| N911UC |  | Centennial Airport (KAPA) | Perry Stokes Airport (KTAD) | 2026-08-22 15:54 UTC | 2026-08-22 16:31 UTC | 37m |
| N116BD |  | Majors Airport (KGVT) | Card Aerodrome (0TX9) | 2026-08-22 16:13 UTC | 2026-08-22 16:30 UTC | 17m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-22 16:13 UTC | 2026-08-22 16:30 UTC | 16m |
| N680WP |  | Kalamazoo/Battle Creek International Airport (KAZO) | Thunder Bay Airport (CYQT) | 2026-08-22 15:21 UTC | 2026-08-22 16:29 UTC | 1h 8m |
| CCAAK | Air China | Municipal de Vitacura Airport (SCLC) | Eulogio Sanchez Airport (SCTB) | 2026-08-22 16:18 UTC | 2026-08-22 16:28 UTC | 10m |
| N46EK |  | K00V (K00V) | Mertens Airport (3CO2) | 2026-08-22 15:22 UTC | 2026-08-22 16:27 UTC | 1h 5m |
| N341TM |  | Rocky Mountain Metro Airport (KBJC) | Crystal Lakes Airport (25CO) | 2026-08-22 15:24 UTC | 2026-08-22 16:25 UTC | 1h 0m |
| N814R |  | Mckinney Ntl Airport (KTKI) | 31TS (31TS) | 2026-08-22 15:44 UTC | 2026-08-22 16:24 UTC | 40m |
| PRKOT | PRK | Jundiai Airport (SBJD) | Campo Belo Airport (SNCA) | 2026-08-22 15:50 UTC | 2026-08-22 16:22 UTC | 31m |
| LN301HC |  | Salt Lake City International Airport (KSLC) | Allen H Tigert Airport (KU78) | 2026-08-22 15:54 UTC | 2026-08-22 16:17 UTC | 22m |
| EJA302 | EJA | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-08-22 16:05 UTC | 2026-08-22 16:16 UTC | 11m |
| FHPCJ | FHP | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-08-22 16:06 UTC | 2026-08-22 16:16 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_13:03:14_UTC-green)

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

**Latest saved flight:** 2026-08-20 13:03:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 13:03:14 UTC

- **219,115** saved flights
- **68,854** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **219,115** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,638,982.9 tonnes** estimated CO2 emissions
- **152,984,514 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8789 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3722 |
| 5 | American Airlines | 3639 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2824 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2073 |
| 10 | AZU | 2006 |
| 11 | Vueling | 1843 |
| 12 | Lufthansa | 1820 |
| 13 | WIF | 1751 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1521 |
| 16 | Swiss International | 1458 |
| 17 | AXM | 1441 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1367 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1319 |
| 23 | VIV | 1197 |
| 24 | GLO | 1191 |
| 25 | Air France | 1190 |
| 26 | PGT | 1188 |
| 27 | WMT | 1152 |
| 28 | Wizz Air | 1119 |
| 29 | JetBlue | 1112 |
| 30 | AEE | 1098 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184272 |
| 2 | 🇪🇸 ES | 14043 |
| 3 | 🇧🇷 BR | 12628 |
| 4 | 🇦🇺 AU | 12412 |
| 5 | 🇨🇦 CA | 12081 |
| 6 | 🇮🇹 IT | 11680 |
| 7 | 🇮🇳 IN | 11607 |
| 8 | 🇩🇪 DE | 10834 |
| 9 | 🇬🇧 GB | 10292 |
| 10 | 🇨🇴 CO | 8990 |
| 11 | 🇯🇵 JP | 8959 |
| 12 | 🇫🇷 FR | 8739 |
| 13 | 🇬🇷 GR | 6391 |
| 14 | 🇹🇷 TR | 6308 |
| 15 | 🇲🇽 MX | 6097 |
| 16 | 🇨🇭 CH | 5805 |
| 17 | 🇳🇴 NO | 5439 |
| 18 | 🇲🇾 MY | 3811 |
| 19 | 🇿🇦 ZA | 3739 |
| 20 | 🇵🇱 PL | 3635 |
| 21 | 🇹🇭 TH | 3632 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2957 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2417 |
| 27 | 🇲🇦 MA | 2209 |
| 28 | 🇳🇱 NL | 1948 |
| 29 | 🇲🇪 ME | 1933 |
| 30 | 🇮🇩 ID | 1864 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3578 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2660 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2418 |
| 7 | Zurich Airport |  | CH | 2274 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2246 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2227 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2056 |
| 12 | Chicago O'Hare International Airport |  | US | 2008 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1848 |
| 16 | Frankfurt am Main International Airport |  | DE | 1784 |
| 17 | Madrid Barajas International Airport |  | ES | 1719 |
| 18 | Capua Airport |  | IT | 1670 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1619 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1605 |
| 22 | Macau International Airport |  | MO | 1574 |
| 23 | Malpensa International Airport |  | IT | 1546 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1541 |
| 25 | Charles de Gaulle International Airport |  | FR | 1509 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1406 |
| 28 | Kuala Lumpur International Airport |  | MY | 1400 |
| 29 | Barcelona International Airport |  | ES | 1346 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1332 |
| 31 | Bengaluru International Airport |  | IN | 1321 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1281 |
| 35 | Calgary International Airport |  | CA | 1236 |
| 36 | Vitoria/Foronda Airport |  | ES | 1215 |
| 37 | Oslo Gardermoen Airport |  | NO | 1213 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1203 |
| 39 | Don Mueang International Airport |  | TH | 1197 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1177 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 786 | 21m | 244 km | 3,309.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 367 | 27m | 275 km | 1,739.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 323 | 1h 50m | 1,423 km | 7,926.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 320 | 44m | 241 km | 1,329.2 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 288 | 21m | 250 km | 1,244.0 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 273 | 1h 38m | 1,156 km | 5,446.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 271 | 24m | 218 km | 1,021.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 269 | 27m | 215 km | 996.3 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 260 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 249 | 19m | 144 km | 619.4 t |
| 26 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 248 | 44m | 555 km | 2,374.7 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N464DA |  | Barrow County Airport (KWDR) | Barrow County Airport (KWDR) | 2026-08-20 12:40 UTC | 2026-08-20 13:03 UTC | 22m |
| N10856 |  | Mckinney Ntl Airport (KTKI) | Square Air Airport (TS63) | 2026-08-20 12:39 UTC | 2026-08-20 12:57 UTC | 18m |
| SLICK22 | SLI | WV23 (WV23) | WV23 (WV23) | 2026-08-20 12:20 UTC | 2026-08-20 12:47 UTC | 26m |
| N123TV |  | Willow Run Airport (KYIP) | Lenawee County Airport (KADG) | 2026-08-20 11:54 UTC | 2026-08-20 12:45 UTC | 51m |
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Joint Base Andrews Airport (KADW) | 2026-08-20 12:13 UTC | 2026-08-20 12:44 UTC | 31m |
| DHFEJ | DHF | Reichelsheim Airport (EDFB) | Reichelsheim Airport (EDFB) | 2026-08-20 12:27 UTC | 2026-08-20 12:43 UTC | 15m |
| N1671Q |  | Old Bridge Airport (K3N6) | Old Bridge Airport (K3N6) | 2026-08-20 12:24 UTC | 2026-08-20 12:41 UTC | 17m |
| FHPCJ | FHP | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-08-20 12:30 UTC | 2026-08-20 12:41 UTC | 11m |
| ERU934 | ERU | Daytona Beach International Airport (KDAB) | Palatka Municipal/Lt Kay Larkin Field (K28J) | 2026-08-20 12:14 UTC | 2026-08-20 12:40 UTC | 25m |
| STW283 | STW | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-08-20 06:23 UTC | 2026-08-20 12:40 UTC | 6h 16m |
| VLG3XB | Vueling | Hamburg Airport (EDDH) | Barcelona International Airport (LEBL) | 2026-08-20 09:53 UTC | 2026-08-20 12:40 UTC | 2h 46m |
| CXK533 | CXK | Arlington Municipal Airport (KGKY) | Mid-Way Regional Airport (KJWY) | 2026-08-20 12:07 UTC | 2026-08-20 12:37 UTC | 30m |
| T342 |  | Dubendorf Airport (LSMD) | LSMF (LSMF) | 2026-08-20 11:40 UTC | 2026-08-20 12:37 UTC | 56m |
| P4301 |  | Pondok Cabe Air Base (WIHP) | Pondok Cabe Air Base (WIHP) | 2026-08-20 12:18 UTC | 2026-08-20 12:35 UTC | 17m |
| N46168 |  | Orlampa Inc Airport (FA08) | Orlampa Inc Airport (FA08) | 2026-08-20 12:20 UTC | 2026-08-20 12:32 UTC | 12m |
| CAL105 | CAL | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-20 09:49 UTC | 2026-08-20 12:32 UTC | 2h 43m |
| N842WF |  | Felts Field (KSFF) | Hanson Airport (0MT6) | 2026-08-20 12:06 UTC | 2026-08-20 12:31 UTC | 25m |
| N671PA |  | Ona Airpark (K12V) | Ocean City Municipal Airport (KOXB) | 2026-08-20 10:37 UTC | 2026-08-20 12:31 UTC | 1h 54m |
| JFA42R | JFA | Wels Airport (LOLW) | Scharnstein Airport (LOLC) | 2026-08-20 12:27 UTC | 2026-08-20 12:31 UTC | 3m |
| FTO382 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-20 12:00 UTC | 2026-08-20 12:30 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

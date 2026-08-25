# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_20:28:56_UTC-green)

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

**Latest saved flight:** 2026-08-25 20:28:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 20:28:56 UTC

- **236,549** saved flights
- **72,227** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **236,549** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,848,661.1 tonnes** estimated CO2 emissions
- **165,139,776 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9491 |
| 2 | SkyWest Airlines | 8348 |
| 3 | EJA | 4593 |
| 4 | IndiGo | 3986 |
| 5 | American Airlines | 3843 |
| 6 | Southwest Airlines | 3608 |
| 7 | Delta Air Lines | 3016 |
| 8 | ENY | 2871 |
| 9 | LATAM Airlines | 2269 |
| 10 | AZU | 2206 |
| 11 | Vueling | 2025 |
| 12 | Lufthansa | 1920 |
| 13 | WIF | 1881 |
| 14 | LXJ | 1848 |
| 15 | easyJet | 1654 |
| 16 | Swiss International | 1587 |
| 17 | AXM | 1576 |
| 18 | EJU | 1520 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1497 |
| 21 | Alaska Airlines | 1420 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1323 |
| 24 | GLO | 1319 |
| 25 | VIV | 1306 |
| 26 | PGT | 1290 |
| 27 | Air France | 1284 |
| 28 | Wizz Air | 1267 |
| 29 | AEE | 1175 |
| 30 | JetBlue | 1174 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 196549 |
| 2 | 🇪🇸 ES | 15204 |
| 3 | 🇧🇷 BR | 13811 |
| 4 | 🇦🇺 AU | 13340 |
| 5 | 🇨🇦 CA | 13073 |
| 6 | 🇮🇹 IT | 12914 |
| 7 | 🇮🇳 IN | 12419 |
| 8 | 🇩🇪 DE | 11659 |
| 9 | 🇬🇧 GB | 11169 |
| 10 | 🇨🇴 CO | 10035 |
| 11 | 🇯🇵 JP | 9546 |
| 12 | 🇫🇷 FR | 9501 |
| 13 | 🇹🇷 TR | 7026 |
| 14 | 🇬🇷 GR | 6975 |
| 15 | 🇲🇽 MX | 6572 |
| 16 | 🇨🇭 CH | 6319 |
| 17 | 🇳🇴 NO | 5862 |
| 18 | 🇲🇾 MY | 4225 |
| 19 | 🇹🇭 TH | 4218 |
| 20 | 🇿🇦 ZA | 4147 |
| 21 | 🇵🇱 PL | 3943 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2964 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2730 |
| 27 | 🇲🇦 MA | 2394 |
| 28 | 🇲🇪 ME | 2202 |
| 29 | 🇳🇱 NL | 2123 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4910 |
| 2 | Denver International Airport |  | US | 3829 |
| 3 | Indira Gandhi International Airport |  | IN | 2884 |
| 4 | Tokyo International Airport |  | JP | 2843 |
| 5 | Guaymaral Airport |  | CO | 2686 |
| 6 | Harry Reid International Airport |  | US | 2528 |
| 7 | Zurich Airport |  | CH | 2477 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2422 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2368 |
| 10 | La Aurora Airport |  | GT | 2260 |
| 11 | El Dorado International Airport |  | CO | 2249 |
| 12 | Chicago O'Hare International Airport |  | US | 2129 |
| 13 | Salt Lake City International Airport |  | US | 2086 |
| 14 | Congonhas Airport |  | BR | 2015 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1982 |
| 16 | Frankfurt am Main International Airport |  | DE | 1878 |
| 17 | Capua Airport |  | IT | 1862 |
| 18 | Madrid Barajas International Airport |  | ES | 1860 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1778 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1745 |
| 21 | Malpensa International Airport |  | IT | 1695 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1677 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1646 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1524 |
| 29 | Barcelona International Airport |  | ES | 1496 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1479 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1435 |
| 32 | Viracopos International Airport |  | BR | 1412 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1385 |
| 34 | Bengaluru International Airport |  | IN | 1384 |
| 35 | Seattle-Tacoma International Airport |  | US | 1383 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1352 |
| 38 | Oslo Gardermoen Airport |  | NO | 1328 |
| 39 | Vancouver International Airport |  | CA | 1290 |
| 40 | O. R. Tambo International Airport |  | ZA | 1289 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1088 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 868 | 21m | 244 km | 3,654.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 599 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 530 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 391 | 27m | 275 km | 1,852.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 367 | 1h 50m | 1,423 km | 9,006.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 343 | 44m | 555 km | 3,284.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 343 | 44m | 241 km | 1,424.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 335 | 21m | 250 km | 1,447.0 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 317 | 24m | 218 km | 1,194.3 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 315 | 1h 40m | 1,156 km | 6,284.1 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 313 | 22m | 55 km | 297.5 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 293 | 19m | 99 km | 501.9 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 274 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 254 | 1h 50m | 1,304 km | 5,714.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 5611 |  | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-08-25 20:00 UTC | 2026-08-25 20:28 UTC | 28m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-08-25 06:10 UTC | 2026-08-25 20:26 UTC | 14h 16m |
| N750BB |  | LA48 (LA48) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-08-25 19:49 UTC | 2026-08-25 20:20 UTC | 30m |
| N93ME |  | Josephine Ranch Airport (2ID3) | Josephine Ranch Airport (2ID3) | 2026-08-25 20:05 UTC | 2026-08-25 20:19 UTC | 13m |
| N8024Q |  | Trenton Mercer Airport (KTTN) | Ocean County Airport (KMJX) | 2026-08-25 19:26 UTC | 2026-08-25 20:16 UTC | 50m |
| DLX50 | DLX | Van Nuys Airport (KVNY) | Santa Barbara Municipal Airport (KSBA) | 2026-08-25 19:58 UTC | 2026-08-25 20:16 UTC | 17m |
| N611GV |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-25 19:46 UTC | 2026-08-25 20:13 UTC | 27m |
| EJA312 | EJA | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-08-25 19:51 UTC | 2026-08-25 20:11 UTC | 20m |
| N610FA |  | Wings Field (KLOM) | Wings Field (KLOM) | 2026-08-25 19:51 UTC | 2026-08-25 20:07 UTC | 15m |
| OXF9846 | OXF | Falcon Field (KFFZ) | Benson Municipal/Paul Kerchum Field (KE95) | 2026-08-25 19:16 UTC | 2026-08-25 20:07 UTC | 50m |
| N287BG |  | Orlando Apopka Airport (KX04) | Leesburg International Airport (KLEE) | 2026-08-25 19:33 UTC | 2026-08-25 20:06 UTC | 33m |
| BLZR278 | BLZ | Kingsville Nas Airport (KNQI) | Duval County Ranch Company Airport (28TA) | 2026-08-25 19:41 UTC | 2026-08-25 20:05 UTC | 23m |
| N897GV |  | Sanderson Field (KSHN) | Boeing Field/King County International Airport (KBFI) | 2026-08-25 19:46 UTC | 2026-08-25 20:02 UTC | 16m |
| N487SF |  | Midland International Air And Space Port Airport (KMAF) | Dyess Afb Airport (KDYS) | 2026-08-25 19:30 UTC | 2026-08-25 19:59 UTC | 29m |
| RDHK710 | RDH | Felker Army Air Field (KFAF) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-08-25 19:40 UTC | 2026-08-25 19:58 UTC | 18m |
| N485K |  | Marina Municipal Airport (KOAR) | Marina Municipal Airport (KOAR) | 2026-08-25 19:25 UTC | 2026-08-25 19:57 UTC | 32m |
| N786FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-08-25 19:11 UTC | 2026-08-25 19:56 UTC | 45m |
| VLG34LB | Vueling | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 2026-08-25 18:46 UTC | 2026-08-25 19:56 UTC | 1h 9m |
|  |  | Pickens County Airport (KLQK) | Pickens County Airport (KLQK) | 2026-08-25 19:55 UTC | 2026-08-25 19:55 UTC | 0m |
| N739WR |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-25 19:38 UTC | 2026-08-25 19:55 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

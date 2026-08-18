# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_14:13:06_UTC-green)

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

**Latest saved flight:** 2026-08-18 14:13:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 14:13:06 UTC

- **211,991** saved flights
- **67,225** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **211,991** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,548,863.7 tonnes** estimated CO2 emissions
- **147,760,214 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8400 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4116 |
| 4 | IndiGo | 3628 |
| 5 | American Airlines | 3534 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2732 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1998 |
| 10 | AZU | 1924 |
| 11 | Lufthansa | 1778 |
| 12 | Vueling | 1772 |
| 13 | WIF | 1705 |
| 14 | LXJ | 1672 |
| 15 | easyJet | 1470 |
| 16 | Swiss International | 1420 |
| 17 | AXM | 1390 |
| 18 | United Airlines | 1342 |
| 19 | QLK | 1320 |
| 20 | Alaska Airlines | 1303 |
| 21 | EJU | 1303 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1165 |
| 24 | Air France | 1143 |
| 25 | GLO | 1143 |
| 26 | PGT | 1143 |
| 27 | WMT | 1082 |
| 28 | JetBlue | 1080 |
| 29 | AEE | 1072 |
| 30 | Wizz Air | 1056 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 179071 |
| 2 | 🇪🇸 ES | 13584 |
| 3 | 🇧🇷 BR | 12157 |
| 4 | 🇦🇺 AU | 11960 |
| 5 | 🇨🇦 CA | 11701 |
| 6 | 🇮🇳 IN | 11313 |
| 7 | 🇮🇹 IT | 11139 |
| 8 | 🇩🇪 DE | 10482 |
| 9 | 🇬🇧 GB | 9893 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8525 |
| 12 | 🇫🇷 FR | 8422 |
| 13 | 🇬🇷 GR | 6209 |
| 14 | 🇹🇷 TR | 6071 |
| 15 | 🇲🇽 MX | 5936 |
| 16 | 🇨🇭 CH | 5628 |
| 17 | 🇳🇴 NO | 5282 |
| 18 | 🇲🇾 MY | 3673 |
| 19 | 🇿🇦 ZA | 3580 |
| 20 | 🇵🇱 PL | 3502 |
| 21 | 🇹🇭 TH | 3441 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2711 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2297 |
| 27 | 🇲🇦 MA | 2136 |
| 28 | 🇳🇱 NL | 1888 |
| 29 | 🇲🇪 ME | 1822 |
| 30 | 🇮🇩 ID | 1769 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4448 |
| 2 | Denver International Airport |  | US | 3458 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2584 |
| 5 | Guaymaral Airport |  | CO | 2534 |
| 6 | Harry Reid International Airport |  | US | 2377 |
| 7 | Zurich Airport |  | CH | 2212 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2186 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 10 | La Aurora Airport |  | GT | 2061 |
| 11 | Chicago O'Hare International Airport |  | US | 1956 |
| 12 | El Dorado International Airport |  | CO | 1948 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1874 |
| 15 | Congonhas Airport |  | BR | 1768 |
| 16 | Frankfurt am Main International Airport |  | DE | 1733 |
| 17 | Madrid Barajas International Airport |  | ES | 1662 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1600 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1596 |
| 20 | Capua Airport |  | IT | 1596 |
| 21 | Macau International Airport |  | MO | 1554 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1547 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1489 |
| 24 | Malpensa International Airport |  | IT | 1470 |
| 25 | Charles de Gaulle International Airport |  | FR | 1456 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1354 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1307 |
| 30 | Bengaluru International Airport |  | IN | 1298 |
| 31 | Barcelona International Airport |  | ES | 1283 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 33 | Seattle-Tacoma International Airport |  | US | 1263 |
| 34 | Viracopos International Airport |  | BR | 1233 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1174 |
| 37 | Vitoria/Foronda Airport |  | ES | 1170 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1143 |
| 40 | Don Mueang International Airport |  | TH | 1137 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1039 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 753 | 21m | 244 km | 3,170.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 479 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 436 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 352 | 27m | 275 km | 1,668.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 348 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 311 | 1h 49m | 1,423 km | 7,632.4 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 311 | 14m | 114 km | 610.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 310 | 44m | 241 km | 1,287.7 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 274 | 21m | 250 km | 1,183.5 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 265 | 19m | 99 km | 453.9 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 262 | 1h 38m | 1,156 km | 5,226.8 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 259 | 27m | 215 km | 959.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 251 | 1h 14m | 961 km | 4,160.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 243 | 19m | 144 km | 604.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 222 | 44m | 555 km | 2,125.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PROVA85 | PRO | Salida/Harriett Alexander Field (KANK) | Central Colorado Regional Airport (KAEJ) | 2026-08-18 13:52 UTC | 2026-08-18 14:13 UTC | 20m |
| N1910R |  | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 2026-08-18 13:56 UTC | 2026-08-18 14:12 UTC | 16m |
| N6911H |  | Bourland Field (K50F) | Fort Worth Spinks Airport (KFWS) | 2026-08-18 13:43 UTC | 2026-08-18 14:12 UTC | 29m |
| MEOW01 | MEO | Flysooner Field (OK50) | Ramey 1 Airport (0OK8) | 2026-08-18 13:42 UTC | 2026-08-18 14:11 UTC | 29m |
| N8318Q |  | Quakertown Airport (KUKT) | Lancaster Airport (KLNS) | 2026-08-18 12:49 UTC | 2026-08-18 14:08 UTC | 1h 18m |
| N721CT |  | Tulsa Riverside Airport (KRVS) | Jantzen Airport (93OK) | 2026-08-18 13:38 UTC | 2026-08-18 14:04 UTC | 26m |
| N12704 |  | Frederick Municipal Airport (KFDK) | Lancaster Airport (KLNS) | 2026-08-18 13:15 UTC | 2026-08-18 14:02 UTC | 47m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-08-18 13:29 UTC | 2026-08-18 14:02 UTC | 33m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-08-18 13:35 UTC | 2026-08-18 14:02 UTC | 26m |
| N13715 |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-18 13:31 UTC | 2026-08-18 14:00 UTC | 28m |
| N6333F |  | KFTG (KFTG) | Limon Municipal Airport (KLIC) | 2026-08-18 13:36 UTC | 2026-08-18 14:00 UTC | 23m |
| OST47 | OST | Stillwater Regional Airport (KSWO) | Bartlesville Municipal Airport (KBVO) | 2026-08-18 13:35 UTC | 2026-08-18 14:00 UTC | 24m |
| CONGO63 | CON | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-08-18 13:21 UTC | 2026-08-18 14:00 UTC | 38m |
| PPJMJ | PPJ | Tres Marias Airport (SDWL) | SNAX (SNAX) | 2026-08-18 13:27 UTC | 2026-08-18 13:59 UTC | 31m |
| ERU964 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-08-18 12:45 UTC | 2026-08-18 13:58 UTC | 1h 12m |
| N253FD |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-08-18 13:18 UTC | 2026-08-18 13:54 UTC | 35m |
| AFL273 | AFL | Suvarnabhumi Airport (VTBS) | Bezymyanka Airfield (UWWG) | 2026-08-18 06:27 UTC | 2026-08-18 13:53 UTC | 7h 25m |
| N3814W |  | Toledo Suburban Airport (KDUH) | Hillsdale Municipal Airport (KJYM) | 2026-08-18 13:19 UTC | 2026-08-18 13:49 UTC | 30m |
| PSSSH | PSS | Tres Marias Airport (SDWL) | Fazenda Sao Francisco Airport (SDFN) | 2026-08-18 13:14 UTC | 2026-08-18 13:49 UTC | 35m |
| N199BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-08-18 12:39 UTC | 2026-08-18 13:47 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

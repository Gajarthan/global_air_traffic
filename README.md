# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_17:49:28_UTC-green)

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

**Latest saved flight:** 2026-08-19 17:49:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 17:49:28 UTC

- **216,637** saved flights
- **68,396** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **216,637** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,606,357.3 tonnes** estimated CO2 emissions
- **151,093,177 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8662 |
| 2 | SkyWest Airlines | 7733 |
| 3 | EJA | 4212 |
| 4 | IndiGo | 3690 |
| 5 | American Airlines | 3609 |
| 6 | Southwest Airlines | 3440 |
| 7 | Delta Air Lines | 2799 |
| 8 | ENY | 2673 |
| 9 | LATAM Airlines | 2051 |
| 10 | AZU | 1978 |
| 11 | Vueling | 1821 |
| 12 | Lufthansa | 1812 |
| 13 | WIF | 1732 |
| 14 | LXJ | 1704 |
| 15 | easyJet | 1502 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1368 |
| 19 | EJU | 1350 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1326 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1186 |
| 24 | PGT | 1176 |
| 25 | Air France | 1175 |
| 26 | GLO | 1175 |
| 27 | WMT | 1135 |
| 28 | JetBlue | 1103 |
| 29 | Wizz Air | 1101 |
| 30 | AEE | 1088 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 182520 |
| 2 | 🇪🇸 ES | 13906 |
| 3 | 🇧🇷 BR | 12475 |
| 4 | 🇦🇺 AU | 12169 |
| 5 | 🇨🇦 CA | 11918 |
| 6 | 🇮🇹 IT | 11496 |
| 7 | 🇮🇳 IN | 11489 |
| 8 | 🇩🇪 DE | 10744 |
| 9 | 🇬🇧 GB | 10175 |
| 10 | 🇯🇵 JP | 8870 |
| 11 | 🇨🇴 CO | 8867 |
| 12 | 🇫🇷 FR | 8650 |
| 13 | 🇬🇷 GR | 6336 |
| 14 | 🇹🇷 TR | 6231 |
| 15 | 🇲🇽 MX | 6047 |
| 16 | 🇨🇭 CH | 5763 |
| 17 | 🇳🇴 NO | 5389 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3683 |
| 20 | 🇵🇱 PL | 3583 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2751 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2372 |
| 27 | 🇲🇦 MA | 2183 |
| 28 | 🇳🇱 NL | 1938 |
| 29 | 🇲🇪 ME | 1889 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4542 |
| 2 | Denver International Airport |  | US | 3524 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2626 |
| 5 | Guaymaral Airport |  | CO | 2586 |
| 6 | Harry Reid International Airport |  | US | 2403 |
| 7 | Zurich Airport |  | CH | 2255 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2224 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2210 |
| 10 | La Aurora Airport |  | GT | 2092 |
| 11 | El Dorado International Airport |  | CO | 2023 |
| 12 | Chicago O'Hare International Airport |  | US | 1988 |
| 13 | Salt Lake City International Airport |  | US | 1909 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1892 |
| 15 | Congonhas Airport |  | BR | 1820 |
| 16 | Frankfurt am Main International Airport |  | DE | 1772 |
| 17 | Madrid Barajas International Airport |  | ES | 1697 |
| 18 | Capua Airport |  | IT | 1650 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1632 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1611 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1591 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Malpensa International Airport |  | IT | 1522 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1489 |
| 26 | Charlotte/Douglas International Airport |  | US | 1456 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1328 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1322 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1292 |
| 33 | Seattle-Tacoma International Airport |  | US | 1283 |
| 34 | Viracopos International Airport |  | BR | 1262 |
| 35 | Calgary International Airport |  | CA | 1218 |
| 36 | Oslo Gardermoen Airport |  | NO | 1201 |
| 37 | Vitoria/Foronda Airport |  | ES | 1199 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1174 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Don Mueang International Airport |  | TH | 1167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1058 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 772 | 21m | 244 km | 3,250.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 488 | 13m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 473 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 361 | 27m | 275 km | 1,710.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 293 | 22m | 55 km | 278.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 266 | 27m | 215 km | 985.2 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 256 | 1h 14m | 961 km | 4,243.3 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 255 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 232 | 1h 49m | 1,304 km | 5,219.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ATG7713 | ATG | Ostend-Bruges International Airport (EBOS) | Zhuhai Airport (ZGSD) | 2026-08-19 06:52 UTC | 2026-08-19 17:49 UTC | 10h 57m |
| ASI3 | ASI | Georgetown Executive Airport (KGTU) | Georgetown Executive Airport (KGTU) | 2026-08-19 17:02 UTC | 2026-08-19 17:49 UTC | 47m |
| N8695M |  | Hemet-Ryan Airport (KHMT) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-19 17:25 UTC | 2026-08-19 17:45 UTC | 19m |
| N340BG |  | Wood County Regional Airport (K1G0) | Donald P Miller Airport (KFZI) | 2026-08-19 17:32 UTC | 2026-08-19 17:43 UTC | 11m |
| TGSUN | TGS | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-19 17:29 UTC | 2026-08-19 17:42 UTC | 13m |
| FIRE02 | FIR | Ovar Airport (LPOV) | Viseu Airport (LPVZ) | 2026-08-19 17:28 UTC | 2026-08-19 17:39 UTC | 11m |
| CXK617 | CXK | Fayette Regional Air Center Airport (K3T5) | Easterwood Field (KCLL) | 2026-08-19 17:07 UTC | 2026-08-19 17:38 UTC | 31m |
| N525VB |  | Somerset Airport (KSMQ) | PS68 (PS68) | 2026-08-19 16:54 UTC | 2026-08-19 17:35 UTC | 41m |
| N570JA |  | Aurora Municipal Airport (KARR) | Wade Airport (56LL) | 2026-08-19 17:16 UTC | 2026-08-19 17:35 UTC | 19m |
| AER121 | AER | Ted Stevens Anchorage International Airport (PANC) | Fairbanks International Airport (PAFA) | 2026-08-19 16:31 UTC | 2026-08-19 17:35 UTC | 1h 4m |
| N82123 |  | Norman Y Mineta San Jose International Airport (KSJC) | Sacramento Mather Airport (KMHR) | 2026-08-19 16:58 UTC | 2026-08-19 17:29 UTC | 30m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-19 14:03 UTC | 2026-08-19 17:27 UTC | 3h 24m |
| ECNGI | ECN | Lousa Private Airport (LPLZ) | Viseu Airport (LPVZ) | 2026-08-19 16:41 UTC | 2026-08-19 17:27 UTC | 45m |
| N75602 |  | Rachel's Landing Airport (8TN6) | Murfreesboro Municipal Airport (KMBT) | 2026-08-19 17:17 UTC | 2026-08-19 17:25 UTC | 7m |
| N616PW |  | UT99 (UT99) | UT99 (UT99) | 2026-08-19 16:20 UTC | 2026-08-19 17:24 UTC | 1h 3m |
| N883MT |  | Flying E Ranch Airport (OK16) | Drake Field (KFYV) | 2026-08-19 16:49 UTC | 2026-08-19 17:24 UTC | 34m |
| N2366W |  | Trenton-Robbinsville Airport (KN87) | Trenton-Robbinsville Airport (KN87) | 2026-08-19 16:36 UTC | 2026-08-19 17:21 UTC | 44m |
| N127CA |  | Scottsdale Airport (KSDL) | Wickenburg Municipal Airport (KE25) | 2026-08-19 16:53 UTC | 2026-08-19 17:20 UTC | 26m |
| N51ZM |  | Boise Air Trml/Gowen Field (KBOI) | Mountain Home Municipal Airport (KU76) | 2026-08-19 17:07 UTC | 2026-08-19 17:19 UTC | 12m |
| N893QA |  | Henderson Executive Airport (KHND) | Grand Canyon West Airport (K1G4) | 2026-08-19 16:31 UTC | 2026-08-19 17:19 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_19:31:03_UTC-green)

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

**Latest saved flight:** 2026-08-20 19:31:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 19:31:03 UTC

- **220,205** saved flights
- **69,090** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **220,205** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,651,230.3 tonnes** estimated CO2 emissions
- **153,694,512 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8829 |
| 2 | SkyWest Airlines | 7842 |
| 3 | EJA | 4271 |
| 4 | IndiGo | 3732 |
| 5 | American Airlines | 3653 |
| 6 | Southwest Airlines | 3481 |
| 7 | Delta Air Lines | 2837 |
| 8 | ENY | 2714 |
| 9 | LATAM Airlines | 2091 |
| 10 | AZU | 2017 |
| 11 | Vueling | 1855 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1762 |
| 14 | LXJ | 1739 |
| 15 | easyJet | 1528 |
| 16 | Swiss International | 1465 |
| 17 | AXM | 1445 |
| 18 | United Airlines | 1385 |
| 19 | QLK | 1375 |
| 20 | EJU | 1372 |
| 21 | Alaska Airlines | 1342 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1203 |
| 24 | VIV | 1202 |
| 25 | Air France | 1196 |
| 26 | PGT | 1193 |
| 27 | WMT | 1160 |
| 28 | Wizz Air | 1122 |
| 29 | JetBlue | 1116 |
| 30 | AEE | 1104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 185281 |
| 2 | 🇪🇸 ES | 14124 |
| 3 | 🇧🇷 BR | 12717 |
| 4 | 🇦🇺 AU | 12418 |
| 5 | 🇨🇦 CA | 12149 |
| 6 | 🇮🇹 IT | 11726 |
| 7 | 🇮🇳 IN | 11635 |
| 8 | 🇩🇪 DE | 10887 |
| 9 | 🇬🇧 GB | 10346 |
| 10 | 🇨🇴 CO | 9035 |
| 11 | 🇯🇵 JP | 8963 |
| 12 | 🇫🇷 FR | 8776 |
| 13 | 🇬🇷 GR | 6430 |
| 14 | 🇹🇷 TR | 6338 |
| 15 | 🇲🇽 MX | 6116 |
| 16 | 🇨🇭 CH | 5826 |
| 17 | 🇳🇴 NO | 5479 |
| 18 | 🇲🇾 MY | 3820 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇹🇭 TH | 3655 |
| 21 | 🇵🇱 PL | 3652 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2961 |
| 24 | 🇬🇹 GT | 2785 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2444 |
| 27 | 🇲🇦 MA | 2218 |
| 28 | 🇳🇱 NL | 1958 |
| 29 | 🇲🇪 ME | 1947 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4621 |
| 2 | Denver International Airport |  | US | 3592 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2668 |
| 5 | Guaymaral Airport |  | CO | 2600 |
| 6 | Harry Reid International Airport |  | US | 2422 |
| 7 | Zurich Airport |  | CH | 2287 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2260 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2238 |
| 10 | La Aurora Airport |  | GT | 2122 |
| 11 | El Dorado International Airport |  | CO | 2058 |
| 12 | Chicago O'Hare International Airport |  | US | 2017 |
| 13 | Salt Lake City International Airport |  | US | 1940 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1906 |
| 15 | Congonhas Airport |  | BR | 1861 |
| 16 | Frankfurt am Main International Airport |  | DE | 1796 |
| 17 | Madrid Barajas International Airport |  | ES | 1730 |
| 18 | Capua Airport |  | IT | 1682 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1652 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1624 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1619 |
| 22 | Macau International Airport |  | MO | 1580 |
| 23 | Malpensa International Airport |  | IT | 1547 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1517 |
| 26 | Charlotte/Douglas International Airport |  | US | 1466 |
| 27 | Ninoy Aquino International Airport |  | PH | 1408 |
| 28 | Kuala Lumpur International Airport |  | MY | 1403 |
| 29 | Barcelona International Airport |  | ES | 1351 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1337 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1309 |
| 33 | Seattle-Tacoma International Airport |  | US | 1301 |
| 34 | Viracopos International Airport |  | BR | 1290 |
| 35 | Calgary International Airport |  | CA | 1243 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1225 |
| 37 | Oslo Gardermoen Airport |  | NO | 1223 |
| 38 | Vitoria/Foronda Airport |  | ES | 1223 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1182 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1062 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 790 | 21m | 244 km | 3,326.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 498 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 495 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 370 | 27m | 275 km | 1,753.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 325 | 1h 50m | 1,423 km | 7,976.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 323 | 44m | 241 km | 1,341.7 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 274 | 1h 38m | 1,156 km | 5,466.2 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 273 | 24m | 218 km | 1,028.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 259 | 1h 14m | 961 km | 4,293.1 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 247 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK139 | CXK | Brunswick Golden Isles Airport (KBQK) | Brunswick Golden Isles Airport (KBQK) | 2026-08-20 19:17 UTC | 2026-08-20 19:31 UTC | 13m |
| N580JH |  | K4R4 (K4R4) | Auburn University Regional Airport (KAUO) | 2026-08-20 18:47 UTC | 2026-08-20 19:29 UTC | 42m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-20 18:45 UTC | 2026-08-20 19:28 UTC | 43m |
| N172SX |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-20 18:34 UTC | 2026-08-20 19:28 UTC | 53m |
| BTZ159 | BTZ | South Lafourche Leonard Miller Jr Airport (KGAO) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-08-20 19:06 UTC | 2026-08-20 19:21 UTC | 14m |
| N111XX |  | Yuba County Airport (KMYV) | San Carlos Airport (KSQL) | 2026-08-20 18:44 UTC | 2026-08-20 19:21 UTC | 37m |
| N248PA |  | Lanai Airport (PHNY) | Kawaihapai Airfield (PHDH) | 2026-08-20 19:06 UTC | 2026-08-20 19:17 UTC | 10m |
| N322CG |  | Flying Cloud Airport (KFCM) | 98IN (98IN) | 2026-08-20 18:10 UTC | 2026-08-20 19:11 UTC | 1h 0m |
| DRACO51 | DRA | 4XA5 (4XA5) | Ramsak Airport (OK67) | 2026-08-20 18:35 UTC | 2026-08-20 19:04 UTC | 28m |
| N356CT |  | Montgomery-Gibbs Executive Airport (KMYF) | Ramona Airport (KRNM) | 2026-08-20 17:20 UTC | 2026-08-20 18:36 UTC | 1h 16m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-08-20 18:23 UTC | 2026-08-20 18:35 UTC | 11m |
| CODE21 | COD | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-08-20 18:11 UTC | 2026-08-20 18:31 UTC | 20m |
|  |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Pinyon Airport (CO43) | 2026-08-20 16:38 UTC | 2026-08-20 18:26 UTC | 1h 48m |
| N251SF |  | Dupage Airport (KDPA) | Vodden Airport (IS15) | 2026-08-20 17:52 UTC | 2026-08-20 18:25 UTC | 32m |
| N143ME |  | Plymouth Municipal Airport (KC65) | Plymouth Municipal Airport (KC65) | 2026-08-20 17:57 UTC | 2026-08-20 18:25 UTC | 27m |
| N13232 |  | Northampton Airport (K7B2) | Northampton Airport (K7B2) | 2026-08-20 18:20 UTC | 2026-08-20 18:21 UTC | 0m |
| N5184J |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-08-20 17:38 UTC | 2026-08-20 18:19 UTC | 40m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-08-20 17:55 UTC | 2026-08-20 18:17 UTC | 21m |
| N8710U |  | Savannah/Hilton Head International Airport (KSAV) | Briar Patch Airport (9GA1) | 2026-08-20 17:40 UTC | 2026-08-20 18:17 UTC | 36m |
| URSA02 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-20 17:47 UTC | 2026-08-20 18:16 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

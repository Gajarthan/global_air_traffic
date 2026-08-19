# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_14:19:57_UTC-green)

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

**Latest saved flight:** 2026-08-19 14:19:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 14:19:57 UTC

- **215,812** saved flights
- **68,191** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **215,812** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,597,414.2 tonnes** estimated CO2 emissions
- **150,574,735 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8626 |
| 2 | SkyWest Airlines | 7705 |
| 3 | EJA | 4188 |
| 4 | IndiGo | 3683 |
| 5 | American Airlines | 3587 |
| 6 | Southwest Airlines | 3434 |
| 7 | Delta Air Lines | 2787 |
| 8 | ENY | 2661 |
| 9 | LATAM Airlines | 2043 |
| 10 | AZU | 1969 |
| 11 | Vueling | 1817 |
| 12 | Lufthansa | 1808 |
| 13 | WIF | 1728 |
| 14 | LXJ | 1698 |
| 15 | easyJet | 1501 |
| 16 | Swiss International | 1438 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1365 |
| 19 | QLK | 1346 |
| 20 | EJU | 1344 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1183 |
| 24 | PGT | 1173 |
| 25 | Air France | 1166 |
| 26 | GLO | 1166 |
| 27 | WMT | 1126 |
| 28 | JetBlue | 1098 |
| 29 | Wizz Air | 1096 |
| 30 | AEE | 1085 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181750 |
| 2 | 🇪🇸 ES | 13856 |
| 3 | 🇧🇷 BR | 12407 |
| 4 | 🇦🇺 AU | 12161 |
| 5 | 🇨🇦 CA | 11876 |
| 6 | 🇮🇳 IN | 11469 |
| 7 | 🇮🇹 IT | 11437 |
| 8 | 🇩🇪 DE | 10713 |
| 9 | 🇬🇧 GB | 10128 |
| 10 | 🇯🇵 JP | 8868 |
| 11 | 🇨🇴 CO | 8801 |
| 12 | 🇫🇷 FR | 8620 |
| 13 | 🇬🇷 GR | 6328 |
| 14 | 🇹🇷 TR | 6201 |
| 15 | 🇲🇽 MX | 6029 |
| 16 | 🇨🇭 CH | 5742 |
| 17 | 🇳🇴 NO | 5366 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3667 |
| 20 | 🇵🇱 PL | 3568 |
| 21 | 🇹🇭 TH | 3529 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2739 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2364 |
| 27 | 🇲🇦 MA | 2172 |
| 28 | 🇳🇱 NL | 1928 |
| 29 | 🇲🇪 ME | 1879 |
| 30 | 🇮🇩 ID | 1814 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4517 |
| 2 | Denver International Airport |  | US | 3509 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2620 |
| 5 | Guaymaral Airport |  | CO | 2570 |
| 6 | Harry Reid International Airport |  | US | 2400 |
| 7 | Zurich Airport |  | CH | 2244 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2213 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2208 |
| 10 | La Aurora Airport |  | GT | 2082 |
| 11 | El Dorado International Airport |  | CO | 2012 |
| 12 | Chicago O'Hare International Airport |  | US | 1984 |
| 13 | Salt Lake City International Airport |  | US | 1901 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1807 |
| 16 | Frankfurt am Main International Airport |  | DE | 1767 |
| 17 | Madrid Barajas International Airport |  | ES | 1687 |
| 18 | Capua Airport |  | IT | 1641 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1626 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1608 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1584 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 24 | Malpensa International Airport |  | IT | 1513 |
| 25 | Charles de Gaulle International Airport |  | FR | 1483 |
| 26 | Charlotte/Douglas International Airport |  | US | 1448 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1323 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 31 | Bengaluru International Airport |  | IN | 1313 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1289 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1259 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1197 |
| 37 | Vitoria/Foronda Airport |  | ES | 1192 |
| 38 | Don Mueang International Airport |  | TH | 1165 |
| 39 | Reno/Tahoe International Airport |  | US | 1164 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1164 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1051 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 770 | 21m | 244 km | 3,242.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 484 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 465 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 358 | 27m | 275 km | 1,696.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 316 | 1h 49m | 1,423 km | 7,755.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 283 | 21m | 250 km | 1,222.4 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 269 | 19m | 99 km | 460.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 264 | 27m | 215 km | 977.7 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 255 | 1h 14m | 961 km | 4,226.8 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 254 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 246 | 19m | 144 km | 611.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 231 | 44m | 555 km | 2,211.9 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GCEWM | GCE | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-19 13:47 UTC | 2026-08-19 14:19 UTC | 32m |
| AUB1320 | AUB | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-08-19 13:55 UTC | 2026-08-19 14:18 UTC | 22m |
| CCA908 | Air China | Madrid Barajas International Airport (LEMD) | Smolensk North Airport (XUBS) | 2026-08-19 11:18 UTC | 2026-08-19 14:16 UTC | 2h 57m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-19 12:44 UTC | 2026-08-19 14:14 UTC | 1h 30m |
| N3300D |  | Crisp County-Cordele Airport (KCKF) | Crisp County-Cordele Airport (KCKF) | 2026-08-19 13:53 UTC | 2026-08-19 14:14 UTC | 20m |
| BOX502 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-08-19 03:54 UTC | 2026-08-19 14:10 UTC | 10h 16m |
| N769FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-08-19 13:14 UTC | 2026-08-19 14:06 UTC | 52m |
| DKH1662 | DKH | Manchester Airport (EGCC) | Ukhta Airport (UUYH) | 2026-08-19 10:27 UTC | 2026-08-19 14:04 UTC | 3h 37m |
| N2028W |  | Al Divine Airport (65CL) | Meadows Field (KBFL) | 2026-08-19 13:30 UTC | 2026-08-19 14:03 UTC | 33m |
| XSN37 | XSN | Charles M Schulz/Sonoma County Airport (KSTS) | Truckee-Tahoe Airport (KTRK) | 2026-08-19 13:18 UTC | 2026-08-19 13:59 UTC | 41m |
| BELIGOUC | Brussels Airlines | Lanveoc-Poulmic Air Base (LFRL) | Lanveoc-Poulmic Air Base (LFRL) | 2026-08-19 13:06 UTC | 2026-08-19 13:59 UTC | 53m |
| ZUMTS | ZUM | Grand Central Airport (FAGC) | Grand Central Airport (FAGC) | 2026-08-19 13:29 UTC | 2026-08-19 13:59 UTC | 29m |
| N922ST |  | Wallom Field (8CA8) | Truckee-Tahoe Airport (KTRK) | 2026-08-19 13:25 UTC | 2026-08-19 13:59 UTC | 33m |
| XAAVA | XAA | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | Licenciado Benito Juarez International Airport (MMMX) | 2026-08-19 13:52 UTC | 2026-08-19 13:57 UTC | 5m |
| N482WT |  | The Eastern Iowa Airport (KCID) | Iowa City Municipal Airport (KIOW) | 2026-08-19 13:41 UTC | 2026-08-19 13:53 UTC | 12m |
| N543TH |  | Trenton Mercer Airport (KTTN) | Central Jersey Regional Airport (K47N) | 2026-08-19 13:05 UTC | 2026-08-19 13:51 UTC | 45m |
| N403TD |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-08-19 13:41 UTC | 2026-08-19 13:48 UTC | 6m |
| N221MJ |  | Fulton County Executive/Charlie Brown Field (KFTY) | Austin-Bergstrom International Airport (KAUS) | 2026-08-19 11:58 UTC | 2026-08-19 13:47 UTC | 1h 49m |
| CO75 |  | Pirassununga Airport (SDPY) | Pirassununga Airport (SDPY) | 2026-08-19 13:42 UTC | 2026-08-19 13:46 UTC | 4m |
| DREAD81 | DRE | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | KNQB (KNQB) | 2026-08-19 13:12 UTC | 2026-08-19 13:45 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

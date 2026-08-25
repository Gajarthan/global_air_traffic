# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_20:52:07_UTC-green)

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

**Latest saved flight:** 2026-08-25 20:52:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 20:52:07 UTC

- **236,625** saved flights
- **72,241** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **236,625** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,849,878.2 tonnes** estimated CO2 emissions
- **165,210,329 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9494 |
| 2 | SkyWest Airlines | 8358 |
| 3 | EJA | 4597 |
| 4 | IndiGo | 3986 |
| 5 | American Airlines | 3844 |
| 6 | Southwest Airlines | 3609 |
| 7 | Delta Air Lines | 3017 |
| 8 | ENY | 2871 |
| 9 | LATAM Airlines | 2269 |
| 10 | AZU | 2208 |
| 11 | Vueling | 2027 |
| 12 | Lufthansa | 1920 |
| 13 | WIF | 1881 |
| 14 | LXJ | 1849 |
| 15 | easyJet | 1654 |
| 16 | Swiss International | 1588 |
| 17 | AXM | 1576 |
| 18 | EJU | 1520 |
| 19 | United Airlines | 1499 |
| 20 | QLK | 1497 |
| 21 | Alaska Airlines | 1421 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1323 |
| 24 | GLO | 1320 |
| 25 | VIV | 1306 |
| 26 | PGT | 1290 |
| 27 | Air France | 1284 |
| 28 | Wizz Air | 1267 |
| 29 | JetBlue | 1177 |
| 30 | AEE | 1175 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 196645 |
| 2 | 🇪🇸 ES | 15210 |
| 3 | 🇧🇷 BR | 13819 |
| 4 | 🇦🇺 AU | 13340 |
| 5 | 🇨🇦 CA | 13082 |
| 6 | 🇮🇹 IT | 12919 |
| 7 | 🇮🇳 IN | 12420 |
| 8 | 🇩🇪 DE | 11660 |
| 9 | 🇬🇧 GB | 11169 |
| 10 | 🇨🇴 CO | 10041 |
| 11 | 🇯🇵 JP | 9546 |
| 12 | 🇫🇷 FR | 9501 |
| 13 | 🇹🇷 TR | 7026 |
| 14 | 🇬🇷 GR | 6978 |
| 15 | 🇲🇽 MX | 6572 |
| 16 | 🇨🇭 CH | 6321 |
| 17 | 🇳🇴 NO | 5862 |
| 18 | 🇲🇾 MY | 4225 |
| 19 | 🇹🇭 TH | 4219 |
| 20 | 🇿🇦 ZA | 4147 |
| 21 | 🇵🇱 PL | 3943 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2964 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2731 |
| 27 | 🇲🇦 MA | 2394 |
| 28 | 🇲🇪 ME | 2202 |
| 29 | 🇳🇱 NL | 2124 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4912 |
| 2 | Denver International Airport |  | US | 3837 |
| 3 | Indira Gandhi International Airport |  | IN | 2884 |
| 4 | Tokyo International Airport |  | JP | 2843 |
| 5 | Guaymaral Airport |  | CO | 2686 |
| 6 | Harry Reid International Airport |  | US | 2531 |
| 7 | Zurich Airport |  | CH | 2477 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2423 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2369 |
| 10 | La Aurora Airport |  | GT | 2260 |
| 11 | El Dorado International Airport |  | CO | 2251 |
| 12 | Chicago O'Hare International Airport |  | US | 2129 |
| 13 | Salt Lake City International Airport |  | US | 2087 |
| 14 | Congonhas Airport |  | BR | 2016 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1982 |
| 16 | Frankfurt am Main International Airport |  | DE | 1878 |
| 17 | Capua Airport |  | IT | 1863 |
| 18 | Madrid Barajas International Airport |  | ES | 1860 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1779 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1746 |
| 21 | Malpensa International Airport |  | IT | 1696 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1678 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1646 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1524 |
| 29 | Barcelona International Airport |  | ES | 1498 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1479 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1435 |
| 32 | Viracopos International Airport |  | BR | 1413 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1386 |
| 34 | Bengaluru International Airport |  | IN | 1384 |
| 35 | Seattle-Tacoma International Airport |  | US | 1383 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1352 |
| 38 | Oslo Gardermoen Airport |  | NO | 1328 |
| 39 | Vancouver International Airport |  | CA | 1292 |
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
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 318 | 24m | 218 km | 1,198.0 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 315 | 1h 40m | 1,156 km | 6,284.1 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 314 | 22m | 55 km | 298.4 t |
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
| N897MT |  | Coulter Field (KCFD) | Easterwood Field (KCLL) | 2026-08-25 20:39 UTC | 2026-08-25 20:52 UTC | 12m |
| SHWK413 | SHW | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-25 19:00 UTC | 2026-08-25 20:49 UTC | 1h 49m |
| VOID21 | VOI | Danaher Airport (7TX0) | Joseph Of Cupertino Stolport Airport (TS20) | 2026-08-25 20:27 UTC | 2026-08-25 20:42 UTC | 14m |
| N1784Q |  | Warrenton/Fauquier Airport (KHWY) | 02VA (02VA) | 2026-08-25 20:08 UTC | 2026-08-25 20:40 UTC | 32m |
| BCS822 | BCS | Leipzig Halle Airport (EDDP) | Malpensa International Airport (LIMC) | 2026-08-25 19:25 UTC | 2026-08-25 20:40 UTC | 1h 15m |
| MAFIA31 | MAF | Laughlin Afb Aux Nr 1 Airport (KT70) | Maverick County Memorial International Airport (K5T9) | 2026-08-25 20:28 UTC | 2026-08-25 20:40 UTC | 11m |
| N445MK |  | Wood County Regional Airport (K1G0) | Wood County Regional Airport (K1G0) | 2026-08-25 20:12 UTC | 2026-08-25 20:39 UTC | 26m |
| ACA7 | Air Canada | Vancouver International Airport (CYVR) | Zhuhai Airport (ZGSD) | 2026-08-25 08:20 UTC | 2026-08-25 20:38 UTC | 12h 18m |
| N2159H |  | Beverly Regional Airport (KBVY) | Lawrence Municipal Airport (KLWM) | 2026-08-25 20:06 UTC | 2026-08-25 20:37 UTC | 31m |
| N782LA |  | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-08-25 19:50 UTC | 2026-08-25 20:37 UTC | 46m |
| N193TH |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-25 19:51 UTC | 2026-08-25 20:33 UTC | 41m |
| N876AD |  | Drummondville Airport (CSC3) | London Airport (CYXU) | 2026-08-25 19:18 UTC | 2026-08-25 20:30 UTC | 1h 11m |
| 5611 |  | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-08-25 20:00 UTC | 2026-08-25 20:28 UTC | 28m |
| N110UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-08-25 19:44 UTC | 2026-08-25 20:27 UTC | 42m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-08-25 06:10 UTC | 2026-08-25 20:26 UTC | 14h 16m |
| N58AY |  | Burke Lakefront Airport (KBKL) | Monmouth Executive Airport (KBLM) | 2026-08-25 19:02 UTC | 2026-08-25 20:23 UTC | 1h 20m |
| N610FA |  | Wings Field (KLOM) | Wings Field (KLOM) | 2026-08-25 20:17 UTC | 2026-08-25 20:22 UTC | 4m |
| N750BB |  | LA48 (LA48) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-08-25 19:49 UTC | 2026-08-25 20:20 UTC | 30m |
| N93ME |  | Josephine Ranch Airport (2ID3) | Josephine Ranch Airport (2ID3) | 2026-08-25 20:05 UTC | 2026-08-25 20:19 UTC | 13m |
| N8024Q |  | Trenton Mercer Airport (KTTN) | Ocean County Airport (KMJX) | 2026-08-25 19:26 UTC | 2026-08-25 20:16 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

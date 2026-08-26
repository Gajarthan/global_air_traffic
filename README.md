# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_16:08:26_UTC-green)

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

**Latest saved flight:** 2026-08-26 16:08:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 16:08:26 UTC

- **238,996** saved flights
- **72,692** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **238,996** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,879,170.6 tonnes** estimated CO2 emissions
- **166,908,441 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9601 |
| 2 | SkyWest Airlines | 8398 |
| 3 | EJA | 4621 |
| 4 | IndiGo | 4035 |
| 5 | American Airlines | 3860 |
| 6 | Southwest Airlines | 3614 |
| 7 | Delta Air Lines | 3040 |
| 8 | ENY | 2889 |
| 9 | LATAM Airlines | 2296 |
| 10 | AZU | 2226 |
| 11 | Vueling | 2059 |
| 12 | Lufthansa | 1935 |
| 13 | WIF | 1899 |
| 14 | LXJ | 1853 |
| 15 | easyJet | 1666 |
| 16 | Swiss International | 1610 |
| 17 | AXM | 1591 |
| 18 | EJU | 1534 |
| 19 | QLK | 1527 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1430 |
| 22 | All Nippon Airways | 1422 |
| 23 | WMT | 1344 |
| 24 | GLO | 1334 |
| 25 | VIV | 1314 |
| 26 | Air France | 1307 |
| 27 | PGT | 1305 |
| 28 | Wizz Air | 1281 |
| 29 | AEE | 1186 |
| 30 | JetBlue | 1183 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197899 |
| 2 | 🇪🇸 ES | 15391 |
| 3 | 🇧🇷 BR | 13949 |
| 4 | 🇦🇺 AU | 13573 |
| 5 | 🇨🇦 CA | 13225 |
| 6 | 🇮🇹 IT | 13078 |
| 7 | 🇮🇳 IN | 12568 |
| 8 | 🇩🇪 DE | 11816 |
| 9 | 🇬🇧 GB | 11291 |
| 10 | 🇨🇴 CO | 10193 |
| 11 | 🇯🇵 JP | 9652 |
| 12 | 🇫🇷 FR | 9631 |
| 13 | 🇹🇷 TR | 7101 |
| 14 | 🇬🇷 GR | 7045 |
| 15 | 🇲🇽 MX | 6613 |
| 16 | 🇨🇭 CH | 6421 |
| 17 | 🇳🇴 NO | 5920 |
| 18 | 🇹🇭 TH | 4338 |
| 19 | 🇲🇾 MY | 4263 |
| 20 | 🇿🇦 ZA | 4203 |
| 21 | 🇵🇱 PL | 3985 |
| 22 | 🇵🇭 PH | 3294 |
| 23 | 🇳🇿 NZ | 3291 |
| 24 | 🇬🇹 GT | 2998 |
| 25 | 🇰🇷 KR | 2842 |
| 26 | 🇭🇷 HR | 2768 |
| 27 | 🇲🇦 MA | 2420 |
| 28 | 🇲🇪 ME | 2235 |
| 29 | 🇳🇱 NL | 2163 |
| 30 | 🇮🇩 ID | 2101 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4943 |
| 2 | Denver International Airport |  | US | 3856 |
| 3 | Indira Gandhi International Airport |  | IN | 2923 |
| 4 | Tokyo International Airport |  | JP | 2873 |
| 5 | Guaymaral Airport |  | CO | 2692 |
| 6 | Harry Reid International Airport |  | US | 2545 |
| 7 | Zurich Airport |  | CH | 2508 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2441 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2388 |
| 10 | El Dorado International Airport |  | CO | 2296 |
| 11 | La Aurora Airport |  | GT | 2288 |
| 12 | Chicago O'Hare International Airport |  | US | 2135 |
| 13 | Salt Lake City International Airport |  | US | 2097 |
| 14 | Congonhas Airport |  | BR | 2033 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1989 |
| 16 | Frankfurt am Main International Airport |  | DE | 1895 |
| 17 | Capua Airport |  | IT | 1885 |
| 18 | Madrid Barajas International Airport |  | ES | 1878 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1803 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1760 |
| 21 | Malpensa International Airport |  | IT | 1716 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1684 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1680 |
| 24 | Charles de Gaulle International Airport |  | FR | 1672 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1598 |
| 27 | Kuala Lumpur International Airport |  | MY | 1540 |
| 28 | Charlotte/Douglas International Airport |  | US | 1531 |
| 29 | Barcelona International Airport |  | ES | 1524 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1504 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1446 |
| 32 | Viracopos International Airport |  | BR | 1426 |
| 33 | Don Mueang International Airport |  | TH | 1400 |
| 34 | Bengaluru International Airport |  | IN | 1399 |
| 35 | Seattle-Tacoma International Airport |  | US | 1392 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 37 | Calgary International Airport |  | CA | 1370 |
| 38 | Oslo Gardermoen Airport |  | NO | 1344 |
| 39 | O. R. Tambo International Airport |  | ZA | 1310 |
| 40 | Vancouver International Airport |  | CA | 1308 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1090 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 878 | 21m | 244 km | 3,697.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 4 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 608 | 8m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 607 | 1h 6m | 770 km | 8,063.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 540 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 396 | 27m | 275 km | 1,876.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 373 | 1h 50m | 1,423 km | 9,154.0 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 361 | 44m | 555 km | 3,456.7 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 346 | 44m | 241 km | 1,437.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 343 | 21m | 250 km | 1,481.6 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 324 | 24m | 218 km | 1,220.6 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 319 | 22m | 55 km | 303.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 318 | 1h 40m | 1,156 km | 6,344.0 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 297 | 19m | 99 km | 508.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 270 | 19m | 144 km | 671.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 256 | 1h 50m | 1,304 km | 5,759.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N171DS |  | Delaware Airpark (K33N) | Ocean City Municipal Airport (KOXB) | 2026-08-26 15:31 UTC | 2026-08-26 16:08 UTC | 36m |
| JUMP14 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-08-26 15:48 UTC | 2026-08-26 16:05 UTC | 16m |
| AIP9936 | AIP | Salt Lake City International Airport (KSLC) | Evanston-Uinta County Burns Field (KEVW) | 2026-08-26 15:51 UTC | 2026-08-26 16:03 UTC | 12m |
| N1330N |  | Centennial Airport (KAPA) | Southeast Colorado Regional Airport (KLAA) | 2026-08-26 14:48 UTC | 2026-08-26 15:59 UTC | 1h 10m |
| SMGLR58 | SMG | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-08-26 15:37 UTC | 2026-08-26 15:59 UTC | 21m |
| N577GA |  | Savannah/Hilton Head International Airport (KSAV) | Savannah/Hilton Head International Airport (KSAV) | 2026-08-26 15:36 UTC | 2026-08-26 15:58 UTC | 21m |
| LTG8503 | LTG | Miami International Airport (KMIA) | Brussels Airport (EBBR) | 2026-08-26 07:46 UTC | 2026-08-26 15:56 UTC | 8h 9m |
| N13232 |  | Westfield-Barnes Regional Airport (KBAF) | Westfield-Barnes Regional Airport (KBAF) | 2026-08-26 15:36 UTC | 2026-08-26 15:56 UTC | 19m |
| N125Z |  | True Grit South Airport (CO95) | Flying M & M Ranch Airport (0CO6) | 2026-08-26 15:32 UTC | 2026-08-26 15:54 UTC | 22m |
| N422WA |  | Hermitage Airport (45CN) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-26 15:22 UTC | 2026-08-26 15:53 UTC | 30m |
| N696MA |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-08-26 15:24 UTC | 2026-08-26 15:52 UTC | 27m |
| EDGE91 | EDG | 4XA5 (4XA5) | Chattanooga Sky Harbor Airport (K92F) | 2026-08-26 15:15 UTC | 2026-08-26 15:50 UTC | 35m |
| N332BG |  | Wood County Regional Airport (K1G0) | Wood County Regional Airport (K1G0) | 2026-08-26 14:00 UTC | 2026-08-26 15:47 UTC | 1h 47m |
| N445AF |  | Norwood Memorial Airport (KOWD) | Norwood Memorial Airport (KOWD) | 2026-08-26 15:06 UTC | 2026-08-26 15:47 UTC | 40m |
| LN279AH |  | West Virginia International Yeager Airport (KCRW) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-26 15:12 UTC | 2026-08-26 15:45 UTC | 33m |
| GCM123 | GCM | Manchester Airport (EGCC) | Manchester Airport (EGCC) | 2026-08-26 14:52 UTC | 2026-08-26 15:45 UTC | 52m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-26 14:51 UTC | 2026-08-26 15:43 UTC | 52m |
| ANE2442 | ANE | Requena Airport (LERE) | Menorca Airport (LEMH) | 2026-08-26 14:58 UTC | 2026-08-26 15:37 UTC | 39m |
| AUR209 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-08-26 15:22 UTC | 2026-08-26 15:37 UTC | 14m |
| N530PS |  | KFTG (KFTG) | KFTG (KFTG) | 2026-08-26 15:32 UTC | 2026-08-26 15:36 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

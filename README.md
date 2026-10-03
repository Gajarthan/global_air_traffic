# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_22:50:53_UTC-green)

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

**Latest saved flight:** 2026-10-03 22:50:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-03 22:50:53 UTC

- **275,816** saved flights
- **80,301** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **275,816** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,338,558.6 tonnes** estimated CO2 emissions
- **193,539,632 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10811 |
| 2 | SkyWest Airlines | 9602 |
| 3 | EJA | 5405 |
| 4 | IndiGo | 4594 |
| 5 | American Airlines | 4270 |
| 6 | Southwest Airlines | 4052 |
| 7 | Delta Air Lines | 3427 |
| 8 | ENY | 3225 |
| 9 | LATAM Airlines | 2672 |
| 10 | AZU | 2594 |
| 11 | Vueling | 2285 |
| 12 | WIF | 2242 |
| 13 | LXJ | 2181 |
| 14 | Lufthansa | 2074 |
| 15 | easyJet | 1833 |
| 16 | Swiss International | 1805 |
| 17 | QLK | 1776 |
| 18 | EJU | 1714 |
| 19 | AXM | 1689 |
| 20 | United Airlines | 1681 |
| 21 | Alaska Airlines | 1626 |
| 22 | All Nippon Airways | 1572 |
| 23 | PGT | 1551 |
| 24 | GLO | 1540 |
| 25 | WMT | 1534 |
| 26 | VIV | 1512 |
| 27 | Air France | 1511 |
| 28 | Wizz Air | 1489 |
| 29 | CXK | 1362 |
| 30 | AEE | 1311 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 230198 |
| 2 | 🇪🇸 ES | 17247 |
| 3 | 🇧🇷 BR | 16197 |
| 4 | 🇦🇺 AU | 15896 |
| 5 | 🇨🇦 CA | 15371 |
| 6 | 🇮🇹 IT | 14860 |
| 7 | 🇮🇳 IN | 14539 |
| 8 | 🇩🇪 DE | 13178 |
| 9 | 🇨🇴 CO | 12812 |
| 10 | 🇬🇧 GB | 12699 |
| 11 | 🇫🇷 FR | 10898 |
| 12 | 🇯🇵 JP | 10504 |
| 13 | 🇹🇷 TR | 8331 |
| 14 | 🇬🇷 GR | 7910 |
| 15 | 🇲🇽 MX | 7621 |
| 16 | 🇨🇭 CH | 7325 |
| 17 | 🇳🇴 NO | 6800 |
| 18 | 🇹🇭 TH | 4936 |
| 19 | 🇲🇾 MY | 4576 |
| 20 | 🇿🇦 ZA | 4562 |
| 21 | 🇵🇱 PL | 4502 |
| 22 | 🇳🇿 NZ | 3907 |
| 23 | 🇵🇭 PH | 3638 |
| 24 | 🇬🇹 GT | 3462 |
| 25 | 🇭🇷 HR | 3137 |
| 26 | 🇰🇷 KR | 3101 |
| 27 | 🇲🇦 MA | 2722 |
| 28 | 🇲🇪 ME | 2588 |
| 29 | 🇳🇱 NL | 2462 |
| 30 | 🇮🇩 ID | 2279 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5597 |
| 2 | Denver International Airport |  | US | 4502 |
| 3 | Indira Gandhi International Airport |  | IN | 3285 |
| 4 | Tokyo International Airport |  | JP | 3150 |
| 5 | El Dorado International Airport |  | CO | 3064 |
| 6 | Harry Reid International Airport |  | US | 2972 |
| 7 | Zurich Airport |  | CH | 2865 |
| 8 | Guaymaral Airport |  | CO | 2853 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2756 |
| 10 | La Aurora Airport |  | GT | 2634 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2631 |
| 12 | Salt Lake City International Airport |  | US | 2454 |
| 13 | Congonhas Airport |  | BR | 2355 |
| 14 | Chicago O'Hare International Airport |  | US | 2328 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2257 |
| 16 | Capua Airport |  | IT | 2141 |
| 17 | Madrid Barajas International Airport |  | ES | 2124 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2106 |
| 19 | Frankfurt am Main International Airport |  | DE | 2072 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1958 |
| 22 | Malpensa International Airport |  | IT | 1949 |
| 23 | Charles de Gaulle International Airport |  | FR | 1949 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1840 |
| 26 | Macau International Airport |  | MO | 1796 |
| 27 | Ninoy Aquino International Airport |  | PH | 1789 |
| 28 | Charlotte/Douglas International Airport |  | US | 1722 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1714 |
| 30 | Barcelona International Airport |  | ES | 1701 |
| 31 | Viracopos International Airport |  | BR | 1652 |
| 32 | Kuala Lumpur International Airport |  | MY | 1640 |
| 33 | Seattle-Tacoma International Airport |  | US | 1622 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1620 |
| 35 | Calgary International Airport |  | CA | 1567 |
| 36 | Don Mueang International Airport |  | TH | 1557 |
| 37 | Oslo Gardermoen Airport |  | NO | 1546 |
| 38 | Vancouver International Airport |  | CA | 1545 |
| 39 | Bengaluru International Airport |  | IN | 1541 |
| 40 | Reno/Tahoe International Airport |  | US | 1496 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1134 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1041 | 21m | 244 km | 4,383.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 697 | 1h 6m | 770 km | 9,259.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 694 | 24m | 225 km | 2,692.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 614 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 444 | 27m | 275 km | 2,103.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 435 | 1h 50m | 1,423 km | 10,675.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 423 | 44m | 241 km | 1,757.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 395 | 24m | 218 km | 1,488.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 375 | 23m | 55 km | 356.4 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 353 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 347 | 1h 6m | 706 km | 4,224.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 321 | 19m | 144 km | 798.5 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 320 | 18m | 14 km | 80.0 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 312 | 1h 14m | 961 km | 5,171.6 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 310 | 42m | 535 km | 2,863.1 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 274 | 51m | 556 km | 2,626.5 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 273 | 44m | 431 km | 2,031.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N216AP |  | Alpine County Airport (KM45) | Lake Tahoe Airport (KTVL) | 2026-10-03 22:25 UTC | 2026-10-03 22:50 UTC | 25m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-10-03 12:01 UTC | 2026-10-03 22:48 UTC | 10h 47m |
| THY170 | Turkish Airlines | Istanbul Airport (LTFM) | Zhuhai Airport (ZGSD) | 2026-10-03 13:26 UTC | 2026-10-03 22:45 UTC | 9h 19m |
| N129JM |  | Lamar Municipal Airport (KLLU) | Bill And Hillary Clinton Ntl/Adams Field (KLIT) | 2026-10-03 21:46 UTC | 2026-10-03 22:43 UTC | 56m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-10-03 11:56 UTC | 2026-10-03 22:40 UTC | 10h 44m |
| BOX748 | BOX | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-10-03 12:53 UTC | 2026-10-03 22:36 UTC | 9h 42m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-10-03 22:14 UTC | 2026-10-03 22:36 UTC | 21m |
| XKV | XKV | Narrabri Airport (YNBR) | Gunnedah Airport (YGDH) | 2026-10-03 22:16 UTC | 2026-10-03 22:35 UTC | 18m |
| N44NC |  | Lee Vining Airport (KO24) | 6CL4 (6CL4) | 2026-10-03 21:44 UTC | 2026-10-03 22:30 UTC | 46m |
| N485K |  | Marina Municipal Airport (KOAR) | Salinas Municipal Airport (KSNS) | 2026-10-03 22:16 UTC | 2026-10-03 22:29 UTC | 12m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-10-03 22:03 UTC | 2026-10-03 22:25 UTC | 21m |
| CPA696 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Zhuhai Airport (ZGSD) | 2026-10-03 17:18 UTC | 2026-10-03 22:23 UTC | 5h 5m |
| CFDJN | CFD | Victoriaville Airport (CSR3) | Victoriaville Airport (CSR3) | 2026-10-03 22:08 UTC | 2026-10-03 22:22 UTC | 14m |
| TKR10 | TKR | Mc Clellan Airfield (KMCC) | Alpine County Airport (KM45) | 2026-10-03 22:04 UTC | 2026-10-03 22:22 UTC | 17m |
| N250LG |  | Hector International Airport (KFAR) | Lake County Airport (KLXV) | 2026-10-03 20:48 UTC | 2026-10-03 22:18 UTC | 1h 29m |
| WNK | WNK | Canberra International Airport (YSCB) | Canberra International Airport (YSCB) | 2026-10-03 22:10 UTC | 2026-10-03 22:17 UTC | 6m |
| CPA732 | Cathay Pacific | Kuala Lumpur International Airport (WMKK) | Chek Lap Kok International Airport (VHHH) | 2026-10-03 18:51 UTC | 2026-10-03 22:14 UTC | 3h 22m |
| LIFELN2 | LIF | City Of Colorado Springs Municipal Airport (KCOS) | 7CO1 (7CO1) | 2026-10-03 22:00 UTC | 2026-10-03 22:14 UTC | 13m |
| LXJ608 | LXJ | Flagstaff Pulliam Airport (KFLG) | John Wayne/Orange County Airport (KSNA) | 2026-10-03 21:15 UTC | 2026-10-03 22:11 UTC | 55m |
| XFB | XFB | Elderslie Airport (YEES) | Elderslie Airport (YEES) | 2026-10-03 21:09 UTC | 2026-10-03 22:09 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

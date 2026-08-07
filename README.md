# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_07:46:30_UTC-green)

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

**Latest saved flight:** 2026-08-07 07:46:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 07:46:30 UTC

- **174,781** saved flights
- **56,506** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **174,781** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,103,174.4 tonnes** estimated CO2 emissions
- **121,923,152 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6925 |
| 2 | SkyWest Airlines | 6391 |
| 3 | EJA | 3458 |
| 4 | IndiGo | 3060 |
| 5 | Southwest Airlines | 2755 |
| 6 | American Airlines | 2735 |
| 7 | ENY | 2173 |
| 8 | Delta Air Lines | 2068 |
| 9 | LATAM Airlines | 1616 |
| 10 | Lufthansa | 1577 |
| 11 | AZU | 1545 |
| 12 | WIF | 1465 |
| 13 | Vueling | 1435 |
| 14 | LXJ | 1369 |
| 15 | AXM | 1191 |
| 16 | Swiss International | 1188 |
| 17 | easyJet | 1184 |
| 18 | QLK | 1077 |
| 19 | All Nippon Airways | 1065 |
| 20 | Alaska Airlines | 1065 |
| 21 | EJU | 1065 |
| 22 | VIV | 963 |
| 23 | Cathay Pacific | 943 |
| 24 | CXK | 927 |
| 25 | GLO | 921 |
| 26 | AEE | 912 |
| 27 | United Airlines | 907 |
| 28 | Air France | 893 |
| 29 | MXY | 882 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150412 |
| 2 | 🇪🇸 ES | 11162 |
| 3 | 🇧🇷 BR | 9948 |
| 4 | 🇦🇺 AU | 9915 |
| 5 | 🇮🇳 IN | 9589 |
| 6 | 🇨🇦 CA | 9564 |
| 7 | 🇮🇹 IT | 9008 |
| 8 | 🇩🇪 DE | 8649 |
| 9 | 🇬🇧 GB | 8078 |
| 10 | 🇯🇵 JP | 7046 |
| 11 | 🇫🇷 FR | 6919 |
| 12 | 🇨🇴 CO | 6423 |
| 13 | 🇬🇷 GR | 5076 |
| 14 | 🇲🇽 MX | 5003 |
| 15 | 🇨🇭 CH | 4609 |
| 16 | 🇳🇴 NO | 4551 |
| 17 | 🇹🇷 TR | 4299 |
| 18 | 🇲🇾 MY | 3108 |
| 19 | 🇵🇱 PL | 2915 |
| 20 | 🇿🇦 ZA | 2822 |
| 21 | 🇹🇭 TH | 2585 |
| 22 | 🇳🇿 NZ | 2551 |
| 23 | 🇵🇭 PH | 2310 |
| 24 | 🇬🇹 GT | 2227 |
| 25 | 🇰🇷 KR | 2195 |
| 26 | 🇲🇦 MA | 1754 |
| 27 | 🇭🇷 HR | 1693 |
| 28 | 🇲🇪 ME | 1596 |
| 29 | 🇳🇱 NL | 1573 |
| 30 | 🇲🇴 MO | 1504 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3606 |
| 2 | Denver International Airport |  | US | 2891 |
| 3 | Tokyo International Airport |  | JP | 2199 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2132 |
| 6 | Harry Reid International Airport |  | US | 2089 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1897 |
| 8 | Zurich Airport |  | CH | 1847 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1829 |
| 10 | La Aurora Airport |  | GT | 1714 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1605 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1576 |
| 14 | Salt Lake City International Airport |  | US | 1565 |
| 15 | Frankfurt am Main International Airport |  | DE | 1542 |
| 16 | Macau International Airport |  | MO | 1504 |
| 17 | Congonhas Airport |  | BR | 1439 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1422 |
| 19 | Capua Airport |  | IT | 1363 |
| 20 | Madrid Barajas International Airport |  | ES | 1360 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1306 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1232 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1232 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1184 |
| 26 | Charles de Gaulle International Airport |  | FR | 1181 |
| 27 | Kuala Lumpur International Airport |  | MY | 1171 |
| 28 | Bengaluru International Airport |  | IN | 1141 |
| 29 | Ninoy Aquino International Airport |  | PH | 1088 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1084 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1079 |
| 32 | Barcelona International Airport |  | ES | 1032 |
| 33 | Daniel K Inouye International Airport |  | US | 1008 |
| 34 | Seattle-Tacoma International Airport |  | US | 1007 |
| 35 | Calgary International Airport |  | CA | 992 |
| 36 | Reno/Tahoe International Airport |  | US | 991 |
| 37 | Viracopos International Airport |  | BR | 990 |
| 38 | Oslo Gardermoen Airport |  | NO | 973 |
| 39 | Tenerife Norte Airport |  | ES | 964 |
| 40 | Scottsdale Airport |  | US | 948 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 640 | 21m | 244 km | 2,694.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 413 | 24m | 225 km | 1,602.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 400 | 1h 8m | 770 km | 5,313.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 322 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 264 | 44m | 241 km | 1,096.6 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 240 | 1h 48m | 1,423 km | 5,890.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 229 | 20m | 250 km | 989.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 224 | 26m | 215 km | 829.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 215 | 20m | 99 km | 368.3 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 207 | 19m | 144 km | 514.9 t |
| 24 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 206 | 8m | - | - |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 203 | 1h 38m | 1,156 km | 4,049.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 202 | 31m | 369 km | 1,285.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 196 | 24m | 218 km | 738.4 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 190 | 43m | 452 km | 1,480.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SXN22 | SXN | Denham Aerodrome (EGLD) | Wroughton Airfield (EGDT) | 2026-08-07 07:24 UTC | 2026-08-07 07:46 UTC | 22m |
| BOX594 | BOX | Narita International Airport (RJAA) | Macau International Airport (VMMC) | 2026-08-07 04:02 UTC | 2026-08-07 07:40 UTC | 3h 37m |
| CKS273 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-08-06 21:49 UTC | 2026-08-07 07:36 UTC | 9h 47m |
| N193RA |  | Rancho Blanco Airport (TE32) | 80TX (80TX) | 2026-08-07 01:03 UTC | 2026-08-07 07:26 UTC | 6h 23m |
| VLG84XR | Vueling | Barcelona International Airport (LEBL) | Napoli / Capodichino International Airport (LIRN) | 2026-08-07 05:59 UTC | 2026-08-07 07:21 UTC | 1h 21m |
| N137MH |  | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-08-07 07:14 UTC | 2026-08-07 07:17 UTC | 3m |
| EAG29V | EAG | Glasgow International Airport (EGPF) | Southampton Airport (EGHI) | 2026-08-06 11:58 UTC | 2026-08-07 07:03 UTC | 19h 5m |
| EWG6NX | EWG | Dusseldorf International Airport (EDDL) | Vienna International Airport (LOWW) | 2026-08-07 05:47 UTC | 2026-08-07 07:03 UTC | 1h 15m |
| IHMBS | IHM | Muenster Aero Airport (LSPU) | Aosta Airport (LIMW) | 2026-08-07 06:21 UTC | 2026-08-07 07:02 UTC | 40m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-07 06:20 UTC | 2026-08-07 06:59 UTC | 39m |
| DFEIC | DFE | Vilshofen Airport (EDMV) | Straubing Airport (EDMS) | 2026-08-07 06:42 UTC | 2026-08-07 06:58 UTC | 15m |
| URSA10 | URS | Fairbanks International Airport (PAFA) | Ladd Army Air Field (PAFB) | 2026-08-07 06:38 UTC | 2026-08-07 06:56 UTC | 17m |
| RYR90RJ | Ryanair | Dublin Airport (EIDW) | Carcassonne Airport (LFMK) | 2026-08-07 05:03 UTC | 2026-08-07 06:56 UTC | 1h 52m |
| THA917 | Thai Airways | Suvarnabhumi Airport (VTBS) | Naypyidaw Airport (VYEL) | 2026-08-06 06:32 UTC | 2026-08-07 06:56 UTC | 24h 23m |
| RYR10TB | Ryanair | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Bari / Palese International Airport (LIBD) | 2026-08-07 05:45 UTC | 2026-08-07 06:55 UTC | 1h 10m |
| RYR77VD | Ryanair | Edinburgh Airport (EGPH) | Oksywie Military Air Base (EPOK) | 2026-08-07 05:15 UTC | 2026-08-07 06:54 UTC | 1h 39m |
| SEJYV | SEJ | Raron Airport (LSTA) | Aosta Airport (LIMW) | 2026-08-07 06:23 UTC | 2026-08-07 06:52 UTC | 28m |
| VLG2UT | Vueling | Alicante International Airport (LEAL) | Vitoria/Foronda Airport (LEVT) | 2026-08-07 06:02 UTC | 2026-08-07 06:51 UTC | 48m |
| RYR2HU | Ryanair | Dublin Airport (EIDW) | La Roche-sur-Yon Airport (LFRI) | 2026-08-07 05:46 UTC | 2026-08-07 06:51 UTC | 1h 4m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-08-07 06:13 UTC | 2026-08-07 06:49 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

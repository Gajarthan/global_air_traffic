# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_08:22:15_UTC-green)

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

**Latest saved flight:** 2026-08-25 08:22:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 08:22:15 UTC

- **234,474** saved flights
- **71,863** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **234,474** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,824,693.7 tonnes** estimated CO2 emissions
- **163,750,361 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9397 |
| 2 | SkyWest Airlines | 8299 |
| 3 | EJA | 4553 |
| 4 | IndiGo | 3961 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2253 |
| 10 | AZU | 2184 |
| 11 | Vueling | 2006 |
| 12 | Lufthansa | 1904 |
| 13 | WIF | 1862 |
| 14 | LXJ | 1844 |
| 15 | easyJet | 1632 |
| 16 | Swiss International | 1567 |
| 17 | AXM | 1566 |
| 18 | EJU | 1499 |
| 19 | QLK | 1496 |
| 20 | United Airlines | 1484 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1396 |
| 23 | GLO | 1306 |
| 24 | WMT | 1299 |
| 25 | VIV | 1294 |
| 26 | PGT | 1278 |
| 27 | Air France | 1269 |
| 28 | Wizz Air | 1241 |
| 29 | AEE | 1164 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195096 |
| 2 | 🇪🇸 ES | 15053 |
| 3 | 🇧🇷 BR | 13686 |
| 4 | 🇦🇺 AU | 13308 |
| 5 | 🇨🇦 CA | 12979 |
| 6 | 🇮🇹 IT | 12732 |
| 7 | 🇮🇳 IN | 12333 |
| 8 | 🇩🇪 DE | 11540 |
| 9 | 🇬🇧 GB | 11019 |
| 10 | 🇨🇴 CO | 9854 |
| 11 | 🇯🇵 JP | 9511 |
| 12 | 🇫🇷 FR | 9367 |
| 13 | 🇹🇷 TR | 6943 |
| 14 | 🇬🇷 GR | 6892 |
| 15 | 🇲🇽 MX | 6527 |
| 16 | 🇨🇭 CH | 6244 |
| 17 | 🇳🇴 NO | 5783 |
| 18 | 🇲🇾 MY | 4189 |
| 19 | 🇹🇭 TH | 4167 |
| 20 | 🇿🇦 ZA | 4087 |
| 21 | 🇵🇱 PL | 3907 |
| 22 | 🇳🇿 NZ | 3247 |
| 23 | 🇵🇭 PH | 3226 |
| 24 | 🇬🇹 GT | 2935 |
| 25 | 🇰🇷 KR | 2747 |
| 26 | 🇭🇷 HR | 2688 |
| 27 | 🇲🇦 MA | 2377 |
| 28 | 🇲🇪 ME | 2163 |
| 29 | 🇳🇱 NL | 2097 |
| 30 | 🇮🇩 ID | 2047 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4874 |
| 2 | Denver International Airport |  | US | 3799 |
| 3 | Indira Gandhi International Airport |  | IN | 2856 |
| 4 | Tokyo International Airport |  | JP | 2830 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2517 |
| 7 | Zurich Airport |  | CH | 2446 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2396 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2347 |
| 10 | La Aurora Airport |  | GT | 2236 |
| 11 | El Dorado International Airport |  | CO | 2197 |
| 12 | Chicago O'Hare International Airport |  | US | 2117 |
| 13 | Salt Lake City International Airport |  | US | 2069 |
| 14 | Congonhas Airport |  | BR | 1997 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1865 |
| 17 | Capua Airport |  | IT | 1846 |
| 18 | Madrid Barajas International Airport |  | ES | 1843 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1765 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1677 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1625 |
| 25 | Macau International Airport |  | MO | 1607 |
| 26 | Ninoy Aquino International Airport |  | PH | 1558 |
| 27 | Kuala Lumpur International Airport |  | MY | 1516 |
| 28 | Charlotte/Douglas International Airport |  | US | 1515 |
| 29 | Barcelona International Airport |  | ES | 1479 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1420 |
| 32 | Viracopos International Airport |  | BR | 1396 |
| 33 | Seattle-Tacoma International Airport |  | US | 1378 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 35 | Bengaluru International Airport |  | IN | 1377 |
| 36 | Don Mueang International Airport |  | TH | 1355 |
| 37 | Calgary International Airport |  | CA | 1345 |
| 38 | Oslo Gardermoen Airport |  | NO | 1310 |
| 39 | Vancouver International Airport |  | CA | 1282 |
| 40 | O. R. Tambo International Airport |  | ZA | 1270 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 862 | 21m | 244 km | 3,629.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 594 | 24m | 225 km | 2,304.4 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 592 | 1h 6m | 770 km | 7,864.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 386 | 27m | 275 km | 1,829.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 362 | 1h 50m | 1,423 km | 8,884.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 361 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 340 | 44m | 241 km | 1,412.3 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 337 | 44m | 555 km | 3,226.9 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 328 | 21m | 250 km | 1,416.8 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 311 | 24m | 218 km | 1,171.7 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 307 | 1h 40m | 1,156 km | 6,124.5 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 290 | 19m | 99 km | 496.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 287 | 27m | 215 km | 1,062.9 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 259 | 15m | 154 km | 686.2 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IBIS2 | IBI | Frankfurt-Egelsbach Airport (EDFE) | Lauterbach Airport (EDFT) | 2026-08-25 07:27 UTC | 2026-08-25 08:22 UTC | 55m |
| IGO1157 | IndiGo | Juhu Aerodrome (VAJJ) | Tribhuvan International Airport (VNKT) | 2026-08-25 05:59 UTC | 2026-08-25 08:21 UTC | 2h 21m |
| RGA06 | RGA | Locarno Airport (LSZL) | Muenster Aero Airport (LSPU) | 2026-08-25 08:01 UTC | 2026-08-25 08:11 UTC | 10m |
| ECC282 | ECC | Luqa Airport (LMML) | Zurich Airport (LSZH) | 2026-08-25 06:07 UTC | 2026-08-25 08:00 UTC | 1h 53m |
| R20653 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-25 07:27 UTC | 2026-08-25 07:57 UTC | 30m |
| PKSNH | PKS | Pondok Cabe Air Base (WIHP) | Pondok Cabe Air Base (WIHP) | 2026-08-25 07:21 UTC | 2026-08-25 07:48 UTC | 26m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Anduki Airport (WBAK) | 2026-08-25 07:16 UTC | 2026-08-25 07:40 UTC | 23m |
| STNGR81 | STN | RAF Akrotiri (LCRA) | RAF Akrotiri (LCRA) | 2026-08-25 06:54 UTC | 2026-08-25 07:37 UTC | 43m |
| NSZ5TQ | NSZ | Malaga Airport (LEMG) | Gothenburg-Landvetter Airport (ESGG) | 2026-08-25 04:20 UTC | 2026-08-25 07:36 UTC | 3h 16m |
| ENT4201 | ENT | Warsaw Chopin Airport (EPWA) | Antalya International Airport (LTAI) | 2026-08-25 04:57 UTC | 2026-08-25 07:34 UTC | 2h 37m |
| TVF63AB | TVF | Francisco de Sá Carneiro Airport (LPPR) | Paris-Orly Airport (LFPO) | 2026-08-25 05:50 UTC | 2026-08-25 07:33 UTC | 1h 42m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-08-25 07:12 UTC | 2026-08-25 07:31 UTC | 18m |
| VOE5AQ | VOE | Menorca Airport (LEMH) | San Sebastian Airport (LESO) | 2026-08-25 06:27 UTC | 2026-08-25 07:29 UTC | 1h 2m |
| UBG149 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-25 06:53 UTC | 2026-08-25 07:29 UTC | 35m |
| YASAT50 | YAS | Abu Dhabi International Airport (OMAA) | Al Minhad Air Base (OMDM) | 2026-08-25 07:07 UTC | 2026-08-25 07:28 UTC | 20m |
| IAM3185 | IAM | Ciampino Airport (LIRA) | Gioia Del Colle Airport (LIBV) | 2026-08-25 06:57 UTC | 2026-08-25 07:27 UTC | 29m |
| AFR96TP | Air France | Charles de Gaulle International Airport (LFPG) | Toulouse-Blagnac Airport (LFBO) | 2026-08-25 06:23 UTC | 2026-08-25 07:25 UTC | 1h 1m |
| SUCCF | SUC | Port Said Airport (HEPS) | Port Said Airport (HEPS) | 2026-08-25 06:11 UTC | 2026-08-25 07:25 UTC | 1h 14m |
| VLG1RM | Vueling | Malaga Airport (LEMG) | Palma De Mallorca Airport (LEPA) | 2026-08-25 06:17 UTC | 2026-08-25 07:21 UTC | 1h 4m |
| ANE55YR | ANE | Valencia Airport (LEVC) | Son Bonet Airport (LESB) | 2026-08-25 06:33 UTC | 2026-08-25 07:21 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

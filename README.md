# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_06:44:11_UTC-green)

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

**Latest saved flight:** 2026-08-13 06:44:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 06:44:11 UTC

- **191,514** saved flights
- **60,394** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,514** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,291,130.5 tonnes** estimated CO2 emissions
- **132,819,158 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7590 |
| 2 | SkyWest Airlines | 6935 |
| 3 | EJA | 3785 |
| 4 | IndiGo | 3320 |
| 5 | Southwest Airlines | 2994 |
| 6 | American Airlines | 2974 |
| 7 | ENY | 2375 |
| 8 | Delta Air Lines | 2254 |
| 9 | LATAM Airlines | 1796 |
| 10 | AZU | 1730 |
| 11 | Lufthansa | 1663 |
| 12 | Vueling | 1586 |
| 13 | WIF | 1585 |
| 14 | LXJ | 1505 |
| 15 | easyJet | 1317 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1258 |
| 18 | QLK | 1180 |
| 19 | EJU | 1179 |
| 20 | All Nippon Airways | 1158 |
| 21 | Alaska Airlines | 1143 |
| 22 | VIV | 1057 |
| 23 | GLO | 1033 |
| 24 | Air France | 995 |
| 25 | PGT | 990 |
| 26 | CXK | 983 |
| 27 | AEE | 978 |
| 28 | United Airlines | 977 |
| 29 | Wizz Air | 950 |
| 30 | WMT | 949 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163358 |
| 2 | 🇪🇸 ES | 12307 |
| 3 | 🇧🇷 BR | 11014 |
| 4 | 🇦🇺 AU | 10762 |
| 5 | 🇨🇦 CA | 10508 |
| 6 | 🇮🇳 IN | 10395 |
| 7 | 🇮🇹 IT | 9934 |
| 8 | 🇩🇪 DE | 9456 |
| 9 | 🇬🇧 GB | 8903 |
| 10 | 🇯🇵 JP | 7821 |
| 11 | 🇫🇷 FR | 7636 |
| 12 | 🇨🇴 CO | 7385 |
| 13 | 🇬🇷 GR | 5586 |
| 14 | 🇲🇽 MX | 5426 |
| 15 | 🇹🇷 TR | 5117 |
| 16 | 🇨🇭 CH | 5113 |
| 17 | 🇳🇴 NO | 4917 |
| 18 | 🇲🇾 MY | 3292 |
| 19 | 🇿🇦 ZA | 3218 |
| 20 | 🇵🇱 PL | 3160 |
| 21 | 🇹🇭 TH | 2954 |
| 22 | 🇳🇿 NZ | 2706 |
| 23 | 🇵🇭 PH | 2527 |
| 24 | 🇬🇹 GT | 2424 |
| 25 | 🇰🇷 KR | 2341 |
| 26 | 🇭🇷 HR | 1966 |
| 27 | 🇲🇦 MA | 1936 |
| 28 | 🇳🇱 NL | 1710 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇮🇩 ID | 1539 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3983 |
| 2 | Denver International Airport |  | US | 3143 |
| 3 | Tokyo International Airport |  | JP | 2411 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2342 |
| 6 | Harry Reid International Airport |  | US | 2229 |
| 7 | Zurich Airport |  | CH | 2025 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2021 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1862 |
| 11 | El Dorado International Airport |  | CO | 1733 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 13 | Salt Lake City International Airport |  | US | 1709 |
| 14 | Chicago O'Hare International Airport |  | US | 1680 |
| 15 | Frankfurt am Main International Airport |  | DE | 1628 |
| 16 | Congonhas Airport |  | BR | 1602 |
| 17 | Macau International Airport |  | MO | 1527 |
| 18 | Madrid Barajas International Airport |  | ES | 1506 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1483 |
| 20 | Capua Airport |  | IT | 1483 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1416 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1375 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1340 |
| 24 | Malpensa International Airport |  | IT | 1320 |
| 25 | Charles de Gaulle International Airport |  | FR | 1307 |
| 26 | Charlotte/Douglas International Airport |  | US | 1278 |
| 27 | Kuala Lumpur International Airport |  | MY | 1231 |
| 28 | Bengaluru International Airport |  | IN | 1227 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1198 |
| 30 | Ninoy Aquino International Airport |  | PH | 1194 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1177 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1113 |
| 34 | Seattle-Tacoma International Airport |  | US | 1103 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1097 |
| 37 | Daniel K Inouye International Airport |  | US | 1078 |
| 38 | Oslo Gardermoen Airport |  | NO | 1070 |
| 39 | Tenerife Norte Airport |  | ES | 1047 |
| 40 | Vitoria/Foronda Airport |  | ES | 1036 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 706 | 21m | 244 km | 2,972.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 465 | 1h 7m | 770 km | 6,177.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 445 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 334 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 321 | 27m | 275 km | 1,521.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 306 | 8m | - | - |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 284 | 44m | 241 km | 1,179.7 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 275 | 1h 49m | 1,423 km | 6,748.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 256 | 20m | 250 km | 1,105.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 240 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 234 | 19m | 99 km | 400.8 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 229 | 24m | 218 km | 862.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BBX56A | BBX | De Kooy Airport (EHKD) | Texel Airport (EHTX) | 2026-08-13 06:10 UTC | 2026-08-13 06:44 UTC | 33m |
| GPJCD | GPJ | Norwich International Airport (EGSH) | Norwich International Airport (EGSH) | 2026-08-13 06:20 UTC | 2026-08-13 06:42 UTC | 21m |
| EIN1AW | Aer Lingus | General Edward Lawrence Logan International Airport (KBOS) | Dublin Airport (EIDW) | 2026-08-13 01:12 UTC | 2026-08-13 06:35 UTC | 5h 23m |
| HSOIC1 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-08-13 06:05 UTC | 2026-08-13 06:34 UTC | 29m |
| SKY015 | SKY | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-13 05:17 UTC | 2026-08-13 06:31 UTC | 1h 13m |
| 87X |  | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-08-13 06:01 UTC | 2026-08-13 06:21 UTC | 20m |
| IHMBS | IHM | Muenster Aero Airport (LSPU) | Aosta Airport (LIMW) | 2026-08-13 06:03 UTC | 2026-08-13 06:20 UTC | 17m |
| RYR72JG | Ryanair | Aarhus Airport (EKAH) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-08-13 05:24 UTC | 2026-08-13 06:16 UTC | 51m |
| VIR104L | Virgin Atlantic | Hartsfield/Jackson Atlanta International Airport (KATL) | London Heathrow Airport (EGLL) | 2026-08-12 22:43 UTC | 2026-08-13 06:07 UTC | 7h 23m |
| TAY7FO | TAY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Luqa Airport (LMML) | 2026-08-13 05:06 UTC | 2026-08-13 06:07 UTC | 1h 0m |
| BBX403 | BBX | Esbjerg Airport (EKEB) | Lemvig Airport (EKLV) | 2026-08-13 05:36 UTC | 2026-08-13 06:03 UTC | 27m |
| FLD7561 | FLD | Rotterdam Airport (EHRD) | London Biggin Hill Airport (EGKB) | 2026-08-13 05:10 UTC | 2026-08-13 06:02 UTC | 52m |
| FDX5342 | FDX | Charles de Gaulle International Airport (LFPG) | Samsun Carsamba Airport (LTFH) | 2026-08-13 02:51 UTC | 2026-08-13 06:02 UTC | 3h 11m |
| A7GHZ |  | Doha International Airport (OTBD) | Das Island Airport (OMAS) | 2026-08-13 05:34 UTC | 2026-08-13 06:01 UTC | 27m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-13 05:48 UTC | 2026-08-13 05:58 UTC | 10m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-08-13 05:30 UTC | 2026-08-13 05:53 UTC | 22m |
| SEJYV | SEJ | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-08-13 05:35 UTC | 2026-08-13 05:52 UTC | 16m |
| WZZ8PV | Wizz Air | Warsaw Chopin Airport (EPWA) | Bergamo / Orio Al Serio Airport (LIME) | 2026-08-13 04:10 UTC | 2026-08-13 05:51 UTC | 1h 40m |
| VLG883P | Vueling | Paris-Orly Airport (LFPO) | San Sebastian Airport (LESO) | 2026-08-13 04:52 UTC | 2026-08-13 05:50 UTC | 58m |
| ASA1112 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-13 05:27 UTC | 2026-08-13 05:50 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

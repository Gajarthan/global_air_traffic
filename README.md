# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_13:45:55_UTC-green)

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

**Latest saved flight:** 2026-08-09 13:45:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 13:45:55 UTC

- **181,092** saved flights
- **57,867** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **181,092** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,177,043.6 tonnes** estimated CO2 emissions
- **126,205,429 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7181 |
| 2 | SkyWest Airlines | 6582 |
| 3 | EJA | 3555 |
| 4 | IndiGo | 3177 |
| 5 | Southwest Airlines | 2840 |
| 6 | American Airlines | 2818 |
| 7 | ENY | 2250 |
| 8 | Delta Air Lines | 2142 |
| 9 | LATAM Airlines | 1688 |
| 10 | AZU | 1621 |
| 11 | Lufthansa | 1612 |
| 12 | Vueling | 1501 |
| 13 | WIF | 1501 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1241 |
| 16 | Swiss International | 1237 |
| 17 | AXM | 1226 |
| 18 | QLK | 1116 |
| 19 | EJU | 1109 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 997 |
| 23 | GLO | 965 |
| 24 | Cathay Pacific | 947 |
| 25 | CXK | 947 |
| 26 | AEE | 946 |
| 27 | Air France | 937 |
| 28 | United Airlines | 929 |
| 29 | PGT | 911 |
| 30 | MXY | 905 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154792 |
| 2 | 🇪🇸 ES | 11666 |
| 3 | 🇧🇷 BR | 10382 |
| 4 | 🇦🇺 AU | 10202 |
| 5 | 🇮🇳 IN | 9964 |
| 6 | 🇨🇦 CA | 9856 |
| 7 | 🇮🇹 IT | 9376 |
| 8 | 🇩🇪 DE | 8977 |
| 9 | 🇬🇧 GB | 8382 |
| 10 | 🇯🇵 JP | 7378 |
| 11 | 🇫🇷 FR | 7216 |
| 12 | 🇨🇴 CO | 6714 |
| 13 | 🇬🇷 GR | 5307 |
| 14 | 🇲🇽 MX | 5166 |
| 15 | 🇨🇭 CH | 4838 |
| 16 | 🇹🇷 TR | 4671 |
| 17 | 🇳🇴 NO | 4669 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3046 |
| 20 | 🇿🇦 ZA | 2984 |
| 21 | 🇹🇭 TH | 2793 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2406 |
| 24 | 🇬🇹 GT | 2298 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1826 |
| 27 | 🇭🇷 HR | 1806 |
| 28 | 🇲🇪 ME | 1644 |
| 29 | 🇳🇱 NL | 1630 |
| 30 | 🇲🇴 MO | 1517 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3733 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2227 |
| 5 | Guaymaral Airport |  | CO | 2224 |
| 6 | Harry Reid International Airport |  | US | 2127 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1950 |
| 8 | Zurich Airport |  | CH | 1930 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1765 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1616 |
| 14 | El Dorado International Airport |  | CO | 1614 |
| 15 | Frankfurt am Main International Airport |  | DE | 1574 |
| 16 | Macau International Airport |  | MO | 1517 |
| 17 | Congonhas Airport |  | BR | 1504 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1437 |
| 19 | Madrid Barajas International Airport |  | ES | 1424 |
| 20 | Capua Airport |  | IT | 1416 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1351 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1291 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1249 |
| 25 | Charles de Gaulle International Airport |  | FR | 1232 |
| 26 | Charlotte/Douglas International Airport |  | US | 1224 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1181 |
| 29 | Ninoy Aquino International Airport |  | PH | 1133 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1123 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1079 |
| 33 | Viracopos International Airport |  | BR | 1042 |
| 34 | Daniel K Inouye International Airport |  | US | 1041 |
| 35 | Seattle-Tacoma International Airport |  | US | 1041 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1003 |
| 39 | Tenerife Norte Airport |  | ES | 992 |
| 40 | Vitoria/Foronda Airport |  | ES | 982 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 418 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 305 | 27m | 275 km | 1,445.3 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 255 | 1h 48m | 1,423 km | 6,258.1 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 240 | 20m | 250 km | 1,036.7 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 228 | 26m | 215 km | 844.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 222 | 19m | 99 km | 380.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 217 | 19m | 144 km | 539.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 214 | 1h 38m | 1,156 km | 4,269.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 210 | 24m | 218 km | 791.2 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EJU38EF | EJU | Malpensa International Airport (LIMC) | Chania International Airport (LGSA) | 2026-08-09 11:37 UTC | 2026-08-09 13:45 UTC | 2h 8m |
| NGH24 | NGH | 3IA5 (3IA5) | Lincoln Airport (KLNK) | 2026-08-09 13:12 UTC | 2026-08-09 13:43 UTC | 30m |
| N338AM |  | Castroville Municipal Airport (KCVB) | San Antonio International Airport (KSAT) | 2026-08-09 13:26 UTC | 2026-08-09 13:36 UTC | 10m |
| CAN26 | CAN | Bari / Palese International Airport (LIBD) | Gioia Del Colle Airport (LIBV) | 2026-08-09 12:14 UTC | 2026-08-09 13:34 UTC | 1h 19m |
| BNOR | BNO | Brønnøysund Airport (ENBN) | Sandnessjoen Airport Stokka (ENST) | 2026-08-09 13:19 UTC | 2026-08-09 13:31 UTC | 11m |
| FGIBV | FGI | Chambery-Savoie Airport (LFLB) | Chambery-Savoie Airport (LFLB) | 2026-08-09 13:16 UTC | 2026-08-09 13:30 UTC | 13m |
| TGRAG | TGR | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-09 13:25 UTC | 2026-08-09 13:25 UTC | 0m |
| GDMBC | GDM | London Luton Airport (EGGW) | Aylesbury/Thame Airport (EGTA) | 2026-08-09 11:48 UTC | 2026-08-09 13:25 UTC | 1h 36m |
| CAP2776 | CAP | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-08-09 13:08 UTC | 2026-08-09 13:25 UTC | 17m |
| N9721N |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-08-09 12:53 UTC | 2026-08-09 13:19 UTC | 25m |
| GLIDER28 | GLI | Little Gransden Airfield (EGMJ) | Turweston Airport (EGBT) | 2026-08-09 12:02 UTC | 2026-08-09 13:18 UTC | 1h 15m |
| LTA945 | LTA | Starke County Airport (KOXI) | Starke County Airport (KOXI) | 2026-08-09 13:17 UTC | 2026-08-09 13:17 UTC | 0m |
| N6269D |  | Montgomery County Airpark (KGAI) | Frederick Municipal Airport (KFDK) | 2026-08-09 13:02 UTC | 2026-08-09 13:13 UTC | 11m |
| N869TA |  | Centennial Airport (KAPA) | Bijou Bottom Strip (9CO8) | 2026-08-09 12:55 UTC | 2026-08-09 13:12 UTC | 16m |
| N1293E |  | Airglades Airport (K2IS) | Airglades Airport (K2IS) | 2026-08-09 12:50 UTC | 2026-08-09 13:08 UTC | 18m |
| DESSC | DES | Friedrichshafen Airport (EDNY) | Friedrichshafen Airport (EDNY) | 2026-08-09 12:37 UTC | 2026-08-09 13:07 UTC | 30m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-09 12:54 UTC | 2026-08-09 13:07 UTC | 12m |
| AZU6122 | AZU | Fazenda Santo Andre Airport (SNRA) | Sacramento Airport (SNSC) | 2026-08-09 12:49 UTC | 2026-08-09 13:05 UTC | 15m |
| SCU26 | SCU | OK13 (OK13) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-09 12:41 UTC | 2026-08-09 13:03 UTC | 22m |
| OKC548 | OKC | Wiley Post Airport (KPWA) | Miller-Herrold Airport (28MI) | 2026-08-09 11:11 UTC | 2026-08-09 13:03 UTC | 1h 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

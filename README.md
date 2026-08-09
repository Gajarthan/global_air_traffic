# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_19:25:27_UTC-green)

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

**Latest saved flight:** 2026-08-09 19:25:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 19:25:27 UTC

- **182,345** saved flights
- **58,211** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **182,345** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,191,556.5 tonnes** estimated CO2 emissions
- **127,046,752 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7234 |
| 2 | SkyWest Airlines | 6628 |
| 3 | EJA | 3595 |
| 4 | IndiGo | 3194 |
| 5 | Southwest Airlines | 2861 |
| 6 | American Airlines | 2839 |
| 7 | ENY | 2270 |
| 8 | Delta Air Lines | 2160 |
| 9 | LATAM Airlines | 1702 |
| 10 | AZU | 1635 |
| 11 | Lufthansa | 1618 |
| 12 | WIF | 1508 |
| 13 | Vueling | 1507 |
| 14 | LXJ | 1431 |
| 15 | Swiss International | 1250 |
| 16 | easyJet | 1247 |
| 17 | AXM | 1226 |
| 18 | EJU | 1122 |
| 19 | QLK | 1116 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 1004 |
| 23 | GLO | 978 |
| 24 | AEE | 953 |
| 25 | CXK | 951 |
| 26 | Air France | 947 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 932 |
| 29 | PGT | 923 |
| 30 | MXY | 911 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 155956 |
| 2 | 🇪🇸 ES | 11736 |
| 3 | 🇧🇷 BR | 10470 |
| 4 | 🇦🇺 AU | 10203 |
| 5 | 🇮🇳 IN | 10007 |
| 6 | 🇨🇦 CA | 9917 |
| 7 | 🇮🇹 IT | 9453 |
| 8 | 🇩🇪 DE | 9045 |
| 9 | 🇬🇧 GB | 8444 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7277 |
| 12 | 🇨🇴 CO | 6783 |
| 13 | 🇬🇷 GR | 5352 |
| 14 | 🇲🇽 MX | 5203 |
| 15 | 🇨🇭 CH | 4874 |
| 16 | 🇹🇷 TR | 4731 |
| 17 | 🇳🇴 NO | 4693 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3059 |
| 20 | 🇿🇦 ZA | 3029 |
| 21 | 🇹🇭 TH | 2804 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2331 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1847 |
| 27 | 🇭🇷 HR | 1818 |
| 28 | 🇲🇪 ME | 1649 |
| 29 | 🇳🇱 NL | 1639 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3770 |
| 2 | Denver International Airport |  | US | 3008 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2237 |
| 5 | Guaymaral Airport |  | CO | 2231 |
| 6 | Harry Reid International Airport |  | US | 2136 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1961 |
| 8 | Zurich Airport |  | CH | 1949 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1894 |
| 10 | La Aurora Airport |  | GT | 1790 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1662 |
| 12 | Chicago O'Hare International Airport |  | US | 1632 |
| 13 | Salt Lake City International Airport |  | US | 1628 |
| 14 | El Dorado International Airport |  | CO | 1627 |
| 15 | Frankfurt am Main International Airport |  | DE | 1584 |
| 16 | Congonhas Airport |  | BR | 1520 |
| 17 | Macau International Airport |  | MO | 1518 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1443 |
| 19 | Madrid Barajas International Airport |  | ES | 1437 |
| 20 | Capua Airport |  | IT | 1430 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1363 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1301 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1262 |
| 25 | Charles de Gaulle International Airport |  | FR | 1245 |
| 26 | Charlotte/Douglas International Airport |  | US | 1236 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1135 |
| 30 | Ninoy Aquino International Airport |  | PH | 1135 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1112 |
| 32 | Barcelona International Airport |  | ES | 1080 |
| 33 | Viracopos International Airport |  | BR | 1049 |
| 34 | Seattle-Tacoma International Airport |  | US | 1047 |
| 35 | Reno/Tahoe International Airport |  | US | 1046 |
| 36 | Daniel K Inouye International Airport |  | US | 1042 |
| 37 | Calgary International Airport |  | CA | 1035 |
| 38 | Oslo Gardermoen Airport |  | NO | 1010 |
| 39 | Tenerife Norte Airport |  | ES | 996 |
| 40 | Amsterdam Airport Schiphol |  | NL | 989 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 920 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 423 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 257 | 1h 48m | 1,423 km | 6,307.2 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 249 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 245 | 20m | 250 km | 1,058.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 223 | 19m | 99 km | 382.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 222 | 1h 15m | 961 km | 3,679.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 219 | 50m | 556 km | 2,099.3 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 218 | 19m | 144 km | 542.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 216 | 1h 38m | 1,156 km | 4,309.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 198 | 1h 1m | 695 km | 2,373.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N294CA |  | Wings Field (KLOM) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-09 18:36 UTC | 2026-08-09 19:25 UTC | 49m |
| N383TA |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-09 18:50 UTC | 2026-08-09 19:24 UTC | 34m |
| N7468Y |  | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-08-09 18:23 UTC | 2026-08-09 19:18 UTC | 55m |
| TKR41 | TKR | Citabriair Airport (UT43) | Creech Afb Airport (KINS) | 2026-08-09 18:50 UTC | 2026-08-09 19:17 UTC | 26m |
| TKR15 | TKR | Wendover Airport (KENV) | Skypark Airport (KBTF) | 2026-08-09 18:58 UTC | 2026-08-09 19:16 UTC | 18m |
| RPA5630 | Republic Airways | Charlotte/Douglas International Airport (KCLT) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-09 17:40 UTC | 2026-08-09 19:16 UTC | 1h 35m |
| XBNLT | XBN | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-09 18:16 UTC | 2026-08-09 19:15 UTC | 59m |
| MSR503 | EgyptAir | Al Maktoum International Airport (OMDW) | Hulwan (HE15) | 2026-08-09 16:19 UTC | 2026-08-09 19:07 UTC | 2h 48m |
| TKR105 | TKR | Jackpot/Hayden Field (K06U) | Morgan County Airport (K42U) | 2026-08-09 18:42 UTC | 2026-08-09 19:03 UTC | 20m |
| TKR162 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-09 18:52 UTC | 2026-08-09 19:00 UTC | 7m |
| N794SC |  | Los Angeles International Airport (KLAX) | Austin-Bergstrom International Airport (KAUS) | 2026-08-09 16:20 UTC | 2026-08-09 19:00 UTC | 2h 39m |
| N3040F |  | 75TN (75TN) | Greeneville Municipal Airport (KGCY) | 2026-08-09 18:46 UTC | 2026-08-09 18:59 UTC | 13m |
| TGTOW | TGT | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-09 18:49 UTC | 2026-08-09 18:58 UTC | 8m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-09 18:39 UTC | 2026-08-09 18:57 UTC | 18m |
| EWG16E | EWG | Hamburg Airport (EDDH) | Graz Airport (LOWG) | 2026-08-09 17:46 UTC | 2026-08-09 18:57 UTC | 1h 11m |
| ADY431 | ADY | Abu Dhabi International Airport (OMAA) | Hulwan (HE15) | 2026-08-09 15:57 UTC | 2026-08-09 18:57 UTC | 2h 59m |
| EJA835 | EJA | Oxnard Airport (KOXR) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-09 17:50 UTC | 2026-08-09 18:56 UTC | 1h 5m |
| XSR361 | XSR | Auburn University Regional Airport (KAUO) | Colonel James Jabara Airport (KAAO) | 2026-08-09 17:09 UTC | 2026-08-09 18:55 UTC | 1h 45m |
| N502GV |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-09 18:29 UTC | 2026-08-09 18:53 UTC | 23m |
| TKR210 | TKR | Savage Field (KU01) | Morgan County Airport (K42U) | 2026-08-09 18:35 UTC | 2026-08-09 18:51 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

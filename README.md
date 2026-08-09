# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_18:51:35_UTC-green)

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

**Latest saved flight:** 2026-08-09 18:51:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 18:51:35 UTC

- **182,196** saved flights
- **58,167** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **182,196** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,189,565.8 tonnes** estimated CO2 emissions
- **126,931,351 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7227 |
| 2 | SkyWest Airlines | 6620 |
| 3 | EJA | 3588 |
| 4 | IndiGo | 3193 |
| 5 | Southwest Airlines | 2858 |
| 6 | American Airlines | 2837 |
| 7 | ENY | 2269 |
| 8 | Delta Air Lines | 2156 |
| 9 | LATAM Airlines | 1701 |
| 10 | AZU | 1633 |
| 11 | Lufthansa | 1618 |
| 12 | Vueling | 1507 |
| 13 | WIF | 1507 |
| 14 | LXJ | 1428 |
| 15 | Swiss International | 1250 |
| 16 | easyJet | 1245 |
| 17 | AXM | 1226 |
| 18 | EJU | 1122 |
| 19 | QLK | 1116 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 1002 |
| 23 | GLO | 976 |
| 24 | CXK | 951 |
| 25 | AEE | 950 |
| 26 | Air France | 947 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 932 |
| 29 | PGT | 922 |
| 30 | MXY | 911 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 155810 |
| 2 | 🇪🇸 ES | 11729 |
| 3 | 🇧🇷 BR | 10459 |
| 4 | 🇦🇺 AU | 10203 |
| 5 | 🇮🇳 IN | 10005 |
| 6 | 🇨🇦 CA | 9911 |
| 7 | 🇮🇹 IT | 9444 |
| 8 | 🇩🇪 DE | 9039 |
| 9 | 🇬🇧 GB | 8435 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7275 |
| 12 | 🇨🇴 CO | 6774 |
| 13 | 🇬🇷 GR | 5343 |
| 14 | 🇲🇽 MX | 5195 |
| 15 | 🇨🇭 CH | 4868 |
| 16 | 🇹🇷 TR | 4724 |
| 17 | 🇳🇴 NO | 4690 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3059 |
| 20 | 🇿🇦 ZA | 3027 |
| 21 | 🇹🇭 TH | 2804 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2325 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1846 |
| 27 | 🇭🇷 HR | 1816 |
| 28 | 🇲🇪 ME | 1648 |
| 29 | 🇳🇱 NL | 1637 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3768 |
| 2 | Denver International Airport |  | US | 3003 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2236 |
| 5 | Guaymaral Airport |  | CO | 2231 |
| 6 | Harry Reid International Airport |  | US | 2136 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1959 |
| 8 | Zurich Airport |  | CH | 1946 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1891 |
| 10 | La Aurora Airport |  | GT | 1785 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1659 |
| 12 | Chicago O'Hare International Airport |  | US | 1632 |
| 13 | El Dorado International Airport |  | CO | 1625 |
| 14 | Salt Lake City International Airport |  | US | 1623 |
| 15 | Frankfurt am Main International Airport |  | DE | 1584 |
| 16 | Macau International Airport |  | MO | 1518 |
| 17 | Congonhas Airport |  | BR | 1517 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1442 |
| 19 | Madrid Barajas International Airport |  | ES | 1436 |
| 20 | Capua Airport |  | IT | 1427 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1361 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1301 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1260 |
| 25 | Charles de Gaulle International Airport |  | FR | 1245 |
| 26 | Charlotte/Douglas International Airport |  | US | 1232 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Ninoy Aquino International Airport |  | PH | 1135 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1131 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1111 |
| 32 | Barcelona International Airport |  | ES | 1080 |
| 33 | Viracopos International Airport |  | BR | 1048 |
| 34 | Seattle-Tacoma International Airport |  | US | 1047 |
| 35 | Reno/Tahoe International Airport |  | US | 1043 |
| 36 | Daniel K Inouye International Airport |  | US | 1042 |
| 37 | Calgary International Airport |  | CA | 1033 |
| 38 | Oslo Gardermoen Airport |  | NO | 1010 |
| 39 | Tenerife Norte Airport |  | ES | 996 |
| 40 | Vitoria/Foronda Airport |  | ES | 988 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 920 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 421 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 257 | 1h 48m | 1,423 km | 6,307.2 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 248 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 245 | 20m | 250 km | 1,058.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 223 | 19m | 99 km | 382.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 221 | 1h 15m | 961 km | 3,663.2 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 219 | 50m | 556 km | 2,099.3 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 218 | 19m | 144 km | 542.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 215 | 1h 38m | 1,156 km | 4,289.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 213 | 24m | 218 km | 802.5 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 198 | 1h 1m | 695 km | 2,373.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TKR210 | TKR | Savage Field (KU01) | Morgan County Airport (K42U) | 2026-08-09 18:35 UTC | 2026-08-09 18:51 UTC | 16m |
| N948G |  | Camarillo Airport (KCMA) | Palo Alto Airport (KPAO) | 2026-08-09 17:52 UTC | 2026-08-09 18:50 UTC | 58m |
| SRG375 | SRG | RNAS Lee-On-Solent (EGHF) | Lydd Airport (EGMD) | 2026-08-09 17:50 UTC | 2026-08-09 18:42 UTC | 52m |
| N789MT |  | Buchanan Field (KCCR) | Mc Clellan Airfield (KMCC) | 2026-08-09 18:05 UTC | 2026-08-09 18:41 UTC | 36m |
| N641PF |  | Brandywine Regional Airport (KOQN) | Brandywine Regional Airport (KOQN) | 2026-08-09 17:52 UTC | 2026-08-09 18:41 UTC | 49m |
| N254EK |  | Palo Alto Airport (KPAO) | Sacramento Mather Airport (KMHR) | 2026-08-09 17:51 UTC | 2026-08-09 18:38 UTC | 46m |
| MSR778 | EgyptAir | London Heathrow Airport (EGLL) | HE12 (HE12) | 2026-08-09 14:40 UTC | 2026-08-09 18:36 UTC | 3h 56m |
| N4776E |  | Clearwater Executive Airport (KCLW) | Clearwater Executive Airport (KCLW) | 2026-08-09 18:04 UTC | 2026-08-09 18:36 UTC | 31m |
| N561BE |  | SD49 (SD49) | Myers Field (KCNB) | 2026-08-09 18:23 UTC | 2026-08-09 18:35 UTC | 11m |
| BOE358 | BOE | Renton Municipal Airport (KRNT) | Christensen Field (8WA6) | 2026-08-09 17:16 UTC | 2026-08-09 18:34 UTC | 1h 18m |
| N135RF |  | Lee Vining Airport (KO24) | Lee Vining Airport (KO24) | 2026-08-09 17:30 UTC | 2026-08-09 18:33 UTC | 1h 2m |
| FLJ64G | FLJ | Farnborough Airport (EGLF) | Manchester Airport (EGCC) | 2026-08-09 17:51 UTC | 2026-08-09 18:29 UTC | 37m |
| N370AB |  | Bartos Farm Airport (47XS) | Throckmorton Municipal Airport (K72F) | 2026-08-09 17:59 UTC | 2026-08-09 18:28 UTC | 29m |
| RFS716 | RFS | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-08-09 17:59 UTC | 2026-08-09 18:26 UTC | 27m |
| DELPD | DEL | Michelstadt/Odenwald Airport (EDFO) | Michelstadt/Odenwald Airport (EDFO) | 2026-08-09 17:47 UTC | 2026-08-09 18:26 UTC | 39m |
| N5QD |  | 0PA0 (0PA0) | Gunden Airport (PS54) | 2026-08-09 18:24 UTC | 2026-08-09 18:26 UTC | 1m |
| N80JF |  | Orange Municipal Airport (KORE) | Orange Municipal Airport (KORE) | 2026-08-09 17:46 UTC | 2026-08-09 18:25 UTC | 39m |
| GCJRZZ | GCJ | RAF Cranwell (EGYD) | RAF Cranwell (EGYD) | 2026-08-09 18:13 UTC | 2026-08-09 18:25 UTC | 12m |
| MSR790 | EgyptAir | Václav Havel Airport (LKPR) | HE42 (HE42) | 2026-08-09 15:21 UTC | 2026-08-09 18:22 UTC | 3h 0m |
| PEA501 | PEA | Olbia / Costa Smeralda Airport (LIEO) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-09 17:32 UTC | 2026-08-09 18:22 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

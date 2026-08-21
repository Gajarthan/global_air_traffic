# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_21:16:59_UTC-green)

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

**Latest saved flight:** 2026-08-21 21:16:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 21:16:59 UTC

- **223,840** saved flights
- **69,878** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **223,840** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,696,790.2 tonnes** estimated CO2 emissions
- **156,335,666 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8972 |
| 2 | SkyWest Airlines | 7957 |
| 3 | EJA | 4335 |
| 4 | IndiGo | 3781 |
| 5 | American Airlines | 3696 |
| 6 | Southwest Airlines | 3506 |
| 7 | Delta Air Lines | 2871 |
| 8 | ENY | 2751 |
| 9 | LATAM Airlines | 2128 |
| 10 | AZU | 2061 |
| 11 | Vueling | 1889 |
| 12 | Lufthansa | 1842 |
| 13 | WIF | 1787 |
| 14 | LXJ | 1767 |
| 15 | easyJet | 1549 |
| 16 | Swiss International | 1491 |
| 17 | AXM | 1467 |
| 18 | United Airlines | 1407 |
| 19 | QLK | 1405 |
| 20 | EJU | 1402 |
| 21 | Alaska Airlines | 1358 |
| 22 | All Nippon Airways | 1333 |
| 23 | GLO | 1232 |
| 24 | PGT | 1228 |
| 25 | VIV | 1217 |
| 26 | Air France | 1213 |
| 27 | WMT | 1193 |
| 28 | Wizz Air | 1153 |
| 29 | JetBlue | 1123 |
| 30 | AEE | 1115 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188008 |
| 2 | 🇪🇸 ES | 14355 |
| 3 | 🇧🇷 BR | 12978 |
| 4 | 🇦🇺 AU | 12655 |
| 5 | 🇨🇦 CA | 12382 |
| 6 | 🇮🇹 IT | 11953 |
| 7 | 🇮🇳 IN | 11793 |
| 8 | 🇩🇪 DE | 11025 |
| 9 | 🇬🇧 GB | 10508 |
| 10 | 🇨🇴 CO | 9230 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8931 |
| 13 | 🇹🇷 TR | 6526 |
| 14 | 🇬🇷 GR | 6524 |
| 15 | 🇲🇽 MX | 6210 |
| 16 | 🇨🇭 CH | 5889 |
| 17 | 🇳🇴 NO | 5560 |
| 18 | 🇲🇾 MY | 3887 |
| 19 | 🇿🇦 ZA | 3861 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3715 |
| 22 | 🇳🇿 NZ | 3090 |
| 23 | 🇵🇭 PH | 3022 |
| 24 | 🇬🇹 GT | 2838 |
| 25 | 🇰🇷 KR | 2657 |
| 26 | 🇭🇷 HR | 2500 |
| 27 | 🇲🇦 MA | 2253 |
| 28 | 🇳🇱 NL | 1990 |
| 29 | 🇲🇪 ME | 1989 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4690 |
| 2 | Denver International Airport |  | US | 3651 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2713 |
| 5 | Guaymaral Airport |  | CO | 2626 |
| 6 | Harry Reid International Airport |  | US | 2456 |
| 7 | Zurich Airport |  | CH | 2321 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2294 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2266 |
| 10 | La Aurora Airport |  | GT | 2163 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2044 |
| 13 | Salt Lake City International Airport |  | US | 1965 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1922 |
| 15 | Congonhas Airport |  | BR | 1898 |
| 16 | Frankfurt am Main International Airport |  | DE | 1809 |
| 17 | Madrid Barajas International Airport |  | ES | 1754 |
| 18 | Capua Airport |  | IT | 1713 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1671 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1656 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1629 |
| 22 | Macau International Airport |  | MO | 1589 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1566 |
| 25 | Charles de Gaulle International Airport |  | FR | 1546 |
| 26 | Charlotte/Douglas International Airport |  | US | 1479 |
| 27 | Ninoy Aquino International Airport |  | PH | 1439 |
| 28 | Kuala Lumpur International Airport |  | MY | 1420 |
| 29 | Barcelona International Airport |  | ES | 1382 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1358 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1323 |
| 33 | Seattle-Tacoma International Airport |  | US | 1319 |
| 34 | Viracopos International Airport |  | BR | 1314 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1297 |
| 36 | Calgary International Airport |  | CA | 1267 |
| 37 | Oslo Gardermoen Airport |  | NO | 1251 |
| 38 | Vitoria/Foronda Airport |  | ES | 1240 |
| 39 | Don Mueang International Airport |  | TH | 1239 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1206 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1071 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 805 | 21m | 244 km | 3,389.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 525 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 507 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 377 | 27m | 275 km | 1,786.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 333 | 1h 50m | 1,423 km | 8,172.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 299 | 21m | 250 km | 1,291.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 283 | 1h 39m | 1,156 km | 5,645.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 278 | 24m | 218 km | 1,047.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 278 | 19m | 99 km | 476.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 20 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 263 | 1h 14m | 961 km | 4,359.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 256 | 19m | 144 km | 636.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 242 | 1h 50m | 1,304 km | 5,444.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-08-21 10:40 UTC | 2026-08-21 21:16 UTC | 10h 36m |
| N6974H |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-21 20:27 UTC | 2026-08-21 21:14 UTC | 46m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Zhuhai Airport (ZGSD) | 2026-08-21 11:19 UTC | 2026-08-21 21:13 UTC | 9h 54m |
| N7828M |  | Long Beach (Daugherty Field) Airport (KLGB) | Hemet-Ryan Airport (KHMT) | 2026-08-21 19:43 UTC | 2026-08-21 21:08 UTC | 1h 25m |
| LXJ604 | LXJ | Boca Raton Airport (KBCT) | Orlando Executive Airport (KORL) | 2026-08-21 20:30 UTC | 2026-08-21 21:05 UTC | 34m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-21 20:28 UTC | 2026-08-21 21:04 UTC | 36m |
| N334BG |  | Putnam County Airport (KOWX) | Wood County Regional Airport (K1G0) | 2026-08-21 20:46 UTC | 2026-08-21 21:04 UTC | 18m |
| AUB121 | AUB | Auburn University Regional Airport (KAUO) | Lagrange/Callaway Airport (KLGC) | 2026-08-21 20:32 UTC | 2026-08-21 21:03 UTC | 30m |
| N474RL |  | 71AL (71AL) | Moton Field Municipal Airport (K06A) | 2026-08-21 20:37 UTC | 2026-08-21 20:57 UTC | 20m |
| N998EA |  | Auburn University Regional Airport (KAUO) | Addison-Henley Field (0MS7) | 2026-08-21 20:17 UTC | 2026-08-21 20:55 UTC | 38m |
| AERT10 | AER | Homer Airport (PAHO) | Homer Airport (PAHO) | 2026-08-21 20:06 UTC | 2026-08-21 20:54 UTC | 47m |
| AAL1806 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Laguardia Airport (KLGA) | 2026-08-21 17:54 UTC | 2026-08-21 20:54 UTC | 3h 0m |
| N459M |  | Lehigh Valley International Airport (KABE) | Vietmeier Airport (WS67) | 2026-08-21 18:53 UTC | 2026-08-21 20:52 UTC | 1h 58m |
| N777MS |  | Livermore Municipal Airport (KLVK) | Meadows Field (KBFL) | 2026-08-21 20:09 UTC | 2026-08-21 20:49 UTC | 39m |
| N9488G |  | Montgomery-Gibbs Executive Airport (KMYF) | Ramona Airport (KRNM) | 2026-08-21 19:21 UTC | 2026-08-21 20:48 UTC | 1h 27m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-08-21 20:42 UTC | 2026-08-21 20:46 UTC | 3m |
| WUP658 | WUP | Monmouth Executive Airport (KBLM) | Topsail Airpark (01NC) | 2026-08-21 19:26 UTC | 2026-08-21 20:46 UTC | 1h 19m |
| SPSTR9 | SPS | Weed Airport (KO46) | Riverside Airport (KRAL) | 2026-08-21 18:33 UTC | 2026-08-21 20:45 UTC | 2h 12m |
| N534Y |  | Cameron Park Airport (KO61) | Lake Tahoe Airport (KTVL) | 2026-08-21 19:58 UTC | 2026-08-21 20:45 UTC | 47m |
| N64RU |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-21 19:01 UTC | 2026-08-21 20:44 UTC | 1h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

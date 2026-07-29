# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_09:53:54_UTC-green)

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

**Latest saved flight:** 2026-07-29 09:53:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 09:53:54 UTC

- **157,933** saved flights
- **52,353** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **157,933** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,895,944.7 tonnes** estimated CO2 emissions
- **109,909,836 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6348 |
| 2 | SkyWest Airlines | 5778 |
| 3 | EJA | 3123 |
| 4 | IndiGo | 2791 |
| 5 | American Airlines | 2515 |
| 6 | Southwest Airlines | 2482 |
| 7 | ENY | 1968 |
| 8 | Delta Air Lines | 1872 |
| 9 | Lufthansa | 1510 |
| 10 | LATAM Airlines | 1477 |
| 11 | AZU | 1384 |
| 12 | WIF | 1332 |
| 13 | Vueling | 1327 |
| 14 | LXJ | 1217 |
| 15 | AXM | 1110 |
| 16 | Swiss International | 1091 |
| 17 | easyJet | 1031 |
| 18 | Alaska Airlines | 991 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 982 |
| 21 | EJU | 967 |
| 22 | VIV | 866 |
| 23 | United Airlines | 838 |
| 24 | CXK | 837 |
| 25 | Cathay Pacific | 832 |
| 26 | GLO | 828 |
| 27 | AEE | 827 |
| 28 | MXY | 821 |
| 29 | Air France | 820 |
| 30 | JetBlue | 817 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 136221 |
| 2 | 🇪🇸 ES | 10161 |
| 3 | 🇧🇷 BR | 9008 |
| 4 | 🇦🇺 AU | 8940 |
| 5 | 🇮🇳 IN | 8777 |
| 6 | 🇨🇦 CA | 8556 |
| 7 | 🇮🇹 IT | 8151 |
| 8 | 🇩🇪 DE | 8012 |
| 9 | 🇬🇧 GB | 7255 |
| 10 | 🇯🇵 JP | 6464 |
| 11 | 🇫🇷 FR | 6245 |
| 12 | 🇨🇴 CO | 5538 |
| 13 | 🇲🇽 MX | 4532 |
| 14 | 🇬🇷 GR | 4512 |
| 15 | 🇳🇴 NO | 4174 |
| 16 | 🇨🇭 CH | 4134 |
| 17 | 🇹🇷 TR | 3777 |
| 18 | 🇲🇾 MY | 2886 |
| 19 | 🇵🇱 PL | 2685 |
| 20 | 🇿🇦 ZA | 2558 |
| 21 | 🇳🇿 NZ | 2348 |
| 22 | 🇹🇭 TH | 2268 |
| 23 | 🇰🇷 KR | 2098 |
| 24 | 🇵🇭 PH | 2085 |
| 25 | 🇬🇹 GT | 2021 |
| 26 | 🇲🇦 MA | 1609 |
| 27 | 🇲🇪 ME | 1519 |
| 28 | 🇭🇷 HR | 1460 |
| 29 | 🇳🇱 NL | 1444 |
| 30 | 🇲🇴 MO | 1307 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3243 |
| 2 | Denver International Airport |  | US | 2639 |
| 3 | Tokyo International Airport |  | JP | 2046 |
| 4 | Guaymaral Airport |  | CO | 1982 |
| 5 | Indira Gandhi International Airport |  | IN | 1951 |
| 6 | Harry Reid International Airport |  | US | 1926 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1751 |
| 8 | Zurich Airport |  | CH | 1697 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1657 |
| 10 | La Aurora Airport |  | GT | 1567 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1475 |
| 12 | Frankfurt am Main International Airport |  | DE | 1460 |
| 13 | El Dorado International Airport |  | CO | 1437 |
| 14 | Chicago O'Hare International Airport |  | US | 1433 |
| 15 | Salt Lake City International Airport |  | US | 1422 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1324 |
| 17 | Macau International Airport |  | MO | 1307 |
| 18 | Congonhas Airport |  | BR | 1299 |
| 19 | Madrid Barajas International Airport |  | ES | 1251 |
| 20 | Capua Airport |  | IT | 1241 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1211 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1135 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1125 |
| 24 | Charlotte/Douglas International Airport |  | US | 1114 |
| 25 | Kuala Lumpur International Airport |  | MY | 1104 |
| 26 | Charles de Gaulle International Airport |  | FR | 1083 |
| 27 | Bengaluru International Airport |  | IN | 1045 |
| 28 | Malpensa International Airport |  | IT | 1040 |
| 29 | Ninoy Aquino International Airport |  | PH | 978 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 961 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 954 |
| 32 | Barcelona International Airport |  | ES | 944 |
| 33 | Daniel K Inouye International Airport |  | US | 933 |
| 34 | Seattle-Tacoma International Airport |  | US | 923 |
| 35 | Calgary International Airport |  | CA | 908 |
| 36 | Tenerife Norte Airport |  | ES | 895 |
| 37 | Viracopos International Airport |  | BR | 895 |
| 38 | Scottsdale Airport |  | US | 891 |
| 39 | Oslo Gardermoen Airport |  | NO | 875 |
| 40 | Amsterdam Airport Schiphol |  | NL | 870 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 832 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 572 | 21m | 244 km | 2,408.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 379 | 24m | 225 km | 1,470.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 376 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 364 | 1h 9m | 770 km | 4,835.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 291 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 277 | 27m | 275 km | 1,312.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 221 | 44m | 241 km | 918.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 213 | 1h 47m | 1,423 km | 5,227.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 207 | 26m | 215 km | 766.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 202 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 190 | 30m | 49 km | 160.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 187 | 1h 15m | 961 km | 3,099.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 187 | 18m | 144 km | 465.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 185 | 31m | 369 km | 1,177.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 179 | 50m | 556 km | 1,715.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 177 | 1h 39m | 1,156 km | 3,531.1 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 1m | 695 km | 2,085.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 49m | 1,304 km | 3,779.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKBUD69 | OKB | Rana Loumy Airport (LKRA) | Roudnice Mad Airport (LKRO) | 2026-07-29 09:21 UTC | 2026-07-29 09:53 UTC | 32m |
| DESFM | DES | Speyer Airport (EDRY) | Friedrichshafen Airport (EDNY) | 2026-07-29 08:42 UTC | 2026-07-29 09:48 UTC | 1h 6m |
| HSORJ2 | HSO | De Kooy Airport (EHKD) | De Kooy Airport (EHKD) | 2026-07-29 09:26 UTC | 2026-07-29 09:41 UTC | 15m |
| UPS197 | UPS | Ted Stevens Anchorage International Airport (PANC) | Spirit River Airport (CFS5) | 2026-07-29 07:22 UTC | 2026-07-29 09:36 UTC | 2h 14m |
| KLM1498 | KLM Royal Dutch | Barcelona International Airport (LEBL) | Amsterdam Airport Schiphol (EHAM) | 2026-07-29 07:39 UTC | 2026-07-29 09:32 UTC | 1h 52m |
| ACA808 | Air Canada | Toronto Pearson International Airport (CYYZ) | Amsterdam Airport Schiphol (EHAM) | 2026-07-29 02:49 UTC | 2026-07-29 09:31 UTC | 6h 41m |
| HBXDA | HBX | Megeve Airport (LFHM) | Raron Airport (LSTA) | 2026-07-29 09:15 UTC | 2026-07-29 09:29 UTC | 14m |
| QFA51 | Qantas | Brisbane International Airport (YBBN) | Changi Air Base (WSAC) | 2026-07-29 01:36 UTC | 2026-07-29 09:28 UTC | 7h 52m |
| YGP | YGP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-29 08:19 UTC | 2026-07-29 09:23 UTC | 1h 3m |
| HBXTP | HBX | Reichenbach Air Base (LSGR) | Wangen-Lachen Airport (LSPV) | 2026-07-29 08:38 UTC | 2026-07-29 09:22 UTC | 43m |
| DKYCK | DKY | EDJG (EDJG) | EDJG (EDJG) | 2026-07-29 09:05 UTC | 2026-07-29 09:16 UTC | 11m |
| HKS40 | HKS | Beccles Airport (EGSM) | Beccles Airport (EGSM) | 2026-07-29 09:12 UTC | 2026-07-29 09:13 UTC | 0m |
| A6FHD |  | Das Island Airport (OMAS) | Das Island Airport (OMAS) | 2026-07-29 08:46 UTC | 2026-07-29 09:08 UTC | 21m |
| 0000313 |  | Be'er Sheva (Teyman) Airport (LLBS) | Be'er Sheva (Teyman) Airport (LLBS) | 2026-07-29 08:27 UTC | 2026-07-29 09:08 UTC | 40m |
| R72098 |  | Hohenfels Army Air Field (ETIH) | Hohenfels Army Air Field (ETIH) | 2026-07-29 09:05 UTC | 2026-07-29 09:05 UTC | 0m |
| HBYIP | HBY | Bad Ragaz Airport (LSZE) | LSMF (LSMF) | 2026-07-29 08:46 UTC | 2026-07-29 09:02 UTC | 16m |
| BRO30 | BRO | Humberside Airport (EGNJ) | East Midlands Airport (EGNX) | 2026-07-29 08:40 UTC | 2026-07-29 09:02 UTC | 22m |
| N218AC |  | Paros Airport (LGPA) | Paros Airport (LGPA) | 2026-07-29 08:03 UTC | 2026-07-29 09:02 UTC | 58m |
| DEOLL | DEO | Schonhagen Airport (EDAZ) | Reinsdorf Airport (EDOD) | 2026-07-29 08:55 UTC | 2026-07-29 09:02 UTC | 6m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-07-28 21:39 UTC | 2026-07-29 08:59 UTC | 11h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_20:56:23_UTC-green)

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

**Latest saved flight:** 2026-08-08 20:56:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 20:56:23 UTC

- **179,594** saved flights
- **57,594** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **179,594** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,158,755.6 tonnes** estimated CO2 emissions
- **125,145,253 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7123 |
| 2 | SkyWest Airlines | 6554 |
| 3 | EJA | 3540 |
| 4 | IndiGo | 3144 |
| 5 | Southwest Airlines | 2827 |
| 6 | American Airlines | 2803 |
| 7 | ENY | 2237 |
| 8 | Delta Air Lines | 2134 |
| 9 | LATAM Airlines | 1675 |
| 10 | AZU | 1606 |
| 11 | Lufthansa | 1600 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1486 |
| 14 | LXJ | 1405 |
| 15 | easyJet | 1226 |
| 16 | Swiss International | 1225 |
| 17 | AXM | 1211 |
| 18 | EJU | 1094 |
| 19 | QLK | 1093 |
| 20 | All Nippon Airways | 1088 |
| 21 | Alaska Airlines | 1085 |
| 22 | VIV | 988 |
| 23 | GLO | 957 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 945 |
| 26 | AEE | 935 |
| 27 | United Airlines | 927 |
| 28 | Air France | 923 |
| 29 | MXY | 902 |
| 30 | PGT | 893 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154038 |
| 2 | 🇪🇸 ES | 11543 |
| 3 | 🇧🇷 BR | 10304 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9856 |
| 6 | 🇨🇦 CA | 9797 |
| 7 | 🇮🇹 IT | 9275 |
| 8 | 🇩🇪 DE | 8893 |
| 9 | 🇬🇧 GB | 8298 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7151 |
| 12 | 🇨🇴 CO | 6664 |
| 13 | 🇬🇷 GR | 5238 |
| 14 | 🇲🇽 MX | 5138 |
| 15 | 🇨🇭 CH | 4787 |
| 16 | 🇳🇴 NO | 4644 |
| 17 | 🇹🇷 TR | 4567 |
| 18 | 🇲🇾 MY | 3160 |
| 19 | 🇵🇱 PL | 2997 |
| 20 | 🇿🇦 ZA | 2922 |
| 21 | 🇹🇭 TH | 2718 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2360 |
| 24 | 🇬🇹 GT | 2290 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1815 |
| 27 | 🇭🇷 HR | 1788 |
| 28 | 🇲🇪 ME | 1634 |
| 29 | 🇳🇱 NL | 1616 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3712 |
| 2 | Denver International Airport |  | US | 2980 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Guaymaral Airport |  | CO | 2218 |
| 5 | Indira Gandhi International Airport |  | IN | 2195 |
| 6 | Harry Reid International Airport |  | US | 2121 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1933 |
| 8 | Zurich Airport |  | CH | 1908 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1871 |
| 10 | La Aurora Airport |  | GT | 1760 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1643 |
| 12 | Chicago O'Hare International Airport |  | US | 1619 |
| 13 | Salt Lake City International Airport |  | US | 1609 |
| 14 | El Dorado International Airport |  | CO | 1603 |
| 15 | Frankfurt am Main International Airport |  | DE | 1564 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1495 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1433 |
| 19 | Madrid Barajas International Airport |  | ES | 1408 |
| 20 | Capua Airport |  | IT | 1401 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1343 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1280 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1238 |
| 25 | Charlotte/Douglas International Airport |  | US | 1220 |
| 26 | Charles de Gaulle International Airport |  | FR | 1214 |
| 27 | Kuala Lumpur International Airport |  | MY | 1191 |
| 28 | Bengaluru International Airport |  | IN | 1175 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1116 |
| 30 | Ninoy Aquino International Airport |  | PH | 1110 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1102 |
| 32 | Barcelona International Airport |  | ES | 1069 |
| 33 | Viracopos International Airport |  | BR | 1032 |
| 34 | Daniel K Inouye International Airport |  | US | 1031 |
| 35 | Seattle-Tacoma International Airport |  | US | 1031 |
| 36 | Reno/Tahoe International Airport |  | US | 1026 |
| 37 | Calgary International Airport |  | CA | 1019 |
| 38 | Oslo Gardermoen Airport |  | NO | 997 |
| 39 | Tenerife Norte Airport |  | ES | 983 |
| 40 | Amsterdam Airport Schiphol |  | NL | 973 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 916 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 661 | 21m | 244 km | 2,783.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 301 | 27m | 275 km | 1,426.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 252 | 1h 48m | 1,423 km | 6,184.5 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 239 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 217 | 50m | 556 km | 2,080.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 216 | 1h 15m | 961 km | 3,580.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 214 | 19m | 144 km | 532.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 212 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 205 | 24m | 218 km | 772.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 195 | 1h 2m | 695 km | 2,337.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RYR98KN | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Palermo / Punta Raisi Airport (LICJ) | 2026-08-08 20:04 UTC | 2026-08-08 20:56 UTC | 51m |
| MSC304 | MSC | Istanbul Airport (LTFM) | HE12 (HE12) | 2026-08-08 19:23 UTC | 2026-08-08 20:55 UTC | 1h 32m |
| N53533 |  | John Wayne/Orange County Airport (KSNA) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-08-08 20:00 UTC | 2026-08-08 20:54 UTC | 53m |
| N642ND |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-08-08 20:30 UTC | 2026-08-08 20:53 UTC | 23m |
| N929GA |  | KPBI (KPBI) | Henderson Executive Airport (KHND) | 2026-08-08 16:24 UTC | 2026-08-08 20:50 UTC | 4h 26m |
| CAP824 | CAP | Vero Beach Regional Airport (KVRB) | 23FD (23FD) | 2026-08-08 20:30 UTC | 2026-08-08 20:45 UTC | 14m |
| N6409D |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-08 19:52 UTC | 2026-08-08 20:34 UTC | 41m |
| N760VM |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-08 19:00 UTC | 2026-08-08 20:28 UTC | 1h 27m |
| XGN420 | XGN | Easton/Newnam Field (KESN) | Norfolk International Airport (KORF) | 2026-08-08 19:53 UTC | 2026-08-08 20:25 UTC | 31m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-08 20:09 UTC | 2026-08-08 20:21 UTC | 12m |
| LIFE6 | LIF | Houston/Southwest Airport (KAXH) | William P Hobby Airport (KHOU) | 2026-08-08 20:15 UTC | 2026-08-08 20:19 UTC | 4m |
| N900LW |  | Chumchal Farms Airport (71TA) | 81NM (81NM) | 2026-08-08 19:54 UTC | 2026-08-08 20:18 UTC | 24m |
| N26EK |  | Truckee-Tahoe Airport (KTRK) | Truckee-Tahoe Airport (KTRK) | 2026-08-08 20:04 UTC | 2026-08-08 20:16 UTC | 11m |
| N1387U |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-08-08 19:29 UTC | 2026-08-08 20:16 UTC | 47m |
| TKR184 | TKR | Ephrata Municipal Airport (KEPH) | Rules Roost Airport (5WA5) | 2026-08-08 19:28 UTC | 2026-08-08 20:14 UTC | 46m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-08 20:04 UTC | 2026-08-08 20:14 UTC | 10m |
| EJA901 | EJA | K36U (K36U) | Siskiyou County Airport (KSIY) | 2026-08-08 18:47 UTC | 2026-08-08 20:11 UTC | 1h 24m |
| N45DG |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-08 18:48 UTC | 2026-08-08 20:11 UTC | 1h 22m |
| N38EE |  | Minden-Tahoe Airport (KMEV) | Bryant Field (KO57) | 2026-08-08 19:01 UTC | 2026-08-08 20:09 UTC | 1h 7m |
| TKR186 | TKR | WN36 (WN36) | 3WA1 (3WA1) | 2026-08-08 19:26 UTC | 2026-08-08 20:09 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

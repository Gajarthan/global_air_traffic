# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_14:45:35_UTC-green)

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

**Latest saved flight:** 2026-08-08 14:45:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 14:45:35 UTC

- **178,417** saved flights
- **57,315** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **178,417** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,144,245.1 tonnes** estimated CO2 emissions
- **124,304,065 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7080 |
| 2 | SkyWest Airlines | 6498 |
| 3 | EJA | 3509 |
| 4 | IndiGo | 3138 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2774 |
| 7 | ENY | 2215 |
| 8 | Delta Air Lines | 2103 |
| 9 | LATAM Airlines | 1655 |
| 10 | Lufthansa | 1596 |
| 11 | AZU | 1593 |
| 12 | WIF | 1492 |
| 13 | Vueling | 1472 |
| 14 | LXJ | 1398 |
| 15 | Swiss International | 1220 |
| 16 | easyJet | 1211 |
| 17 | AXM | 1210 |
| 18 | QLK | 1093 |
| 19 | All Nippon Airways | 1088 |
| 20 | EJU | 1086 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 981 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 943 |
| 25 | GLO | 942 |
| 26 | AEE | 929 |
| 27 | Air France | 920 |
| 28 | United Airlines | 919 |
| 29 | MXY | 897 |
| 30 | PGT | 883 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152919 |
| 2 | 🇪🇸 ES | 11434 |
| 3 | 🇧🇷 BR | 10196 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9838 |
| 6 | 🇨🇦 CA | 9740 |
| 7 | 🇮🇹 IT | 9234 |
| 8 | 🇩🇪 DE | 8843 |
| 9 | 🇬🇧 GB | 8249 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7104 |
| 12 | 🇨🇴 CO | 6561 |
| 13 | 🇬🇷 GR | 5207 |
| 14 | 🇲🇽 MX | 5105 |
| 15 | 🇨🇭 CH | 4761 |
| 16 | 🇳🇴 NO | 4634 |
| 17 | 🇹🇷 TR | 4490 |
| 18 | 🇲🇾 MY | 3159 |
| 19 | 🇵🇱 PL | 2973 |
| 20 | 🇿🇦 ZA | 2916 |
| 21 | 🇹🇭 TH | 2714 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2281 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1804 |
| 27 | 🇭🇷 HR | 1770 |
| 28 | 🇲🇪 ME | 1624 |
| 29 | 🇳🇱 NL | 1607 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3676 |
| 2 | Denver International Airport |  | US | 2949 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Indira Gandhi International Airport |  | IN | 2189 |
| 5 | Guaymaral Airport |  | CO | 2182 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1927 |
| 8 | Zurich Airport |  | CH | 1899 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1855 |
| 10 | La Aurora Airport |  | GT | 1752 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1600 |
| 13 | Salt Lake City International Airport |  | US | 1592 |
| 14 | El Dorado International Airport |  | CO | 1589 |
| 15 | Frankfurt am Main International Airport |  | DE | 1559 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1478 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1430 |
| 19 | Capua Airport |  | IT | 1397 |
| 20 | Madrid Barajas International Airport |  | ES | 1392 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1323 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1263 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1225 |
| 25 | Charlotte/Douglas International Airport |  | US | 1215 |
| 26 | Charles de Gaulle International Airport |  | FR | 1212 |
| 27 | Kuala Lumpur International Airport |  | MY | 1190 |
| 28 | Bengaluru International Airport |  | IN | 1172 |
| 29 | Ninoy Aquino International Airport |  | PH | 1109 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1105 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1061 |
| 33 | Daniel K Inouye International Airport |  | US | 1026 |
| 34 | Viracopos International Airport |  | BR | 1025 |
| 35 | Seattle-Tacoma International Airport |  | US | 1025 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 992 |
| 39 | Tenerife Norte Airport |  | ES | 975 |
| 40 | Amsterdam Airport Schiphol |  | NL | 965 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 901 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 656 | 21m | 244 km | 2,762.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 415 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 299 | 27m | 275 km | 1,416.8 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 249 | 1h 48m | 1,423 km | 6,110.9 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 18 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 228 | 8m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 214 | 1h 15m | 961 km | 3,547.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 212 | 19m | 144 km | 527.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 204 | 24m | 218 km | 768.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 195 | 1h 2m | 695 km | 2,337.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GTOPE | GTO | Popham Airport (EGHP) | Llanbedr Airport (EGOD) | 2026-08-08 13:44 UTC | 2026-08-08 14:45 UTC | 1h 1m |
| EJU72PQ | EJU | London Gatwick Airport (EGKK) | Palma De Mallorca Airport (LEPA) | 2026-08-08 12:50 UTC | 2026-08-08 14:42 UTC | 1h 52m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-08 14:24 UTC | 2026-08-08 14:42 UTC | 17m |
| N811AT |  | Arlington Municipal Airport (KGKY) | Austin-Bergstrom International Airport (KAUS) | 2026-08-08 13:35 UTC | 2026-08-08 14:40 UTC | 1h 5m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-08 14:22 UTC | 2026-08-08 14:39 UTC | 17m |
| HB2311 |  | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-08-08 09:45 UTC | 2026-08-08 14:38 UTC | 4h 53m |
| N714LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Richmond Executive/Chesterfield County Airport (KFCI) | 2026-08-08 13:51 UTC | 2026-08-08 14:34 UTC | 42m |
| N260ND |  | Boire Field (KASH) | Concord Municipal Airport (KCON) | 2026-08-08 14:09 UTC | 2026-08-08 14:32 UTC | 22m |
| N229HL |  | 3IL1 (3IL1) | 3IL1 (3IL1) | 2026-08-08 14:28 UTC | 2026-08-08 14:28 UTC | 0m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-08 14:18 UTC | 2026-08-08 14:28 UTC | 10m |
| N7223Q |  | Fernando Luis Ribas Dominicci Airport (TJIG) | Fernando Luis Ribas Dominicci Airport (TJIG) | 2026-08-08 14:07 UTC | 2026-08-08 14:25 UTC | 18m |
| N6004W |  | Medina Municipal Airport (K1G5) | 2OI8 (2OI8) | 2026-08-08 13:55 UTC | 2026-08-08 14:18 UTC | 22m |
| N469BL |  | Pensacola International Airport (KPNS) | Pensacola International Airport (KPNS) | 2026-08-08 14:16 UTC | 2026-08-08 14:18 UTC | 1m |
| TGBOP | TGB | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-08-08 13:46 UTC | 2026-08-08 14:12 UTC | 25m |
| N819LM |  | Chicago Executive Airport (KPWK) | East Jordan City Airport (KY94) | 2026-08-08 13:24 UTC | 2026-08-08 14:12 UTC | 48m |
| N246DW |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-08-08 13:58 UTC | 2026-08-08 14:09 UTC | 11m |
|  |  | Fazenda Centro de Voo a Vela Ipua Airport (SDIP) | Helibras Airport (SIYS) | 2026-08-08 13:10 UTC | 2026-08-08 14:09 UTC | 58m |
| N264MC |  | Valence-Chabeuil Airport (LFLU) | Le Puy-Loudes Airport (LFHP) | 2026-08-08 13:39 UTC | 2026-08-08 14:09 UTC | 29m |
| EZY85KR | easyJet | London Gatwick Airport (EGKK) | Rennes-Saint-Jacques Airport (LFRN) | 2026-08-08 13:21 UTC | 2026-08-08 14:08 UTC | 46m |
| N73VR |  | Morristown Municipal Airport (KMMU) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-08 12:43 UTC | 2026-08-08 14:07 UTC | 1h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

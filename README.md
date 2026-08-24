# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_14:49:47_UTC-green)

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

**Latest saved flight:** 2026-08-24 14:49:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 14:49:47 UTC

- **232,075** saved flights
- **71,403** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **232,075** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,798,151.4 tonnes** estimated CO2 emissions
- **162,211,677 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9321 |
| 2 | SkyWest Airlines | 8206 |
| 3 | EJA | 4475 |
| 4 | IndiGo | 3935 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3577 |
| 7 | Delta Air Lines | 2960 |
| 8 | ENY | 2820 |
| 9 | LATAM Airlines | 2232 |
| 10 | AZU | 2158 |
| 11 | Vueling | 1986 |
| 12 | Lufthansa | 1892 |
| 13 | WIF | 1839 |
| 14 | LXJ | 1825 |
| 15 | easyJet | 1626 |
| 16 | Swiss International | 1553 |
| 17 | AXM | 1551 |
| 18 | EJU | 1486 |
| 19 | QLK | 1474 |
| 20 | United Airlines | 1473 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1293 |
| 24 | WMT | 1284 |
| 25 | VIV | 1274 |
| 26 | PGT | 1267 |
| 27 | Air France | 1261 |
| 28 | Wizz Air | 1225 |
| 29 | AEE | 1156 |
| 30 | JetBlue | 1154 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 193085 |
| 2 | 🇪🇸 ES | 14909 |
| 3 | 🇧🇷 BR | 13560 |
| 4 | 🇦🇺 AU | 13162 |
| 5 | 🇨🇦 CA | 12768 |
| 6 | 🇮🇹 IT | 12628 |
| 7 | 🇮🇳 IN | 12256 |
| 8 | 🇩🇪 DE | 11442 |
| 9 | 🇬🇧 GB | 10958 |
| 10 | 🇨🇴 CO | 9652 |
| 11 | 🇯🇵 JP | 9446 |
| 12 | 🇫🇷 FR | 9293 |
| 13 | 🇹🇷 TR | 6860 |
| 14 | 🇬🇷 GR | 6834 |
| 15 | 🇲🇽 MX | 6441 |
| 16 | 🇨🇭 CH | 6194 |
| 17 | 🇳🇴 NO | 5730 |
| 18 | 🇲🇾 MY | 4143 |
| 19 | 🇹🇭 TH | 4103 |
| 20 | 🇿🇦 ZA | 4063 |
| 21 | 🇵🇱 PL | 3861 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3184 |
| 24 | 🇬🇹 GT | 2914 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2673 |
| 27 | 🇲🇦 MA | 2355 |
| 28 | 🇲🇪 ME | 2137 |
| 29 | 🇳🇱 NL | 2082 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4821 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2835 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2664 |
| 6 | Harry Reid International Airport |  | US | 2496 |
| 7 | Zurich Airport |  | CH | 2424 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2367 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2333 |
| 10 | La Aurora Airport |  | GT | 2220 |
| 11 | El Dorado International Airport |  | CO | 2150 |
| 12 | Chicago O'Hare International Airport |  | US | 2097 |
| 13 | Salt Lake City International Airport |  | US | 2039 |
| 14 | Congonhas Airport |  | BR | 1976 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1958 |
| 16 | Frankfurt am Main International Airport |  | DE | 1851 |
| 17 | Madrid Barajas International Airport |  | ES | 1824 |
| 18 | Capua Airport |  | IT | 1824 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1747 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1720 |
| 21 | Malpensa International Airport |  | IT | 1666 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1658 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1611 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1533 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1466 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1403 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1401 |
| 32 | Viracopos International Airport |  | BR | 1380 |
| 33 | Bengaluru International Airport |  | IN | 1371 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1361 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1317 |
| 38 | Oslo Gardermoen Airport |  | NO | 1301 |
| 39 | O. R. Tambo International Airport |  | ZA | 1262 |
| 40 | Vitoria/Foronda Airport |  | ES | 1258 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1081 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 846 | 21m | 244 km | 3,562.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 569 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 519 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 382 | 27m | 275 km | 1,810.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 359 | 1h 50m | 1,423 km | 8,810.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 338 | 44m | 241 km | 1,404.0 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 307 | 24m | 218 km | 1,156.6 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 302 | 1h 38m | 1,156 km | 6,024.8 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 288 | 19m | 99 km | 493.3 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 283 | 27m | 215 km | 1,048.1 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 268 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 264 | 19m | 144 km | 656.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 248 | 1h 50m | 1,304 km | 5,579.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N274EF |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-24 14:00 UTC | 2026-08-24 14:49 UTC | 49m |
| N234WL |  | Linden Airport (KLDJ) | Laguardia Airport (KLGA) | 2026-08-24 14:29 UTC | 2026-08-24 14:41 UTC | 12m |
| BOMR816 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Lantana Ridge Airport (18XA) | 2026-08-24 13:48 UTC | 2026-08-24 14:38 UTC | 50m |
| SCU13 | SCU | OK13 (OK13) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-24 14:15 UTC | 2026-08-24 14:36 UTC | 20m |
| N211UT |  | Mesa Gateway Airport (KIWA) | 4AZ7 (4AZ7) | 2026-08-24 14:02 UTC | 2026-08-24 14:35 UTC | 33m |
| N127RF |  | Las Cruces International Airport (KLRU) | NM13 (NM13) | 2026-08-24 13:33 UTC | 2026-08-24 14:35 UTC | 1h 2m |
| N1232U |  | Frisbee Lndg Airport (MS62) | Olive Branch/Taylor Field (KOLV) | 2026-08-24 14:28 UTC | 2026-08-24 14:34 UTC | 6m |
| TRP7 | TRP | Robinson Airport (MD14) | Joint Base Andrews Airport (KADW) | 2026-08-24 14:19 UTC | 2026-08-24 14:29 UTC | 10m |
| STING21 | STI | Anacacho Ranch Airport (0XS7) | Fort Clark Springs Airport (74TX) | 2026-08-24 14:03 UTC | 2026-08-24 14:27 UTC | 23m |
| FXC22 | FXC | Morristown Municipal Airport (KMMU) | Laguardia Airport (KLGA) | 2026-08-24 14:10 UTC | 2026-08-24 14:26 UTC | 15m |
| N8116B |  | Lake In The Hills Airport (K3CK) | Jack W Watson Airport (0IL9) | 2026-08-24 13:58 UTC | 2026-08-24 14:25 UTC | 26m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-24 14:02 UTC | 2026-08-24 14:20 UTC | 17m |
| SWR2HY | Swiss International | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Zurich Airport (LSZH) | 2026-08-24 13:21 UTC | 2026-08-24 14:19 UTC | 57m |
| EPI252 | EPI | St George Regional Airport (KSGU) | Colorado City Municipal Airport (KAZC) | 2026-08-24 13:57 UTC | 2026-08-24 14:19 UTC | 21m |
| N722UE |  | North Las Vegas Airport (KVGT) | Caas Airport (NV98) | 2026-08-24 14:04 UTC | 2026-08-24 14:18 UTC | 14m |
| N636EJ |  | Springdale Municipal Airport (KASG) | Landers Loop Airport (AR89) | 2026-08-24 14:03 UTC | 2026-08-24 14:17 UTC | 13m |
| N20267 |  | Sky Acres Airport (K44N) | Sky Acres Airport (K44N) | 2026-08-24 13:42 UTC | 2026-08-24 14:15 UTC | 33m |
| N739HK |  | Double Eagle Ii Airport (KAEG) | Socorro Municipal Airport (KONM) | 2026-08-24 13:34 UTC | 2026-08-24 14:14 UTC | 39m |
| CNS1010 | CNS | Grand Junction Regional Airport (KGJT) | True Grit South Airport (CO95) | 2026-08-24 13:56 UTC | 2026-08-24 14:12 UTC | 16m |
| TGIMT | TGI | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-24 13:41 UTC | 2026-08-24 14:11 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

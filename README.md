# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_15:41:44_UTC-green)

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

**Latest saved flight:** 2026-08-23 15:41:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 15:41:44 UTC

- **228,880** saved flights
- **70,764** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,880** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,760,463.2 tonnes** estimated CO2 emissions
- **160,026,853 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9192 |
| 2 | SkyWest Airlines | 8108 |
| 3 | EJA | 4399 |
| 4 | IndiGo | 3874 |
| 5 | American Airlines | 3745 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2927 |
| 8 | ENY | 2794 |
| 9 | LATAM Airlines | 2198 |
| 10 | AZU | 2126 |
| 11 | Vueling | 1944 |
| 12 | Lufthansa | 1873 |
| 13 | WIF | 1804 |
| 14 | LXJ | 1791 |
| 15 | easyJet | 1599 |
| 16 | Swiss International | 1529 |
| 17 | AXM | 1520 |
| 18 | EJU | 1459 |
| 19 | United Airlines | 1449 |
| 20 | QLK | 1448 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1272 |
| 24 | VIV | 1255 |
| 25 | PGT | 1252 |
| 26 | WMT | 1252 |
| 27 | Air France | 1244 |
| 28 | Wizz Air | 1196 |
| 29 | JetBlue | 1143 |
| 30 | AEE | 1140 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190924 |
| 2 | 🇪🇸 ES | 14694 |
| 3 | 🇧🇷 BR | 13365 |
| 4 | 🇦🇺 AU | 12961 |
| 5 | 🇨🇦 CA | 12632 |
| 6 | 🇮🇹 IT | 12374 |
| 7 | 🇮🇳 IN | 12075 |
| 8 | 🇩🇪 DE | 11278 |
| 9 | 🇬🇧 GB | 10781 |
| 10 | 🇨🇴 CO | 9429 |
| 11 | 🇯🇵 JP | 9312 |
| 12 | 🇫🇷 FR | 9180 |
| 13 | 🇹🇷 TR | 6744 |
| 14 | 🇬🇷 GR | 6731 |
| 15 | 🇲🇽 MX | 6364 |
| 16 | 🇨🇭 CH | 6084 |
| 17 | 🇳🇴 NO | 5630 |
| 18 | 🇲🇾 MY | 4062 |
| 19 | 🇹🇭 TH | 3997 |
| 20 | 🇿🇦 ZA | 3993 |
| 21 | 🇵🇱 PL | 3811 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3144 |
| 24 | 🇬🇹 GT | 2878 |
| 25 | 🇰🇷 KR | 2705 |
| 26 | 🇭🇷 HR | 2615 |
| 27 | 🇲🇦 MA | 2321 |
| 28 | 🇲🇪 ME | 2090 |
| 29 | 🇳🇱 NL | 2053 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4775 |
| 2 | Denver International Airport |  | US | 3716 |
| 3 | Indira Gandhi International Airport |  | IN | 2791 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2648 |
| 6 | Harry Reid International Airport |  | US | 2475 |
| 7 | Zurich Airport |  | CH | 2384 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2337 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2309 |
| 10 | La Aurora Airport |  | GT | 2192 |
| 11 | El Dorado International Airport |  | CO | 2092 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2011 |
| 14 | Congonhas Airport |  | BR | 1950 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1939 |
| 16 | Frankfurt am Main International Airport |  | DE | 1836 |
| 17 | Madrid Barajas International Airport |  | ES | 1790 |
| 18 | Capua Airport |  | IT | 1783 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1714 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1702 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1650 |
| 22 | Malpensa International Airport |  | IT | 1637 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Macau International Airport |  | MO | 1596 |
| 25 | Charles de Gaulle International Airport |  | FR | 1587 |
| 26 | Ninoy Aquino International Airport |  | PH | 1509 |
| 27 | Charlotte/Douglas International Airport |  | US | 1494 |
| 28 | Kuala Lumpur International Airport |  | MY | 1471 |
| 29 | Barcelona International Airport |  | ES | 1434 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1385 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1362 |
| 32 | Viracopos International Airport |  | BR | 1360 |
| 33 | Bengaluru International Airport |  | IN | 1357 |
| 34 | Seattle-Tacoma International Airport |  | US | 1348 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1299 |
| 38 | Oslo Gardermoen Airport |  | NO | 1272 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | O. R. Tambo International Airport |  | ZA | 1240 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 833 | 21m | 244 km | 3,507.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 552 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 350 | 1h 50m | 1,423 km | 8,589.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 317 | 21m | 250 km | 1,369.2 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 296 | 24m | 218 km | 1,115.2 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 293 | 1h 38m | 1,156 km | 5,845.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 278 | 27m | 215 km | 1,029.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 268 | 1h 14m | 961 km | 4,442.2 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 261 | 19m | 144 km | 649.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 240 | 28m | 152 km | 627.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NDU679 | NDU | Pinal Airpark (KMZJ) | Sarita Airport (37AZ) | 2026-08-23 15:18 UTC | 2026-08-23 15:41 UTC | 23m |
| SFY114 | SFY | Broocke Air Patch Airport (FL95) | Fellsmere Airport (4FL3) | 2026-08-23 15:11 UTC | 2026-08-23 15:37 UTC | 25m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-08-23 15:19 UTC | 2026-08-23 15:34 UTC | 15m |
| N930AA |  | General Dewitt Spain Airport (KM01) | Jonesboro Municipal Airport (KJBR) | 2026-08-23 15:01 UTC | 2026-08-23 15:30 UTC | 28m |
| WSN88 | WSN | Lake Havasu City Airport (KHII) | Hemet-Ryan Airport (KHMT) | 2026-08-23 15:00 UTC | 2026-08-23 15:28 UTC | 27m |
| N470CM |  | Prescott Regional/Ernest A Love Field (KPRC) | Prescott Regional/Ernest A Love Field (KPRC) | 2026-08-23 15:14 UTC | 2026-08-23 15:24 UTC | 10m |
| AIZ419 | AIZ | Ben Gurion International Airport (LLBG) | Trabzon International Airport (LTCG) | 2026-08-23 13:58 UTC | 2026-08-23 15:23 UTC | 1h 24m |
| AVL110 | AVL | Washington Manassas/Harry P Davis Field (KHEF) | Hanover County Municipal Airport (KOFP) | 2026-08-23 14:40 UTC | 2026-08-23 15:19 UTC | 39m |
| XBPNV | XBP | Hermanos Serdan International Airport (MMPB) | Ingeniero Juan Guillermo Villasana Airport (MMPC) | 2026-08-23 14:53 UTC | 2026-08-23 15:17 UTC | 24m |
| N65JA |  | Aurora Municipal Airport (KARR) | Walnut Creek Airport (49IL) | 2026-08-23 14:45 UTC | 2026-08-23 15:12 UTC | 27m |
| CGOLC | CGO | Vancouver International Airport (CYVR) | Stuart Island West Airport (2WA3) | 2026-08-23 14:57 UTC | 2026-08-23 15:11 UTC | 14m |
| N81441 |  | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-08-23 14:49 UTC | 2026-08-23 15:10 UTC | 21m |
| N6419V |  | Frederick Municipal Airport (KFDK) | Eastern Wv Regional/Shepherd Field (KMRB) | 2026-08-23 14:41 UTC | 2026-08-23 15:10 UTC | 29m |
| N7998U |  | Morrow County Airport (K4I9) | Morrow County Airport (K4I9) | 2026-08-23 14:55 UTC | 2026-08-23 15:08 UTC | 12m |
| CGIOZ | CGI | CPJ6 (CPJ6) | CPJ6 (CPJ6) | 2026-08-23 14:15 UTC | 2026-08-23 15:07 UTC | 51m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-23 14:58 UTC | 2026-08-23 15:07 UTC | 9m |
| N205NB |  | Nephi Municipal Airport (KU14) | KU42 (KU42) | 2026-08-23 14:40 UTC | 2026-08-23 15:06 UTC | 25m |
| N839SP |  | Roberts Field/Redmond Municipal Airport (KRDM) | Dry Creek Airpark (OG21) | 2026-08-23 14:32 UTC | 2026-08-23 15:04 UTC | 32m |
| FIN7EN | Finnair | Helsinki Vantaa Airport (EFHK) | Pyhoselka Airport (EFPH) | 2026-08-23 14:11 UTC | 2026-08-23 15:04 UTC | 52m |
| DMDTR | DMD | Trier-Fohren Airport (EDRT) | Luxembourg-Findel International Airport (ELLX) | 2026-08-23 14:58 UTC | 2026-08-23 15:02 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

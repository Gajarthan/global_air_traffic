# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_23:15:19_UTC-green)

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

**Latest saved flight:** 2026-08-29 23:15:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-29 23:15:19 UTC

- **241,413** saved flights
- **73,254** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **241,413** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,905,784.1 tonnes** estimated CO2 emissions
- **168,451,255 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9685 |
| 2 | SkyWest Airlines | 8472 |
| 3 | EJA | 4672 |
| 4 | IndiGo | 4068 |
| 5 | American Airlines | 3889 |
| 6 | Southwest Airlines | 3632 |
| 7 | Delta Air Lines | 3076 |
| 8 | ENY | 2915 |
| 9 | LATAM Airlines | 2315 |
| 10 | AZU | 2242 |
| 11 | Vueling | 2072 |
| 12 | Lufthansa | 1941 |
| 13 | WIF | 1909 |
| 14 | LXJ | 1869 |
| 15 | easyJet | 1685 |
| 16 | Swiss International | 1627 |
| 17 | AXM | 1597 |
| 18 | EJU | 1547 |
| 19 | QLK | 1538 |
| 20 | United Airlines | 1515 |
| 21 | Alaska Airlines | 1443 |
| 22 | All Nippon Airways | 1429 |
| 23 | WMT | 1358 |
| 24 | GLO | 1347 |
| 25 | VIV | 1322 |
| 26 | Air France | 1320 |
| 27 | PGT | 1318 |
| 28 | Wizz Air | 1302 |
| 29 | JetBlue | 1196 |
| 30 | AEE | 1194 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 200120 |
| 2 | 🇪🇸 ES | 15517 |
| 3 | 🇧🇷 BR | 14069 |
| 4 | 🇦🇺 AU | 13678 |
| 5 | 🇨🇦 CA | 13434 |
| 6 | 🇮🇹 IT | 13203 |
| 7 | 🇮🇳 IN | 12663 |
| 8 | 🇩🇪 DE | 11911 |
| 9 | 🇬🇧 GB | 11402 |
| 10 | 🇨🇴 CO | 10387 |
| 11 | 🇫🇷 FR | 9731 |
| 12 | 🇯🇵 JP | 9686 |
| 13 | 🇹🇷 TR | 7160 |
| 14 | 🇬🇷 GR | 7111 |
| 15 | 🇲🇽 MX | 6667 |
| 16 | 🇨🇭 CH | 6471 |
| 17 | 🇳🇴 NO | 5950 |
| 18 | 🇹🇭 TH | 4380 |
| 19 | 🇲🇾 MY | 4278 |
| 20 | 🇿🇦 ZA | 4217 |
| 21 | 🇵🇱 PL | 4047 |
| 22 | 🇳🇿 NZ | 3316 |
| 23 | 🇵🇭 PH | 3313 |
| 24 | 🇬🇹 GT | 3031 |
| 25 | 🇰🇷 KR | 2849 |
| 26 | 🇭🇷 HR | 2788 |
| 27 | 🇲🇦 MA | 2439 |
| 28 | 🇲🇪 ME | 2255 |
| 29 | 🇳🇱 NL | 2187 |
| 30 | 🇮🇩 ID | 2112 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4989 |
| 2 | Denver International Airport |  | US | 3894 |
| 3 | Indira Gandhi International Airport |  | IN | 2948 |
| 4 | Tokyo International Airport |  | JP | 2883 |
| 5 | Guaymaral Airport |  | CO | 2701 |
| 6 | Harry Reid International Airport |  | US | 2565 |
| 7 | Zurich Airport |  | CH | 2530 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2470 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2405 |
| 10 | El Dorado International Airport |  | CO | 2353 |
| 11 | La Aurora Airport |  | GT | 2311 |
| 12 | Chicago O'Hare International Airport |  | US | 2148 |
| 13 | Salt Lake City International Airport |  | US | 2124 |
| 14 | Congonhas Airport |  | BR | 2056 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1999 |
| 16 | Frankfurt am Main International Airport |  | DE | 1910 |
| 17 | Capua Airport |  | IT | 1903 |
| 18 | Madrid Barajas International Airport |  | ES | 1900 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1814 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1777 |
| 21 | Malpensa International Airport |  | IT | 1729 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1702 |
| 23 | Charles de Gaulle International Airport |  | FR | 1690 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1689 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1609 |
| 27 | Charlotte/Douglas International Airport |  | US | 1547 |
| 28 | Kuala Lumpur International Airport |  | MY | 1545 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1538 |
| 30 | Barcelona International Airport |  | ES | 1538 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1457 |
| 32 | Viracopos International Airport |  | BR | 1434 |
| 33 | Don Mueang International Airport |  | TH | 1410 |
| 34 | Seattle-Tacoma International Airport |  | US | 1410 |
| 35 | Bengaluru International Airport |  | IN | 1407 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1403 |
| 37 | Calgary International Airport |  | CA | 1386 |
| 38 | Oslo Gardermoen Airport |  | NO | 1354 |
| 39 | Vancouver International Airport |  | CA | 1333 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1319 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1094 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 889 | 21m | 244 km | 3,743.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 621 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 613 | 24m | 225 km | 2,378.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 610 | 1h 6m | 770 km | 8,103.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 398 | 27m | 275 km | 1,886.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 380 | 1h 50m | 1,423 km | 9,325.8 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 367 | 44m | 555 km | 3,514.2 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 350 | 44m | 241 km | 1,453.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 328 | 24m | 218 km | 1,235.7 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 321 | 1h 40m | 1,156 km | 6,403.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 299 | 19m | 99 km | 512.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 294 | 26m | 215 km | 1,088.9 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 283 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 279 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 275 | 1h 14m | 961 km | 4,558.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 272 | 19m | 144 km | 676.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 259 | 1h 50m | 1,304 km | 5,826.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5217H |  | Wadsworth Municipal Airport (K3G3) | Harry Clever Field (KPHD) | 2026-08-29 22:49 UTC | 2026-08-29 23:15 UTC | 25m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-29 22:56 UTC | 2026-08-29 23:11 UTC | 14m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-29 11:47 UTC | 2026-08-29 23:10 UTC | 11h 22m |
| N901ST |  | 75IS (75IS) | Staton Airport (4LL1) | 2026-08-29 22:56 UTC | 2026-08-29 23:09 UTC | 12m |
| N280SL |  | Ocean City Municipal Airport (KOXB) | Capital City Airport (KCXY) | 2026-08-29 21:39 UTC | 2026-08-29 23:08 UTC | 1h 28m |
| CKS273 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-08-29 13:53 UTC | 2026-08-29 23:02 UTC | 9h 9m |
| THY170 | Turkish Airlines | Istanbul Hezarfen Airfield (LTBW) | Zhuhai Airport (ZGSD) | 2026-08-29 13:41 UTC | 2026-08-29 23:01 UTC | 9h 19m |
| YMV | YMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-08-29 22:38 UTC | 2026-08-29 22:58 UTC | 19m |
| AIC7FM | Air India | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-08-29 21:02 UTC | 2026-08-29 22:55 UTC | 1h 52m |
| N5352U |  | Wasilla Airport (PAWS) | Homer Airport (PAHO) | 2026-08-29 21:35 UTC | 2026-08-29 22:55 UTC | 1h 19m |
| CAP4661 | CAP | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-08-29 22:12 UTC | 2026-08-29 22:43 UTC | 30m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-08-29 22:05 UTC | 2026-08-29 22:37 UTC | 31m |
| KFB12 | KFB | Springfield/Beckley Municipal Airport (KSGH) | Van Nuys Airport (KVNY) | 2026-08-29 18:23 UTC | 2026-08-29 22:34 UTC | 4h 11m |
| PSMSA | PSM | Congonhas Airport (SBSP) | Araxa Airport (SBAX) | 2026-08-29 21:48 UTC | 2026-08-29 22:29 UTC | 41m |
| LIFELN1 | LIF | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-08-29 22:25 UTC | 2026-08-29 22:27 UTC | 1m |
|  |  | Beaufort Executive Airport (KARW) | Beaufort Executive Airport (KARW) | 2026-08-29 22:26 UTC | 2026-08-29 22:26 UTC | 0m |
| N117NT |  | Joe Foss Field (KFSD) | Wall Municipal Airport (K6V4) | 2026-08-29 21:43 UTC | 2026-08-29 22:21 UTC | 37m |
| N283TY |  | Ryan Field (KRYN) | Ryan Field (KRYN) | 2026-08-29 22:15 UTC | 2026-08-29 22:21 UTC | 5m |
| RYR1FD | Ryanair | Leeds Bradford Airport (EGNM) | Dublin Airport (EIDW) | 2026-08-29 21:44 UTC | 2026-08-29 22:18 UTC | 34m |
| JBU1263 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | 6MI0 (6MI0) | 2026-08-29 20:38 UTC | 2026-08-29 22:18 UTC | 1h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

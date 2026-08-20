# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_03:43:41_UTC-green)

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

**Latest saved flight:** 2026-08-20 03:43:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 03:43:41 UTC

- **218,096** saved flights
- **68,695** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,096** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,623,845.0 tonnes** estimated CO2 emissions
- **152,106,960 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8714 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3696 |
| 5 | American Airlines | 3635 |
| 6 | Southwest Airlines | 3468 |
| 7 | Delta Air Lines | 2821 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2068 |
| 10 | AZU | 2000 |
| 11 | Vueling | 1827 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1738 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1420 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1358 |
| 20 | EJU | 1355 |
| 21 | Alaska Airlines | 1335 |
| 22 | All Nippon Airways | 1309 |
| 23 | VIV | 1195 |
| 24 | GLO | 1187 |
| 25 | PGT | 1180 |
| 26 | Air France | 1178 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1110 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1089 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184090 |
| 2 | 🇪🇸 ES | 13942 |
| 3 | 🇧🇷 BR | 12592 |
| 4 | 🇦🇺 AU | 12277 |
| 5 | 🇨🇦 CA | 12045 |
| 6 | 🇮🇹 IT | 11562 |
| 7 | 🇮🇳 IN | 11512 |
| 8 | 🇩🇪 DE | 10768 |
| 9 | 🇬🇧 GB | 10215 |
| 10 | 🇨🇴 CO | 8975 |
| 11 | 🇯🇵 JP | 8895 |
| 12 | 🇫🇷 FR | 8668 |
| 13 | 🇬🇷 GR | 6347 |
| 14 | 🇹🇷 TR | 6268 |
| 15 | 🇲🇽 MX | 6090 |
| 16 | 🇨🇭 CH | 5770 |
| 17 | 🇳🇴 NO | 5405 |
| 18 | 🇲🇾 MY | 3753 |
| 19 | 🇿🇦 ZA | 3685 |
| 20 | 🇵🇱 PL | 3597 |
| 21 | 🇹🇭 TH | 3554 |
| 22 | 🇳🇿 NZ | 3030 |
| 23 | 🇵🇭 PH | 2916 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2618 |
| 26 | 🇭🇷 HR | 2390 |
| 27 | 🇲🇦 MA | 2189 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1909 |
| 30 | 🇮🇩 ID | 1830 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3575 |
| 3 | Tokyo International Airport |  | JP | 2673 |
| 4 | Indira Gandhi International Airport |  | IN | 2636 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2416 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2244 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2213 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2051 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1930 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1840 |
| 16 | Frankfurt am Main International Airport |  | DE | 1779 |
| 17 | Madrid Barajas International Airport |  | ES | 1703 |
| 18 | Capua Airport |  | IT | 1655 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1615 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1603 |
| 22 | Macau International Airport |  | MO | 1565 |
| 23 | Malpensa International Airport |  | IT | 1534 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1524 |
| 25 | Charles de Gaulle International Airport |  | FR | 1494 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1384 |
| 28 | Kuala Lumpur International Airport |  | MY | 1381 |
| 29 | Barcelona International Airport |  | ES | 1333 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1330 |
| 31 | Bengaluru International Airport |  | IN | 1316 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1305 |
| 33 | Seattle-Tacoma International Airport |  | US | 1298 |
| 34 | Viracopos International Airport |  | BR | 1277 |
| 35 | Calgary International Airport |  | CA | 1234 |
| 36 | Oslo Gardermoen Airport |  | NO | 1205 |
| 37 | Vitoria/Foronda Airport |  | ES | 1204 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Don Mueang International Airport |  | TH | 1171 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 780 | 21m | 244 km | 3,284.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 538 | 1h 7m | 770 km | 7,146.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 511 | 24m | 225 km | 1,982.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 363 | 27m | 275 km | 1,720.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 319 | 1h 49m | 1,423 km | 7,828.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 311 | 1h 7m | 706 km | 3,786.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 271 | 1h 38m | 1,156 km | 5,406.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 258 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 257 | 31m | 369 km | 1,635.9 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZFB | ZFB | Redcliffe Airport (YRED) | Brisbane Archerfield Airport (YBAF) | 2026-08-20 03:20 UTC | 2026-08-20 03:43 UTC | 23m |
| BAW63 | British Airways | London Heathrow Airport (EGLL) | Jomo Kenyatta International Airport (HKJK) | 2026-08-19 18:59 UTC | 2026-08-20 03:33 UTC | 8h 34m |
| OXG | OXG | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-20 03:17 UTC | 2026-08-20 03:30 UTC | 12m |
| N135TJ |  | NJ64 (NJ64) | Trenton Mercer Airport (KTTN) | 2026-08-20 02:56 UTC | 2026-08-20 03:13 UTC | 16m |
| ASA2626 | Alaska Airlines | 0TS2 (0TS2) | John F Kennedy International Airport (KJFK) | 2026-08-20 00:08 UTC | 2026-08-20 03:02 UTC | 2h 53m |
| GTI9789 | GTI | Bordeaux-Merignac (BA 106) Airport (LFBD) | Zhuhai Airport (ZGSD) | 2026-08-19 15:37 UTC | 2026-08-20 03:00 UTC | 11h 23m |
| FD614 |  | Perth Jandakot Airport (YPJT) | Wagin Airport (YWGN) | 2026-08-20 02:26 UTC | 2026-08-20 02:58 UTC | 31m |
| N523AB |  | Erie Municipal Airport (KEIK) | Rocky Mountain Metro Airport (KBJC) | 2026-08-20 02:39 UTC | 2026-08-20 02:54 UTC | 15m |
| CCA103 | Air China | Tianjin Binhai International Airport (ZBTJ) | Zhuhai Airport (ZGSD) | 2026-08-20 00:16 UTC | 2026-08-20 02:52 UTC | 2h 35m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-08-20 02:04 UTC | 2026-08-20 02:50 UTC | 45m |
| USHER11 | USH | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-08-20 00:56 UTC | 2026-08-20 02:47 UTC | 1h 50m |
| PFA316 | PFA | Broocke Air Patch Airport (FL95) | Vero Beach Regional Airport (KVRB) | 2026-08-20 00:45 UTC | 2026-08-20 02:46 UTC | 2h 1m |
| CUL552 | CUL | WA70 (WA70) | 3WA1 (3WA1) | 2026-08-20 02:28 UTC | 2026-08-20 02:44 UTC | 15m |
| XASKA | XAS | Estancia Floresta Airport (SJGW) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-08-19 15:20 UTC | 2026-08-20 02:44 UTC | 11h 24m |
| N268Z |  | Byron Airport (KC83) | Tracy Municipal Airport (KTCY) | 2026-08-20 02:18 UTC | 2026-08-20 02:43 UTC | 25m |
| C2701 |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-20 02:02 UTC | 2026-08-20 02:41 UTC | 38m |
| AUB128 | AUB | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-08-20 02:33 UTC | 2026-08-20 02:40 UTC | 6m |
| N221LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-08-20 01:20 UTC | 2026-08-20 02:37 UTC | 1h 17m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Fairview Airport (YFVW) | 2026-08-20 02:06 UTC | 2026-08-20 02:36 UTC | 30m |
| FDX1254 | FDX | Rhode Island Tf Green International Airport (KPVD) | Basting Airport (3II3) | 2026-08-20 00:52 UTC | 2026-08-20 02:35 UTC | 1h 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

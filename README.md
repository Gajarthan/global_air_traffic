# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_09:14:51_UTC-green)

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

**Latest saved flight:** 2026-08-22 09:14:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 09:14:51 UTC

- **225,030** saved flights
- **70,087** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **225,030** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,710,593.4 tonnes** estimated CO2 emissions
- **157,135,848 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9020 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4353 |
| 4 | IndiGo | 3801 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2879 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2140 |
| 10 | AZU | 2074 |
| 11 | Vueling | 1899 |
| 12 | Lufthansa | 1850 |
| 13 | WIF | 1789 |
| 14 | LXJ | 1777 |
| 15 | easyJet | 1555 |
| 16 | Swiss International | 1496 |
| 17 | AXM | 1485 |
| 18 | QLK | 1420 |
| 19 | United Airlines | 1417 |
| 20 | EJU | 1416 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1350 |
| 23 | GLO | 1244 |
| 24 | PGT | 1236 |
| 25 | VIV | 1231 |
| 26 | Air France | 1221 |
| 27 | WMT | 1199 |
| 28 | Wizz Air | 1158 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1120 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188728 |
| 2 | 🇪🇸 ES | 14403 |
| 3 | 🇧🇷 BR | 13053 |
| 4 | 🇦🇺 AU | 12770 |
| 5 | 🇨🇦 CA | 12480 |
| 6 | 🇮🇹 IT | 12035 |
| 7 | 🇮🇳 IN | 11852 |
| 8 | 🇩🇪 DE | 11076 |
| 9 | 🇬🇧 GB | 10535 |
| 10 | 🇨🇴 CO | 9256 |
| 11 | 🇯🇵 JP | 9161 |
| 12 | 🇫🇷 FR | 8975 |
| 13 | 🇹🇷 TR | 6572 |
| 14 | 🇬🇷 GR | 6560 |
| 15 | 🇲🇽 MX | 6259 |
| 16 | 🇨🇭 CH | 5919 |
| 17 | 🇳🇴 NO | 5567 |
| 18 | 🇲🇾 MY | 3953 |
| 19 | 🇿🇦 ZA | 3883 |
| 20 | 🇹🇭 TH | 3842 |
| 21 | 🇵🇱 PL | 3727 |
| 22 | 🇳🇿 NZ | 3138 |
| 23 | 🇵🇭 PH | 3070 |
| 24 | 🇬🇹 GT | 2850 |
| 25 | 🇰🇷 KR | 2673 |
| 26 | 🇭🇷 HR | 2521 |
| 27 | 🇲🇦 MA | 2261 |
| 28 | 🇲🇪 ME | 2004 |
| 29 | 🇳🇱 NL | 1997 |
| 30 | 🇮🇩 ID | 1940 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2739 |
| 4 | Indira Gandhi International Airport |  | IN | 2729 |
| 5 | Guaymaral Airport |  | CO | 2630 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2331 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2274 |
| 10 | La Aurora Airport |  | GT | 2172 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1909 |
| 16 | Frankfurt am Main International Airport |  | DE | 1816 |
| 17 | Madrid Barajas International Airport |  | ES | 1757 |
| 18 | Capua Airport |  | IT | 1728 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1677 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1667 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1592 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1587 |
| 24 | Malpensa International Airport |  | IT | 1579 |
| 25 | Charles de Gaulle International Airport |  | FR | 1555 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1467 |
| 28 | Kuala Lumpur International Airport |  | MY | 1439 |
| 29 | Barcelona International Airport |  | ES | 1390 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1368 |
| 31 | Bengaluru International Airport |  | IN | 1341 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1333 |
| 33 | Seattle-Tacoma International Airport |  | US | 1329 |
| 34 | Viracopos International Airport |  | BR | 1323 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1262 |
| 38 | Oslo Gardermoen Airport |  | NO | 1253 |
| 39 | Vitoria/Foronda Airport |  | ES | 1242 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1212 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 815 | 21m | 244 km | 3,431.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 560 | 1h 7m | 770 km | 7,439.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 553 | 24m | 225 km | 2,145.4 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 354 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 337 | 1h 50m | 1,423 km | 8,270.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 327 | 44m | 241 km | 1,358.3 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 286 | 1h 38m | 1,156 km | 5,705.6 t |
| 17 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 285 | 44m | 555 km | 2,729.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 282 | 24m | 218 km | 1,062.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 280 | 19m | 99 km | 479.6 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 257 | 19m | 144 km | 639.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKCUN20 | OKC | Brno-Turany Airport (LKTB) | Brno-Turany Airport (LKTB) | 2026-08-22 08:13 UTC | 2026-08-22 09:14 UTC | 1h 1m |
| DAL2186 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Fairbanks International Airport (PAFA) | 2026-08-22 05:26 UTC | 2026-08-22 08:33 UTC | 3h 7m |
| SUBTR | SUB | October Airport (HEOC) | HE30 (HE30) | 2026-08-22 07:57 UTC | 2026-08-22 08:33 UTC | 36m |
| ANE2305 | ANE | Santiago de Compostela Airport (LEST) | Leon Airport (LELN) | 2026-08-22 08:01 UTC | 2026-08-22 08:29 UTC | 28m |
| DLH4X | Lufthansa | Munich International Airport (EDDM) | Berlin Brandenburg Airport (EDDB) | 2026-08-22 07:46 UTC | 2026-08-22 08:29 UTC | 43m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-08-22 08:08 UTC | 2026-08-22 08:26 UTC | 17m |
| 8AX |  | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-08-22 08:12 UTC | 2026-08-22 08:25 UTC | 13m |
| FBTQY | FBT | Villefranche De Rouergue Airport (LFCV) | Villefranche De Rouergue Airport (LFCV) | 2026-08-22 07:56 UTC | 2026-08-22 08:25 UTC | 28m |
| THA211 | Thai Airways | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 2026-08-22 07:44 UTC | 2026-08-22 08:23 UTC | 38m |
| KLC1787 | KLC | Amsterdam Airport Schiphol (EHAM) | Hannover Airport (EDDV) | 2026-08-22 07:47 UTC | 2026-08-22 08:23 UTC | 36m |
| ZKICU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-22 08:17 UTC | 2026-08-22 08:21 UTC | 4m |
| HBXVF | HBX | Buochs Airport (LSZC) | Zurich Airport (LSZH) | 2026-08-22 08:03 UTC | 2026-08-22 08:18 UTC | 14m |
| AXB2931 | AXB | Bengaluru International Airport (VOBL) | Yongphulla Airport (VQ10) | 2026-08-22 05:44 UTC | 2026-08-22 08:16 UTC | 2h 32m |
| WMT6MM | WMT | Stuttgart Airport (EDDS) | Sibiu International Airport (LRSB) | 2026-08-22 06:59 UTC | 2026-08-22 08:16 UTC | 1h 16m |
| AFR54YT | Air France | Charles de Gaulle International Airport (LFPG) | London Gatwick Airport (EGKK) | 2026-08-22 07:32 UTC | 2026-08-22 08:16 UTC | 43m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 08:05 UTC | 2026-08-22 08:15 UTC | 10m |
| FJIRZ | FJI | Toulouse-Lasbordes Airport (LFCL) | Toulouse-Lasbordes Airport (LFCL) | 2026-08-22 07:09 UTC | 2026-08-22 08:14 UTC | 1h 5m |
| WUK276 | WUK | London Luton Airport (EGGW) | Plovdiv International Airport (LBPD) | 2026-08-22 05:34 UTC | 2026-08-22 08:14 UTC | 2h 39m |
| AIQ3360 | AIQ | Don Mueang International Airport (VTBD) | Surin Airport (VTUJ) | 2026-08-22 07:39 UTC | 2026-08-22 08:14 UTC | 34m |
| RYR1FT | Ryanair | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-08-22 07:35 UTC | 2026-08-22 08:12 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_07:43:41_UTC-green)

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

**Latest saved flight:** 2026-08-09 07:43:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 07:43:41 UTC

- **180,447** saved flights
- **57,759** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **180,447** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,168,433.6 tonnes** estimated CO2 emissions
- **125,706,294 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7142 |
| 2 | SkyWest Airlines | 6582 |
| 3 | EJA | 3555 |
| 4 | IndiGo | 3161 |
| 5 | Southwest Airlines | 2840 |
| 6 | American Airlines | 2817 |
| 7 | ENY | 2250 |
| 8 | Delta Air Lines | 2142 |
| 9 | LATAM Airlines | 1680 |
| 10 | AZU | 1613 |
| 11 | Lufthansa | 1602 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1490 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1229 |
| 16 | Swiss International | 1227 |
| 17 | AXM | 1219 |
| 18 | QLK | 1115 |
| 19 | EJU | 1100 |
| 20 | Alaska Airlines | 1097 |
| 21 | All Nippon Airways | 1096 |
| 22 | VIV | 996 |
| 23 | GLO | 965 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 941 |
| 27 | United Airlines | 929 |
| 28 | Air France | 924 |
| 29 | MXY | 905 |
| 30 | PGT | 903 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154722 |
| 2 | 🇪🇸 ES | 11580 |
| 3 | 🇧🇷 BR | 10344 |
| 4 | 🇦🇺 AU | 10177 |
| 5 | 🇮🇳 IN | 9914 |
| 6 | 🇨🇦 CA | 9852 |
| 7 | 🇮🇹 IT | 9308 |
| 8 | 🇩🇪 DE | 8911 |
| 9 | 🇬🇧 GB | 8312 |
| 10 | 🇯🇵 JP | 7296 |
| 11 | 🇫🇷 FR | 7158 |
| 12 | 🇨🇴 CO | 6707 |
| 13 | 🇬🇷 GR | 5268 |
| 14 | 🇲🇽 MX | 5164 |
| 15 | 🇨🇭 CH | 4798 |
| 16 | 🇳🇴 NO | 4646 |
| 17 | 🇹🇷 TR | 4614 |
| 18 | 🇲🇾 MY | 3181 |
| 19 | 🇵🇱 PL | 3010 |
| 20 | 🇿🇦 ZA | 2932 |
| 21 | 🇹🇭 TH | 2751 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2390 |
| 24 | 🇬🇹 GT | 2294 |
| 25 | 🇰🇷 KR | 2256 |
| 26 | 🇲🇦 MA | 1818 |
| 27 | 🇭🇷 HR | 1796 |
| 28 | 🇲🇪 ME | 1636 |
| 29 | 🇳🇱 NL | 1618 |
| 30 | 🇲🇴 MO | 1512 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3732 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2266 |
| 4 | Guaymaral Airport |  | CO | 2223 |
| 5 | Indira Gandhi International Airport |  | IN | 2213 |
| 6 | Harry Reid International Airport |  | US | 2126 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1941 |
| 8 | Zurich Airport |  | CH | 1913 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1762 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1615 |
| 14 | El Dorado International Airport |  | CO | 1611 |
| 15 | Frankfurt am Main International Airport |  | DE | 1565 |
| 16 | Macau International Airport |  | MO | 1512 |
| 17 | Congonhas Airport |  | BR | 1500 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1436 |
| 19 | Madrid Barajas International Airport |  | ES | 1415 |
| 20 | Capua Airport |  | IT | 1410 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1351 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1284 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1242 |
| 25 | Charlotte/Douglas International Airport |  | US | 1224 |
| 26 | Charles de Gaulle International Airport |  | FR | 1216 |
| 27 | Kuala Lumpur International Airport |  | MY | 1196 |
| 28 | Bengaluru International Airport |  | IN | 1178 |
| 29 | Ninoy Aquino International Airport |  | PH | 1125 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1122 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1074 |
| 33 | Seattle-Tacoma International Airport |  | US | 1041 |
| 34 | Daniel K Inouye International Airport |  | US | 1040 |
| 35 | Viracopos International Airport |  | BR | 1036 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 998 |
| 39 | Tenerife Norte Airport |  | ES | 983 |
| 40 | Amsterdam Airport Schiphol |  | NL | 975 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 669 | 21m | 244 km | 2,817.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 427 | 1h 8m | 770 km | 5,672.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 426 | 24m | 225 km | 1,652.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 303 | 27m | 275 km | 1,435.8 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 297 | 1h 7m | 706 km | 3,616.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 253 | 1h 48m | 1,423 km | 6,209.0 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 235 | 20m | 250 km | 1,015.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 215 | 19m | 144 km | 534.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 211 | 1h 38m | 1,156 km | 4,209.4 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 210 | 31m | 369 km | 1,336.7 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 206 | 24m | 218 km | 776.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-09 07:31 UTC | 2026-08-09 07:43 UTC | 12m |
| HSOIC1 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-08-09 07:07 UTC | 2026-08-09 07:43 UTC | 36m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 07:27 UTC | 2026-08-09 07:40 UTC | 12m |
| AEE4SR | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-09 07:16 UTC | 2026-08-09 07:34 UTC | 18m |
| LIFE7 | LIF | William P Hobby Airport (KHOU) | KEYQ (KEYQ) | 2026-08-09 06:55 UTC | 2026-08-09 07:18 UTC | 23m |
| CSZ9601 | CSZ | Shenzhen Bao'an International Airport (ZGSZ) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-09 04:54 UTC | 2026-08-09 07:18 UTC | 2h 24m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-08-09 06:53 UTC | 2026-08-09 07:08 UTC | 14m |
| EJU68QR | EJU | Alicante International Airport (LEAL) | Biel-Kappelen Airport (LSZP) | 2026-08-09 05:10 UTC | 2026-08-09 07:07 UTC | 1h 56m |
| ESF615 | ESF | Miami International Airport (KMIA) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-09 02:34 UTC | 2026-08-09 07:06 UTC | 4h 31m |
| FSF663Z | FSF | St. Johann In Tirol Airport (LOIJ) | Raron Airport (LSTA) | 2026-08-09 06:05 UTC | 2026-08-09 07:04 UTC | 58m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-09 06:43 UTC | 2026-08-09 06:56 UTC | 12m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 06:46 UTC | 2026-08-09 06:56 UTC | 10m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-09 06:32 UTC | 2026-08-09 06:54 UTC | 22m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-08-09 06:16 UTC | 2026-08-09 06:51 UTC | 35m |
| SFR118 | SFR | Cape Town International Airport (FACT) | Rand Airport (FAGM) | 2026-08-09 05:19 UTC | 2026-08-09 06:50 UTC | 1h 30m |
| THY1BX | Turkish Airlines | Istanbul Airport (LTFM) | Smolensk North Airport (XUBS) | 2026-08-09 04:33 UTC | 2026-08-09 06:48 UTC | 2h 14m |
| AEE590 | AEE | Thessaloniki Macedonia International Airport (LGTS) | Kalymnos Airport (LGKY) | 2026-08-09 06:08 UTC | 2026-08-09 06:47 UTC | 39m |
| BAW82DM | British Airways | London Heathrow Airport (EGLL) | Dublin Airport (EIDW) | 2026-08-09 05:52 UTC | 2026-08-09 06:45 UTC | 53m |
| EZS59XA | EZS | Nice-Cote d'Azur Airport (LFMN) | Annemasse Airport (LFLI) | 2026-08-09 06:02 UTC | 2026-08-09 06:45 UTC | 43m |
| ENT7755 | ENT | Poznań-Ławica Airport (EPPO) | Antalya International Airport (LTAI) | 2026-08-09 04:04 UTC | 2026-08-09 06:45 UTC | 2h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

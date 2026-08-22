# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_14:57:22_UTC-green)

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

**Latest saved flight:** 2026-08-22 14:57:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 14:57:22 UTC

- **225,756** saved flights
- **70,219** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **225,756** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,720,376.6 tonnes** estimated CO2 emissions
- **157,702,993 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9062 |
| 2 | SkyWest Airlines | 7999 |
| 3 | EJA | 4355 |
| 4 | IndiGo | 3821 |
| 5 | American Airlines | 3706 |
| 6 | Southwest Airlines | 3525 |
| 7 | Delta Air Lines | 2879 |
| 8 | ENY | 2760 |
| 9 | LATAM Airlines | 2156 |
| 10 | AZU | 2089 |
| 11 | Vueling | 1911 |
| 12 | Lufthansa | 1852 |
| 13 | WIF | 1796 |
| 14 | LXJ | 1780 |
| 15 | easyJet | 1565 |
| 16 | Swiss International | 1504 |
| 17 | AXM | 1493 |
| 18 | QLK | 1421 |
| 19 | EJU | 1420 |
| 20 | United Airlines | 1419 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1251 |
| 24 | PGT | 1242 |
| 25 | VIV | 1234 |
| 26 | Air France | 1230 |
| 27 | WMT | 1213 |
| 28 | Wizz Air | 1172 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1124 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188928 |
| 2 | 🇪🇸 ES | 14466 |
| 3 | 🇧🇷 BR | 13143 |
| 4 | 🇦🇺 AU | 12776 |
| 5 | 🇨🇦 CA | 12492 |
| 6 | 🇮🇹 IT | 12110 |
| 7 | 🇮🇳 IN | 11911 |
| 8 | 🇩🇪 DE | 11116 |
| 9 | 🇬🇧 GB | 10617 |
| 10 | 🇨🇴 CO | 9277 |
| 11 | 🇯🇵 JP | 9192 |
| 12 | 🇫🇷 FR | 9033 |
| 13 | 🇹🇷 TR | 6616 |
| 14 | 🇬🇷 GR | 6603 |
| 15 | 🇲🇽 MX | 6268 |
| 16 | 🇨🇭 CH | 5973 |
| 17 | 🇳🇴 NO | 5590 |
| 18 | 🇲🇾 MY | 3981 |
| 19 | 🇿🇦 ZA | 3911 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3753 |
| 22 | 🇳🇿 NZ | 3138 |
| 23 | 🇵🇭 PH | 3085 |
| 24 | 🇬🇹 GT | 2858 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2546 |
| 27 | 🇲🇦 MA | 2273 |
| 28 | 🇲🇪 ME | 2031 |
| 29 | 🇳🇱 NL | 2019 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4707 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2748 |
| 4 | Indira Gandhi International Airport |  | IN | 2743 |
| 5 | Guaymaral Airport |  | CO | 2632 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2347 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2283 |
| 10 | La Aurora Airport |  | GT | 2178 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1921 |
| 16 | Frankfurt am Main International Airport |  | DE | 1819 |
| 17 | Madrid Barajas International Airport |  | ES | 1762 |
| 18 | Capua Airport |  | IT | 1741 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1679 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1677 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Malpensa International Airport |  | IT | 1594 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 25 | Charles de Gaulle International Airport |  | FR | 1564 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1475 |
| 28 | Kuala Lumpur International Airport |  | MY | 1446 |
| 29 | Barcelona International Airport |  | ES | 1402 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1370 |
| 31 | Bengaluru International Airport |  | IN | 1344 |
| 32 | Viracopos International Airport |  | BR | 1335 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1334 |
| 34 | Seattle-Tacoma International Airport |  | US | 1329 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1310 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1259 |
| 39 | Vitoria/Foronda Airport |  | ES | 1242 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1222 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1073 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 816 | 21m | 244 km | 3,436.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 563 | 1h 6m | 770 km | 7,479.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 530 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 511 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 340 | 1h 50m | 1,423 km | 8,344.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 300 | 22m | 55 km | 285.1 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 293 | 44m | 555 km | 2,805.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 289 | 1h 38m | 1,156 km | 5,765.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 284 | 24m | 218 km | 1,069.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 281 | 19m | 99 km | 481.3 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 265 | 1h 14m | 961 km | 4,392.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 258 | 19m | 144 km | 641.8 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N470RG |  | KU77 (KU77) | Provo Municipal Airport (KPVU) | 2026-08-22 14:31 UTC | 2026-08-22 14:57 UTC | 25m |
| N35683 |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-08-22 14:38 UTC | 2026-08-22 14:52 UTC | 13m |
| N734ES |  | Ramona Airport (KRNM) | Chino Airport (KCNO) | 2026-08-22 14:04 UTC | 2026-08-22 14:50 UTC | 46m |
| CXK1107 | CXK | Conroe/North Houston Regional Airport (KCXO) | Navasota Municipal Airport (K60R) | 2026-08-22 13:54 UTC | 2026-08-22 14:47 UTC | 52m |
| N4120R |  | 36AZ (36AZ) | Sarita Airport (37AZ) | 2026-08-22 12:44 UTC | 2026-08-22 14:46 UTC | 2h 1m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-08-22 14:31 UTC | 2026-08-22 14:45 UTC | 14m |
| TCFNH | TCF | Ataturk International Airport (LTBA) | Mikonos Airport (LGMK) | 2026-08-22 13:54 UTC | 2026-08-22 14:42 UTC | 48m |
| N40EA |  | Knoxville Municipal Airport (KOXV) | Knoxville Municipal Airport (KOXV) | 2026-08-22 14:19 UTC | 2026-08-22 14:40 UTC | 21m |
| N5518W |  | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Pheasant Wings Airport (26OK) | 2026-08-22 14:01 UTC | 2026-08-22 14:33 UTC | 32m |
| N202FF |  | Flying Cloud Airport (KFCM) | Webb Lake Airport (MN00) | 2026-08-22 13:52 UTC | 2026-08-22 14:32 UTC | 40m |
| HB3342 |  | Buttwil Airport (LSZU) | Buttwil Airport (LSZU) | 2026-08-22 13:21 UTC | 2026-08-22 14:28 UTC | 1h 7m |
| N1293E |  | Airglades Airport (K2IS) | Airglades Airport (K2IS) | 2026-08-22 14:15 UTC | 2026-08-22 14:26 UTC | 10m |
| CJT490 | CJT | Louisville Muhammad Ali International Airport (KSDF) | Vancouver International Airport (CYVR) | 2026-08-22 09:51 UTC | 2026-08-22 14:25 UTC | 4h 33m |
| WIF3LA | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-22 13:41 UTC | 2026-08-22 14:20 UTC | 39m |
| BSM31 | BSM | Rocket Ranch Airport (OK90) | TA22 (TA22) | 2026-08-22 13:59 UTC | 2026-08-22 14:19 UTC | 20m |
| N6309B |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-08-22 14:04 UTC | 2026-08-22 14:19 UTC | 14m |
| N745CD |  | Rancho Murieta Airport (KRIU) | CA38 (CA38) | 2026-08-22 13:49 UTC | 2026-08-22 14:18 UTC | 28m |
| N342NL |  | Fort Lauderdale Executive Airport (KFXE) | Fort Lauderdale Executive Airport (KFXE) | 2026-08-22 14:10 UTC | 2026-08-22 14:17 UTC | 6m |
| N65716 |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-08-22 14:13 UTC | 2026-08-22 14:16 UTC | 2m |
| N383AA |  | Casa Grande Airport (SPCG) | Quiruvilca Airport (SPQR) | 2026-08-22 14:02 UTC | 2026-08-22 14:15 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

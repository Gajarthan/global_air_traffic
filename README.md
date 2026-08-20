# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_16:55:29_UTC-green)

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

**Latest saved flight:** 2026-08-20 16:55:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 16:55:29 UTC

- **219,852** saved flights
- **69,011** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **219,852** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,647,055.8 tonnes** estimated CO2 emissions
- **153,452,507 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8818 |
| 2 | SkyWest Airlines | 7826 |
| 3 | EJA | 4260 |
| 4 | IndiGo | 3731 |
| 5 | American Airlines | 3647 |
| 6 | Southwest Airlines | 3475 |
| 7 | Delta Air Lines | 2832 |
| 8 | ENY | 2706 |
| 9 | LATAM Airlines | 2088 |
| 10 | AZU | 2013 |
| 11 | Vueling | 1849 |
| 12 | Lufthansa | 1829 |
| 13 | WIF | 1761 |
| 14 | LXJ | 1734 |
| 15 | easyJet | 1524 |
| 16 | Swiss International | 1464 |
| 17 | AXM | 1444 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1371 |
| 21 | Alaska Airlines | 1340 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1201 |
| 24 | VIV | 1199 |
| 25 | Air France | 1192 |
| 26 | PGT | 1191 |
| 27 | WMT | 1158 |
| 28 | Wizz Air | 1121 |
| 29 | JetBlue | 1115 |
| 30 | AEE | 1102 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184903 |
| 2 | 🇪🇸 ES | 14098 |
| 3 | 🇧🇷 BR | 12697 |
| 4 | 🇦🇺 AU | 12418 |
| 5 | 🇨🇦 CA | 12121 |
| 6 | 🇮🇹 IT | 11713 |
| 7 | 🇮🇳 IN | 11631 |
| 8 | 🇩🇪 DE | 10870 |
| 9 | 🇬🇧 GB | 10333 |
| 10 | 🇨🇴 CO | 9018 |
| 11 | 🇯🇵 JP | 8962 |
| 12 | 🇫🇷 FR | 8758 |
| 13 | 🇬🇷 GR | 6414 |
| 14 | 🇹🇷 TR | 6329 |
| 15 | 🇲🇽 MX | 6107 |
| 16 | 🇨🇭 CH | 5821 |
| 17 | 🇳🇴 NO | 5469 |
| 18 | 🇲🇾 MY | 3819 |
| 19 | 🇿🇦 ZA | 3761 |
| 20 | 🇹🇭 TH | 3655 |
| 21 | 🇵🇱 PL | 3647 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2961 |
| 24 | 🇬🇹 GT | 2785 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2438 |
| 27 | 🇲🇦 MA | 2216 |
| 28 | 🇳🇱 NL | 1957 |
| 29 | 🇲🇪 ME | 1942 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4610 |
| 2 | Denver International Airport |  | US | 3585 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2666 |
| 5 | Guaymaral Airport |  | CO | 2597 |
| 6 | Harry Reid International Airport |  | US | 2421 |
| 7 | Zurich Airport |  | CH | 2283 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2254 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2235 |
| 10 | La Aurora Airport |  | GT | 2122 |
| 11 | El Dorado International Airport |  | CO | 2058 |
| 12 | Chicago O'Hare International Airport |  | US | 2013 |
| 13 | Salt Lake City International Airport |  | US | 1935 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1902 |
| 15 | Congonhas Airport |  | BR | 1859 |
| 16 | Frankfurt am Main International Airport |  | DE | 1792 |
| 17 | Madrid Barajas International Airport |  | ES | 1727 |
| 18 | Capua Airport |  | IT | 1680 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1645 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1623 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1616 |
| 22 | Macau International Airport |  | MO | 1579 |
| 23 | Malpensa International Airport |  | IT | 1546 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1513 |
| 26 | Charlotte/Douglas International Airport |  | US | 1463 |
| 27 | Ninoy Aquino International Airport |  | PH | 1408 |
| 28 | Kuala Lumpur International Airport |  | MY | 1402 |
| 29 | Barcelona International Airport |  | ES | 1347 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1336 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1301 |
| 34 | Viracopos International Airport |  | BR | 1287 |
| 35 | Calgary International Airport |  | CA | 1237 |
| 36 | Vitoria/Foronda Airport |  | ES | 1220 |
| 37 | Oslo Gardermoen Airport |  | NO | 1219 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1215 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1182 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 787 | 21m | 244 km | 3,313.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 498 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 490 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 369 | 27m | 275 km | 1,748.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 323 | 1h 50m | 1,423 km | 7,926.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 322 | 44m | 241 km | 1,337.5 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 274 | 1h 38m | 1,156 km | 5,466.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 272 | 24m | 218 km | 1,024.7 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 259 | 1h 14m | 961 km | 4,293.1 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-20 16:37 UTC | 2026-08-20 16:55 UTC | 18m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-08-20 16:02 UTC | 2026-08-20 16:51 UTC | 48m |
| UPS118 | UPS | Narita International Airport (RJAA) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-08-20 12:48 UTC | 2026-08-20 16:50 UTC | 4h 1m |
| CXK225 | CXK | Georgetown Executive Airport (KGTU) | Easterwood Field (KCLL) | 2026-08-20 16:03 UTC | 2026-08-20 16:50 UTC | 46m |
| N638SS |  | Santa Monica Municipal Airport (KSMO) | Santa Barbara Municipal Airport (KSBA) | 2026-08-20 15:54 UTC | 2026-08-20 16:47 UTC | 52m |
| N414GM |  | Mason City Municipal Airport (KMCW) | Mason City Municipal Airport (KMCW) | 2026-08-20 16:36 UTC | 2026-08-20 16:45 UTC | 8m |
| N5197R |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-08-20 16:26 UTC | 2026-08-20 16:38 UTC | 11m |
| N226LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-08-20 15:31 UTC | 2026-08-20 16:37 UTC | 1h 6m |
| BLZR216 | BLZ | Kingsville Nas Airport (KNQI) | El Coyote Ranch Airport (2TA8) | 2026-08-20 16:15 UTC | 2026-08-20 16:36 UTC | 21m |
| N138BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-08-20 16:06 UTC | 2026-08-20 16:36 UTC | 30m |
| N814SS |  | Trading Bay Production Airport (5AK0) | Nikolai Creek Airport (9AK3) | 2026-08-20 16:25 UTC | 2026-08-20 16:36 UTC | 11m |
| CFJHA | CFJ | Sechelt-Gibsons Airport (CAP3) | Nanaimo Airport (CYCD) | 2026-08-20 16:23 UTC | 2026-08-20 16:34 UTC | 11m |
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-20 16:18 UTC | 2026-08-20 16:34 UTC | 16m |
| N977DT |  | Midland International Air And Space Port Airport (KMAF) | 81NM (81NM) | 2026-08-20 16:00 UTC | 2026-08-20 16:29 UTC | 29m |
| ERU29 | ERU | Big Sandy Airport (AZ71) | Big Sandy Airport (AZ71) | 2026-08-20 16:25 UTC | 2026-08-20 16:29 UTC | 3m |
| N721AZ |  | Phoenix Sky Harbor International Airport (KPHX) | Henderson Executive Airport (KHND) | 2026-08-20 15:47 UTC | 2026-08-20 16:28 UTC | 41m |
| AUR214 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-08-20 16:09 UTC | 2026-08-20 16:27 UTC | 18m |
| ERU11 | ERU | AZ86 (AZ86) | Cottonwood Airport (KP52) | 2026-08-20 16:08 UTC | 2026-08-20 16:27 UTC | 19m |
| N591SS |  | Reno/Tahoe International Airport (KRNO) | Truckee-Tahoe Airport (KTRK) | 2026-08-20 16:03 UTC | 2026-08-20 16:24 UTC | 21m |
| N318SV |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-08-20 15:41 UTC | 2026-08-20 16:24 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

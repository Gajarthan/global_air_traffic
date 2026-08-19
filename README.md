# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_19:32:47_UTC-green)

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

**Latest saved flight:** 2026-08-19 19:32:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 19:32:47 UTC

- **217,009** saved flights
- **68,462** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **217,009** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,610,724.6 tonnes** estimated CO2 emissions
- **151,346,352 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8680 |
| 2 | SkyWest Airlines | 7748 |
| 3 | EJA | 4217 |
| 4 | IndiGo | 3691 |
| 5 | American Airlines | 3616 |
| 6 | Southwest Airlines | 3448 |
| 7 | Delta Air Lines | 2806 |
| 8 | ENY | 2681 |
| 9 | LATAM Airlines | 2053 |
| 10 | AZU | 1988 |
| 11 | Vueling | 1823 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1737 |
| 14 | LXJ | 1708 |
| 15 | easyJet | 1506 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1369 |
| 19 | EJU | 1353 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1327 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1191 |
| 24 | GLO | 1181 |
| 25 | Air France | 1177 |
| 26 | PGT | 1177 |
| 27 | WMT | 1139 |
| 28 | JetBlue | 1106 |
| 29 | Wizz Air | 1104 |
| 30 | AEE | 1088 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 182909 |
| 2 | 🇪🇸 ES | 13921 |
| 3 | 🇧🇷 BR | 12513 |
| 4 | 🇦🇺 AU | 12169 |
| 5 | 🇨🇦 CA | 11948 |
| 6 | 🇮🇹 IT | 11522 |
| 7 | 🇮🇳 IN | 11491 |
| 8 | 🇩🇪 DE | 10754 |
| 9 | 🇬🇧 GB | 10196 |
| 10 | 🇨🇴 CO | 8898 |
| 11 | 🇯🇵 JP | 8870 |
| 12 | 🇫🇷 FR | 8657 |
| 13 | 🇬🇷 GR | 6341 |
| 14 | 🇹🇷 TR | 6243 |
| 15 | 🇲🇽 MX | 6061 |
| 16 | 🇨🇭 CH | 5767 |
| 17 | 🇳🇴 NO | 5400 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3683 |
| 20 | 🇵🇱 PL | 3586 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2755 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2380 |
| 27 | 🇲🇦 MA | 2185 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1897 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4554 |
| 2 | Denver International Airport |  | US | 3532 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2627 |
| 5 | Guaymaral Airport |  | CO | 2592 |
| 6 | Harry Reid International Airport |  | US | 2406 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2228 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2210 |
| 10 | La Aurora Airport |  | GT | 2095 |
| 11 | El Dorado International Airport |  | CO | 2027 |
| 12 | Chicago O'Hare International Airport |  | US | 1994 |
| 13 | Salt Lake City International Airport |  | US | 1917 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1894 |
| 15 | Congonhas Airport |  | BR | 1828 |
| 16 | Frankfurt am Main International Airport |  | DE | 1776 |
| 17 | Madrid Barajas International Airport |  | ES | 1699 |
| 18 | Capua Airport |  | IT | 1653 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1636 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1611 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1593 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Malpensa International Airport |  | IT | 1524 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1491 |
| 26 | Charlotte/Douglas International Airport |  | US | 1458 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1330 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1326 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1293 |
| 33 | Seattle-Tacoma International Airport |  | US | 1283 |
| 34 | Viracopos International Airport |  | BR | 1269 |
| 35 | Calgary International Airport |  | CA | 1221 |
| 36 | Oslo Gardermoen Airport |  | NO | 1203 |
| 37 | Vitoria/Foronda Airport |  | ES | 1202 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1186 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Don Mueang International Airport |  | TH | 1167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 773 | 21m | 244 km | 3,254.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 489 | 13m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 478 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 362 | 27m | 275 km | 1,715.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 293 | 22m | 55 km | 278.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 257 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 256 | 1h 14m | 961 km | 4,243.3 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 234 | 1h 49m | 1,304 km | 5,264.4 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VAR488 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-19 18:31 UTC | 2026-08-19 19:32 UTC | 1h 0m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-19 19:13 UTC | 2026-08-19 19:31 UTC | 18m |
| N5000Y |  | Santa Monica Municipal Airport (KSMO) | Van Nuys Airport (KVNY) | 2026-08-19 19:09 UTC | 2026-08-19 19:29 UTC | 19m |
| N82BH |  | 7CO1 (7CO1) | Fremont County Airport (K1V6) | 2026-08-19 19:15 UTC | 2026-08-19 19:27 UTC | 12m |
| N313NR |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-08-19 19:03 UTC | 2026-08-19 19:19 UTC | 16m |
| TAUNT31 | TAU | Vance Afb Airport (KEND) | 6OK0 (6OK0) | 2026-08-19 19:02 UTC | 2026-08-19 19:18 UTC | 16m |
| CGEKA | CGE | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-08-19 17:51 UTC | 2026-08-19 19:16 UTC | 1h 24m |
| N1115M |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-19 18:49 UTC | 2026-08-19 19:13 UTC | 24m |
| SEE01 | SEE | Tipella Airport (CBB7) | Woodcock Airport (CBQ8) | 2026-08-19 15:35 UTC | 2026-08-19 19:13 UTC | 3h 38m |
| N611GV |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-19 18:49 UTC | 2026-08-19 19:12 UTC | 23m |
| N920CF |  | Dupage Airport (KDPA) | 26LL (26LL) | 2026-08-19 18:44 UTC | 2026-08-19 19:12 UTC | 27m |
| N9421F |  | Pennridge Airport (KCKZ) | Pennridge Airport (KCKZ) | 2026-08-19 18:57 UTC | 2026-08-19 19:12 UTC | 14m |
| N576ME |  | Moorhead Airpark (PN40) | Fairview Evergreen Airport (PN18) | 2026-08-19 19:01 UTC | 2026-08-19 19:11 UTC | 9m |
| N7778U |  | Nephi Municipal Airport (KU14) | Wendover Airport (KENV) | 2026-08-19 18:03 UTC | 2026-08-19 19:11 UTC | 1h 8m |
| N407DV |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-19 18:50 UTC | 2026-08-19 19:09 UTC | 18m |
| GFY1124 | GFY | Portland-Hillsboro Airport (KHIO) | Boeing Field/King County International Airport (KBFI) | 2026-08-19 18:02 UTC | 2026-08-19 19:07 UTC | 1h 5m |
| N37AT |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-19 17:58 UTC | 2026-08-19 19:06 UTC | 1h 7m |
| N408GG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-19 17:19 UTC | 2026-08-19 19:06 UTC | 1h 47m |
| N738AZ |  | Riverside Airport (KRAL) | Hemet-Ryan Airport (KHMT) | 2026-08-19 18:44 UTC | 2026-08-19 19:04 UTC | 19m |
| N4899R |  | Drift River Airport (3AK5) | Falcon Lake Strip (0AK9) | 2026-08-19 18:06 UTC | 2026-08-19 19:03 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

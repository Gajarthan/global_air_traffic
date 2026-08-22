# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_16:30:37_UTC-green)

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

**Latest saved flight:** 2026-08-22 16:30:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 16:30:37 UTC

- **226,100** saved flights
- **70,283** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **226,100** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,724,282.7 tonnes** estimated CO2 emissions
- **157,929,429 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9075 |
| 2 | SkyWest Airlines | 8012 |
| 3 | EJA | 4364 |
| 4 | IndiGo | 3825 |
| 5 | American Airlines | 3708 |
| 6 | Southwest Airlines | 3526 |
| 7 | Delta Air Lines | 2888 |
| 8 | ENY | 2763 |
| 9 | LATAM Airlines | 2163 |
| 10 | AZU | 2090 |
| 11 | Vueling | 1915 |
| 12 | Lufthansa | 1855 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1782 |
| 15 | easyJet | 1566 |
| 16 | Swiss International | 1507 |
| 17 | AXM | 1493 |
| 18 | EJU | 1427 |
| 19 | United Airlines | 1423 |
| 20 | QLK | 1421 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1257 |
| 24 | PGT | 1243 |
| 25 | VIV | 1234 |
| 26 | Air France | 1233 |
| 27 | WMT | 1220 |
| 28 | Wizz Air | 1172 |
| 29 | JetBlue | 1130 |
| 30 | AEE | 1126 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 189190 |
| 2 | 🇪🇸 ES | 14498 |
| 3 | 🇧🇷 BR | 13184 |
| 4 | 🇦🇺 AU | 12778 |
| 5 | 🇨🇦 CA | 12512 |
| 6 | 🇮🇹 IT | 12146 |
| 7 | 🇮🇳 IN | 11922 |
| 8 | 🇩🇪 DE | 11142 |
| 9 | 🇬🇧 GB | 10626 |
| 10 | 🇨🇴 CO | 9297 |
| 11 | 🇯🇵 JP | 9194 |
| 12 | 🇫🇷 FR | 9060 |
| 13 | 🇹🇷 TR | 6628 |
| 14 | 🇬🇷 GR | 6617 |
| 15 | 🇲🇽 MX | 6275 |
| 16 | 🇨🇭 CH | 5980 |
| 17 | 🇳🇴 NO | 5592 |
| 18 | 🇲🇾 MY | 3981 |
| 19 | 🇿🇦 ZA | 3913 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3762 |
| 22 | 🇳🇿 NZ | 3140 |
| 23 | 🇵🇭 PH | 3087 |
| 24 | 🇬🇹 GT | 2862 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2552 |
| 27 | 🇲🇦 MA | 2281 |
| 28 | 🇲🇪 ME | 2033 |
| 29 | 🇳🇱 NL | 2022 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4714 |
| 2 | Denver International Airport |  | US | 3678 |
| 3 | Tokyo International Airport |  | JP | 2748 |
| 4 | Indira Gandhi International Airport |  | IN | 2745 |
| 5 | Guaymaral Airport |  | CO | 2635 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2350 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2308 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2287 |
| 10 | La Aurora Airport |  | GT | 2180 |
| 11 | El Dorado International Airport |  | CO | 2081 |
| 12 | Chicago O'Hare International Airport |  | US | 2051 |
| 13 | Salt Lake City International Airport |  | US | 1983 |
| 14 | Congonhas Airport |  | BR | 1927 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 16 | Frankfurt am Main International Airport |  | DE | 1821 |
| 17 | Madrid Barajas International Airport |  | ES | 1765 |
| 18 | Capua Airport |  | IT | 1750 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1684 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1681 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1637 |
| 22 | Malpensa International Airport |  | IT | 1601 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 25 | Charles de Gaulle International Airport |  | FR | 1568 |
| 26 | Charlotte/Douglas International Airport |  | US | 1484 |
| 27 | Ninoy Aquino International Airport |  | PH | 1476 |
| 28 | Kuala Lumpur International Airport |  | MY | 1446 |
| 29 | Barcelona International Airport |  | ES | 1406 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1370 |
| 31 | Bengaluru International Airport |  | IN | 1345 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1337 |
| 33 | Viracopos International Airport |  | BR | 1337 |
| 34 | Seattle-Tacoma International Airport |  | US | 1330 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1319 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1259 |
| 39 | Vitoria/Foronda Airport |  | ES | 1244 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1224 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1074 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 817 | 21m | 244 km | 3,440.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 563 | 1h 6m | 770 km | 7,479.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 534 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 511 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 341 | 1h 50m | 1,423 km | 8,368.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 301 | 22m | 55 km | 286.1 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 293 | 44m | 555 km | 2,805.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 289 | 1h 38m | 1,156 km | 5,765.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 287 | 24m | 218 km | 1,081.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 283 | 19m | 99 km | 484.8 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 265 | 1h 14m | 961 km | 4,392.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
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
| N116BD |  | Majors Airport (KGVT) | Card Aerodrome (0TX9) | 2026-08-22 16:13 UTC | 2026-08-22 16:30 UTC | 17m |
| CCAAK | Air China | Municipal de Vitacura Airport (SCLC) | Eulogio Sanchez Airport (SCTB) | 2026-08-22 16:18 UTC | 2026-08-22 16:28 UTC | 10m |
| N46EK |  | K00V (K00V) | Mertens Airport (3CO2) | 2026-08-22 15:22 UTC | 2026-08-22 16:27 UTC | 1h 5m |
| N814R |  | Mckinney Ntl Airport (KTKI) | 31TS (31TS) | 2026-08-22 15:44 UTC | 2026-08-22 16:24 UTC | 40m |
| PRKOT | PRK | Jundiai Airport (SBJD) | Campo Belo Airport (SNCA) | 2026-08-22 15:50 UTC | 2026-08-22 16:22 UTC | 31m |
| EJA302 | EJA | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-08-22 16:05 UTC | 2026-08-22 16:16 UTC | 11m |
| FHPCJ | FHP | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-08-22 16:06 UTC | 2026-08-22 16:16 UTC | 10m |
| N738GJ |  | Mesquite Metro Airport (KHQZ) | Mesquite Metro Airport (KHQZ) | 2026-08-22 16:14 UTC | 2026-08-22 16:15 UTC | 1m |
| HKW386 | HKW | Dvoracek Field (23MI) | Mason County Airport (KLDM) | 2026-08-22 15:50 UTC | 2026-08-22 16:11 UTC | 21m |
| N8222W |  | Waco Regional Airport (KACT) | Waco Regional Airport (KACT) | 2026-08-22 16:05 UTC | 2026-08-22 16:10 UTC | 5m |
| N239P |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-08-22 15:54 UTC | 2026-08-22 16:09 UTC | 15m |
| N485SC |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-08-22 14:11 UTC | 2026-08-22 16:09 UTC | 1h 57m |
| N100LE |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-22 15:45 UTC | 2026-08-22 16:06 UTC | 21m |
| ES807 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-08-22 16:01 UTC | 2026-08-22 16:06 UTC | 5m |
| FJO53F | FJO | Geneva Cointrin International Airport (LSGG) | Barcelona International Airport (LEBL) | 2026-08-22 14:52 UTC | 2026-08-22 16:01 UTC | 1h 9m |
| N257EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-22 12:47 UTC | 2026-08-22 15:57 UTC | 3h 10m |
| CXK236 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-22 15:32 UTC | 2026-08-22 15:55 UTC | 22m |
| RYR4164 | Ryanair | Stockholm-Arlanda Airport (ESSA) | Visoko Sport Airfield (LQVI) | 2026-08-22 13:34 UTC | 2026-08-22 15:52 UTC | 2h 17m |
| N4883G |  | KL38 (KL38) | KL38 (KL38) | 2026-08-22 15:39 UTC | 2026-08-22 15:52 UTC | 12m |
| N104ET |  | Wayne County Airport (KBJJ) | Wayne County Airport (KBJJ) | 2026-08-22 15:31 UTC | 2026-08-22 15:51 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

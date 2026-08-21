# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_16:18:07_UTC-green)

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

**Latest saved flight:** 2026-08-21 16:18:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 16:18:07 UTC

- **222,657** saved flights
- **69,598** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **222,657** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,680,510.5 tonnes** estimated CO2 emissions
- **155,391,914 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8929 |
| 2 | SkyWest Airlines | 7900 |
| 3 | EJA | 4298 |
| 4 | IndiGo | 3777 |
| 5 | American Airlines | 3678 |
| 6 | Southwest Airlines | 3495 |
| 7 | Delta Air Lines | 2855 |
| 8 | ENY | 2733 |
| 9 | LATAM Airlines | 2120 |
| 10 | AZU | 2047 |
| 11 | Vueling | 1879 |
| 12 | Lufthansa | 1840 |
| 13 | WIF | 1783 |
| 14 | LXJ | 1750 |
| 15 | easyJet | 1542 |
| 16 | Swiss International | 1482 |
| 17 | AXM | 1466 |
| 18 | QLK | 1405 |
| 19 | United Airlines | 1395 |
| 20 | EJU | 1394 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1333 |
| 23 | PGT | 1221 |
| 24 | GLO | 1219 |
| 25 | VIV | 1210 |
| 26 | Air France | 1207 |
| 27 | WMT | 1186 |
| 28 | Wizz Air | 1146 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186822 |
| 2 | 🇪🇸 ES | 14278 |
| 3 | 🇧🇷 BR | 12886 |
| 4 | 🇦🇺 AU | 12653 |
| 5 | 🇨🇦 CA | 12289 |
| 6 | 🇮🇹 IT | 11870 |
| 7 | 🇮🇳 IN | 11782 |
| 8 | 🇩🇪 DE | 10995 |
| 9 | 🇬🇧 GB | 10449 |
| 10 | 🇨🇴 CO | 9171 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8875 |
| 13 | 🇬🇷 GR | 6499 |
| 14 | 🇹🇷 TR | 6460 |
| 15 | 🇲🇽 MX | 6171 |
| 16 | 🇨🇭 CH | 5865 |
| 17 | 🇳🇴 NO | 5544 |
| 18 | 🇲🇾 MY | 3885 |
| 19 | 🇿🇦 ZA | 3841 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3699 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3020 |
| 24 | 🇬🇹 GT | 2810 |
| 25 | 🇰🇷 KR | 2656 |
| 26 | 🇭🇷 HR | 2486 |
| 27 | 🇲🇦 MA | 2241 |
| 28 | 🇲🇪 ME | 1980 |
| 29 | 🇳🇱 NL | 1979 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4658 |
| 2 | Denver International Airport |  | US | 3623 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2707 |
| 5 | Guaymaral Airport |  | CO | 2619 |
| 6 | Harry Reid International Airport |  | US | 2446 |
| 7 | Zurich Airport |  | CH | 2307 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2282 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2259 |
| 10 | La Aurora Airport |  | GT | 2141 |
| 11 | El Dorado International Airport |  | CO | 2079 |
| 12 | Chicago O'Hare International Airport |  | US | 2029 |
| 13 | Salt Lake City International Airport |  | US | 1949 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1913 |
| 15 | Congonhas Airport |  | BR | 1884 |
| 16 | Frankfurt am Main International Airport |  | DE | 1806 |
| 17 | Madrid Barajas International Airport |  | ES | 1742 |
| 18 | Capua Airport |  | IT | 1701 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1663 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1643 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1626 |
| 22 | Macau International Airport |  | MO | 1588 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1562 |
| 25 | Charles de Gaulle International Airport |  | FR | 1534 |
| 26 | Charlotte/Douglas International Airport |  | US | 1474 |
| 27 | Ninoy Aquino International Airport |  | PH | 1438 |
| 28 | Kuala Lumpur International Airport |  | MY | 1418 |
| 29 | Barcelona International Airport |  | ES | 1372 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1348 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1316 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1308 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1264 |
| 36 | Calgary International Airport |  | CA | 1258 |
| 37 | Oslo Gardermoen Airport |  | NO | 1243 |
| 38 | Don Mueang International Airport |  | TH | 1239 |
| 39 | Vitoria/Foronda Airport |  | ES | 1236 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1199 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1069 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 802 | 21m | 244 km | 3,377.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 510 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 502 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 375 | 27m | 275 km | 1,777.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 331 | 1h 50m | 1,423 km | 8,123.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 298 | 21m | 250 km | 1,287.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 281 | 1h 39m | 1,156 km | 5,605.8 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 278 | 24m | 218 km | 1,047.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 19 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 274 | 19m | 99 km | 469.3 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 262 | 1h 14m | 961 km | 4,342.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 253 | 19m | 144 km | 629.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 241 | 1h 50m | 1,304 km | 5,421.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 235 | 28m | 152 km | 614.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N605JG |  | Sanderson Field (KSHN) | Coeur D'Alene Airport (KCOE) | 2026-08-21 15:18 UTC | 2026-08-21 16:18 UTC | 59m |
| SCU58 | SCU | Tulsa International Airport (KTUL) | Tulsa International Airport (KTUL) | 2026-08-21 15:22 UTC | 2026-08-21 16:17 UTC | 54m |
| N38373 |  | Stockton Metro Airport (KSCK) | Hayward Executive Airport (KHWD) | 2026-08-21 15:40 UTC | 2026-08-21 16:16 UTC | 35m |
| N526BP |  | Essex County Airport (KCDW) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-21 15:39 UTC | 2026-08-21 16:16 UTC | 36m |
| N451DS |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-21 15:52 UTC | 2026-08-21 16:11 UTC | 18m |
| N265FA |  | Wings Field (KLOM) | Lehigh Valley International Airport (KABE) | 2026-08-21 15:19 UTC | 2026-08-21 16:10 UTC | 50m |
| N20ET |  | St Pete-Clearwater International Airport (KPIE) | Post Oak Ranch Airport (1FA1) | 2026-08-21 15:34 UTC | 2026-08-21 16:07 UTC | 32m |
| N70MC |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-08-21 15:10 UTC | 2026-08-21 16:02 UTC | 51m |
| N50ZM |  | Merritt Island Airport (KCOI) | Merritt Island Airport (KCOI) | 2026-08-21 15:42 UTC | 2026-08-21 16:00 UTC | 17m |
| N733CE |  | Reno/Tahoe International Airport (KRNO) | NV44 (NV44) | 2026-08-21 15:35 UTC | 2026-08-21 15:59 UTC | 24m |
| N7039C |  | Van Nuys Airport (KVNY) | Henderson Executive Airport (KHND) | 2026-08-21 14:15 UTC | 2026-08-21 15:58 UTC | 1h 43m |
| OZN923 | OZN | Miami Executive Airport (KTMB) | Mjd Airport (FL31) | 2026-08-21 15:45 UTC | 2026-08-21 15:58 UTC | 12m |
| N983RA |  | Marana Regional Airport (KAVQ) | Marana Regional Airport (KAVQ) | 2026-08-21 15:03 UTC | 2026-08-21 15:57 UTC | 53m |
| N945RF |  | Essex County Airport (KCDW) | Newark Liberty International Airport (KEWR) | 2026-08-21 13:52 UTC | 2026-08-21 15:57 UTC | 2h 4m |
| N630CB |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-21 15:27 UTC | 2026-08-21 15:56 UTC | 28m |
| N420SP |  | Denton Enterprise Airport (KDTO) | Dreamland Airport (XA48) | 2026-08-21 15:22 UTC | 2026-08-21 15:53 UTC | 31m |
| N216SR |  | Camp Bullis Als (Cals) Airport (9TX5) | Kestrel Airpark (K1T7) | 2026-08-21 15:35 UTC | 2026-08-21 15:53 UTC | 18m |
| N707GP |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-21 15:31 UTC | 2026-08-21 15:52 UTC | 20m |
| N407GM |  | Fuller Airport (TS00) | Fuller Airport (TS00) | 2026-08-21 14:49 UTC | 2026-08-21 15:51 UTC | 1h 2m |
| N2441D |  | Dupage Airport (KDPA) | Colonial Acres Airport (4LL8) | 2026-08-21 14:53 UTC | 2026-08-21 15:51 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
